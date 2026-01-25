import math
import os
import shutil
import pandas as pd
import numpy as np
from CompileAndRun import compile_and_run_files_in_directory
from VisualisationErrors import visulation_as_Error_heatmap
from Visulation import visulation_as_heatmap

# Define the languages
languages = ['C', 'C++', 'C#', 'Java', 'Javascript', 'Pascal', 'Python', 'Haskell']

def compileAllTranslations(dirPath, logs, forceFlag, flag_object):
    compilation_matrix_array = []
    counter = 0
    
    for file in os.listdir(dirPath):
        if(check_if_allready_compiled(dirPath, counter, logs) or forceFlag):
            execution_status = compile_and_run_files_in_directory(os.path.join(dirPath, file), logs, flag_object)
            compilation_matrix_array.append(execution_status.compilation_matrix)        
            save_dataframe_to_csv(dirPath, logs, execution_status.compilation_matrix, 'compilation_matrix'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.compilation_failed, 'compilation_failed'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.runtime_error, 'runtime_error'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.infinite_loop, 'infinite_loop'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.test_failure, 'test_failure'+ str(counter))
        counter = counter + 1


def compileAllTranslationsQuant(dirPath, logs, forceFlag, counter, flag_object, filenameWhiteList):
    compilation_matrix_array = []
    
    for file in os.listdir(dirPath):
        if len(os.listdir(os.path.join(dirPath, file))) == 0: 
            shutil.rmtree(os.path.join(dirPath, file))
            continue
        if(check_if_allready_compiled(dirPath, counter, logs) or forceFlag):
            execution_status = compile_and_run_files_in_directory(os.path.join(dirPath, file), logs, flag_object, filenameWhiteList)
            compilation_matrix_array.append(execution_status.compilation_matrix)        
            save_dataframe_to_csv(dirPath, logs, execution_status.compilation_matrix, 'compilation_matrix'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.compilation_failed, 'compilation_failed'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.runtime_error, 'runtime_error'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.infinite_loop, 'infinite_loop'+ str(counter))
            save_dataframe_to_csv(dirPath, logs, execution_status.test_failure, 'test_failure'+ str(counter))
        counter = counter + 1
    return counter

def save_dataframe_to_csv(dirname, log, dataframe, filename):
    logs_dir = os.path.join(dirname, '../' + log)
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    file_path = os.path.join(logs_dir, filename)
    dataframe.to_csv(file_path)

def read_dataframe_from_csv(dirname, log, count, matrixType):
    logs_dir = os.path.join(dirname, '../' + log)
    avg_matrix_path = os.path.join(logs_dir, matrixType+ str(count))
    dataframe = pd.read_csv(avg_matrix_path, index_col=0)
    return dataframe 

def calc_compilation_matrix_avg(dirPath, log, compilation_matrix_array, totalRuns):
    compilation_matrix_avg = pd.DataFrame(0, index=languages, columns=languages, dtype=float)
    for i in range(len(languages)):
        for j in range(len(languages)):
            valueSum = 0   
            for matrix in compilation_matrix_array:
                valueSum = valueSum + matrix.iat[i, j]
            compilation_matrix_avg.iat[i, j] = valueSum / totalRuns    
    save_dataframe_to_csv(dirPath,log,compilation_matrix_avg, 'compilation_matrix_avg')
    return compilation_matrix_avg

def calc_compilation_matrix_std_deviation(dirPath, log, compilation_matrix_array, totalRuns, compilation_matrix_avg):
    compilation_matrix_std_deviation = pd.DataFrame(0, index=languages, columns=languages, dtype=float)
    
    for i in range(len(languages)):
        for j in range(len(languages)):
            # Extract the specific element (i, j) from each matrix in the array
            elements = np.array([matrix.iat[i, j] for matrix in compilation_matrix_array])
            
            # Calculate the standard deviation directly using np.std()
            compilation_matrix_std_deviation.iat[i, j] = np.std(elements, ddof=0)
    
    save_dataframe_to_csv(dirPath, log, compilation_matrix_std_deviation, 'compilation_matrix_std_deviation')
    return compilation_matrix_std_deviation

def get_compilation_matrix_count(dirPath, log, matrixType):
    logs_dir = os.path.join(dirPath, '..' , log)
    files = os.listdir(logs_dir)
    file_pattern = matrixType
    count = len([f for f in files if f.startswith(file_pattern) and f[len(file_pattern)].isdigit()])
    return count

def check_if_allready_compiled(directory, count, logs):
    logs_dir = os.path.join(directory, '..' , logs)
    filename = f"compilation_matrix{count}" 
    if not os.path.exists(logs_dir):
        return True
    files = os.listdir(logs_dir)
    
    if filename in files:
        print("False " + filename)
        return False
    print("True " + filename)
    return True

