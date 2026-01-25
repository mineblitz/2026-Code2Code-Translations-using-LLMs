import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def getErrorsPerIteration(path = "./Projects",  basenameFile = "logsHumanEvalXExp10Run1_42"):
    pathHumanEval = os.path.join(path, "HumanEvalX")
    problemNumbers = [f for f in os.listdir(pathHumanEval) if f.isdigit() and 0 <= int(f) < 164]
    sortedProblemNumbers = sorted(problemNumbers, key=lambda x: int(x))

    values = {}

    basename = "compilation_matrix"
    compilation_matrixs = [f for f in os.listdir(os.path.join(path, basenameFile)) if basename in f]

    for index, matrix in enumerate(compilation_matrixs):
        summed_Errors = 0
        if matrix == "compilation_matrix_avg": continue
        if matrix == "compilation_matrix_sum": continue
        if matrix == "compilation_matrix_std_deviation": continue
        # Construct the file name
        compilation_matrix_file = os.path.join(path,basenameFile,  matrix)
        compilationMatrix = pd.read_csv(compilation_matrix_file, index_col=0)
        summed_Errors += 28 - compilationMatrix.sum().sum()
        # this should match the matrix to the problem number
        values[sortedProblemNumbers[index]] = summed_Errors
    
    sorted_values = dict(sorted(values.items(), key=lambda item: item[1], reverse=True))
    
    return sorted_values


def load_error_per_iteration(error_dict, path="./Projects", basenameFile="logsHumanEvalXExp14Run1_18"):
    """
    Load failed compilation values for the given problems (from error_dict keys) 
    for the specified experiment/run.

    Parameters:
    - error_dict: dict {problem_id: value}, the subset of problems to load
    - path: base path to Projects
    - basenameFile: experiment/run folder name

    Returns:
    - dict {problem_id: failed_compilation_count}
    """
    pathHumanEval = os.path.join(path, "HumanEvalX")
    problemNumbers = [f for f in os.listdir(pathHumanEval) if f.isdigit() and 0 <= int(f) < 164]
    sortedProblemNumbers = sorted(problemNumbers, key=lambda x: int(x))

    values = {}
    basename = "compilation_matrix"
    compilation_matrixs = [f for f in os.listdir(os.path.join(path, basenameFile)) if basename in f]

    # Map problem index to problem number for consistent ordering
    index_to_problem = {i: sortedProblemNumbers[i] for i in range(len(sortedProblemNumbers))}

    for index, matrix in enumerate(compilation_matrixs):
        if matrix in ["compilation_matrix_avg", "compilation_matrix_sum", "compilation_matrix_std_deviation"]:
            continue
        
        problem_number = index_to_problem.get(index)
        if problem_number not in error_dict:
            continue  # only process problems in the given dict

        compilation_matrix_file = os.path.join(path, basenameFile, matrix)
        compilationMatrix = pd.read_csv(compilation_matrix_file, index_col=0)
        
        failed_count = 28 - compilationMatrix.sum().sum()  # same as original method
        values[problem_number] = failed_count

    return values


def get_first_10_elements(dict):
    # Use a dictionary comprehension with enumerate to limit to 10 items
    return {key: dict[key] for i, (key, value) in enumerate(dict.items()) if i < 10}

def onlyWithAtLeast1(dict):
    return {key: dict[key] for i, (key, value) in enumerate(dict.items()) if value > 0}

def createBarChart(error_data):
    # Extract keys and values
    programs = list(error_data.keys())
    errors = list(error_data.values())

    # Set y-axis limit to 28

    # Create bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(programs, errors, color='skyblue')

    plt.ylim(0, 28)
    # Add major ticks every 5 units with labels
    plt.yticks(range(0, 29, 5), fontsize=14 )

    # Add minor ticks at every integer without labels
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))

    # Add gridlines for better visibility
    # plt.grid(which='both', axis='y', linestyle='--', linewidth=0.5)

    # Increase the thickness of the ticks
    plt.tick_params(axis='y', width=2)  # For major ticks
    plt.tick_params(axis='y', which='minor', width=1)  # For minor ticks

    plt.xticks(fontsize=14)

    # Add titles and labels with increased font size and weight
    plt.title('Number of Errors by Program', fontsize=16 )
    plt.xlabel('Programs', fontsize=14 )
    plt.ylabel('Number of Errors', fontsize=14 )

    # Show the chart
    plt.show()


