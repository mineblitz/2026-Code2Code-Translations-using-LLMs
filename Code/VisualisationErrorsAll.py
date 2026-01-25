import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_avg_dataframe(experiment: int, run: int) -> pd.DataFrame:
    """
    Load the average dataframe for a given experiment and run.
    """
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')
    executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{run}')
    compile_filepath = os.path.join(executionDir, 'compilation_failed_sum')
    runtime_filepath = os.path.join(executionDir, 'runtime_error_sum')
    test_filepath = os.path.join(executionDir, 'test_failure_sum')
    timeout_filepath = os.path.join(executionDir, 'infinitie_loop_sum')

    if not (os.path.exists(compile_filepath) and os.path.exists(runtime_filepath) and os.path.exists(test_filepath) and os.path.exists(timeout_filepath)):
        raise FileNotFoundError(f"Average dataframe file not found: {compile_filepath} or {runtime_filepath} or {test_filepath} or {timeout_filepath}")

    dataframe_compile = pd.read_csv(compile_filepath, index_col=0)    
    dataframe_compile = dataframe_compile.drop(dataframe_compile.index[[0, 2, 5, 7]])
    dataframe_runtime = pd.read_csv(runtime_filepath, index_col=0)    
    dataframe_runtime = dataframe_runtime.drop(dataframe_runtime.index[[0, 2, 5, 7]])
    dataframe_test = pd.read_csv(test_filepath, index_col=0)
    dataframe_test = dataframe_test.drop(dataframe_test.index[[0, 2, 5, 7]])
    dataframe_timeout = pd.read_csv(timeout_filepath, index_col=0)
    dataframe_timeout = dataframe_timeout.drop(dataframe_timeout.index[[0, 2, 5, 7]])

    dataframe_combined = combine_erros_for_one_dataframe([dataframe_compile, dataframe_runtime, dataframe_test, dataframe_timeout])
    return dataframe_combined

def combine_erros_for_one_dataframe(dataFrameList: list) -> pd.DataFrame:
    combined_rows = []

    num_rows = len(dataFrameList[0])
    num_cols = len(dataFrameList[0].columns)


    # for each row in that dataframe
    for i in range(num_rows):
        # for each dataframe
        for df in dataFrameList:
            row_data = []
            for j in range(num_cols):
                row_data.append(df.iloc[i, j])
            combined_rows.append(row_data)

    df_combined = pd.DataFrame(
        combined_rows,
        columns=dataFrameList[0].columns
    )

    return df_combined


def sum_every_4(df: pd.DataFrame) -> pd.DataFrame:
    """
    For each column, sum every 4th row separately:
    rows 0,4,8,... → sum1
    rows 1,5,9,... → sum2
    rows 2,6,10,... → sum3
    rows 3,7,11,... → sum4

    Returns the original df with 4 additional rows at the end.
    """
    sums = []

    # There will be 4 sums
    for offset in range(4):
        sums.append(df.iloc[offset::4, :].sum())

    # Create a DataFrame for the 4 new rows
    sum_df = pd.DataFrame(sums, index=[f'Sum_{i+1}' for i in range(4)])

    # Append to the original dataframe
    return pd.concat([df, sum_df])

