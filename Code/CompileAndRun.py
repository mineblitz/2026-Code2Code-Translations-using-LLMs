import os
import numpy as np
import pandas as pd
from Compile.compileC import compile_and_run_c_file
from Compile.compileCsharp import compile_and_run_csharp_file
from Compile.compileJava import compile_and_run_java_file
from Compile.compilePython import compile_and_run_python_file
from Compile.compileCpp import compile_and_run_cpp_file
from Compile.compileHaskell import compile_and_run_haskell_file
from Compile.compileJavascript import compile_and_run_js_file
from Compile.compilePascal import compile_and_run_pascal_file
from Compile.helper import addToDataFrame, remove_backticks_lines, remove_pascal_crt_lib
from Test.HelloWorld.TestFactorial import test_Factorial
from Test.HelloWorld.TestHelloWorld import test_helloworld
from Test.HelloWorld.TestHumanEvalX import test_HumanEvalX
from Test.HelloWorld.TestPrimeNumber import test_PrimeNumber
from Test.HelloWorld.TestBaklava import test_baklava

# Define the languages
languages = ['C', 'C++', 'C#', 'Java', 'Javascript', 'Pascal', 'Python', 'Haskell']

languageDict = {}
languageDict['c'] = 'C'
languageDict['c++'] = 'C++'
languageDict['cs'] = 'C#'
languageDict['java'] = 'Java'
languageDict['js'] = 'Javascript'
languageDict['pas'] = 'Pascal'
languageDict['py'] = 'Python'
languageDict['hs'] = 'Haskell'
class ExecutionStatus:
    def __init__(self):
        self.compiled_and_ran =      {'Python': [], 'Java': [], 'C#': [], 'C': [], 'C++': [], 'Haskell': [], 'JavaScript': [], 'Pascal': []}
        self.compilation_failed =    pd.DataFrame(0, index=languages, columns=languages)
        self.runtime_error =         pd.DataFrame(0, index=languages, columns=languages)
        self.infinite_loop =         pd.DataFrame(0, index=languages, columns=languages)
        self.test_failure =          pd.DataFrame(0, index=languages, columns=languages)
        self.total_files =           {'Python': 0,  'Java': 0,  'C#': 0,  'C': 0,  'C++': 0,  'Haskell': 0,  'JavaScript': 0,  'Pascal': 0}
        self.compilation_matrix =    pd.DataFrame(np.nan, index=languages, columns=languages)

def compile_and_run_files_in_directory(directory_path, logs, flag_object, whiteListFileName = None):
    remove_artifacts(directory_path)
    execution_status = ExecutionStatus() 
    
    if whiteListFileName is not None: whiteList = recreateFilenamesFromCSV(whiteListFileName)  
    for file in os.listdir(directory_path):
        if whiteListFileName is not None: 
            if file in whiteList:
                addToDataFrame(execution_status.compilation_matrix, file, 1)
                continue
        
        joinedPath = os.path.join(directory_path, file)
        if not flag_object.notRemoveBackTicks:
            remove_backticks_lines(joinedPath, flag_object.removeAfterBackTicks)

        if not flag_object.notRmeoveCRTlib:
            remove_pascal_crt_lib(joinedPath)

        runArguments = None
        currentLan = ""

        result = 0
        if file.endswith('.py'):
            currentLan = 'Python'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_python_file(joinedPath, execution_status, logs)

        elif file.endswith('.java'):
            currentLan = 'Java'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_java_file(joinedPath, execution_status, logs, flag_object)

        elif file.endswith('.cs'):
            currentLan = 'C#'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_csharp_file(joinedPath, execution_status, logs, flag_object)

        elif file.endswith('.c'):
            currentLan = 'C'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_c_file(joinedPath, execution_status, logs)
            
        elif file.endswith('.c++'):
            currentLan = 'C++'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_cpp_file(joinedPath, execution_status, logs)

        elif file.endswith('.hs'):
            currentLan = 'Haskell'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_haskell_file(joinedPath, execution_status, logs, flag_object)

        elif file.endswith('.js'):
            currentLan = 'JavaScript'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_js_file(joinedPath, execution_status, logs)
      
        elif file.endswith('.pas'):
            currentLan = 'Pascal'
            execution_status.total_files[currentLan] += 1
            runArguments = compile_and_run_pascal_file(joinedPath, execution_status, logs, flag_object)

        if(runArguments):
            result = run_tests(directory_path, runArguments, execution_status, currentLan, file, logs)

        addToDataFrame(execution_status.compilation_matrix, file, result)

    # Aufräumarbeiten
    remove_artifacts(directory_path)

    return execution_status