def visualize_from_file(dirPath, log):
    compilation_matrix_count = get_compilation_matrix_count(dirPath, log, 'compilation_matrix')
    compilation_matrix_array = [read_dataframe_from_csv(dirPath, log, i, 'compilation_matrix') for i in range(compilation_matrix_count)]

    totalRuns = len(compilation_matrix_array)

    compilation_matrix_avg = calc_compilation_matrix_avg(dirPath, log, compilation_matrix_array, totalRuns)
    
    totalavg = compilation_matrix_avg.sum().sum()

    deleted_rows = visulation_as_heatmap(compilation_matrix_avg, totalavg)
    return deleted_rows

def visualize_from_file_CompilationError(dirPath, log, showErrosFlag, deleted_rows):
    compilation_failed = get_compilation_matrix_count(dirPath, log, 'compilation_failed')
    runtime_error = get_compilation_matrix_count(dirPath, log, 'runtime_error')
    infinite_loop = get_compilation_matrix_count(dirPath, log, 'infinite_loop')
    test_failure = get_compilation_matrix_count(dirPath, log, 'test_failure')
    
    compilation_failed_array = [read_dataframe_from_csv(dirPath, log, i, 'compilation_failed') for i in range(compilation_failed)]
    runtime_error_array = [read_dataframe_from_csv(dirPath, log, i, 'runtime_error') for i in range(runtime_error)]
    infinite_loop_array = [read_dataframe_from_csv(dirPath, log, i, 'infinite_loop') for i in range(infinite_loop)]
    test_failure_array = [read_dataframe_from_csv(dirPath, log, i, 'test_failure') for i in range(test_failure)]

    combinedErros = combine_all(compilation_failed_array,runtime_error_array,infinite_loop_array,test_failure_array)

    if showErrosFlag:
        visulation_as_Error_heatmap(combinedErros, len(compilation_failed_array), len(compilation_failed_array)*(len(languages)-1), 
                                len(compilation_failed_array)*(len(languages)-1)*len(languages), deleted_rows)
    
    return combinedErros
        
def combine_all(compilation_failed_array, runtime_error_array, infinite_loop_array, test_failure_array):
    index_columns = []
    counter = 0
    for language in languages:
        index_columns.append(str(counter))
        counter = counter +1
        index_columns.append(language)
    index_columns.append('')
    index_columns.append('Total')

    big_error_matrix = pd.DataFrame(0, index=index_columns, columns=index_columns, dtype=float)

        # compilation_failed  | infinite_loop_array
        # -----------------------------------------
        # runtime_error_array | test_failure_array

    for i in range(len(languages)):
        for j in range(len(languages)):
            valueSum = 0   
            if i == j:
                valueSum = math.nan

            for matrix in compilation_failed_array:
                valueSum = valueSum + matrix.iat[i, j]
            big_error_matrix.iat[2*i, 2*j] = valueSum    

            valueSum = 0   
            if i == j:
                valueSum = math.nan
            for matrix in runtime_error_array:
                valueSum = valueSum + matrix.iat[i, j]
            big_error_matrix.iat[2*i+1, 2*j] = valueSum    

            valueSum = 0   
            if i == j:
                valueSum = math.nan
            for matrix in infinite_loop_array:
                valueSum = valueSum + matrix.iat[i, j]
            big_error_matrix.iat[2*i, 2*j+1] = valueSum    
            
            valueSum = 0   
            if i == j:
                valueSum = math.nan
            for matrix in test_failure_array:
                valueSum = valueSum + matrix.iat[i, j]
            big_error_matrix.iat[2*i+1, 2*j+1] = valueSum   

    for i in range(len(index_columns)-2):         
        big_error_matrix.iat[i, len(index_columns)-2] = sum_every_second_value(big_error_matrix.iloc[i], True)
        big_error_matrix.iat[i, len(index_columns)-1] = sum_every_second_value(big_error_matrix.iloc[i], False)
        
        # Update the last two rows of the current column
        big_error_matrix.iat[len(index_columns)-2, i] = sum_every_second_value(big_error_matrix.iloc[:, i], True)
        big_error_matrix.iat[len(index_columns)-1, i] = sum_every_second_value(big_error_matrix.iloc[:, i], False)
    
    big_error_matrix.iat[-2, -2] = sum_every_second_value(big_error_matrix.iloc[-2], True) 
    big_error_matrix.iat[-2, -1] = sum_every_second_value(big_error_matrix.iloc[-2], False)
   
    big_error_matrix.iat[-1, -2] = sum_every_second_value(big_error_matrix.iloc[-1], True)
    big_error_matrix.iat[-1, -1] = sum_every_second_value(big_error_matrix.iloc[-1], False)

    return big_error_matrix


