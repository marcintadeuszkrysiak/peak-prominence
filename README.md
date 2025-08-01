# peakprom — Detect Prominent Peaks in Irregular Data

**peakprom** is a lightweight Python tool for detecting prominent peaks in datasets, even when the data is irregularly spaced.  
It’s designed for scientists, analysts, and hobbyists who want a simple way to measure **peak prominence** in time series, spectra, or periodograms.

---

## Features
- Detect peaks **with prominence values**.
- Works with **irregularly spaced data** (not just evenly sampled).
- Returns results as a Python `dict` **or** as a clean `pandas.DataFrame`.
- Built-in **plotting function** to visualize detected peaks.
- Perfect for **spectral analysis**, e.g., Lomb–Scargle periodograms.

---

## Installation

**From GitHub (latest version)**:
```bash
pip install git+https://github.com/marcintadeuszkrysiak/peak-prominence.git
```

## Quick start
```bash
import pandas as pd
from peakprom import find_peaks, peaks_dataframe, plot_peaks

# Example dataset
df = pd.DataFrame({
    "x": [0, 1, 2, 3, 4, 5, 6],
    "y": [0, 2, 0, 3, 0, 1, 0]
})

# Detect peaks
peaks = find_peaks(df, x_col="x", y_col="y")
print("Detected peaks (index → prominence):", peaks)
```
# Get peaks as a DataFrame
peaks_df = peaks_dataframe(df, x_col="x", y_col="y")
print(peaks_df)

# Plot data with peaks marked
plot_peaks(df, x_col="x", y_col="y")

