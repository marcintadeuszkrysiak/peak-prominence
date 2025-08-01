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
