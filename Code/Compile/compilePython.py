import os
import subprocess
from Compile.helper import addToDataFrame, logCompileError

def compile_and_run_python_file(file_path, execution_status, logs):
    try:
        file_directory, file_name = os.path.split(file_path)

        subprocess.run(["python", "-m", "py_compile", os.path.join(file_directory, file_name)], check=True, capture_output=True, timeout=30)

        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        return ['python', os.path.join(file_directory, file_name)]
    except subprocess.CalledProcessError as e:
        addToDataFrame(execution_status.compilation_failed, file_name, 1)
        logCompileError(e, file_path ,file_name , "Python", logs)
        stdout = -1
        return None