def remove_artifacts(directory):
     if os.path.exists(os.path.join(directory, '__pycache__')):
        delete_directory(os.path.join(directory, '__pycache__'))
     for file_name in os.listdir(directory):
        if file_name.endswith('.exe') or file_name.endswith('.o') or file_name.endswith('.hi') or file_name.endswith('.class'):
            file_path = os.path.join(directory, file_name)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

def recreateFilenamesFromCSV(file_path):
    # Load the dataframe from the CSV
    dataframe = pd.read_csv(file_path, index_col=0)
    
    filenames = []
    for row_label in dataframe.index:
        for col_label in dataframe.columns:
            if dataframe.loc[row_label, col_label] == 1:
                # Find the key corresponding to the column label
                file_extension_key = next(key for key, value in languageDict.items() if value == col_label)
                # Construct the filename
                filename = f"{row_label}To{col_label}.{file_extension_key}"
                filenames.append(filename)
    
    return filenames


def delete_directory(directory_path):
    if not os.path.isdir(directory_path):
        return

    for root, dirs, files in os.walk(directory_path, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                os.rmdir(dir_path)
                print(f"Deleted directory: {dir_path}")
            except Exception as e:
                print(f"Error deleting directory {dir_path}: {e}")
    
    try:
        os.rmdir(directory_path)
    except Exception as e:
        print(f"Error deleting root directory {directory_path}: {e}")

def run_tests(directory_path, runArguments, execution_status, currentLan, filename, logs):
    result = 0

    up_two_dirs = os.path.abspath(os.path.join(directory_path, "../.."))
    up_thre_dirs = os.path.abspath(os.path.join(directory_path, "../../.."))
    # up_two_dirs = os.path.abspath(os.path.join(directory_path, ".."))
    dir_name = os.path.basename(up_two_dirs)
    dir_name3up = os.path.basename(up_thre_dirs)

    if dir_name == "HelloWorld":
        result = test_helloworld(runArguments, execution_status, currentLan, filename, directory_path, logs)
    if dir_name == "PrimeNumber":
        result = test_PrimeNumber(runArguments, execution_status, currentLan, filename, directory_path, logs)
    if dir_name == "Baklava":
        result = test_baklava(runArguments, execution_status, currentLan, filename, directory_path, logs)  
    if dir_name == "Factorial":
        result = test_Factorial(runArguments, execution_status, currentLan, filename, directory_path, logs)  
    if dir_name3up == "HumanEvalX":
    # if dir_name == "HumanEvalX":
        result = test_HumanEvalX(runArguments, execution_status, currentLan, filename, directory_path, logs)  
    
    return result

if __name__ == "__main__":
    # remove_artifacts('./Projects/PrimeNumber/Executions1/07-27-2024_13h06m26s')
    
    directory_path = "./Projects/HelloWorld/Executions1/07-06-2024_09h34m"
    # directory_path = "./Projects/PrimeNumber/Executions/07-26-2024_19h43m24s"
    # directory_path = "./Projects/PrimeNumber/Code_Input"
    # directory_path = "./Projects/Baklava/Code_Input"

    # directory_path = f"./Projects/HumanEvalX/162/Code_Input"
    execution_status = compile_and_run_files_in_directory(directory_path, "logs")

    # for i in range(163):
    #     if i in {12, 22, 32, 33, 37,38, 44, 50,51, 52, 53, 61, 72, 77,78,90, 92, 95, 97, 103, 107,112, 114, 117, 125, 128, 136, 137, 144, 148, 151, 154, 155, 160, 162, 115, 111, 87, 129}: continue    
    #     directory_path = f"./Projects/HumanEvalX/{i}/Code_Input"

    #     execution_status = compile_and_run_files_in_directory(directory_path)

   


   

