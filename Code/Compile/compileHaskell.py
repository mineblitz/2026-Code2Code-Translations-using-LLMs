import os
import subprocess
from Compile.helper import add_HaskellImports, addToDataFrame, logCompileError

def compile_and_run_haskell_file(file_path, execution_status, logs, flag_object):
    try:
        file_directory, file_name = os.path.split(file_path)

        if flag_object.HaskellAddImportsFlag: add_HaskellImports(file_path)

        
        # Compile the Haskell file
        compile_process = subprocess.run(
            ["ghc", file_path, "-o", os.path.join(file_directory, 'outputHS')],
            check=True,
            capture_output=True,
            timeout=30
        )

        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        return [os.path.join(file_directory, 'outputHS')]
    except subprocess.CalledProcessError as e:
        addToDataFrame(execution_status.compilation_failed, file_name, 1)        
        logCompileError(e, file_path, file_name , 'Haskell', logs)
        None
