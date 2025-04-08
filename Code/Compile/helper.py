import os
import re
import csv

log_file_pathCompilation = 'LogCompilationFailed.csv'
log_file_pathTest = 'LogTestFailed.csv'
log_reTranslate = 'reTranslate.csv'
rerunRows = ['ErrorType', 'dirPath', 'StackTrace', 'Output', 'stdErr', "TestInput" , "TestOutput", "GeneratedOutput"]

languages = ['C', 'C++', 'C#', 'Java', 'Javascript', 'Pascal', 'Python', 'Haskell']

def extract_public_class_name(file_path):
    class_pattern = re.compile(r'\bpublic\s+class\s+(\w+)\b')
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        match = class_pattern.search(content)
        if match:
            return match.group(1)
        else:
            return None
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    
def remove_backticks_lines(file_path, removeAfterBackTicks):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        
        FirstEncounter = True
        for line in lines:
            if '```' in line: FirstEncounter = False

        with open(file_path, 'w') as file:
            for line in lines:
                if '```' not in line and FirstEncounter:
                    file.write(line)  
                elif '```' in line and FirstEncounter and removeAfterBackTicks: break
                elif '```' in line: FirstEncounter = True
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def remove_pascal_crt_lib(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        with open(file_path, 'w') as file:
            for line in lines:
                if 'uses crt;' not in line:
                    file.write(line)    
    except FileNotFoundError:
        print(f"File not found: {file_path}")

def logCompileError(e, DirPath, filename, language, logs):
    saveForRerunCompilationFailed(e, DirPath)
    two_dirs_up = os.path.dirname(os.path.dirname(os.path.dirname(DirPath)))
    Pathlog_file_pathCompilation= os.path.join(two_dirs_up, logs, log_file_pathCompilation)
    file_exists = os.path.isfile(Pathlog_file_pathCompilation)
    
    with open(Pathlog_file_pathCompilation, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(['language', 'filename', 'DirPath', 'Returncode', 'Command', 'Output', 'Stdout', 'Stderr'])  # Write header if file is new
        
        stderr_str = e.stderr.decode('utf-8') if e.stderr else ''
        
        writer.writerow([language, filename , DirPath, str(e.returncode), ' '.join(e.cmd), str(e.output), stderr_str])

def logTestError(lan, file_path,filename,returncode,input,  Expected, actualy, logs):  
    saveForRerunTestFailed(file_path, input, Expected, actualy)
    two_dirs_up = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
    Pathlog_file_pathTest = os.path.join(two_dirs_up, logs, log_file_pathTest)
    file_exists = os.path.isfile(Pathlog_file_pathTest)
    
    with open(Pathlog_file_pathTest, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(['language', 'File Path',filename ,'returncode','input', 'Expected', 'actualy'])  # Write header if file is new
        
        writer.writerow([lan, file_path,filename,returncode,input,Expected, actualy])

def addToDataFrame(dataframe, file, value):
    if any(substring in file for substring in ['.pas', '.js', '.hs', '.c++', '.c', '.cs', '.java', '.py']):
        LangNames = file.split("To")            
        dataframe.loc[LangNames[0], LangNames[1].split('.')[0]] = value


def saveForRerunCompilationFailed(e, DirPath):
    file_exists = os.path.isfile(log_reTranslate)

    with open(log_reTranslate, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(rerunRows)  # Write header if file is new        
        writer.writerow(["CompilationFailed", DirPath,"", str(e.output), str(e.stderr), "", "", ""])

def saveForRerunRunttimeFailed(stderr, DirPath):
    file_exists = os.path.isfile(log_reTranslate)

    with open(log_reTranslate, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(rerunRows)  # Write header if file is new                
        writer.writerow(["RuntimeFailed", DirPath, stderr,"", "", "", "", ""])

def saveForRerunTestFailed(DirPath, Input, Output, generated):
    Input = remove_problematic_chars(Input)
    Output = remove_problematic_chars(Output)
    generated = remove_problematic_chars(generated)
    file_exists = os.path.isfile(log_reTranslate)

    with open(log_reTranslate, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(rerunRows)  # Write header if file is new                
        writer.writerow(["TestFailed", DirPath, "","", "", Input, Output, generated])

def remove_problematic_chars(text):
    if isinstance(text, list):
        return [t.encode("ascii", "ignore").decode("ascii") if isinstance(t, str) else t for t in text]
    elif isinstance(text, str):
        return text.encode("ascii", "ignore").decode("ascii")
    else:
        return text

def saveForRerunInfinitieLoop(DirPath):
    file_exists = os.path.isfile(log_reTranslate)

    with open(log_reTranslate, 'a', newline='') as log_file:
        writer = csv.writer(log_file)
        if not file_exists:
            writer.writerow(rerunRows)  # Write header if file is new                
        writer.writerow(["InfiniteLoop", DirPath, "","", "", "", "", ""])

def add_mode_directive(file_path):
    old_directive = "{$mode objfpc}{$H+}\n"
    new_directive = "{$mode delphi}{$H+}\n"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Check if the old directive is present
    directive_found = False
    for i in range(min(5, len(lines))):  # Check the first 5 lines for the directive
        if lines[i] == old_directive:
            directive_found = True
            lines[i] = new_directive
            break
    
        # Check if the old directive is present
    directive_found_new = False
    for i in range(min(5, len(lines))):  # Check the first 5 lines for the directive
        if lines[i] == new_directive:
            directive_found_new = True
            break

    # If the old directive was found and replaced
    if directive_found:
        with open(file_path, 'w') as file:
            file.writelines(lines)
    else:
        # If the old directive was not found, optionally add the new one at the beginning
        with open(file_path, 'w') as file:
            if not directive_found_new: file.write(new_directive)
            file.writelines(lines)


def add_HaskellImports(file_path):
    Imports = "import System.Environment (getArgs)\n"
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Check for module declaration
    module_index = next((i for i, line in enumerate(lines) if line.strip().startswith('module ')), None)
    
    # Remove any existing instance of the import
    lines = [line for line in lines if line.strip() != Imports.strip()]
    
    # Insert the import statement after the module declaration, if it exists
    if module_index is not None:
        lines.insert(module_index + 1, Imports)
    else:
        lines.insert(0, Imports)
    
    # Write the updated lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)
