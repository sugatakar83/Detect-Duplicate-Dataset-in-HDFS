from CommonScripts.LogExceptions import logException
from pandas.api.types import is_numeric_dtype

def outliersiqr(dset):
    """
    .. module:: remove outliers
        :platform: Hadoop
        :synopsis: Using IQR method, this fuction will remove the 5% records from the beginning and from the end of a shorted list

    """
    low = .05
    high = .95
    quartildiff = dset.quantile([low, high])
    try:

        for name in list(dset.columns):
            if is_numeric_dtype(dset[name]):
                # for the neumeric type columns, filter the date which are under 5%-95% distribution
                dset = dset[(dset[name] > quartildiff.loc[low, name]) & (dset[name] < quartildiff.loc[high, name])]
        return dset
    except Exception as e:
        logException(str(e))




