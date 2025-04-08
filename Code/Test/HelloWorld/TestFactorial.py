import json
from subprocess import Popen, PIPE
import os
import subprocess
from Compile.helper import addToDataFrame, logCompileError, logTestError, saveForRerunInfinitieLoop, saveForRerunRunttimeFailed

def test_Factorial(runArguments, execution_status, currentLan, filename, dirPath, logs):
    test_cases = []
    with open(os.path.join(dirPath, "..", "..", "TestData.json"), 'r') as file:
        test_cases = json.load(file)
        
    for test in test_cases:
        try:
            runningApplication = Popen([*runArguments, test['input']], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        
            try:
                stdout, stderr = runningApplication.communicate(timeout=10)                                     
                formatedString = stdout.strip().decode('utf-8')
            except subprocess.TimeoutExpired:
                saveForRerunInfinitieLoop(os.path.join(dirPath, filename))
                addToDataFrame(execution_status.infinite_loop, filename, 1)
                return 0

            if formatedString.lower() in test['expected'].lower():
                continue
            else:     
                if stderr.decode()=='':               
                    addToDataFrame(execution_status.test_failure, filename, 1)
                    logTestError(currentLan, os.path.join(dirPath, filename), filename,runningApplication.returncode, test['input'], test['expected'].lower(), formatedString.lower(), logs)
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
