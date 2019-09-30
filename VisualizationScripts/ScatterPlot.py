import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Scatterplot for grouped categorical variables. parameters to be passed for this function are dataset and the column
# for X asis and the column for Y axis respectively.
def scatterplotgrouped(dset, colx, coly):
    """
    .. module:: code for generating scatter plot
        :platform: Hadoop
        :synopsis: using seaborn and matplotlib, this function will generate a scatter plot for a given dataset with X and Y axis parameters

    """
    sns.set(style="darkgrid")
    sns.scatterplot(x=colx, y=coly, data=dset)
    plt.show()