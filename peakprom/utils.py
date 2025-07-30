import numpy as np
import pandas as pd

def add_index_column(df, index_col='index'):
    df = df.copy()
    df[index_col] = np.arange(len(df))
    return df

def split_into_segments(df, index_col='index'):

    breaks = df[index_col].diff() != 1
    group_id = breaks.cumsum()
    return [segment for _, segment in df.groupby(group_id)]
