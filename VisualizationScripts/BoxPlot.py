import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Boxplot for a single column. parameters to be passed for this function are dataset and the column.
def boxplotsingle(dset,col):
    """
    .. module:: box plot visualization
        :platform: Hadoop
        :synopsis: this function will produce a box plot of a given column from a dataset using seaborn and matplotlib

    """
    sns.set(style="whitegrid")
    sns.boxplot(x=dset[col])
    plt.show()

# Boxplot for grouped categorical variables. parameters to be passed for this function are dataset and the column
# for X asis and the column for Y axis respectively.
def boxplotgrouped(dset, colx, coly):
    """
    .. module:: box plot visualization
        :platform: Hadoop
        :synopsis: this function will produce a dependent box plot for col X with col Y from a dataset using seaborn and matplotlib

    """
    sns.set(style="whitegrid")
    sns.boxplot(x=colx, y=coly, data=dset)
    plt.show()

# Boxplot for each numerical columns in a dataset
# consider Orientation as Horizontal
def boxplotallnum(dset):
    """
    .. module:: box plot visualization
        :platform: Hadoop
        :synopsis: this function will produce a box plot for all columns from a dataset using seaborn and matplotlib

    """
    sns.set(style="whitegrid")
    sns.boxplot(data=dset, orient="h", palette="Set2")
    plt.show()

