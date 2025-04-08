import os
import subprocess
from Compile.helper import add_mode_directive, addToDataFrame, logCompileError

def compile_and_run_pascal_file(file_path, execution_status, logs, flag_object):
    try:
        file_directory, file_name = os.path.split(file_path)
        file_name_no_ending = file_name.split('.')[0] 
        
        if flag_object.PascallAddCompileOptionFlag: add_mode_directive(file_path)

        # Compile the Pascal file
        compile_process = subprocess.run(
            ["fpc", file_path],
            check=True,
            capture_output=True,
            timeout=30
        )        
        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        return [os.path.join(file_directory, file_name_no_ending)]
    except subprocess.CalledProcessError as e:        
        addToDataFrame(execution_status.compilation_failed, file_name, 1)
        logCompileError(e,file_path , file_name, "Pascal", logs)
        stdout = -1
        return None