def sum_cols(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a column at the end containing the average of each row 
    """
    col_avg = df.sum(axis=1) 
    df['Total'] = col_avg
    return df

def combine_dataframes(dataFrameList: list) -> pd.DataFrame:
    """
    combine the list of dataframes into a single dataframe
    """
    combined_rows = []
    num_rows = len(dataFrameList[0])
    num_cols = len(dataFrameList[0].columns)
    
    # For each row in the source dataframes
    for i in range(num_rows):
        row_data = []
        # For each column in the source dataframes
        for j in range(num_cols):
            # For each dataframe
            for df in dataFrameList:
                row_data.append(df.iloc[i, j])
        combined_rows.append(row_data)
    
    df = pd.DataFrame(combined_rows)
    
    # Create column names with only subcols repeated
    languages = ['C', 'C++', 'C#', 'Java', 'JavaScript', 'Pascal', 'Python', 'Haskell', 'Total']
    subcols = ['OG', 'CS', 'GG', 'OC'] # OG = OpenAI GPT4o, CS = Claude Sonet, Google Gemini GG, OC = OpenAI Codex 
    
    # Dynamically create column names based on actual number of columns
    col_names = []
    
    for lang in languages:
        for subcol in subcols:
            if subcol == "OG":
                col_names.append("                 " + lang + "\n"+ subcol)
            else:
                col_names.append(" \n"+ subcol)
                    
    # Set simple column names (only subcols, no MultiIndex)
    if len(col_names) == len(df.columns):
        df.columns = col_names
    
    return df

def visualize_combined_matrix(dataframe: pd.DataFrame):
    NumberofRuns = 125
    last_vmax = 4 * NumberofRuns
    corner_vmax = 7* last_vmax

    plt.figure(figsize=(16, 9))
    
    # Create a mask for the main heatmap (excluding the last two rows and columns)
    mask_main = np.zeros_like(dataframe, dtype=bool)
    mask_main[-4:, :] = True
    mask_main[:, -4:] = True
    
    mask_last = np.ones_like(dataframe, dtype=bool)
    mask_last[-4:, :] = False
    mask_last[:, -4:] = False
    mask_last[-4:, -4:] = True
        
    # Create a mask for the 4x4 square in the bottom right corner
    mask_corner = np.ones_like(dataframe, dtype=bool)
    mask_corner[-4:, -4:] = False
    
    # Plot the main heatmap
    heatmap_main = sns.heatmap(dataframe, cbar=False, annot=True, cmap='RdYlGn_r', fmt='d', linewidths=0.5, 
                               linecolor='gray', annot_kws={"size": 14}, vmin=0, vmax=NumberofRuns, mask=mask_main)
    
    # Plot the last two columns and rows heatmap excluding the 2x2 square
    heatmap_last = sns.heatmap(dataframe, cbar=False, annot=True, cmap='RdYlGn_r', fmt='d', linewidths=0.5, 
                               linecolor='gray', annot_kws={"size": 14}, vmin=0, vmax=last_vmax, mask=mask_last)
    
    # Plot the 2x2 square in the bottom right corner
    heatmap_corner = sns.heatmap(dataframe, cbar=False, annot=True, cmap='RdYlGn_r', fmt='d', linewidths=0.5, 
                                 linecolor='gray', annot_kws={"size": 14}, vmin=0, vmax=corner_vmax, mask=mask_corner)
    

    # Customize the grid lines
    for i in range(4, dataframe.shape[0], 4):
        heatmap_main.axhline(i, color='black', linewidth=2)
    for j in range(4, dataframe.shape[1], 4):
        heatmap_main.axvline(j, color='black', linewidth=2)

    # Set the tick labels to show every second label
    # heatmap_main.set_xticks([i for i in range(dataframe.shape[1]) if i % 4 == 2])
    heatmap_main.set_xticklabels([dataframe.columns[i] for i in range(dataframe.shape[1])], fontsize=13)
    heatmap_main.set_yticks([i for i in range(dataframe.shape[0]) if i % 4 == 2])
    heatmap_main.set_yticklabels([dataframe.index[i] for i in range(dataframe.shape[0]) if i % 4 == 2], fontsize=16, rotation=90)

    # Move the x-axis labels to the top
    heatmap_main.xaxis.set_ticks_position('top')
    heatmap_main.xaxis.set_label_position('top')

        # Define the regions to fill with white and write 'n/a'
    na_regions = [
        (4,0,7,3),
        (12,4,15,7),
        (16,8,19,11),
        (24,12,27,15)
    ]

    for r0, c0, r1, c1 in na_regions:
        # Fill the entire region white
        width = c1 - c0 + 1
        height = r1 - r0 + 1
        heatmap_main.add_patch(
            plt.Rectangle(
                (r0, c0),   # x = col, y = row
                width,
                height,
                fill=True,
                color='white',
                ec='gray',
                lw=0.5
            )
        )
        # Write 'n/a' once, centered in the region
        heatmap_main.text(
            r0 + width/2,
            c0 + height/2,
            'N/A',
            ha='center',
            va='center',
            color='black',
            fontsize=12
        )

    plt.tight_layout()
    plt.show()

def main():
    """
    Load the experiments and create the combined visualization.
    """
    # experiments = [(5, 1), (13, 1), (19, 1), (22, 1)] # 1TUrn
    experiments = [(6, "2_43"), (14, "1_18"), (20, "1_10"), (23, "1_5")] #Retranslate
    dataframes = []
    
    for exp, run in experiments:
        try:
            df = load_avg_dataframe(exp, run)
            df = sum_every_4(df)
            df = sum_cols(df)
            dataframes.append(df)
            print(f"Loaded Exp{exp}Run{run}")
        except FileNotFoundError as e:
            print(f"Error loading Exp{exp}Run{run}: {e}")
    
    if dataframes:
        combined_matrix = combine_dataframes(dataframes)        
        # Set row labels
        combined_matrix.index = ['C++','C++','C++','C++', 'Java','Java','Java','Java', 'JavaScript','JavaScript','JavaScript','JavaScript', 'Python','Python','Python','Python', 'Total', 'Total', 'Total', 'Total']
                # print("\nCombined Matrix:")
        # print(combined_matrix)
        
        # Visualize the combined matrix
        visualize_combined_matrix(combined_matrix)
    else:
        print("No dataframes loaded.")

if __name__ == "__main__":
    main()

