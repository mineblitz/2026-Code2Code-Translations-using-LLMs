import os
import pandas as pd
from glob import glob


def sum_error_dataframes(experiment: int, run: str) -> None:
    """
    For a given experiment and run, find all error CSV files,
    sum them per error type, and write 4 summary CSVs.
    """

    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')
    executionDir = os.path.join(
        fullProjectDir,
        f'logsHumanEvalXExp{experiment}Run{run}'
    )

    error_types = {
        "test_failure": "test_failure",
        "runtime_error": "runtime_error",
        "infinitie_loop": "infinite_loop",
        "compilation_failed": "compilation_failed",
        "compilation_matrix": "compilation_matrix"
    }

    for error_name, pattern in error_types.items():
        output_path = os.path.join(
            executionDir,
            f"{error_name}_sum"
        )

        # >>> SKIP if sum already exists
        if os.path.exists(output_path):
            continue

        file_pattern = os.path.join(executionDir, f"{pattern}*")
        files = sorted(glob(file_pattern))

        if not files:
            raise FileNotFoundError(f"No files found for {error_name}: {file_pattern}")

        summed_df = None

        for filepath in files:
            if "_avg" in filepath:
                continue
            if "_std_deviation" in filepath:
                continue
            df = pd.read_csv(filepath, index_col=0)

            if summed_df is None:
                summed_df = df
            else:
                summed_df = summed_df.add(df, fill_value=0)



        summed_df.to_csv(output_path)


def call_sum_for_runs(experiment_runs):
    """
    Call sum_error_dataframes for all runs from 0 to the last number in the run string.
    
    experiment_runs: list of tuples (experiment_number, run_string)
    e.g. [(6, "2_43"), (14, "1_18"), (20, "1_10"), (23, "1_5")]
    """
    for experiment, run_str in experiment_runs:
        # Split the run string into prefix and last number
        prefix, last_num_str = run_str.split('_')
        last_num = int(last_num_str)
        
        # Call function for all runs from 0 to last_num inclusive
        for i in range(last_num + 1):
            current_run = f"{prefix}_{i}"
            sum_error_dataframes(experiment=experiment, run=current_run)

            
if __name__ == "__main__":
    # Example usage
    sum_error_dataframes(experiment=5, run="1")
    sum_error_dataframes(experiment=5, run="2")
    sum_error_dataframes(experiment=13, run="1")
    sum_error_dataframes(experiment=19, run="1")
    sum_error_dataframes(experiment=22, run="1")
    
    experiment_runs = [
        (6, "2_43"),
        (14, "1_18"),
        (20, "1_10"),
        (23, "1_5")
    ]

    call_sum_for_runs(experiment_runs)