import os
from subprocess import Popen, PIPE
import subprocess
from Compile.helper import addToDataFrame, logCompileError, logTestError, saveForRerunInfinitieLoop, saveForRerunRunttimeFailed

def test_helloworld(runArguments, execution_status, currentLan, filename, dirPath, logs):

    expected_output1 = "\bHello World\r\n"
    expected_output2 = "\bHello World"
    
    try:
        runningApplication = Popen([*runArguments], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        try:
            stdout, stderr = runningApplication.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            saveForRerunInfinitieLoop(os.path.join(dirPath, filename))
            addToDataFrame(execution_status.infinite_loop, filename, 1)
            return 0
        
        if stdout.strip() == expected_output1 or expected_output2:
                return 1
        else:
            if stderr.decode()=='': 
                addToDataFrame(execution_status.test_failure, filename, 1)
                logTestError(currentLan, os.path.join(dirPath, filename), filename,runningApplication.returncode, "", expected_output1, stdout.strip(), logs)
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