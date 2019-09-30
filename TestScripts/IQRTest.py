import pandas as pd
from CommonScripts.RemoveOutliers import *

# This script will call the remove outliers function and return a cleaned dataset
# Dataset summary has been captured before and after the function call to highlight the differences
dataset = pd.read_csv("/Users/sugatakumarkar/Desktop/DataScience/TestData/Mall_Customers.csv")
print(dataset.describe())
cdataset = outliersiqr(dataset)
print(cdataset.describe())
