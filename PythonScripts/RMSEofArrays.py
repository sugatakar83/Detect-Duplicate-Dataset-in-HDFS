import numpy as np
from CommonScripts.LogExceptions import logException

# this function will return root mean square error for two given arrays
def rmseofarrays(prediction,target):
    """
    .. module:: determine root mean square error between two numerical arrays
        :platform: Hadoop
        :synopsis: RMSE is a measure of how spread the data points are from the regression line
        :prediction: first argument. 2D array of the existing table's mean and std
        :target: second argument. 2D array of the input table's mean and std
        :returns: the mean(RMSE) of the two inputs

    """
    try:
        return np.sqrt(((prediction-target)**2).mean())

    except Exception as e:
        logException("Exception raised while calculating RMSE in RMSEofArrays.py"+" "+str(e))
