import os
from subprocess import Popen, PIPE
import subprocess
from Compile.helper import addToDataFrame, logCompileError, logTestError, saveForRerunInfinitieLoop, saveForRerunRunttimeFailed

expected_output1 = '''\
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    ***************
   *****************
  *******************
 *********************
  *******************
   *****************
    ***************
     *************
      ***********
       *********
        *******
         *****
          ***
           *
'''.rstrip()

expected_output2 = '''\
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
*********************
 *******************
  *****************
   ***************
    *************
     ***********
      *********
       *******
        *****
         ***
          *
'''.rstrip()

def test_baklava(runArguments, execution_status, currentLan, filename, dirPath, logs):
    try:
        runningApplication = Popen([*runArguments], stdin=PIPE, stdout=PIPE, stderr=PIPE)
        try:
            stdout, stderr = runningApplication.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            saveForRerunInfinitieLoop(os.path.join(dirPath, filename))
            addToDataFrame(execution_status.infinite_loop, filename, 1)
            return 0
        
        formatedString = stdout.decode('utf-8').replace('\r\n','\n').rstrip()

        if formatedString == expected_output1 or formatedString == expected_output2:
            execution_status.compiled_and_ran[currentLan].append(runArguments[-1])
            return 1
        else:
            if stderr.decode()=='': 
                addToDataFrame(execution_status.test_failure, filename, 1)
                logTestError(currentLan, os.path.join(dirPath, filename), filename,runningApplication.returncode,"", expected_output1 , formatedString, logs)
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
                logCompileError(e, os.path.join(dirPath, filename), filename, currentLan, logs)