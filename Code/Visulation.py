import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visulation_as_heatmap(dataframe_avg, totalavg):
    behindComma = 2

    # Identify rows that are completely filled with NaN
    deleted_rows = dataframe_avg.index[dataframe_avg.isna().all(axis=1)].tolist()

    total_non_nan_values = dataframe_avg.notna().sum().sum()

    # Drop rows completely filled with NaN (only on avg dataframe)
    dataframe_avg = dataframe_avg.dropna(how='all')

    # Round the avg dataframe to the specified decimal places
    dataframe_avg = dataframe_avg.round(behindComma)

    # Calculate counts for rows and columns (non-NaN values)
    row_counts = dataframe_avg.notna().sum(axis=1)
    col_counts = dataframe_avg.notna().sum(axis=0)

    # Calculate per-row and per-column averages (safely divide by counts)
    row_sums_avg = (dataframe_avg.sum(axis=1) / row_counts).round(behindComma)
    col_sums_avg = (dataframe_avg.sum(axis=0) / col_counts).round(behindComma)

    # Append row sums to dataframe
    dataframe_avg['Row Sum'] = row_sums_avg

    # Append column sums to dataframe (and set the bottom-right cell)
    col_sums_avg['Row Sum'] = col_sums_avg.sum()
    dataframe_avg.loc['Column Sum'] = col_sums_avg

    # Set overall average in bottom-right cell (consistent with original code)
    dataframe_avg.at['Column Sum', 'Row Sum'] = round(totalavg / total_non_nan_values, behindComma)

    # Create annotation DataFrame from the rounded averages (strings for consistent annotation)
    annot_df = dataframe_avg.astype(str)

    # Plot the heatmap (only using averages)
    fig, ax = plt.subplots(figsize=(10, 8))
    heatmap = sns.heatmap(
        dataframe_avg,
        annot=annot_df,
        fmt='',
        cmap='RdYlGn',
        cbar=False,
        linewidths=.5,
        vmin=0,
        vmax=1,
        annot_kws={"size": 25},
        ax=ax
    )

    # Styling
    plt.title('Translation Success Matrix', fontsize=30, pad=20)
    heatmap.xaxis.set_ticks_position('top')
    heatmap.xaxis.set_label_position('top')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

    # Add heavy separator lines between the data and the summary row/column
    ax.axhline(y=dataframe_avg.shape[0] - 1, color='black', linewidth=6)
    ax.axvline(x=dataframe_avg.shape[1] - 1, color='black', linewidth=6)

    # Display only total average at the bottom (no std deviation)
    plt.text(
        0.5, -0.05,
        f'Total Average: {totalavg:.2f}',
        horizontalalignment='center',
        verticalalignment='bottom',
        transform=plt.gca().transAxes,
        fontsize=18
    )

    plt.show()

    return deleted_rows