def visualize_from_fileCombineAllResults(dirPath, logs, sperateLog):
    compilation_matrix_countList = [
        get_compilation_matrix_count(dirPath, log, 'compilation_matrix')
        for log in logs
    ]  
    compilation_matrix_array = []

    for k in range(compilation_matrix_countList[0]):
        compilation_matrix = None      
        compilation_failed = None      
        infinite_loop = None      
        runtime_error = None      
        test_failure = None      
        for log in logs:
            compilation_matrixDir = read_dataframe_from_csv(dirPath, log, k, 'compilation_matrix')
            compilation_failedDir = read_dataframe_from_csv(dirPath, log, k, 'compilation_failed')
            infinite_loopDir = read_dataframe_from_csv(dirPath, log, k, 'infinite_loop')
            runtime_errorDir = read_dataframe_from_csv(dirPath, log, k, 'runtime_error')
            test_failureDir = read_dataframe_from_csv(dirPath, log, k, 'test_failure')

            if compilation_failed is None:
                compilation_failed = compilation_failedDir
            if infinite_loop is None:
                infinite_loop = infinite_loopDir
            if runtime_error is None:
                runtime_error = runtime_errorDir
            if test_failure is None:
                test_failure = test_failureDir
            if compilation_matrix is None:
                compilation_matrix = compilation_matrixDir
            for i in range(len(languages)):
                for j in range(len(languages)): 
                    if compilation_matrix.iat[i, j] is np.nan and compilation_matrixDir.iat[i, j] is np.nan: continue
                    if compilation_matrix.iat[i, j] == 1 or compilation_matrixDir.iat[i, j] == 1:
                        compilation_matrix.iat[i, j] = 1
                        compilation_failed.iat[i, j] = 0
                        infinite_loop.iat[i, j] = 0
                        runtime_error.iat[i, j] = 0
                        test_failure.iat[i, j] = 0

        compilation_matrix_array.append(compilation_matrix)
        save_dataframe_to_csv(dirPath, sperateLog, compilation_matrix, 'compilation_matrix'+str(k))
        save_dataframe_to_csv(dirPath, sperateLog, compilation_failed, 'compilation_failed'+str(k))
        save_dataframe_to_csv(dirPath, sperateLog, infinite_loop, 'infinite_loop'+str(k))
        save_dataframe_to_csv(dirPath, sperateLog, runtime_error, 'runtime_error'+str(k))
        save_dataframe_to_csv(dirPath, sperateLog, test_failure, 'test_failure'+str(k))


def sum_every_second_value(rowOrCol, firstOrSecondFlag):
    # firstOrSecondFlag True for start at the first element
    if firstOrSecondFlag:
        return rowOrCol[0::2].sum()
    else:
        return rowOrCol[1::2].sum()

def sortLogTest(logFIle, firstName, sortArray):
    # Load data from the CSV file
    if os.path.exists(logFIle):
        data = pd.read_csv(logFIle)

        # Convert the 'input' column to a string type to handle mixed types
        data[firstName] = data[firstName].astype(str)

        # Sort the data by 'input' and then by 'language'
        sorted_data = data.sort_values(by=sortArray)

        # Write the sorted data to a new CSV file
        sorted_data.to_csv(logFIle, index=False)


def compile_all_Quant(flag_object, showVisual, experiment, run, ExecutionDir = None, logPath = None, PrevlogPath=None):
    pathOverall = './Projects/HumanEvalX'
    if ExecutionDir is None: ExecutionDir = f'ExecutionsExp{experiment}Run{run}'

    if logPath is None: logPath =  "../../logsHumanEvalXQuant3"

    log_reTranslate = 'reTranslate.csv' 
    force_run = False
    counter = 0
    
    # 0 weil es egal ist in welchen ordner der sprint eh hoch
    log_file_pathCompilation = os.path.join(pathOverall, '0' , logPath , './LogCompilationFailed.csv')
    log_file_pathTest = os.path.join(pathOverall, '0', logPath, './LogTestFailed.csv')

    if os.path.exists(log_file_pathCompilation) and force_run:
        os.remove(log_file_pathCompilation)
    if os.path.exists(log_file_pathTest) and force_run:
        os.remove(log_file_pathTest)
    if os.path.exists(log_reTranslate) and force_run:
        os.remove(log_reTranslate)

    Projects = os.listdir(pathOverall)
    for entry in Projects:       
        path = os.path.join(pathOverall, entry, ExecutionDir)
        log_file_pathCompilation = os.path.join(path, '..', logPath , './LogCompilationFailed.csv')
        log_file_pathTest = os.path.join(path, '..', logPath, './LogTestFailed.csv')

        if not os.path.exists(os.path.join(path, '../', logPath)):
            os.makedirs(os.path.join(path, '../', logPath))
    
        if PrevlogPath is not None:
            filenameWhiteList = os.path.join(path, '..', PrevlogPath, f"compilation_matrix{counter}") 
        else:
            filenameWhiteList = None

        counter = compileAllTranslationsQuant(path, logPath, force_run, counter, flag_object, filenameWhiteList)

        if(force_run):
            sortLogTest(log_file_pathTest,'input', ['language', 'input', 'language'])
            sortLogTest(log_file_pathCompilation,"language", ['language', 'filename'])
   
    if(showVisual):
        deleted_rows = visualize_from_file(path, logPath)
        visualize_from_file_CompilationError(path, logPath, True, deleted_rows)





