from peakprom.core import find_prominence_peaks
import pandas as pd

def test_find_prominence_peaks_runs():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': [0, 1, 0]})
    df['index'] = df.index
    peaks = find_prominence_peaks(df, 'x', 'y')
    assert isinstance(peaks, dict)
