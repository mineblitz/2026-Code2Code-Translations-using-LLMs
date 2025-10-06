import pandas as pd
import matplotlib.pyplot as plt

def plot_results(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))

    custom_colors = [
        "orange", "purple", "brown", "pink",
        "cyan", "olive", "teal", "gold", "gray"
    ]

    colors = [custom_colors[i % len(custom_colors)] for i in range(len(df))]
    scatter = plt.scatter(
        df["cost"], df["quality"],
        c=colors,
        s=120
    )

    for i, row in df.iterrows():
        label = None if row["breakPercentage"] in ["GPT Only", "Claude Only"] else str(row["breakPercentage"])
        plt.scatter(
            row["cost"], row["quality"],
            color=colors[i],
            s=120,
            label=label
        )

    for _, row in df.iterrows():
        if row["breakPercentage"] in ["GPT Only"]:
            plt.text(
                row["cost"] + 1.5,
                row["quality"] + 0.0028,
                str(row["breakPercentage"]),
                fontsize=12, fontweight="bold", ha="center"
            )
        if row["breakPercentage"] in ["Claude Only"]:
            plt.text(
                row["cost"] - 2.5,
                row["quality"] + 0.0028,
                str(row["breakPercentage"]),
                fontsize=12, fontweight="bold", ha="center"
            )


    plt.xlabel("complete cost (GPT process + Claude process)", fontsize=18, fontweight="bold")
    plt.ylabel("Translation correctness", fontsize=18, fontweight="bold")
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.ylim(0.88, 1.0)

    plt.legend(
        title="Stop Threshold", fontsize=14, title_fontsize=16,
        scatterpoints=1, markerscale=1.5
    )

    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("results.csv")
    plot_results(df)
