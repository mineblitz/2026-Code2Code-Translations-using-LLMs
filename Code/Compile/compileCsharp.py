import os
import subprocess
from Compile.helper import addToDataFrame, logCompileError

def compile_and_run_csharp_file(file_path, execution_status, logs, flag_object):
    try:
        file_directory, file_name = os.path.split(file_path)
        if not flag_object.NotCScharfAenderung:
            subprocess.run(["csc.bat", "/out:" + os.path.join(file_directory, os.path.splitext(file_name)[0] + ".exe"), file_path], check=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else: 
            cscPath = "C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\csc.exe"
            subprocess.run([cscPath, "/out:" + os.path.join(file_directory, os.path.splitext(file_name)[0] + ".exe"), file_path], check=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        executable_path = os.path.splitext(file_path)[0] + ".exe"
        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        return ["mono", executable_path]
    except subprocess.CalledProcessError as e:
        addToDataFrame(execution_status.compilation_failed, file_name, 1)
        logCompileError(e, file_path, file_name, "c#", logs)
        return None