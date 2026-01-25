import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter

def plot_global_cost_per_percent(flip_axes: bool = False):
    # Beispiel-Daten
    x_gpt = [
        0.6480, 0.7586, 0.7951, 0.8143, 0.8266, 0.8340, 0.8403, 0.8403,
        0.8520, 0.8543, 0.8589, 0.8614, 0.8631, 0.8657, 0.8694, 0.8714,
        0.8729, 0.8757, 0.8774, 0.8780, 0.8789, 0.8800, 0.8817, 0.8831,
        0.8837, 0.8843, 0.8857, 0.8866, 0.8874, 0.8886, 0.8891, 0.8906,
        0.8917, 0.8929, 0.8934, 0.8937, 0.8949, 0.8957, 0.8960, 0.8977,
        0.8989, 0.8997, 0.9000, 0.9000
    ]
    y_gpt = [
        0.86, 1.26, 1.53, 1.76, 1.97, 2.17, 2.36, 2.54,
        2.72, 2.89, 3.05, 3.21, 3.37, 3.52, 3.68, 3.83,
        3.97, 4.11, 4.26, 4.39, 4.53, 4.67, 4.81, 4.94,
        5.07, 5.20, 5.34, 5.46, 5.59, 5.72, 5.85, 5.97,
        6.10, 6.22, 6.34, 6.46, 6.58, 6.70, 6.82, 6.94,
        7.05, 7.17, 7.28, 7.39
    ]


    x_gemini = [
        0.8589, 0.9526, 0.9814, 0.9911, 0.9934,
        0.9946, 0.9949, 0.9957, 0.9963, 0.9971, 0.9971
    ]
    y_gemini = [
        12.79, 51.04, 63.89, 68.93, 71.33, 73.11,
        74.58, 75.97, 77.13, 78.14, 78.92
    ]

    x_codex = [0.9437, 0.9937, 0.9980, 0.9991, 0.9994, 0.9994]
    y_codex = [29.20, 35.01, 35.66, 35.86, 35.95, 36.01]
    x_claude = [
        0.8323, 0.8920, 0.9271, 0.9383, 0.9443,
        0.9471, 0.9494, 0.9509, 0.9531, 0.9549,
        0.9557, 0.9563, 0.9574, 0.9580, 0.9583,
        0.9589, 0.9597, 0.9606, 0.9606
    ]
    y_claude = [
        11.03, 16.02, 19.23, 21.40, 23.23,
        24.89, 26.46, 27.97, 29.43, 30.82,
        32.16, 33.48, 34.78, 36.05, 37.30,
        38.54, 39.76, 40.96, 42.13
    ]

    plt.figure(figsize=(7.5, 5.2))

    if flip_axes:
        plt.plot(y_gpt, x_gpt, label="ChatGpt 4o mini", color="#390099", linewidth=2)
        plt.plot(y_gemini, x_gemini, label="Gemini", color="#FF0054", linewidth=2)
        plt.plot(y_codex, x_codex, label="Codex", color="#E47A00", linewidth=2)
        plt.plot(y_claude, x_claude, label="Claude Sonnet 3.7", color="#9E0059", linewidth=2)
        plt.ylabel("Cost in $", fontsize=14)
        plt.xlabel("Quality in %", fontsize=14)
        plt.xlim(0, 90)
        plt.ylim(0.5, 1.0)
        plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
    else:
        plt.plot(x_gpt, y_gpt, label="ChatGpt 4o mini", color="#390099", linewidth=2)
        plt.plot(x_gemini, y_gemini, label="Gemini", color="#FF0054", linewidth=2)
        plt.plot(x_codex, y_codex, label="Codex", color="#E47A00", linewidth=2)
        plt.plot(x_claude, y_claude, label="Claude Sonnet 3.7", color="#9E0059", linewidth=2)
        plt.ylabel("Cost in $", fontsize=14)
        plt.xlabel("Quality in %", fontsize=14)
        plt.xlim(0.5, 1.0)
        plt.ylim(0, 90)
        plt.gca().xaxis.set_major_formatter(PercentFormatter(1.0))

    plt.grid(True, which="major", linestyle="-", alpha=0.4)
    plt.legend(frameon=False, loc="upper left", ncol=4)
    plt.tight_layout()
    plt.show()

# Beispielaufruf:
plot_global_cost_per_percent(flip_axes=False)  # x- und y-Achse getauscht
