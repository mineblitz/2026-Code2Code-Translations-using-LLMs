import os
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Given data

def extract_number(s):
    match = re.search(r'\d+$', s)  # Extract the trailing digits
    return int(match.group()) if match else 0

def getErrorsPerIteration(path = "./Projects",  basenameFile = "logsHumanEvalXExp11Run1", normaliseFalg = False):

    matching_files = [f for f in os.listdir(path) if basenameFile in f]
    sorted_strings = sorted(matching_files, key=extract_number)

    firstSum = 0
    values = []
    for file in sorted_strings:
        basename = "compilation_matrix"
        compilation_matrixs = [f for f in os.listdir(os.path.join(path, file)) if basename in f]

        summed_df = 0
        for matrix in compilation_matrixs:
            if matrix == "compilation_matrix_avg": continue
            if matrix == "compilation_matrix_std_deviation": continue
            # Construct the file name
            compilation_matrix_file = os.path.join(path,file,  matrix)
            
            
            df2 = pd.read_csv(compilation_matrix_file, index_col=0)
            
            summed_df += 28 - df2.sum().sum()
        if firstSum == 0:
            firstSum = summed_df
        if normaliseFalg: values.append(summed_df/firstSum)
        else: values.append(summed_df)
    
    return values


def inverse_func(x, a, b, c):
    return a / (x + b) + c

# Function to plot a regression for a given dataset
def plot_regression_curve(values, label_suffix, color=None):
    x = np.arange(1, len(values) + 1) 
    
    plt.plot(x, values, '-', label=f'Remaining errors in {label_suffix}', color=color)

    # if not normalisedFlag:
    #     initial_guess = [1317.7888880283174, 0.5213728046162626, 363.48768149939497]
    #     params, _ = curve_fit(inverse_func, x, values, p0=initial_guess, maxfev=10000)
    # else: params, _ = curve_fit(inverse_func, x, values, maxfev=10000)    
    
    # # Print fitted parameters and predicted value at x=40 for inspection
    # print(f"Fitted parameters for {label_suffix}: {params}")
    # print(f"Predicted value at x=40 for {label_suffix}: {inverse_func(40, *params)}")

    # # Compute the fitted curve
    # y_reg = inverse_func(x, *params)
    

def LayoutRetrans():
    # Customize the plot with specified font sizes
    plt.title("Remaining translation errors per iteration for each experiment", fontsize=16)
    plt.xlabel("Iterations", fontsize=14)
    plt.ylabel("Number of errors in translations", fontsize=14)
    plt.legend(fontsize=14)
    plt.grid(True)

    # Show the plot
    plt.show()

def totalRetranslate():
    # Retrieve your datasets
    valuesExp6Run2 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp6Run2")
    valuesExp10Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp10Run1")
    # valuesExp11Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp11Run1")
    # valuesExp12Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp12Run1")

    plt.figure(figsize=(10, 6))

    # Plot each dataset
    plot_regression_curve(valuesExp6Run2, 'Experiment 7', color='blue')
    plot_regression_curve(valuesExp10Run1, 'Experiment 11', color='red')
    # plot_regression_curve(valuesExp11Run1, 'Experiment 12', color='green')
    # plot_regression_curve(valuesExp12Run1, 'Experiment 13', color='yellow')

    LayoutRetrans()


def normalisedRetranslate():
    # Retrieve your datasets
    valuesExp6Run2 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp6Run2", True)
    valuesExp10Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp10Run1", True)
    # valuesExp11Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp11Run1", True)
    # valuesExp12Run1 = getErrorsPerIteration("./Projects", "logsHumanEvalXExp12Run1", True)
    
    plt.figure(figsize=(10, 6))

    # Plot each dataset
    plot_regression_curve(valuesExp6Run2, 'Experiment 7', color='blue')
    plot_regression_curve(valuesExp10Run1, 'Experiment 11', color='red')
    # plot_regression_curve(valuesExp11Run1, 'Experiment 12', color='green')
    # plot_regression_curve(valuesExp12Run1, 'Experiment 13', color='yellow')

    # Customize the plot
    LayoutRetrans()