def compile_all(flag_object, showVisual):
    # Path to project that gets translated
    # path = './Projects/HelloWorld/Executions5'
    # path = './Projects/PrimeNumber/Executions1'
    # path = './Projects/Baklava/Executions4'
    # path = './Projects/Factorial/Executions'
    # path = './Projects/HumanEvalX/142/ExecutionsExp6Run0_4'
    # path = './Projects/HumanEvalX/142/ExecutionsExp7Run3'
    # path = './Projects/HumanEvalX/142/ExecutionsExp9Run8'
    path = './Projects/HumanEvalX/142/Executions1'
    # path = './Projects/HumanEvalX/23/Executions4'

    logPath =  "logs1"

    log_file_pathCompilation = os.path.join(path, '..', logPath , './LogCompilationFailed.csv')
    log_file_pathTest = os.path.join(path, '..', logPath, './LogTestFailed.csv')
    log_reTranslate = 'reTranslate.csv' 

    force_run = False

    if os.path.exists(log_file_pathCompilation) and force_run:
        os.remove(log_file_pathCompilation)
    if os.path.exists(log_file_pathTest) and force_run:
        os.remove(log_file_pathTest)
    if os.path.exists(log_reTranslate) and force_run:
        os.remove(log_reTranslate)

    if not os.path.exists(os.path.join(path, '../', logPath)):
        os.makedirs(os.path.join(path, '../', logPath))
 
    compileAllTranslations(path, logPath, force_run, flag_object)

    if(force_run or True):
        sortLogTest(log_file_pathTest,'input', ['language', 'input', 'language'])
        sortLogTest(log_file_pathCompilation,"language", ['language', 'filename'])

    if(showVisual):
        deleted_rows = visualize_from_file(path, logPath)
        visualize_from_file_CompilationError(path, logPath, True, deleted_rows)


class FlagObject:
    def __init__(self):
        self.HaskellAddImportsFlag = False
        self.PascallAddCompileOptionFlag = False
        self.removeAfterBackTicks = False
        self.addLibarys = False
        self.notJavaClassNameChange = False
        self.notRemoveBackTicks = False
        self.NotCScharfAenderung = False
        self.notRmeoveCRTlib = True


if __name__ == "__main__":
    flagObject = FlagObject()
    # compile_all(flagObject, True)
    # compile_all_Quant(flagObject, True, 12,1, "ExecutionsExp12Run1_44", "../../logsHumanEvalXExp12Run1_44")
    # compile_all_Quant(flagObject, True, 12,1, "ExecutionsExp5Run1", "../../logsHumanEvalXQuant1")
    compile_all_Quant(flagObject, True, 22, 1, "ExecutionsExp22Run1", "../../logsHumanEvalXExp22Run1", PrevlogPath=None)
      
    
    # logs = [
    #     "logsHumanEvalXExp12Run1_44",
    #     "logsHumanEvalXExp11Run1_48",
    #     "logsHumanEvalXExp9Run9",
    #     "logsHumanEvalXExp8Run6",
    #     "logsHumanEvalXExp8Run10",
    #     "logsHumanEvalXExp8Run14",
    #     "logsHumanEvalXExp7Run4",
    #     "logsHumanEvalXExp6Run2_43",
    #     # "logsHumanEvalXQuant1",      
    #     # "logsHumanEvalXQuant2"      
    #     ]
    
    # visualize_from_fileCombineAllResults("./Projects/HelloWorld", logs,  "CombinedResultOfAll")

    # deleted_rows = visualize_from_file("./Projects/HelloWorld", "CombinedResultOfAll")
    # visualize_from_file_CompilationError("./Projects/HelloWorld", "CombinedResultOfAll", True, deleted_rows)
      