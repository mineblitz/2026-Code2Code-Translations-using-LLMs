import ast
import json
from subprocess import Popen, PIPE
import os
import subprocess
from Compile.helper import addToDataFrame, logCompileError, logTestError, saveForRerunInfinitieLoop, saveForRerunRunttimeFailed

def test_HumanEvalX(runArguments, execution_status, currentLan, filename, dirPath, logs):
    test_cases = []
    with open(os.path.join(dirPath, "..", "..", "TestData.json"), 'r') as file:
        test_cases = json.load(file)
        
    for test in test_cases:
        runningApplication = None
        try:
            runningApplication = Popen([*runArguments, * [str(item) for item in test['input']]], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        
            try:
                stdout, stderr = runningApplication.communicate(timeout=10)  
                try:                                   
                    formatedString = stdout.strip().decode('utf-8')
                except UnicodeDecodeError:
                    logTestError(currentLan, os.path.join(dirPath, filename), filename,runningApplication.returncode, test['input'], test['expected'], stdout.strip(), logs)
                    return 0  

            except subprocess.TimeoutExpired:
                saveForRerunInfinitieLoop(os.path.join(dirPath, filename))
                addToDataFrame(execution_status.infinite_loop, filename, 1)
                return 0

            answer, answerValue = processAnswer(formatedString, test)
            if answer:
                continue
            else:     
                if stderr.decode()=='':               
                    addToDataFrame(execution_status.test_failure, filename, 1)
                    logTestError(currentLan, os.path.join(dirPath, filename), filename,runningApplication.returncode, test['input'], test['expected'], answerValue, logs)
                    return 0   
                else:
                    addToDataFrame(execution_status.runtime_error, filename, 1)
                    saveForRerunRunttimeFailed(stderr, os.path.join(dirPath, filename))
                    return 0    
        except (subprocess.CalledProcessError) as e:
            addToDataFrame(execution_status.compilation_failed, filename, 1)
            logCompileError(e, os.path.join(dirPath, filename), filename, currentLan, logs)
            return 0
        finally:
            if runningApplication is not None:
                try:
                    runningApplication.terminate()
                except Exception as e:
                    print("Fehler beim schließen")
       
        
    execution_status.compiled_and_ran[currentLan].append(runArguments[-1])
    return 1

def processAnswer(string, test):
    evaluedString = evaluate_string(string)
    
    if isinstance(evaluedString, str):
        if evaluedString == "true": evaluedString = True
        elif evaluedString == "false": evaluedString = False
    if isinstance(test['expected'], str):
        test['expected'] = evaluate_string(test['expected'])
    if not test['postProcessingValue'] == "":  
        if isinstance(test['postProcessingValue'], str):
            if "/" in test['postProcessingValue']:
                part1 = evaluate_string(test['postProcessingValue'].split("/")[0])
                part2 = evaluate_string(test['postProcessingValue'].split("/")[1])
                test['postProcessingValue'] = part1 / part2
        if not isinstance(test['postProcessingValue'], (int, float)): return [False, evaluedString]
        if not isinstance(evaluedString, (int, float)): return [False, evaluedString]
        if test['postProcessingOperator'] == "-":       
            evaluedString = abs(evaluedString - test['postProcessingValue'])
        if test['postProcessingOperator'] == "+":
            evaluedString = abs(evaluedString + test['postProcessingValue'])
    
    if test["operator"] == "==":
        return [evaluedString == test['expected'], evaluedString]
    if test["operator"] == "<":
        return [evaluedString < test['expected'], evaluedString]
    if test["operator"] == ">":
        return [evaluedString > test['expected'], evaluedString]
    if test["operator"] == "<=":
        return [evaluedString <= test['expected'], evaluedString]
    if test["operator"] == ">=":
        return [evaluedString >= test['expected'], evaluedString]
    return [False, evaluedString]


def evaluate_string(s):
    try:
        # Try to evaluate the string using ast.literal_eval to safely evaluate literals
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        # If literal_eval fails, it means the string isn't a valid literal
        return s