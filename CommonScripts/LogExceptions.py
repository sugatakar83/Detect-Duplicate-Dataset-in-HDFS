from datetime import datetime
import yaml
from os import path
import os


def logException(msg):
    # open the file for writing. Create it, if not exist
    with open('../CommonScripts/config.yaml', 'r') as f:
        configfile = yaml.safe_load(f)
        excpfilepath = configfile['exceptionloggingfilepath']
        logfilesize = configfile['logfilesizeinBytes']
        now = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        # check the file size before writing. If more than threshold size then purge it.
        if path.exists(excpfilepath+"log.dat"):
            if os.path.getsize(excpfilepath+"log.dat") > logfilesize:
                excpfile = open(excpfilepath+"log.dat", "r+")
                excpfile.truncate()
            else:
                fileToWrite = open(excpfilepath + "log.dat", "a+")
                fileToWrite.write(dt_string + msg + " " + "\r\n")
        else:
            fileToWrite = open(excpfilepath + "log.dat", "a+")
            fileToWrite.write(dt_string+msg+" "+"\r\n")
