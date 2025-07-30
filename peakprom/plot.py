import matplotlib.pyplot as plt


def plot_peaks(df, peaks, x_col, y_col, index_col='index'):
    """
    Plot data and highlight the most prominent peaks.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df[x_col], df[y_col], label='Signal')

    for idx, prominence in peaks.items():
        row = df[df[index_col] == idx]
        plt.plot(row[x_col], row[y_col], 'ro')
        plt.text(row[x_col].values[0], row[y_col].values[0] + 0.05,
                 f"{prominence:.2f}", color='red', fontsize=8, ha='center')

    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title("Prominent Peaks")
    plt.legend()
    plt.tight_layout()
    plt.show()
