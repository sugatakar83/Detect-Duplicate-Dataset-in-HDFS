from itertools import combinations as comb
import numpy as np
from scipy.stats import mannwhitneyu


def exact_mc_perm_test(xs, ys, nmc):
    """
    .. module:: permutation test for non-Gaussian distribution using monte-carlo method
        :platform: Hadoop
        :synopsis: nonparametric test procedures to test the null hypothesis
        :xs: input array of the column values for an existing table
        :ys: input array of the column values for to be tested table
        :nmc: number of replication for the permutation test
        :returns: results from permutation test, contains all permutations

    """
    n, k = len(xs), 0
    diff = np.abs(np.mean(xs) - np.mean(ys))
    zs = np.concatenate([xs, ys])
    for j in range(nmc):
        np.random.shuffle(zs)
        k += diff < np.abs(np.mean(zs[:n]) - np.mean(zs[n:]))
    return k / nmc
