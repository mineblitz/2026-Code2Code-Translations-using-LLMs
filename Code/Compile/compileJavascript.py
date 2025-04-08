import os
import subprocess
from Compile.helper import addToDataFrame, logCompileError

def compile_and_run_js_file(file_path, execution_status, logs):
    try:
        file_directory, file_name = os.path.split(file_path)

        # javascript does not need to be compiled bevorhand so there are no errors tracked for compilation
        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        return ['node', os.path.join(file_directory, file_name)]
    except subprocess.CalledProcessError as e:
        addToDataFrame(execution_status.compilation_failed, file_name, 1)
        logCompileError(e,file_path,  file_name, "javascript", logs)
        return None