def getErrorTypeMatrx(path, file):
    basenameCompilationFailed = "compilation_failed"
    basenameInfinitieLoop = "infinite_loop"
    basenameRuntime_error = "runtime_error"
    basenameTest_failure = "test_failure"
    compilation_failed_matrixs = [f for f in os.listdir(os.path.join(path, file)) if basenameCompilationFailed in f]
    infinite_loop_matrixs = [f for f in os.listdir(os.path.join(path, file)) if basenameInfinitieLoop in f]
    runtime_error_matrixs = [f for f in os.listdir(os.path.join(path, file)) if basenameRuntime_error in f]
    test_failure_matrixs = [f for f in os.listdir(os.path.join(path, file)) if basenameTest_failure in f]
    return compilation_failed_matrixs, infinite_loop_matrixs, runtime_error_matrixs, test_failure_matrixs

def sumMatrix(path,file,matrixs):
    summed_df = 0
    for matrix in matrixs:
        if matrix == "LogCompilationFailed.csv": continue
        if matrix == "LogTestFailed.csv": continue
        if matrix == "compilation_matrix_avg": continue
        if matrix == "compilation_matrix_std_deviation": continue
        # Construct the file name
        compilation_matrix_file = os.path.join(path,file,  matrix)
        
        
        df2 = pd.read_csv(compilation_matrix_file, index_col=0)
        
        summed_df += df2.sum().sum()    
    return summed_df

def getErrorTypesPerIteration(path = "./Projects",  basename = "logsHumanEvalXExp11Run1", relative = False):

    matching_files = [f for f in os.listdir(path) if basename in f]
    sorted_strings = sorted(matching_files, key=extract_number)


    values = {
        "CompilationFailed": [],
        "InfiniteLoop": [],
        "RuntimeError": [],
        "TestFailure": [],
        }
    
    for file in sorted_strings:
        compilation_failed_matrixs, infinite_loop_matrixs, runtime_error_matrixs, test_failure_matrixs = getErrorTypeMatrx(path, file)

        if not relative:
            values["CompilationFailed"].append(sumMatrix(path,file,compilation_failed_matrixs))
            values["InfiniteLoop"].append(sumMatrix(path,file,infinite_loop_matrixs))
            values["RuntimeError"].append(sumMatrix(path,file,runtime_error_matrixs))
            values["TestFailure"].append(sumMatrix(path,file,test_failure_matrixs))
        else:
            sum_compilation_failed = (sumMatrix(path,file,compilation_failed_matrixs))
            sum_infinite_loop = (sumMatrix(path,file,infinite_loop_matrixs))
            sum_runtime_error = (sumMatrix(path,file,runtime_error_matrixs))
            sum_test_failure = (sumMatrix(path,file,test_failure_matrixs))

            totalSum = sum_compilation_failed + sum_infinite_loop + sum_runtime_error + sum_test_failure

            print(str(sum_compilation_failed/totalSum) + " " + str(sum_infinite_loop/totalSum)+ " " + str(sum_runtime_error/totalSum)+ " " + str(sum_test_failure/totalSum))
            values["CompilationFailed"].append(sum_compilation_failed/totalSum)
            values["InfiniteLoop"].append(sum_infinite_loop/totalSum)
            values["RuntimeError"].append(sum_runtime_error/totalSum)
            values["TestFailure"].append(sum_test_failure/totalSum)
    
    return values


def stackedPlot(errorTypes):
    iterations = list(range(0, len(errorTypes["CompilationFailed"]))) 

    # Stack data
    data = np.vstack([errorTypes["CompilationFailed"], errorTypes["TestFailure"], errorTypes["RuntimeError"], errorTypes["InfiniteLoop"]])

    plt.stackplot(iterations, data, labels=['CompilationFailed', 'TestFailure', 'RuntimeError', 'InfiniteLoop'], 
                  colors=['#1f77b4', '#2ca02c', '#d62728', '#ff7f0e'], alpha=0.6)

    # Add the legend with increased font size
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)

    # Customize the plot with increased font sizes
    plt.title("Error type for each translation", fontsize=16)
    plt.xlabel("Iterations", fontsize=14)
    plt.ylabel("Number of errors in error type", fontsize=14)
    plt.grid(True)

    # Show the plot
    plt.show()


def stackedPlotAbsolut(basename):
    errorTypes = getErrorTypesPerIteration(path = "./Projects",  basename = basename, relative = False)
    stackedPlot(errorTypes)

def stackedPlotRelative(basename):
    errorTypes = getErrorTypesPerIteration(path = "./Projects",  basename = basename, relative = True)
    stackedPlot(errorTypes)



normalisedRetranslate()
totalRetranslate()
# stackedPlotRelative("logsHumanEvalXExp10Run1")
# stackedPlotRelative("logsHumanEvalXExp11Run1")
# stackedPlotRelative("logsHumanEvalXExp12Run1")