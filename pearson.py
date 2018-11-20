import math

import scipy.stats as ss

from sample import DiscreteSample
from stats import SampleStats


def __poisson(k, mu):
    return (mu ** k) * (math.e ** (-mu)) / math.factorial(k)


def pearson(sample: DiscreteSample):
    if sample.amount <= 50:
        return None, None, "Sample amount is to small"

    mu = SampleStats(sample).average

    table = []
    for i, actual in enumerate(sample.freq_table.values()):
        expected = sample.amount * __poisson(i, mu)
        table.append((actual, expected))

    classes = len(sample.freq_table.values())
    for i, (actual, expected) in enumerate(table):
        if actual < 5:
            if i == 0:
                table[1] = tuple(map(sum, zip(table[1], (actual, expected))))
                del table[0]
            elif (i + 1) == classes:
                table[i - 1] = tuple(map(sum, zip(table[i - 1], (actual, expected))))
            else:
                p_actual = table[i - 1][0]
                n_actual = table[i + 1][0]
                if p_actual < n_actual:
                    table[i] = tuple(map(sum, zip(table[i], table[i - 1])))
                    del table[i - 1]
                else:
                    table[i] = tuple(map(sum, zip(table[i], table[i + 1])))
                    del table[i + 1]

    res = 0
    for i, (mi, npi) in enumerate(table):
        res += ((mi - npi) ** 2) / npi

    _df = len(table) - 2
    return res, ss.chi2.isf(q=0.05, df=_df), "OK"
