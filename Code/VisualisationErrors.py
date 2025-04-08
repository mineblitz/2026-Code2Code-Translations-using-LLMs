import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def visulation_as_Error_heatmap(dataframe_avg, NumberofRuns, last_vmax, corner_vmax, deleted_rows):   
    # Delete the rows in deleted_rows and the next row
    for row in deleted_rows:
        if row in dataframe_avg.index:      
                 
            prev_row = dataframe_avg.index.get_loc(row) - 1
            
            if prev_row < len(dataframe_avg):
               dataframe_avg = dataframe_avg.drop(dataframe_avg.index[prev_row])
            dataframe_avg = dataframe_avg.drop(index=row)
    plt.figure(figsize=(14, 12))
    
    # Create a mask for the main heatmap (excluding the last two rows and columns)
    mask_main = np.zeros_like(dataframe_avg, dtype=bool)
    mask_main[-2:, :] = True
    mask_main[:, -2:] = True
    
    mask_last = np.ones_like(dataframe_avg, dtype=bool)
    mask_last[-2:, :] = False
    mask_last[:, -2:] = False
    mask_last[-2:, -2:] = True
        
    # Create a mask for the 2x2 square in the bottom right corner
    mask_corner = np.ones_like(dataframe_avg, dtype=bool)
    mask_corner[-2:, -2:] = False
    
    # Plot the main heatmap
    heatmap_main = sns.heatmap(dataframe_avg, cbar=False, annot=True, cmap='RdYlGn_r', fmt='.1f', linewidths=0.5, 
                               linecolor='gray', annot_kws={"size": 16}, vmin=0, vmax=NumberofRuns, mask=mask_main)
    
    # Plot the last two columns and rows heatmap excluding the 2x2 square
    heatmap_last = sns.heatmap(dataframe_avg, cbar=False, annot=True, cmap='RdYlGn_r', fmt='.1f', linewidths=0.5, 
                               linecolor='gray', annot_kws={"size": 16}, vmin=0, vmax=last_vmax, mask=mask_last)
    
    # Plot the 2x2 square in the bottom right corner
    heatmap_corner = sns.heatmap(dataframe_avg, cbar=False, annot=True, cmap='RdYlGn_r', fmt='.1f', linewidths=0.5, 
                                 linecolor='gray', annot_kws={"size": 16}, vmin=0, vmax=corner_vmax, mask=mask_corner)
    
    plt.title('Translation Success Matrix', fontsize=20, pad=10)

    # Customize the grid lines
    for i in range(2, dataframe_avg.shape[0], 2):
        heatmap_main.axhline(i, color='black', linewidth=2)
    for j in range(2, dataframe_avg.shape[1], 2):
        heatmap_main.axvline(j, color='black', linewidth=2)

    # Set the tick labels to show every second label
    heatmap_main.set_xticks([i for i in range(dataframe_avg.shape[1]) if i % 2 == 1])
    heatmap_main.set_xticklabels([dataframe_avg.columns[i] for i in range(dataframe_avg.shape[1]) if i % 2 == 1], fontsize=16)
    heatmap_main.set_yticks([i for i in range(dataframe_avg.shape[0]) if i % 2 == 1])
    heatmap_main.set_yticklabels([dataframe_avg.index[i] for i in range(dataframe_avg.shape[0]) if i % 2 == 1], fontsize=16, rotation=0)

    # Move the x-axis labels to the top
    heatmap_main.xaxis.set_ticks_position('top')
    heatmap_main.xaxis.set_label_position('top')

    plt.show()
