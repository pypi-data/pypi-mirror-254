# from pandas.core.strings import str_count
import boto3
import geopandas as gpd
import hana_ml
import io
import json
import numpy as np
import pandas as pd
import pymssql
import oracledb
import redshift_connector
import sys
import time

from gmlutil import config as conf
from fuzzywuzzy import fuzz
from pytrends.request import TrendReq
from sqlalchemy import create_engine, Table, MetaData
from types import SimpleNamespace

limit = np.int64(10**9 * 2.1)
sys.setrecursionlimit(limit)

run_mode = "cloud"
if run_mode == "local":
    path_to_folder = '../'
    sys.path.append(path_to_folder)
    import credentials as cred
else:
    def credf(keys):
        client = boto3.client('secretsmanager', region_name = conf.secretsm_region)
        if keys == "redshift":
            response = client.get_secret_value(SecretId=conf.secretsm_redshift_keys)
            database_secrets = json.loads(response['SecretString'])
            cred = SimpleNamespace(**database_secrets)
        else:
            response = client.get_secret_value(SecretId=conf.secretsm_master_keys)
            database_secrets = json.loads(response['SecretString'])
            cred = SimpleNamespace(**database_secrets)
        return cred
    cred = credf('master')
    credr = credf('redshift')

    
########################### Data Extraction ###########################
class data_extraction:
    def __init__(self):
        pass

    
    def aws_connection(self, aws_client='s3'):
        client_conn = boto3.client(aws_client, 
            region_name = cred.AWS_REGION_NAME,
            aws_access_key_id = cred.AWS_ACCESS_KEY,
            aws_secret_access_key = cred.AWS_SECRET_KEY
            )
        return client_conn
    

    def hana_connection(self):
        conn = hana_ml.dataframe.ConnectionContext(
            address= cred.HANA_ADDRESS,
            port=cred.HANA_PORT,
            user=cred.HANA_USER,
            password=cred.HANA_PASSWORD
            )
        return conn


    def irigco_connection(self):
        conn = pymssql.connect(server = cred.GCO_SERVER, # 'lv1sqlprdwdb02', 
                            user=cred.GCO_USERNAME, 
                            password = cred.GCO_PASSWORD, 
                            database = cred.GCO_DATABASE, # 'IRIGCO', 
                            port = cred.GCO_PORT) # 61433)
        return conn


    def rs_connection(self):
        engine_string = 'redshift+psycopg2://{}:{}@{}'.format(credr.username, credr.password, credr.host + ":" + credr.port + "/" + credr.dbName)
        conn = create_engine(engine_string)
        return conn 


    # READING IN ACV DATA
    def read_from_acv_s3(self, bucket_name=cred.S3_BUCKET, file_name=cred.benchmark_acv_str, geofile_name=cred.benchmark_geo_str, fuzz_ratio=90, state_choice1=['New Mexico','New_Mexico'], state_choice2=['DC','District of Columbia']):
        """gets our acv curves from s3 in order to run the distributor path option for upcs
        Returns:
             df: acv_df is the accounts with the respective net list running percent for each category and tier 
        """ 
        acv_df = self.read_from_s3(bucket_name, file_name)
        columns = ['9L VOLUME','PHYS VOLUME','NET LIST DOLLARS']
        for column in columns:
            acv_df[column] = round(acv_df[column],2)
        columns = ['nl_percent','nl_running_percent']
        for column in columns:
            acv_df[column] = round(acv_df[column],4)
        acv_df['Rtl_Acct_ID'] = acv_df['Rtl_Acct_ID'].astype(int)
        acv_df['geoCode'] = acv_df['geoCode'].astype(str)
        acv_df['concat'] = acv_df['Mkt_Grp_State'] + ' ' + acv_df['Acct_City']
        acv_df['concat'] = acv_df['concat'].astype(str)
        unique_citystates = acv_df[['Mkt_Grp_State','Acct_City','concat']].drop_duplicates()
        # Read in geocodes and fuzzy match them--> need to do ts cause some cities have different spellings from the hana side
        geo_codes = self.read_from_s3(bucket_name, geofile_name)
        geo_codes['concat'] =geo_codes['Mkt_Grp_State'] + ' ' + geo_codes['City']
        matchers = {}
        for j in unique_citystates['concat']:
            for i in geo_codes['concat']:
                if (j[:2] == i[:2]):
                    if fuzz.ratio(i,j) > fuzz_ratio:
                        matchers[j] = i
        acv_df['new_concat'] = acv_df['concat'].map(matchers)
        acv_df_new = acv_df.merge(geo_codes[['geoCode','concat']],left_on = 'new_concat',right_on = 'concat',how='left')
        acv_df_new['new_concat'] = acv_df_new['new_concat'].astype(str)
        acv_df_new = acv_df_new.drop(['geoCode_x','concat_x','concat_y','new_concat','geoCode_x'],axis = 1)
        acv_df_new = acv_df_new.rename(columns = {'geoCode_y':'geoCode'})
        acv_df_new['geoCode'] =acv_df_new['geoCode'].astype(str)
        acv_df_new['State'] = np.where(acv_df_new['State'] in state_choice1, acv_df_new['State'])
        acv_df_new['State'] = np.where(acv_df_new['State'] in state_choice2, acv_df_new['State'])
        return acv_df_new


    def read_from_ocdb(self, sql, host='oradb07.est1933.com', port=2001, service_name='db07.est1933.com'):
        dsn_conn = oracledb.makedsn(host, port, service_name=service_name)
        conn = oracledb.connect(user=cred.ORACLE_USERID, password=cred.ORACLE_PASSWORD, dsn=dsn_conn, encoding='ISO-8859-1')
        df_ora = pd.read_sql(sql, con=conn)
        conn.close()
        return df_ora


    # PYTRENDS FUNCTION THAT GETS TRENDING CITIES BASED ON KEYWORD(BRAND)
    def read_from_gcity(self, keyword, hl='en-US', cat='71', geo='US', gprop='', timeframe='today 3-m', resolution='DMA', inc_low_vol=True, inc_geo_code=True, num_keywords=30):
        """generates the google trends piece from a keyword that is entered(benchmark)
        Args:
            keyword (str): planning brand that is entered in order to generate city list
        Returns:
            df: cities that are trending for the keyword
        """
        print('gathering google trends data')
        pytrends = TrendReq(hl=hl)
        # Building our payload for the trends query
        keywords = [keyword]
        # Pytrends function to get google data
        pytrends.build_payload(keywords, cat, timeframe, geo,gprop)
        try:
            output= pytrends.interest_by_region(resolution=resolution, inc_low_vol=inc_low_vol, inc_geo_code=inc_geo_code)
            city_queries = output[output[keywords[0]] > num_keywords]
            city_queries['Google'] = 'Y'
            city_queries = city_queries[['geoCode','Google']]
        except:
            city_queries = pd.DataFrame([], columns=['geoCode','Google'])
        time.sleep(1)
        return city_queries

    
    def read_from_geo_s3(self, bucket_name, file_name=cred.geospatial_str): 
        nav_county_polys = self.read_from_s3(bucket_name, file_name)
        nav_county_polys['geometry'] = gpd.GeoSeries.from_wkt(nav_county_polys['geometry'])
        nav_county_polys = gpd.GeoDataFrame(nav_county_polys, geometry = 'geometry',crs='EPSG:4326')
        return nav_county_polys
    

    def read_from_mssql(self, sql):
        conn = self.mssql_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data)
        return df


    def read_from_rs(self, table_name, schema_name=credr.dbName):
        metadata = MetaData()
        conn = self.rs_connection()
        dt = Table(table_name, metadata, autoload=True, autoload_with=conn, schema=schema_name)
        df_columns = dt.columns.keys()
        return dt, conn, df_columns


    def read_from_s3(self, bucket_name, file_name, encoding='utf8', low_memory=False, dtypes = None, file_type='csv'):
        s3c = self.aws_connection()
        KEY = '{}'.format(file_name)
        obj = s3c.get_object(Bucket=bucket_name, Key = KEY)
        data = obj['Body'].read()
        if file_type == 'csv':                         
            df = pd.read_csv(io.BytesIO(data) , encoding=encoding, low_memory=low_memory, dtype = dtypes) # , on_bad_lines='skip')
        elif file_type == 'xlsx':
            df = pd.read_excel(io.BytesIO(data), engine='openpyxl')
        return df
    
    
    # GETTING OUR UPCS DF WCH CONTAINS CATEGORY AND PRICE TIER FOR INDIVIDUAL ITEMS
    def read_from_upc_s3(self, bucket_name=cred.S3_BUCKET, file_name=cred.upc_tier_str):
        """gets our upc df: a dataframe with all upcs and thier corresponding price tier and category
        Returns:
            [df]: [upc_df is all upcs and their corresponding price tier and category: to be merged onto acv df]
        """
        upc_df = self.read_from_s3(bucket_name, file_name)
        # Add leading zeros to UPC to match Gallo data
        upc_df['UPC'] = upc_df['UPC'].astype(int).astype(str).str.rjust(12, "0")
        return upc_df


    def upload_to_rs(self, bucket_name, file_name, table_name=credr.winegrowing_table, host = credr.winegrowing_host, database = credr.winegrowing_database, user = credr.winegrowing_user, password = credr.winegrowing_password): # prophet/Deployment/DS_Collab/winegrowing_research/GQI/model_outputs/gqi_calc.csv
        rs_push_query = """call """ + table_name + """.copy_gqi_calc('s3://"""+ bucket_name + """/""" + file_name + """')"""
        conn_redshift = redshift_connector.connect(
            host = host,
            database = database,
            user = user,
            password = password
        )
        cursor = conn_redshift.cursor()
        cursor.execute(rs_push_query)
        conn_redshift.commit()
        conn_redshift.close()
        cursor.close()
        print("Successfully pushed to Redshift.")    
    

    def upload_to_s3(self, df, bucket_name, file_name, index=False, file_type='csv'):
        s3c = self.aws_connection()
        KEY = '{}'.format(file_name)
        if file_type == 'csv':
            df.to_csv('buffer', index=index)
            s3c.upload_file(Bucket = bucket_name, Filename = 'buffer', Key = KEY)
        elif file_type == 'xlsx':
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                df.to_excel(writer)
            data = buffer.getvalue()
            s3c.put_object(Bucket=bucket_name, Key=KEY, Body=data)
            writer.close()
        print("Uploading is successful...")



