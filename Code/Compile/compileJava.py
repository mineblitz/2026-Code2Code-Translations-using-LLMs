import os
import subprocess
from Compile.helper import addToDataFrame, extract_public_class_name
from Compile.helper import logCompileError

def compile_and_run_java_file(file_path, execution_status, logs, flag_object):
    file_directory, file_name = os.path.split(file_path)
    oldFileName = file_path    
    className = extract_public_class_name(file_path)
    originalName = "Main.java"

    if(className is None or flag_object.notJavaClassNameChange):
        originalName = file_name
    else:
        originalName = className + ".java"
        

    newPath = os.path.join(file_directory, originalName)
    classpath = newPath
    classpath = classpath[:-len('java')] + 'class'
    if(className is None):
        className = file_name[:-len('.java')]

    relativJavaLibarys = "./JavaLibs/*"
    absoluteJavaLibarys = os.path.abspath(relativJavaLibarys)

    

    try:
        os.rename(oldFileName, newPath)

        if flag_object.addLibarys:
            subprocess.run(["javac","-cp", relativJavaLibarys, newPath], check=True, capture_output=True, timeout=30)
        else: 
            subprocess.run(["javac", newPath], check=True, capture_output=True, timeout=30)

        if os.path.isfile(newPath):
            os.rename(newPath, oldFileName)
        addToDataFrame(execution_status.compilation_failed, file_name, 0)
        if flag_object.addLibarys:
            return ['java', '-cp', f'{file_directory};{relativJavaLibarys}', className]
        else:
            return ['java', '-cp', file_directory, className]

    except subprocess.CalledProcessError as e:
        addToDataFrame(execution_status.compilation_failed, file_name, 1)
        logCompileError(e,file_path,  file_name, "Java", logs)
        if os.path.isfile(newPath):
            os.rename(newPath, oldFileName)
        return None