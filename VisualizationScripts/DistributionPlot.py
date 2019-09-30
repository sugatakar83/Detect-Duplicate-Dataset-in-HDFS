import seaborn as sns
import matplotlib.pyplot as plt

# Gives the univariate distribution details of a column in a dataset
# mentioning histogram and rug plot is optional
def distplot(dset):
    """
    .. module:: distribution plot for a given dataset
        :platform: Hadoop
        :synopsis: this function will give a visual image of how different columns are distributed in a dataset

    """
    sns.distplot(dset, hist=True, rug=True)
    plt.show()
