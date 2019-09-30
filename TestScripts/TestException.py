
import yaml
from CommonScripts.LogExceptions import logException
import os
from pathlib import Path
from os import path

# this unit test case is for testing the common error logging functionality
try:
    projPath = Path(__file__).parent
    yamlPath = (projPath / "../CommonScripts/config.yaml").resolve()
    if path.exists(yamlPath):
        with open(yamlPath, 'r') as f:
            config = yaml.safe_load(f)
            # input table location
            pathdir = config['tablefilepath']
    else:
        print("path does not exist:"+yamlPath)
except Exception as e:
    logException("From Exception test script"+str(e))


