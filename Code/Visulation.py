import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visulation_as_heatmap(dataframe_avg, dataframe_std_dev, totalavg, std_deviation, spalten_std_deviation, zeilen_std_deviation):
    behindComma = 2
    behindCommaStdDeviation = 2
    
    # Identify rows that are completely filled with NaN
    deleted_rows = dataframe_avg.index[dataframe_avg.isna().all(axis=1)].tolist()
    # print(deleted_rows)

    total_non_nan_values = dataframe_avg.notna().sum().sum()

    # Assuming dataframe_avg has an index that aligns with zeilen_std_deviation
    zeilen_std_deviation_series = pd.Series(zeilen_std_deviation, index=dataframe_avg.index)

    # Delete rows from zeilen_std_deviation
    for row in deleted_rows:
        if row in zeilen_std_deviation_series.index:   
            zeilen_std_deviation_series = zeilen_std_deviation_series.drop(index=row)

    # Convert back to numpy array if needed
    zeilen_std_deviation = zeilen_std_deviation_series.values
    
    # Drop rows completely filled with NaN in both dataframes
    dataframe_avg = dataframe_avg.dropna(how='all')
    dataframe_std_dev = dataframe_std_dev.dropna(how='all')
    
    # Round the dataframes to the specified decimal places
    dataframe_avg = dataframe_avg.round(behindComma)
    dataframe_std_dev = dataframe_std_dev.round(behindCommaStdDeviation)
    
    # Calculate sums for rows and columns, dividing by the number of non-NaN values
    row_counts = dataframe_avg.notna().sum(axis=1)
    col_counts = dataframe_avg.notna().sum(axis=0)
    
    row_sums_avg = (dataframe_avg.sum(axis=1) / row_counts).round(behindComma)
    col_sums_avg = (dataframe_avg.sum(axis=0) / col_counts).round(behindComma)
    
    # Convert spalten_std_deviation and zeilen_std_deviation to Pandas Series
    row_sums_std_dev = (pd.Series(zeilen_std_deviation, index=dataframe_avg.index) / row_counts).round(behindCommaStdDeviation)
    col_sums_std_dev = (pd.Series(spalten_std_deviation, index=dataframe_avg.columns) / col_counts).round(behindCommaStdDeviation)
    
    # Append row sums to dataframe
    dataframe_avg['Row Sum'] = row_sums_avg
    dataframe_std_dev['Row Sum'] = row_sums_std_dev
    
    # Append column sums to dataframe
    col_sums_avg['Row Sum'] = col_sums_avg.sum()
    dataframe_avg.loc['Column Sum'] = col_sums_avg
    
    col_sums_std_dev['Row Sum'] = col_sums_std_dev.sum()
    dataframe_std_dev.loc['Column Sum'] = col_sums_std_dev
    
    dataframe_avg.at['Column Sum', 'Row Sum'] = round(totalavg / total_non_nan_values, behindComma)
    dataframe_std_dev.at['Column Sum', 'Row Sum'] = round(std_deviation / total_non_nan_values, behindCommaStdDeviation)


    # Create combined dataframe for annotations
    combined = dataframe_avg.astype(str) + " (" + dataframe_std_dev.astype(str) + ")"
    
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    heatmap = sns.heatmap(dataframe_avg, annot=combined, fmt='', cmap='RdYlGn', cbar=False, linewidths=.5, vmin=0, vmax=1, annot_kws={"size": 14}, ax=ax)
    
    # Set title with larger font size and additional padding
    plt.title('Translation Success Matrix', fontsize=20, pad=20)
    
    # Move the x-axis labels to the top and increase their font size
    heatmap.xaxis.set_ticks_position('top')
    heatmap.xaxis.set_label_position('top')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    
    # Add horizontal line to separate the last row
    ax.axhline(y=dataframe_avg.shape[0] - 1, color='black', linewidth=6)
    
    # Add vertical line to separate the last column
    ax.axvline(x=dataframe_avg.shape[1] - 1, color='black', linewidth=6)
    
    # Display total average and standard deviation at the bottom, centered with larger font size
    plt.text(0.5, -0.05, f'Total Average: {totalavg:.2f}, Standard Deviation: {std_deviation:.2f}', 
             horizontalalignment='center', verticalalignment='bottom', transform=plt.gca().transAxes, fontsize=18)

    plt.show()

    return deleted_rows
