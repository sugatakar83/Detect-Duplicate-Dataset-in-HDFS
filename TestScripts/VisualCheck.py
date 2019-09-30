from VisualizationScripts.BoxPlot import *
from VisualizationScripts.ScatterPlot import *
from VisualizationScripts.DistributionPlot import *
import pandas as pd


# read the csv to create a dataframe
dataset = pd.read_csv("/Users/sugatakumarkar/Desktop/DataScience/TestData/Mall_Customers.csv")

#print(dataset.describe())
print(dataset.info())


# Calling the box plot
boxplotallnum(dataset)

# Calling scatterplot
scatterplotgrouped(dataset, "Age", "Annual Income (k$)")

# Calling the normal plotting function.
distplot(dataset[['Age']])

