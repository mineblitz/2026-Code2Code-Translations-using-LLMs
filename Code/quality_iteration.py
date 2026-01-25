import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_aggregated_dataframe(experiment: int, run: str, ratio: bool = False):
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')

    summed_results = []

    prefix, last_num_str = run.split('_')
    last_num = int(last_num_str)
    
    for i in range(last_num + 1):
        current_run = f"{prefix}_{i}"
        executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{current_run}')
        dataFrame_filepath = os.path.join(executionDir, "compilation_matrix_sum")

        if not os.path.exists(dataFrame_filepath):
            raise FileNotFoundError(f"Average dataframe file not found: {dataFrame_filepath}")

        dataframe = pd.read_csv(dataFrame_filepath, index_col=0)   
        if not ratio: 
            summed_results.append(dataframe.sum().sum() / 3500 )    # to get quality in percentage  
        else:
            summed_results.append(dataframe.sum().sum() / (3500) / (i + 1)) # to get ratio

    return summed_results

def load_single_dataframe(experiment: int, run: str):
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')

    result = []

    executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{run}')
    dataFrame_filepath = os.path.join(executionDir, "compilation_matrix_sum")

    if not os.path.exists(dataFrame_filepath):
        raise FileNotFoundError(f"Average dataframe file not found: {dataFrame_filepath}")

    dataframe = pd.read_csv(dataFrame_filepath, index_col=0)    
    result = dataframe.sum().sum() / 3500 # to get quality

    return result

# ratio = qualität / anzahl aufrufe
# quality = quality / anzahl aufrufe

def plot_data(QualityPointsStart, QualityPointsEnd, QualityArray, RatioArray):
    """
    QualityPointsStart: list of 4 floats (one per experiment)
    QualityPointsEnd:   list of 4 floats (one per experiment)
    QualityArray:  list of 4 lists (quality curves)
    RatioArray:    list of 4 lists (ratio curves)
    """

    labels = ["OG", "CS", "GG", "OC"]
    colors = ["#390099", "#9E0059", "#FF0054", "#E47A00"]

    fig, ax_quality = plt.subplots(figsize=(10, 6))
    ax_ratio = ax_quality.twinx()

    # Log-scaled x-axis (base 2)

    ax_quality.set_ylabel("Quality")
    ax_quality.set_yscale("logit")
    ax_quality.set_ylim(0.5, 0.9999)
    quality_tick_positions = [0.5, 0.65, 0.8, 0.9, 0.95, 0.99, 0.999, 0.9999]
    quality_tick_labels   = ["0.5", "0.65", "0.8", "0.9", "0.95", "0.99", "0.999", "1"]
    ax_quality.set_yticks(quality_tick_positions)
    ax_quality.set_yticklabels(quality_tick_labels)

    ax_ratio.set_ylabel("Ratio")
    ax_ratio.set_yscale("symlog", linthresh=0.02)
    ax_ratio.set_ylim(0, 1)
    ratio_ticks = [0, 0.01, 0.05, 0.1, 0.2, 0.5, 1]
    ax_ratio.set_yticks(ratio_ticks)
    ax_ratio.set_yticklabels(ratio_ticks)

    xticks = [1e-3, 1, 2, 4, 6, 10, 14, 20, 26, 34, 44]
    xtick_labels = [0, 1, 2, 4, 6, 10, 14, 20, 26, 34, 44]
    ax_quality.set_xticks(xticks)
    ax_quality.set_xticklabels(xtick_labels)
    ax_quality.set_xlabel("Numeer of requests")

    
    xValuesEnd = [44, 19, 11, 6]

    # Plot lines and points
    for i in range(4):
        # X values from index (start at 1 for log scale)
        if i == 2:
            QualityArray[i][0] = 0.867
        x_quality = np.arange(1, len(QualityArray[i]) + 1)
        x_ratio = np.arange(1, len(RatioArray[i]) + 1)

        # Quality line
        ax_quality.plot(
            x_quality,
            QualityArray[i],
            color=colors[i],
            linewidth=2,
            label=f"{labels[i]} Quality"
        )

        # Ratio dashed line
        ax_ratio.plot(
            x_ratio,
            RatioArray[i],
            color=colors[i],
            linestyle="--",
            linewidth=2,
            label=f"{labels[i]} Ratio"
        )

        if i == 2:
            QualityPointsStart[i] = 0.867
        # Quality point
        ax_quality.scatter(
            1,
            QualityPointsStart[i],
            color=colors[i],
            marker="o",
            s=80
        )

        # Ratio point (cross)
        ax_quality.scatter(
            xValuesEnd[i],
            QualityPointsEnd[i],
            color=colors[i],
            marker="o",
            s=80
        )

        ax_quality.annotate(
            f"{QualityPointsStart[i]:.3f}",
            (1, QualityPointsStart[i]),
            textcoords="offset points",
            xytext=(-28, 6),
            fontsize=10,
            color=colors[i]
        )

        # End point label
        ax_quality.annotate(
            f"{QualityPointsEnd[i]:.3f}",
            (xValuesEnd[i], QualityPointsEnd[i]),
            textcoords="offset points",
            xytext=(5, 5),
            fontsize=10,
            color=colors[i]
        )

    # Legend (combined)
    handles1, labels1 = ax_quality.get_legend_handles_labels()
    handles2, labels2 = ax_ratio.get_legend_handles_labels()
    ax_quality.legend(handles1 + handles2, labels1 + labels2, loc="best")

    ax_quality.grid(True, which="major", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    QualityPointsStart = []
    QualityPointsStart.append(load_single_dataframe(6, "2_0"))
    QualityPointsStart.append(load_single_dataframe(14, "1_0"))
    QualityPointsStart.append(load_single_dataframe(20, "1_0"))
    QualityPointsStart.append(load_single_dataframe(23, "1_0"))

    QualityPointsEnd = []
    QualityPointsEnd.append(load_single_dataframe(6, "2_43"))
    QualityPointsEnd.append(load_single_dataframe(14, "1_18"))
    QualityPointsEnd.append(load_single_dataframe(20, "1_10"))
    QualityPointsEnd.append(load_single_dataframe(23, "1_5"))

    QualityArray = []
    QualityArray.append(load_aggregated_dataframe(6, "2_43"))
    QualityArray.append(load_aggregated_dataframe(14, "1_18"))
    QualityArray.append(load_aggregated_dataframe(20, "1_10"))
    QualityArray.append(load_aggregated_dataframe(23, "1_5"))

    
    RatioArray = []
    RatioArray.append(load_aggregated_dataframe(6, "2_43", ratio=True))
    RatioArray.append(load_aggregated_dataframe(14, "1_18", ratio=True))
    RatioArray.append(load_aggregated_dataframe(20, "1_10", ratio=True))
    RatioArray.append(load_aggregated_dataframe(23, "1_5", ratio=True))

    plot_data(QualityPointsStart, QualityPointsEnd, QualityArray, RatioArray)