import numpy as np
import pandas as pd
import re
from gmlutil import data_extraction as dte

cred = dte.cred
de = dte.data_extraction()

########################### Data Cleaning ###########################
class data_cleaning:
    def __init__(self):
        pass


    def clean_upc(self, upc):
        """need to clean some upcs in order to account for zfill and other objects 
        Args:
            upc ([str]): [unique identifier of item]
        Returns:
            [str]: [refurbished upc item]
        """
        if upc[0] != '0':
            upc = '0' + upc[:-1]
            return upc
        else:
            return upc

    
    def dec_to_perc(self, num):
        perc = str(round(num * 100, 2)) + "%"
        return perc

    
    def oned_cross_merging(self, df1, df2):
        df1['key'] = 1
        df2['key'] = 1
        df = pd.merge(df1, df2, on ='key').drop("key", 1)
        return df
    
    
    def remove_decimal(self, word):
        new_word =  re.sub('(\.0+)','',word)
        return new_word


########################### Prime Directive Processing ###########################

class prime_directive:
    def __init__(self, change_names = {'FINE_WINE':'Fine_Wine_Acct_Flag', 'INFLUENCER':'Fine_Wine_Inflncr_Acct_Flag','ICON':'Fine_Wine_Icon_Acct_Flag'}):
        self.change_names = change_names

        
    def brand_standard_process(self, df, bucket_name=cred.S3_BUCKET, file_name=cred.brand_standards_str):
        if len(df) != 0:
            #what Patrick is changing
#             df.columns = df.columns.str.lower()
            df['UPC'] = df['UPC'].astype(str).str.zfill(12)
            try:
                upc_list = list(set(df['UPC']))
            except:
                upc_list = list(set(df['UPC']))
            brand_standard_list = []
            standard_change = ['Fine_Wine_Acct_Flag','Fine_Wine_Inflncr_Acct_Flag', 'Fine_Wine_Icon_Acct_Flag',
                   'Prem_Spirit_Acct_Flag', 'Whiskey_Segment']
            standard_change = [element.lower() for element in standard_change]
            store_list = ['GROCERY','LIQUOR','CONVENIENCE','DRUG','MASS MERCHANDISER','ALL OTHER-OFF SALE','DOLLAR','CLUB']
            for upc in upc_list:
                try:
                    search_dict = self.search_func(upc, bucket_name, file_name)
                    upc_df = df[df['UPC']==upc]
                    upc_df = upc_df.rename(columns = self.change_names)
                    upc_df.columns = map(str.lower, upc_df.columns)
                    for i in standard_change:
                        upc_df[i] = upc_df[i].apply(lambda x: self.create_score(x))
                    upc_df['gsp'] = np.where((upc_df['prem_spirit_acct_flag'] ==1) | (upc_df['whiskey_segment'] == 1),1,0)
                    upc_df['zone_check'] = np.where(upc_df['key_acct_zone'].str.contains('1|2|3'),'zone1_3','zone4_5')
                    upc_df = upc_df[upc_df['channel_of_distribution'].isin(store_list)]
                    upc_df['standards_check'] = upc_df.apply(lambda x: self.standards_check(search_dict,x['zone_check'],x['channel_of_distribution'],
                                                                   x['fine_wine_icon_acct_flag'],x['fine_wine_inflncr_acct_flag'],
                                                                  x['fine_wine_acct_flag'],x['gsp']), axis = 1)
                    upc_df = upc_df[upc_df['standards_check'] == 'Y']
                except Exception as err:
                    print('passing this upc {}... {}...'.format(upc, err))
                    continue
                brand_standard_list.append(upc_df)
            try:
                brand_standard_df = pd.concat(brand_standard_list)
            except:
                print("Concat failed...")
                brand_standard_df = pd.DataFrame([], columns=df.columns)
        else:
            print("Data Empty...")
            brand_standard_df = df.copy()
        return brand_standard_df


    def create_score(self, check_value):
        if check_value == 'Y':
            return 1
        elif check_value == 'N':
            return 0
        elif  check_value in ['Gold','Silver']:
            return 1
        else:
            return 0
        
        
    def search_func(self, upc_value, bucket_name, file_name, platform='cloud'):
        if platform == "local":
            brand_standards = pd.read_csv("../data/off_brand_standards.csv", low_memory=False, dtypes = {'UPC':str})
        else:
            brand_standards = de.read_from_s3(bucket_name, file_name, dtypes = {'UPC':str})
        brand_standards['UPC'] = brand_standards['UPC'].astype(str).str.zfill(12)
        upc_search = brand_standards[brand_standards['UPC'] == upc_value].drop_duplicates()
        try:
            upc_search = upc_search.rename(columns = self.change_names)
            upc_search.columns = map(str.lower, upc_search.columns)
        except:
            print("No such columns exist...")
            print()
        search_dict = upc_search.to_dict('records')[0]
        return search_dict

    
    def standards_check(self, dictionary, zone, channel, icon, influencer, finewine, gsp):
        #zone checker
        check_value = 0
        if dictionary['segmentation'] == 'BROAD':
            return 'Y'
        else:
            check_value += int(dictionary[zone.lower()])
            #channel of dist checker
            check_value += int(dictionary[channel.lower()])
            #icon checker
            #influencer checker
            if dictionary['fine_wine_acct_flag'] == 1:
                check_value += finewine
            elif dictionary['fine_wine_inflncr_acct_flag'] == 1:
                check_value += influencer
            #fine wine checker
            elif dictionary['fine_wine_icon_acct_flag'] == 1:
                check_value += icon
            #we're going to vet liquor items
            if (dictionary['gsp'] == 1) and (dictionary['not_gsp'] == 1) :
                check_value += 1
            elif dictionary['gsp'] == 1:
                check_value += gsp
            elif dictionary['not_gsp'] == 1:
                check_value -= gsp
            if (dictionary['segmentation'] == 'GSP') and (check_value == 3) and (gsp == 1):
                return 'Y'
            else:
                if check_value == 4:
                    return 'Y'
                else:
                    return 'N'

