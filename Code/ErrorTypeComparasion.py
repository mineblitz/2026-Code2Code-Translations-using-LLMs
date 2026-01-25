import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

compilation = "compilation_failed_sum"
runtime = "runtime_error_sum"
test = "test_failure_sum" 
timeout = "infinitie_loop_sum"

def load_avg_dataframe(experiment: int, run: int, error_type: str) -> pd.DataFrame:
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')

    summed_error = []

    prefix, last_num_str = run.split('_')
    last_num = int(last_num_str)
    
    for i in range(last_num + 1):
        current_run = f"{prefix}_{i}"
        executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{current_run}')
        dataFrame_filepath = os.path.join(executionDir, error_type)

        if not os.path.exists(dataFrame_filepath):
            raise FileNotFoundError(f"Average dataframe file not found: {dataFrame_filepath}")

        dataframe = pd.read_csv(dataFrame_filepath, index_col=0)    
        summed_error.append(dataframe.sum().sum())        

    return summed_error

def plot_errors(gptErrors, ClaudeErrors, GeminiErrors, CodexErrors):    
    plt.figure(figsize=(10,6))
    
    labels = ['OG', 'CS', 'GG', 'OC']
    colors = ['#390099', '#9E0059', '#FF0054', "#E47A00"]  # OG, CO, GG, OC
    small_value = 1e-1  # klassischer kleiner Offset
    
    x_gpt     = np.arange(1, len(gptErrors)+1) - (1 - small_value)
    x_claude  = np.arange(1, len(ClaudeErrors)+1) - (1 - small_value)
    x_gemini  = np.arange(1, len(GeminiErrors)+1) - (1 - small_value)
    x_codex   = np.arange(1, len(CodexErrors)+1) - (1 - small_value)

    plt.plot(x_gpt, gptErrors, label=labels[0], color=colors[0])
    plt.plot(x_claude, ClaudeErrors, label=labels[1], color=colors[1])
    plt.plot(x_gemini, GeminiErrors, label=labels[2], color=colors[2])
    plt.plot(x_codex, CodexErrors, label=labels[3], color=colors[3])

    # Logarithmische Skalierung
    plt.xscale('log', base=2)
    plt.yscale('log')

    # Gewünschte x-Achsenwerte
    xticks = [0,1,2,3,4,5,6,8,10,14,18,24,30,36,43]    
    xticks_for_plot = [x if x>0 else 0.1 for x in xticks]    
    ax = plt.gca()
    ax.set_xticks(xticks_for_plot)
    ax.set_xticklabels(xticks, fontsize=13)  # Ticklabels Textgröße

    # Gewünschte y-Achsenwerte
    yticks = [1,2,3,4,5,6,8,10]
    # yticks = [2,6,20,60,120,200,320,600]
    yticks_for_plot = [y if y>0 else 0.1 for y in yticks]
    ax.set_yticks(yticks_for_plot)
    ax.set_yticklabels(yticks, fontsize=14)  # Ticklabels Textgröße
    
    plt.xlabel("Number of Requests", fontsize=18)
    plt.ylabel("Number of Errors", fontsize=18)
    
    ax.grid(which='major', linestyle='--', alpha=0.5)
    plt.legend(fontsize=18)  # Legend Textgröße
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # error_type = timeout # Change this to select different error types
    error_type = timeout # Change this to select different error types

    gptErrors = load_avg_dataframe(6, "2_43", error_type)
    ClaudeErrors = load_avg_dataframe(14, "1_18", error_type)
    GeminiErrors = load_avg_dataframe(20, "1_10", error_type)
    CodexErrors = load_avg_dataframe(23, "1_5", error_type)


    plot_errors(
        gptErrors,
        ClaudeErrors,
        GeminiErrors,
        CodexErrors,
    )