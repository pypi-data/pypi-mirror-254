# MLUTIL (Machine Learning Utility) Library Documentation

## data_cleaning: This library provides methods for cleaning data in general and for prime directive.

### data_cleaning: This class provides cleaning methods.
- clean_upc: This cleans upc so that it has a leading 0.
- dec_to_perc: This performs a conversion from a decimal to a percent.
- oned_cross_merging: This performs a cross-mergeing of two pandas datasets.
- remove_decimal: This removes a decimal from a string.

### prime_directive: This class provides methods used in the brand standard process.
- brand_standard_process: This removes brands that are not in the brand standard list.
- create_score: This creates scores that will be used in the brand standard process.
- search_func: This cleans data that will be used in the brand standard process.
- standards_check: This checks for various conditions and returns data that will be used in the brand standard process.

## data_extraction: Methods in this class requires a python file that contains various credentials stored in the root directory (Hana, AWS credentials, etc).
- aws_connection: This connects to a resource of choice.  It returns an aws resource connection object.  Default resource is s3.
- hana_connection: This connects to a hana database.  It returns a connection object.
- irigco_connection: This connects to an iri-gco database in a mssql server.  It returns a connection object.
- rs_connection: This connects to a redshift database.  It returns a connection object.
- read_from_acv_s3: This retrieves acv data from S3.  It returns a pandas dataframe.
- read_from_ocdb: This reads pandas dataframe in from Oracle Database.  It returns a pandas dataframe.
- read_from_gcity: This retrieves data from google trends based on a keyword.  It returns a pandas dataframe.
- read_from_geo_s3: This retrieves geospatial data from S3. It returns a pandas dataframe.
- read_from_mssql:  This retrieves data from mssql server.  It returns a pandas dataframe.
- read_from_rs: This reads in table name and schema name from a redshift table.  Default schema name has been set to ‘prophet’.   Outputs include general sqlalchemy all select statement, connection engine for sqlalchemy, and all column names for soon-to-be extracted data table.
- read_from_s3: This reads pandas dataframe in from s3.  It takes in string file name as an argument.  It returns a pandas dataframe.
- read_from_upc_s3:  This retrieves upc data from S3.  It returns a pandas dataframe.
- upload_to_rs: This calls upon a copy command procedure in redshift to migrate data from S3 to RedShift.
- upload_to_s3: This uploads a pandas dataframe to S3 from your local setup.  It takes in pandas dataframe and string file name as arguments.

## feature_engineering: This class provides various feature engineering functions that can be easily utilized in analysis of data and reduction of dimensionality.

### data_conversion: This class requires categorical and numerical list inputs for converting data.
- load_labels: This loads a label dictionary from a pickle file.  It takes in string pickle  file name as an argument.  It returns a label dictionary.
- save_labels: This saves a label dictionary as pickle file.  It takes in label dictionary and string pickle file name as arguments.
- data_conversion_cat_onehot: This converts categorical variables into 0s and 1s using onehot encoding.  It takes in pandas dataframe as an argument.  It returns a converted pandas dataframe.
- data_conversion_cat: This converts categorical variables into numbers using label encoder object.  It takes in pandas dataframe and string label name as arguments.  It returns a converted pandas dataframe.
- data_conversion_num: This scales numerical variables using different strategies.  Default option is set to min-max scaling but power transformation or standard scaling can be chosen.  It takes in pandas dataframe and optionally scaler type as arguments.  It returns a converted pandas dataframe.

### data_preparation: This class provides methods to prepare data for various purpose.
- train_testsets: This can be used to split training and test datasets, over and undersample training datasets.  It takes in pandas dataframe and target label as arguments.  Optionally, test size, oversampling and undersampling methods can be set.  It returns target, non-target training, test datasets.

## non-timeseries models: This library provides ML tools that are needed to analyze and visualize data and train/test non-timeseries models.

### data_visualization: This class provides various visualization functions that can be easily utilized in analysis.
- data_visualization: This plots a 2 dimensional graph.
- elbow_graph: This plots an elbow representation of number of clusters vs. distortion.  It takes in pandas dataframe as an argument.
- pca_graph: This plots 1st and 2nd principal components of a fit dataset on x-y grid.  It takes in pandas dataframe as an argument.  Optionally percent of variability explained in the dataset can be set.  Default is set at 0.99.
- tsne_graph: This plots a 2 dimensional representation of a fit dataset.  It uses TSNE model to embed a dataset into 2D.  It takes in pandas dataframe as an argument.
- umap_graph: This plots a 2 dimensional representation of a fit dataset.  It uses UMAP model to embed a dataset into 2D.  It takes in pandas dataframe as an argument.

### model_training: This class provides various model learning models and save/load mechanisms without explicitly using the sklearn library.
- load_model_trained: This loads a trained model.  It takes in model name and label name as arguments.  It returns a trained model.
- save_model_trained: This saves a trained model.  It takes in trained model, model name, and label name as arguments.
- ba_model: This trains a bagging model.  It takes in target, non-target training and test datasets as arguments.  It returns a trained bagging model.
- rf_model: This trains a random forest model.  It takes in target, non-target training and test datasets as arguments.  It returns a trained random forest model.
- build_stacking: This builds a stacking structure for a stacking model.
- model_stacking: This initializes models in the stacking model.
- evaluate_stacking: This evaluates standalone models in the stacking model against the stacking model.  It takes in model, non-target, and target training datasets.  It returns evaluation scores.
- st_model: This trains a stacking model.  It takes in target, non-target training and test datasets as arguments.  It returns a trained stacking model.
- xgb_model: This trains a gradient boosted tree model.  It takes in target, non-target training and test datasets as arguments.  It returns a trained gradient boosted tree model.
- xgb_feature: This shows feature importance of the data attributes using XGBoost algorithm.  It takes in XGBoost trained model as an argument.
- kmeans_model: This trains a kmeans model.  It takes in pandas dataframe.  Optionally number of clusters, algorithm type, and the number of processors can be used to train.  These are set to 4, elkan, and:1 respectively.  It returns a trained kmeans model.
- birch_model: This trains a birch model.  It takes in pandas dataframe.  Optionally threshold and number of clusters.  These are set to 0.01 and 4 respectively.  It returns a trained birch model.
- db_model: This trains a dbscan model.  It takes in pandas dataframe.  It returns a trained dbscan model.
- kp_model: This trains a kprototype model.  It takes in pandas dataframe.  Optionally number of clusters, initialization method, and the number of processors can be used to train.  These are set to 4, Cao, and:1 respectively.  It returns a trained kprototype model.

## timeseries_models: This library provides ML tools that are needed to analyze and visualize data and train/test timeseries models.

### time_series_models: This class provides methods needed to analyze and train/test timeseries models.
- arima_stationarity_test: This runs the advanced ad-fuller stationarity test on a fed dataset.

## map_functions: This file provides methods related to geospatial analysis exploration.
- Left_index: This method calculates the minimum index of a point that can be before it crosses another point that was left of it.
- orientation: This method calculates orientation of a point whether it's left, right, or on another point that was previously left of it.  
- convexHull: This algorithm uses Left_index and orientation to select outermost points in the provided list of points.
- cluster_creator: This method creates clusters based on index_list.  It uses DBSCAN algorithm.
- polygon_creator: This method creates a polygon based on latitude and longitude of a point.
- map_creator: This method creates polygons using polygon_creator for a list of points.
- boundary_test: This method determines whether a list of points are within or on a certain boundary.