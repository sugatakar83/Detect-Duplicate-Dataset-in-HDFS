from pyspark.sql import HiveContext
import yaml
from fuzzywuzzy import fuzz
from PythonScripts.RMSEofArrays import rmseofarrays
import numpy as np
from PythonScripts.ExtractInputsFromToBeTestFile import inputtablevalues
from CommonScripts.LogExceptions import logException
from pathlib import Path
from os import path

# Creating sql context for reading data from Hive
sqlContext = HiveContext(sc)
# Read the config file to get the path where table names are stored along with the fields
try:
    projPath = Path(__file__).parent
    yamlPath = (projPath / "../CommonScripts/config.yaml").resolve()
    if path.exists(yamlPath):
        with open(yamlPath, 'r') as f:
            configfile = yaml.safe_load(f)
            filepath = configfile['tablefilepathcoulmnmatch']
            filenameContent = configfile['filenamecontent']
            filecolumnstomatch = configfile['inputtablecolumns']
except Exception as e:
    logException("Error in reading YAML file in TableDataAnalysisForDuplicacy.py"+" "+str(e))

# Create a 2D array for the features from the input dataframe, which has to be tested
input_features_arr = inputtablevalues()
# Create the array for the input columns from the to be tested file
columnarray=[]
columnarray.append(filecolumnstomatch)

try:
    # Read each table from the file which has been created after column matching
    readfile = open(filepath+"colmatchingtables.txt")
    while True:
        line = readfile.readline()
        tableName = line.replace(filenameContent, '')
        # Create the sql dataframe from Hive table
        data = sqlContext.table(tableName)
        # Select the columns which are not string type; remove them and create a numerical only dataframe
        columnList = [item[0] for item in data.dtypes if item[1].startswith('string') == False]
        data_number_only = data.selectExpr(columnList).cache()
        # Fill the NA values with 0 for all columns
        data_number_only = data_number_only.fillna(0)
        # Get the approx row count
        cntInterval = data_number_only.rdd.countApprox(timeout=300000, confidence=.1)
        # Create the sampled dataframe if row count is more than a million
        if cntInterval > 1000000:
            # consider 20% data of equal probability weight (None) with no replacement (False)
            sampledData = data_number_only.sample(False, .2, None)
        elif cntInterval > 10000000:
            sampledData = data_number_only.sample(False, .1, None)
        else:
            sampledData = data_number_only
        # Convert pyspark dataframe to pandas dataframe
        sampledPdDf = sampledData.toPandas().astype(float)
        # Selecting the columns from the base table which all have to be considered for the matching
        # Creating a 2D array which will have mean and variance for each column in a Table
        list_insight = []
        columns = list(sampledPdDf)
        for i in columns:
            for j in columnarray:
                if (fuzz.token_set_ratio(i, j) > 50):
                    # get the mean and standard deviation from the existing table
                    arr = []
                    arr.append(sampledPdDf[i].mean())
                    arr.append(sampledPdDf[i].std())
                    list_insight.append(arr)
        # Calculate the RMSE value between input table's features to existing table's feature
        rmse_val = rmseofarrays(np.array(input_features_arr), np.array(list_insight))
        # Consider as a match if the RMSE value is less than 25
        if 0 <= rmse_val < 25:
            print(line)
        if not line:
            break
    readfile.close()

except Exception as e:
    logException("Error while executing RMSE in TableDataAnalysisForDuplicacy.py"+" "+str(e))




