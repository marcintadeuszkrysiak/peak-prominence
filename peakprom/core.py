import pandas as pd
from collections import deque
from .utils import add_index_column, split_into_segments

def find_peaks(df: pd.DataFrame, x_col: str, y_col: str, index_col: str = 'peakprom_index') -> dict:
    if x_col not in df.columns or y_col not in df.columns:
        raise ValueError(f"Expected columns {x_col!r} and {y_col!r} in dataframe; got {list(df.columns)}")

    working = df.copy()
    working = working.sort_values(by=x_col, ignore_index=True)
    if index_col not in working.columns:
        working = add_index_column(working, index_col=index_col)

    peaks = {}
    df_segments = deque([working])

    while df_segments:
        segment = df_segments.popleft()
        y_min = segment[y_col].min()
        filtered = segment[segment[y_col] != y_min]
        if filtered.empty:
            continue

        subsegments = split_into_segments(filtered, index_col=index_col)
        for sub in subsegments:
            y_high = sub[y_col].max()
            y_high_index = sub.loc[sub[y_col].idxmax(), index_col]
            if y_high_index not in peaks:
                peaks[y_high_index] = y_high - y_min
        df_segments.extend(subsegments)

    return peaks  # internal index -> prominence


def peaks_dataframe(df: pd.DataFrame, x_col: str, y_col: str, index_col: str = 'peakprom_index') -> pd.DataFrame:
    # Prepare the same working copy for consistency
    working = df.copy()
    working = working.sort_values(by=x_col, ignore_index=True)
    if index_col not in working.columns:
        working = add_index_column(working, index_col=index_col)

    peaks = find_peaks(working, x_col=x_col, y_col=y_col, index_col=index_col)

    # Speed up lookup by setting index
    working_indexed = working.set_index(index_col, drop=False)
    rows = []
    for idx, prom in peaks.items():
        row = working_indexed.loc[idx]
        rows.append({
            x_col: row[x_col],
            y_col: row[y_col],
            'prominence': prom,
            'index': idx
        })
    return pd.DataFrame(rows).sort_values('prominence', ascending=False)
