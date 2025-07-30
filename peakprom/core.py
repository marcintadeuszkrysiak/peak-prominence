import pandas as pd
from .utils import split_into_segments

def find_prominence_peaks(df, x_col, y_col, index_col='index'):

    peaks = {}
    df_segments = [df]

    while df_segments:
        segment = df_segments.pop(0)
        y_min = segment[y_col].min()

        # Remove rows at current lowest level
        filtered = segment[segment[y_col] != y_min]

        if filtered.empty:
            continue

        # Split into disconnected segments
        new_segments = split_into_segments(filtered, index_col=index_col)

        for new in new_segments:
            y_high = new[y_col].max()
            y_high_index = new.loc[new[y_col].idxmax(), index_col]

            if y_high_index not in peaks:
                prominence = y_high - y_min
                peaks[y_high_index] = prominence

        df_segments.extend(new_segments)

    return peaks