def createGroupedBarChart(errorsGPT, errorsClaude, errorsGemini, errorsCodex):
    """
    Create a grouped bar chart for 4 dicts, grouped by problem.
    The problems are sorted by errorsGPT descending.
    Even 0 values are shown as a tiny mark.
    
    errorsGPT, errorsClaude, errorsGemini, errorsCodex: dict {problem_id: error_count}
    """
    
    # Sort problems by GPT errors descending
    sorted_problems = sorted(errorsGPT.keys(), key=lambda x: errorsGPT[x], reverse=True)
    
    # Extract values for all 4 models in the sorted order
    gpt_values     = [errorsGPT.get(p, 0) for p in sorted_problems]
    claude_values  = [errorsClaude.get(p, 0) for p in sorted_problems]
    gemini_values  = [errorsGemini.get(p, 0) for p in sorted_problems]
    codex_values   = [errorsCodex.get(p, 0) for p in sorted_problems]
    
    # Bar width and positions
    n = len(sorted_problems)
    bar_width = 0.2
    x = np.arange(n)
    
    plt.figure(figsize=(12,6))
    
    # For 0 values, replace by tiny value to show mark
    tiny = 0.5
    bottom = -0.5
    plt.bar(x - 1.5*bar_width, [v+0.5 if v>0 else tiny for v in gpt_values], width=bar_width, label='OG', bottom=bottom, color='#390099')   # OG
    plt.bar(x - 0.5*bar_width, [v+0.5 if v>0 else tiny for v in claude_values], width=bar_width, label='CO',  bottom=bottom,color='#9E0059')  # CO
    plt.bar(x + 0.5*bar_width, [v+0.5 if v>0 else tiny for v in gemini_values], width=bar_width, label='GG', bottom=bottom, color='#FF0054') # GG
    plt.bar(x + 1.5*bar_width, [v+0.5 if v>0 else tiny for v in codex_values], width=bar_width, label='OC',  bottom=bottom,color='#E47A00')  # OC

    
    # Labels and axes
    plt.xticks(x, sorted_problems, fontsize=16)
    # plt.yticks(range(0, 20, 5))
    # plt.ylim(0, 21)
    plt.yticks(range(0, 20, 5), fontsize=16)
    plt.ylim(-0.5, 21)
    
    # Minor ticks for better visibility
    plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(1))
    
    # Grid
    plt.grid(which='major', axis='y', linestyle='--', alpha=0.5)
    
    # Axis labels and title
    plt.xlabel("Programs", fontsize=18)
    plt.ylabel("Number of Errors", fontsize=18)
    
    # Legend
    plt.legend()
    
    plt.tight_layout()
    plt.show()

    

if __name__ == "__main__":
    ErrorsForProblemsGPT = getErrorsPerIteration(basenameFile = "logsHumanEvalXExp6Run2_43")
    ErrorsForProblemsGPT = get_first_10_elements(ErrorsForProblemsGPT)
    ErrorsForProblemsClaude = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp14Run1_18")
    ErrorsForProblemsGemini = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp20Run1_10")
    ErrorsForProblemsCodex = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp23Run1_5")

    # ErrorsForProblemsGPT = getErrorsPerIteration(basenameFile = "logsHumanEvalXExp5Run2")
    # ErrorsForProblemsGPT = get_first_10_elements(ErrorsForProblemsGPT)
    # ErrorsForProblemsClaude = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp13Run1")
    # ErrorsForProblemsGemini = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp19Run1")
    # ErrorsForProblemsCodex = load_error_per_iteration(ErrorsForProblemsGPT, basenameFile = "logsHumanEvalXExp22Run1")

    # atLeast1 = onlyWithAtLeast1(ErrorsForProblems)
    # createBarChart(atLeast1)

    # createBarChart(ErrorsForProblemsGPT)
    createGroupedBarChart(ErrorsForProblemsGPT, ErrorsForProblemsClaude, ErrorsForProblemsGemini, ErrorsForProblemsCodex)
