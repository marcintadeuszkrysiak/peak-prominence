import matplotlib.pyplot as plt
from .core import peaks_dataframe
from .utils import add_index_column

def plot_peaks(
    df,
    x_col,
    y_col,
    index_col='peakprom_index',
    figsize=(10, 5),
    annotate=True,
    annotate_text=x
    peak_marker='o',
    peak_color='red',
    data_label='Data',
    peak_label='Peak',
    top_n=None,
    **kwargs,
):
    working = df.copy()
    working = working.sort_values(by=x_col, ignore_index=True)
    if index_col not in working.columns:
        working = add_index_column(working, index_col=index_col)

    peaks_df = peaks_dataframe(working, x_col=x_col, y_col=y_col, index_col=index_col)
    if top_n is not None:
        peaks_df = peaks_df.head(top_n)

    plt.figure(figsize=figsize)
    plt.plot(working[x_col], working[y_col], label=data_label, **kwargs)

    first = True
    for _, row in peaks_df.iterrows():
        = row[x_col]
        y = row[y_col]
        prominence = row['prominence']
        label = peak_label if first else None
        plt.plot(x, y, marker=peak_marker, color=peak_color, linestyle='', label=label)
        if annotate:
            plt.annotate(f"{annotate_text}", (x, y),
                         textcoords="offset points", xytext=(0, 6),
                         ha='center', fontsize=8, color=peak_color)
        first = False

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title("Detected Peaks with Prominence")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
