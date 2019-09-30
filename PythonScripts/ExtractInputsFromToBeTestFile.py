from pathlib import Path
from os import path
import pandas as pd
import yaml
from fuzzywuzzy import fuzz, process
from CommonScripts.LogExceptions import logException


def inputtablevalues():
    """
    .. module:: extract information from input table
        :platform: Hadoop
        :synopsis: This function will create a 2D array, which will have mean and standard deviation for each column from the input table

    """
    try:
        projPath = Path(__file__).parent
        yamlPath = (projPath / "../CommonScripts/config.yaml").resolve()
        if path.exists(yamlPath):
            with open(yamlPath, 'r') as f:
                config = yaml.safe_load(f)
                # Read the input file from the directory path. File should be in csv format
                pathdir = config['inputtablelocation']
                columnnames = config['inputtablecolumns']
    except Exception as e:
        logException("Exception while reading YAML file in ExtractInputsFromToBeTestFile.py"+" "+str(e))

    inputvalusarray=[]
    # Create the dataframe which will be used for feature determination
    inputdata = pd.read_csv(pathdir)
    # Read only the columns, which has to be considered for the test, from the config file
    # calculate the Mean, Standard Deviation for each of them
    columnarray=[]
    columnarray.append(columnnames)
    try:
        for m in list(inputdata):

            for n in columnarray:

                if fuzz.token_set_ratio(m, n) > 50:
                    inputvalusarraytemp=[]
                    inputvalusarraytemp.append(inputdata[m].mean())
                    inputvalusarraytemp.append(inputdata[m].std())
                    inputvalusarray.append(inputvalusarraytemp)
        return inputvalusarray

    except Exception as e:
        logException("Exception while extracting mean and std in ExtractInputsFromToBeTestFile.py"+" "+str(e))


