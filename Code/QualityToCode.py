import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

percentages = [0, 0.1, 0.5, 1, 5, 10, 50, 75, 100]
thresholds = [p / 100 for p in percentages]
# CostGPT = 0.000290918539777344 # aus vorherigen Ergebnissen
CostGPTIn = 0.15/1000000
CostGPTOut = 0.60/1000000
CostClaudeIn = 3/1000000
CostClaudeOut = 15/1000000
CostGeminiIn = 1.25/1000000
CostGeminiOut = 10/1000000
CostCodexIn = 1.25/1000000
CostCodexOut = 10/1000000
avgTokenGPTIn = 789.7142857
avgTokenGPTOut = 342.1714286
avgTokenClaudeIn = 300
avgTokenClaudeOut = 600
avgTokenGeminiIn = 888.2941176
avgTokenGeminiOut = 7632.029412
avgTokenCodexIn = 891.1428571
avgTokenCodexOut = 2836
results = []


def get_QualityToCode_DataGPT(experiment, run, threshold):
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')

    if (threshold == 0):
        print("Running GPT Only experiment...")
    prefix, last_num_str = run.split('_')
    last_num = int(last_num_str)
    
    highest_run = -1
    previous_diff = 0
    sum_all_translations = 0

    for i in range(last_num + 1):
        current_run = f"{prefix}_{i}"
        executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{current_run}')
        dataFrame_filepath = os.path.join(executionDir, "compilation_matrix_sum")

        if not os.path.exists(dataFrame_filepath):
            raise FileNotFoundError(f"Average dataframe file not found: {dataFrame_filepath}")

        dataframe = pd.read_csv(dataFrame_filepath, index_col=0)  
        sum_all_translations += (3500 - previous_diff)
        # print(sum_all_translations)
        diff = dataframe.sum().sum()    # to get quality in percentage  
        improvement = (diff - previous_diff) / previous_diff if previous_diff != 0 else 0.644285714285714 # GPT Result
        previous_diff = diff
        if improvement < threshold:
            highest_run = i
            break
    if highest_run == -1:
        highest_run = last_num
    # liste erstllen mit allen matrizen in higehst run
    allDataframes = []
    current_run = f"{prefix}_{highest_run}"
    executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{current_run}')
    # bekomme liste von allen dateien die compilation_matrixXXX wo XXX zahlen sind
    # außer compilation_matrix_sum udn compilation_matrix_avg und compilation_matrix_std_deviation
    # 
    dataFrame_filepath = os.path.join(executionDir, "compilation_matrix_sum")

    if not os.path.exists(dataFrame_filepath):
        raise FileNotFoundError(f"Average dataframe file not found: {dataFrame_filepath}")

    return sum_all_translations, get_all_dataframes(executionDir)

def get_all_dataframes(executionDir):
    allDataframes = []
    for fname in os.listdir(executionDir):
        # nur compilation_matrixXXX mit XXX = Zahl
        if not fname.startswith("compilation_matrix"):
            continue
        if fname in {
            "compilation_matrix_sum",
            "compilation_matrix_avg",
            "compilation_matrix_std_deviation",
        }:
            continue

        suffix = fname.replace("compilation_matrix", "")
        if not suffix.isdigit():
            continue
        dataframe = pd.read_csv(os.path.join(executionDir, fname), index_col=0)   
        allDataframes.append(dataframe)
    return allDataframes

def fix_with_other_model(experiment, run, gptDataFrames):
    dirname = os.path.dirname(__file__)
    fullProjectDir = os.path.join(dirname, 'Projects')

    prefix, last_num_str = run.split('_')
    last_num = int(last_num_str)

    counter = 0
    for i in range(last_num + 1):
        current_run = f"{prefix}_{i}"
        executionDir = os.path.join(fullProjectDir, f'logsHumanEvalXExp{experiment}Run{current_run}')

        currentDataframes = get_all_dataframes(executionDir)
        counter, gptDataFrames = improve_dataframe(counter, gptDataFrames, currentDataframes)

    return counter, gptDataFrames

def improve_dataframe(count, dataframesCorected, dataframes):
    for i in range(len(dataframesCorected)):   
        df = dataframesCorected[i]
        for index, row in df.iterrows():
            for col in df.columns:
                if df.at[index, col] == 0:
                    count += 1
                    # ersetze wert mit wert aus dataframes
                    df.at[index, col] = dataframes[i].at[index, col]
        dataframesCorected[i] = df

    return count, dataframesCorected


def get_cost_from_model(model_name):
    if model_name == "Claude":
        return avgTokenClaudeIn * CostClaudeIn + avgTokenClaudeOut *CostClaudeOut
    elif model_name == "Gemini":
        return avgTokenGeminiIn * CostGeminiIn + avgTokenGeminiOut * CostGeminiOut
    elif model_name == "GPT":
        return avgTokenGPTIn * CostGPTIn + avgTokenGPTOut * CostGPTOut
    elif model_name == "Codex":
        return avgTokenCodexIn * CostCodexIn + avgTokenCodexOut * CostCodexOut
    else:
        raise ValueError(f"Unknown model name: {model_name}")
    

def run_model(model_name, run_id, prefix, gpt_run_id, gpt_prefix):
    for p, t in zip(percentages, thresholds):
        print("model_name:", model_name, "break at:", p, "%")
        gptCounter, dataframesGPT = get_QualityToCode_DataGPT(6, gpt_run_id, t)
        count, combined = fix_with_other_model(run_id, prefix, dataframesGPT)

        total_sum = sum(df.sum().sum() for df in combined)
        quality = total_sum / 3500

        label = f"{p}%" if p != 100 else f"{model_name} Only"
        results.append({
            "breakPercentage": label,
            "cost": get_cost_from_model("GPT") * gptCounter + count * (get_cost_from_model(model_name)),
            "quality": quality
        })

if __name__ == "__main__":
    # Claude
    run_model("Claude", 14, "1_18", "2_43", "GPT")

    # Gemini
    run_model("Gemini", 20, "1_10", "2_43", "GPT")

    # Codex
    run_model("Codex", 23, "1_5", "2_43", "GPT")

    df = pd.DataFrame(results)
    df.to_csv("break_threshold_results.csv", index=False)