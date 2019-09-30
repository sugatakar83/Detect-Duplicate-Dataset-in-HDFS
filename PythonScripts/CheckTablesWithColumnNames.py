# fuzz is used to compare TWO strings
from fuzzywuzzy import fuzz
# python packages for file handling
import os
from pathlib import Path
from os import path
# python package for reading config from a yaml file
import yaml
from CommonScripts.LogExceptions import logException


def checkTableWithCoulmnNames():
    """
    .. module:: compare two tables with column names
        :platform: Hadoop
        :synopsis: Using Lavenstein distance algorithm, the function will measure the likeliness between two string arrays

    """
    try:
        # reading the input files which are collected from the existing hadoop environment and having column names
        projPath = Path(__file__).parent
        yamlPath = (projPath / "../CommonScripts/config.yaml").resolve()
        if path.exists(yamlPath):
            with open(yamlPath, 'r') as f:
                config = yaml.safe_load(f)
                # input table location
                pathdir = config['tablefilepath']
                # output table(s) store location. this will store a file with matching table names based on column names
                pathmatching = config['tablefilepathcoulmnmatch']
                # sample test data which will be validated against the collected
                sampleData = config['inputtablecolumns']
    except Exception as e:
        logException("Exception occured while reading YAML file in CheckTablesWithColumnNames.py"+" "+str(e))
# reading all files from the stored location iteratively which contains the column names for each table
    for filename in os.listdir(pathdir):
        with open(os.path.join(pathdir, filename)) as f:
            # creating an array for all the column names present in the file for the given table
            try:
                lines = f.readlines()
                # transferring the array to a string type for fuzzy matching
                arrElements = ''.join(lines).replace("\n", ",").strip()

                # find the approx match from the historical data by using Levenshtein Distance algorithm
                # the algorithm is implemented in fuzzywuzzy python package, which is used
                # higher the match, more will be the ratio
                ratio = fuzz.token_set_ratio(arrElements, sampleData)
                # consider the tables where ratio is more than 75
                if ratio > 75:
                    print(sampleData, arrElements, ratio)
                    print(filename)
                    # write the matching table names in preconfigured path
                    filetowrite = open(pathmatching + "colmatchingtables.txt", "w")
                    filetowrite.write(filename + "\n")
            except Exception as e:
                logException("Exception while comparing with column names in CheckTablesWithColumnNames.py"+" "+str(e))

checkTableWithCoulmnNames()