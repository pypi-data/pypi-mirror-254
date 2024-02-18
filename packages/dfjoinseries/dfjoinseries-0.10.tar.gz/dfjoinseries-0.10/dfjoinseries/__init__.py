import pandas as pd
import numpy as np
import operator
import functools
from pandas.core.frame import DataFrame


reprf = np.frompyfunc(repr, 1, 1)
strf = np.frompyfunc(str, 1, 1)


def df_to_str(df):
    return df.apply(strf, raw=True)


def df_to_repr(df):
    return df.apply(reprf, raw=True)


def join_series(df, sep=""):
    if sep:
        sep = str(sep)
        return functools.reduce(
            lambda a, b: operator.add(a + sep, df[b]),
            df[df.columns[1:]],
            df[df.columns[0]],
        )
    else:
        return functools.reduce(
            lambda a, b: operator.add(a, df[b]), df[df.columns[1:]], df[df.columns[0]]
        )


def pd_add_str_tools():
    DataFrame.d_to_str = df_to_str
    DataFrame.d_to_repr = df_to_repr
    DataFrame.d_join = join_series
