import ast
import csv
import json
import re
import shutil
from openai import OpenAI
# from dotenv import load_dotenv
from datetime import datetime
import os

import pandas as pd

from CompileAllTranslation import compile_all, compile_all_Quant
# from PostProcessingAfterSplit import addProgrammStructure, removeBackticks

languageDict = {}
languageDict['c'] = 'C'
languageDict['c++'] = 'C++'
languageDict['cs'] = 'C#'
languageDict['java'] = 'Java'
languageDict['js'] = 'Javascript'
languageDict['pas'] = 'Pascal'
languageDict['py'] = 'Python'
languageDict['hs'] = 'Haskell'


def translateInititialy(flag_object, experiment, run):

    ExecutionsDirName = f'ExecutionsExp{experiment}Run{run}'
    # load_dotenv()

    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )
    for x in range(flag_object.numberOfRuns):
        timeStamp = datetime.now().strftime("%m-%d-%Y_%Hh%Mm%Ss")

        dirname = os.path.dirname(__file__)
        fullProjectDir = os.path.join(dirname, flag_object.currentProjectDir)
        codesnipetDir = os.path.join(fullProjectDir,'Code_Input')
        executionDir = os.path.join(fullProjectDir, ExecutionsDirName)
        currentExecutionDir = os.path.join(executionDir, timeStamp)
        filenames = os.listdir(codesnipetDir)

        os.makedirs(currentExecutionDir, exist_ok=True)

        for languageFile in filenames:
            fullFileName = languageFile.split('/')[-1]
            fileEnding = fullFileName.split('.')[1]
            fileCodeName = fullFileName.split('.')[0]

            SOURCE_CODE = ""
            with open(codesnipetDir + "/" + languageFile) as f:
                SOURCE_CODE = f.read()

            SOURCE_LANG = languageDict[fileEnding]

            for language in languageDict.items():
                if fileEnding == language[0]:
                    continue
                
                TARGET_LANG = language[1]
                TEXT_TARGET_LANG = language[1]
                if flag_object.JavascriptNodeJS:
                    if TEXT_TARGET_LANG == "Javascript":
                        TEXT_TARGET_LANG = "Javascript Node.js"
                    TEXT_SOURCE_LANG = SOURCE_LANG
                    if TEXT_SOURCE_LANG == "Javascript":
                        TEXT_SOURCE_LANG = "Javascript Node.js"

                userContentMessage = ""
                if not flag_object.WithTestsFlag:  
                        userContentMessage = flag_object.Message.format(
                        SOURCE_CODE=SOURCE_CODE,
                        TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                        TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                        )
                else:
                    with open(os.path.join(flag_object.currentProjectDir, "TestData.json"), 'r') as file:
                        test_cases = json.load(file)                    

                    test_cases_string = ""
                    for case in test_cases:
                        if not case['postProcessingValue'] == "":  
                            if isinstance(case['postProcessingValue'], str):
                                if "/" in case['postProcessingValue']:
                                    part1 = evaluate_string(case['postProcessingValue'].split("/")[0])
                                    part2 = evaluate_string(case['postProcessingValue'].split("/")[1])
                                    case['postProcessingValue'] = part1 / part2
                            if case['postProcessingOperator'] == "-":       
                                case["expected"] = abs(case["expected"] - case['postProcessingValue'])
                            if case['postProcessingOperator'] == "+":
                                case["expected"] = abs(case["expected"] + case['postProcessingValue'])
                        input_value = case["input"]
                        expected_output = case["expected"]
                        test_cases_string += f"Input: {input_value}, expected output: {expected_output}\n"
                    
                    if flag_object.WithExplanation:
                        EXPLANATION = getCodeExplanation(client, flag_object, SOURCE_CODE, TEXT_SOURCE_LANG, TEXT_TARGET_LANG)
                        userContentMessage = flag_object.Message.format(
                            SOURCE_CODE=SOURCE_CODE,
                            TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                            TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                            EXPLANATION=EXPLANATION,
                            test_cases_string=test_cases_string
                            )
                    else:
                        userContentMessage = flag_object.Message.format(
                            SOURCE_CODE=SOURCE_CODE,
                            TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                            TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                            test_cases_string=test_cases_string
                            )   
                SystemRole = flag_object.SystemRole.format(
                    TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                    TEXT_TARGET_LANG=TEXT_TARGET_LANG)
                            
                completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                      {"role": "system", "content": SystemRole},
                    {"role": "user", "content": userContentMessage}
                ]
                )

                responseMessage = completion.choices[0].message.content

                try:
                    logString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n----------\n" + userContentMessage + "\n----------\n" + responseMessage + "\n" + "################\n"
                    with open("Log.txt", "a") as text_file:
                        text_file.write(logString)
                except UnicodeEncodeError as e:
                    print(f"Unicode encoding error: {e}")

                fileStringWithEnding = SOURCE_LANG + 'To' + TARGET_LANG + '.' + language[0]
                with open(currentExecutionDir + "/" + fileStringWithEnding, "w") as lang_file:
                    lang_file.write(responseMessage)


def getexplanationForFunctions(client, flag_object, functions, SOURCE_CODE, TEXT_SOURCE_LANG, TEXT_TARGET_LANG):
    explanations = []
    for function in functions:    
        userContentMessage = flag_object.MessageFunctionExplanation.format(
        FUNCTION = function,
        SOURCE_CODE=SOURCE_CODE,
        TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
        TEXT_TARGET_LANG=TEXT_TARGET_LANG)

        SystemRole = flag_object.SystemRoleFunctionExplanation.format(
        TEXT_SOURCE_LANG=TEXT_SOURCE_LANG)

        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
                {"role": "system", "content": SystemRole},
            {"role": "user", "content": userContentMessage}
        ]
        )

        responseMessage = completion.choices[0].message.content

        try:
            logString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n----------\n" + userContentMessage + "\n----------\n" + responseMessage + "\n" + "################\n"
            with open("Log.txt", "a") as text_file:
                text_file.write(logString)
        except UnicodeEncodeError as e:
            print(f"Unicode encoding error: {e}")

        explanations.append(responseMessage)

    return explanations

def getCodeExplanation(client, flag_object, SOURCE_CODE, TEXT_SOURCE_LANG, TEXT_TARGET_LANG):
    userContentMessage = flag_object.MessageExplanation.format(
    SOURCE_CODE=SOURCE_CODE,
    TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
    TEXT_TARGET_LANG=TEXT_TARGET_LANG)

    SystemRole = flag_object.SystemRoleExplanation.format(
    TEXT_SOURCE_LANG=TEXT_SOURCE_LANG)

    completion = client.chat.completions.create(
    model=flag_object.modelName,
    messages=[
            {"role": "system", "content": SystemRole},
        {"role": "user", "content": userContentMessage}
    ]
    )

    # responseMessage = 
    responseMessage = completion.choices[0].message.content

    try:
        logString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n----------\n" + userContentMessage + "\n----------\n" + responseMessage + "\n" + "################\n"
        with open("Log.txt", "a") as text_file:
            text_file.write(logString)
    except UnicodeEncodeError as e:
        print(f"Unicode encoding error: {e}")

    return responseMessage

def evaluate_string(s):
    try:
        # Try to evaluate the string using ast.literal_eval to safely evaluate literals
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        # If literal_eval fails, it means the string isn't a valid literal
        return s
        
def reTranslate(flag_object, ExecutionsDir, safeToDir):
    # load_dotenv()

    client = OpenAI(
        api_key=os.environ['OPENAI_API_KEY'],
    )


    log_reTranslate = 'reTranslate.csv'
    failedTranslations = pd.read_csv(log_reTranslate)

    # Convert the 'input' column to a string type to handle mixed types
    failedTranslations["ErrorType"] = failedTranslations["ErrorType"].astype(str)
    # print(failedTranslations.columns)
    counter = 0
    for index, row in failedTranslations.iterrows():        
        # print(counter)
        counter += 1

        file_path = row['dirPath']   

        if os.path.exists(file_path):
            continue
    
        file_name = os.path.basename(file_path)
        file_name = os.path.splitext(file_name)[0]
        parts = file_name.split("To")    
        SOURCE_LANG = parts[0]
        TARGET_LANG = parts[1]

        
        with open(file_path) as f:
            TRANSLATED_CODE = f.read()
        
        sourceCodePath = os.path.join(file_path, "..", "..", "..", "Code_Input")
        sourceCodePath = getFilePathSourceCode(sourceCodePath, SOURCE_LANG)
        with open(sourceCodePath) as f:
            SOURCE_CODE = f.read()
        
        STDERR = ''
        if row["ErrorType"] == "CompilationFailed":
            if (row["stdErr"] == "") or (row["stdErr"] == "b''"):
                STDERR = row["Output"] 
            else:
                STDERR = row["stdErr"]
        elif row["ErrorType"] == "RuntimeFailed":
            STDERR = row["StackTrace"]
        elif row["ErrorType"] == "InfiniteLoop":
            STDERR = "the program enters infinite loop"

        userContentMessage = ""

        if not row["ErrorType"] == "TestFailed": 
            userContentMessage = flag_object.reTranslateError.format(
                    SOURCE_LANG=SOURCE_LANG,
                    TARGET_LANG=TARGET_LANG,
                    SOURCE_CODE=SOURCE_CODE,
                    TRANSLATED_CODE=TRANSLATED_CODE,
                    STDERR=STDERR)
            
        else: 
            GENERATED_OUTPUT = row["GeneratedOutput"]
            EXPECTED_OUTPUT = row["TestOutput"]
            TEST_INPUT = row["TestInput"]

            userContentMessage = flag_object.reTranslateTestFailed.format(
            SOURCE_LANG=SOURCE_LANG,
            TARGET_LANG=TARGET_LANG,
            SOURCE_CODE=SOURCE_CODE,
            TRANSLATED_CODE=TRANSLATED_CODE,
            TEST_INPUT=TEST_INPUT,
            EXPECTED_OUTPUT=EXPECTED_OUTPUT,
            GENERATED_OUTPUT=GENERATED_OUTPUT)

        completion = client.chat.completions.create(
        model= flag_object.modelName,
        messages=[
            {"role": "system", "content": "You will be provided with a piece of code, and your task is to translate it into a given programming language so that it is compilable."},
            {"role": "user", "content": userContentMessage}
        ]
        )

        responseMessage = completion.choices[0].message.content

        try:
            logString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n----------\n" + userContentMessage + "\n----------\n" + responseMessage + "\n" + "################\n"
            with open("Log.txt", "a") as text_file:
                text_file.write(logString)
        except UnicodeEncodeError as e:
            print(f"Unicode encoding error: {e}")

        SafeToFilePath = file_path.replace(ExecutionsDir, safeToDir)
        with open(file_path, "w") as lang_file:
            lang_file.write(responseMessage)

def getFilePathSourceCode(getFilePathSourceCode, SourceLang):
    extension = next((k for k, v in languageDict.items() if v == SourceLang), None)
    for file in os.listdir(getFilePathSourceCode):       
        fileEnding = file.split('.')[1]
        full_path = os.path.join(getFilePathSourceCode, file)
        if fileEnding == extension:
            return full_path

def translateInititialyQuant(flag_object, experiment, run):
    # load_dotenv()

    match flag_object.modelName:
        case "google/gemini-2.5-pro":            
            client = OpenAI(
                api_key=os.environ["OPENROUTER_API_KEY"],
                base_url="https://openrouter.ai/api/v1"
            )
        case "gpt-5.1-codex-max":            
            client = OpenAI(
                api_key=os.environ['OPENAI_API_KEY'],
            )
            
    counter = 0
    startAt = 0
    for x in range(flag_object.numberOfRuns):
        Projects = os.listdir(flag_object.currentProjectDir)
        for entry in Projects:

            projectDir = os.path.join(flag_object.currentProjectDir, entry)
            dirname = os.path.dirname(__file__)
            fullProjectDir = os.path.join(dirname, projectDir)
            codesnipetDir = os.path.join(fullProjectDir,'Code_Input')
            executionDir = os.path.join(fullProjectDir, f'ExecutionsExp{experiment}Run{run}')

            os.makedirs(executionDir, exist_ok=True)

            existing_runs = [
                d for d in os.listdir(executionDir)
                if os.path.isdir(os.path.join(executionDir, d))
            ]
            if existing_runs:
                latest_timestamp = sorted(existing_runs)[-1]
                currentExecutionDir = os.path.join(executionDir, latest_timestamp)
            else:
                timeStamp = datetime.now().strftime("%m-%d-%Y_%Hh%Mm%Ss")
                currentExecutionDir = os.path.join(executionDir, timeStamp)
                os.makedirs(currentExecutionDir)

            filenames = os.listdir(codesnipetDir)

            for languageFile in filenames:
                print(counter)                
                counter += 1
                if(counter < startAt): continue

                fullFileName = languageFile.split('/')[-1]
                fileEnding = fullFileName.split('.')[1]
                fileCodeName = fullFileName.split('.')[0]

                SOURCE_CODE = ""
                with open(codesnipetDir + "/" + languageFile) as f:
                    SOURCE_CODE = f.read()

                SOURCE_LANG = languageDict[fileEnding]

                for language in languageDict.items():
                    # 0 = file ending 1 = language name
                    if fileEnding == language[0]:
                        continue    
                    TARGET_LANG = language[1]                    
                    TEXT_TARGET_LANG = language[1]
                    
                    fileStringWithEnding = SOURCE_LANG + 'To' + TARGET_LANG + '.' + language[0]
                    newSaveFile = currentExecutionDir + "/" + fileStringWithEnding
                    if(os.path.exists(newSaveFile)):
                        continue

                    if flag_object.JavascriptNodeJS:
                        if TEXT_TARGET_LANG == "Javascript":
                            TEXT_TARGET_LANG = "Javascript Node.js"
                        TEXT_SOURCE_LANG = SOURCE_LANG
                        if TEXT_SOURCE_LANG == "Javascript":
                            TEXT_SOURCE_LANG = "Javascript Node.js"
                    userContentMessage = ""
                    if not flag_object.WithTestsFlag:  
                        userContentMessage = flag_object.Message.format(
                            SOURCE_CODE=SOURCE_CODE,
                            TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                            TEXT_TARGET_LANG=TEXT_TARGET_LANG
                            )
                    else:
                        with open(os.path.join(projectDir, "TestData.json"), 'r') as file:
                            test_cases = json.load(file)                        

                        test_cases_string = ""
                        for case in test_cases:
                            if not case['postProcessingValue'] == "":  
                                if isinstance(case['postProcessingValue'], str):
                                    if "/" in case['postProcessingValue']:
                                        part1 = evaluate_string(case['postProcessingValue'].split("/")[0])
                                        part2 = evaluate_string(case['postProcessingValue'].split("/")[1])
                                        case['postProcessingValue'] = part1 / part2
                                if case['postProcessingOperator'] == "-":       
                                    case["expected"] = abs(case["expected"] - case['postProcessingValue'])
                                if case['postProcessingOperator'] == "+":
                                    case["expected"] = abs(case["expected"] + case['postProcessingValue'])
                            input_value = case["input"]
                            expected_output = case["expected"]
                            test_cases_string += f"Input: {input_value}, expected output: {expected_output}\n"
                        
                    if flag_object.WithExplanation:
                        EXPLANATION = getCodeExplanation(client, flag_object, SOURCE_CODE, TEXT_SOURCE_LANG, TEXT_TARGET_LANG)
                        userContentMessage = flag_object.Message.format(
                            SOURCE_CODE=SOURCE_CODE,
                            TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                            TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                            EXPLANATION=EXPLANATION,
                            test_cases_string=test_cases_string
                            )
                    else:
                        userContentMessage = flag_object.Message.format(
                            SOURCE_CODE=SOURCE_CODE,
                            TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                            TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                            test_cases_string=test_cases_string
                            )  
                    SystemRole = flag_object.SystemRole.format(
                        TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                        TEXT_TARGET_LANG=TEXT_TARGET_LANG)
                    

                    match flag_object.modelName:
                        case "google/gemini-2.5-pro":
                            completion = client.chat.completions.create(
                            # completion = client.responses.create(
                            model = flag_object.modelName,
                            messages=[
                                {"role": "system", "content": SystemRole},
                                {"role": "user", "content": userContentMessage}
                            ]
                            )           
                            responseMessage = completion.choices[0].message.content                 
                        case "gpt-5.1-codex-max":                            
                                prompt = (
                                    f"You must follow the system instructions strictly.\n\n"
                                    f"System:\n{SystemRole}\n\n"
                                    f"User:\n{userContentMessage}\n\n"
                                    f"Assistant:\n"
                                )

                                completion = client.responses.create(
                                model = flag_object.modelName,
                                input=prompt,
                                )

                                responseMessage = completion.output_text
                    
                    # responseMessage = completion

                    try:
                        logString = datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n----------\n" + userContentMessage + "\n----------\n" + responseMessage + "\n" + "################\n"
                        with open("Log.txt", "a") as text_file:
                            text_file.write(logString)

                        with open(newSaveFile, "w") as lang_file:
                            lang_file.write(responseMessage)

                    except UnicodeEncodeError as e:
                        print(f"Unicode encoding error: {e}")


def reTranslateRun(flag_object, experiment, run):

    threshold = 0.05
    initialDir = "Executions"
    initialDirLogs = "logs"
    ExecutionsDirName = f'ExecutionsExp{experiment}Run{run}_'
    LogsDirName = f'logsExp{experiment}Run{run}_'
    counter = 0
    FailedBefore = 0
    FailedAfter = 0 

    source_dir = os.path.join(flag_object.currentProjectDir, initialDir)
    source_dirLogs = os.path.join(flag_object.currentProjectDir, initialDirLogs)

    if not os.path.exists(source_dir):
        translateInititialy(flag_object)
    if not os.path.exists(source_dirLogs):
        compile_all(flag_object, False)

    while True:
        
        ExecutionsDirNameCurrent = ExecutionsDirName+str(counter)
        destination_dir = os.path.join(flag_object.currentProjectDir, ExecutionsDirNameCurrent)    
        shutil.copytree(source_dir, destination_dir)

        LogsDirNameCurrent = LogsDirName+str(counter)
        Logsdestination_dir = os.path.join(flag_object.currentProjectDir, LogsDirNameCurrent)    
        os.rename(source_dirLogs, Logsdestination_dir) 

        FailedBefore = getNumberOfFails()
        if os.path.exists(source_dir):
            reTranslate(flag_object, initialDir, ExecutionsDirNameCurrent)
        if not os.path.exists(source_dirLogs):
            compile_all(flag_object, False)
        FailedAfter = getNumberOfFails()        
        counter += 1

        diffFailed = FailedBefore - FailedAfter
        if diffFailed/FailedBefore < threshold or counter > 1000:
            print(diffFailed/FailedBefore)
            break

    ExecutionsDirNameCurrent = ExecutionsDirName+str(counter)
    destination_dir = os.path.join(flag_object.currentProjectDir, ExecutionsDirNameCurrent)   
    os.rename(source_dir, destination_dir) 

    LogsDirNameCurrent = LogsDirName+str(counter)
    Logsdestination_dir = os.path.join(flag_object.currentProjectDir, LogsDirNameCurrent)    
    os.rename(source_dirLogs, Logsdestination_dir) 

def reTranslateRunQuant(flag_object, experiment, run):

    pathOverall = flag_object.currentProjectDir
    threshold = 0.05
    initialDir = f"ExecutionsExp{experiment}Run{run}"
    initialDirLogs = f"../../logsHumanEvalXExp{experiment}Run{run}_0"
    ExecutionsDirName = f'ExecutionsExp{experiment}Run{run}_'
    LogsDirName = f'../../logsHumanEvalXExp{experiment}Run{run}_'
    counter = 0
    FailedBefore = 0
    FailedAfter = 0 
    ReturnCounter = 0

    source_dir = os.path.join(flag_object.currentProjectDir,"0", initialDir)
    source_dirLogs = os.path.join(flag_object.currentProjectDir,"0", initialDirLogs)

    ExecutionsDirNameCurrent = ExecutionsDirName+str(0)
    Projects = os.listdir(pathOverall)
    for entry in Projects:           
        basePath = os.path.join(pathOverall, entry)   
        initialDir_Dir = os.path.join(pathOverall, entry, initialDir)   
        if not os.path.exists(initialDir_Dir): 
            copyToNewDirQuant(initialDir,basePath, flag_object)
    if not os.path.exists(source_dirLogs):
        compile_all_Quant(flag_object, False, experiment, run,initialDir, initialDirLogs)

    while True:
        ExecutionsDirNameCurrent = ExecutionsDirName+str(counter)
        Projects = os.listdir(pathOverall)
        for entry in Projects:           
            destination_dir = os.path.join(pathOverall, entry, ExecutionsDirNameCurrent)   
            initialDir_Dir = os.path.join(pathOverall, entry, initialDir)   
            if not os.path.exists(destination_dir): 
                shutil.copytree(initialDir_Dir, destination_dir)

        LogsDirNameCurrent = LogsDirName+str(counter+1)
        Logsdestination_dir = os.path.join(pathOverall, "0", LogsDirNameCurrent)    

        FailedBefore = 1 # initialise
        FailedAfter = 0

        if os.path.exists(source_dir) and not os.path.exists(Logsdestination_dir):
            FailedBefore = getNumberOfFails()
            shutil.copy('./reTranslate.csv', './reTranslate.csv'+str(counter))  
            if counter >= ReturnCounter: 
                reTranslate(flag_object, initialDir, ExecutionsDirNameCurrent)
                # vorheriger log pfad um erfolgreiche übersetzungen nicht erneut zu kompilieren
            PrevlogPath = LogsDirName+str(counter)  
            compile_all_Quant(flag_object, False, experiment, run,initialDir, LogsDirNameCurrent,PrevlogPath)       
            FailedAfter = getNumberOfFails() 
        print("FailedBefore: " + str(FailedBefore))  
        print("FailedAfter: " + str(FailedAfter))  
        
        diffFailed = FailedBefore - FailedAfter
        print("Percentage Improvement: " + str(diffFailed/FailedBefore))
        # Numbers only work for HumanEvalX
        successfulTranslation = ((3500 - FailedAfter) / 3500) * 28
        print("Erfolgreiche Übersetzungen: " + str(successfulTranslation))

        counter += 1

        if (diffFailed == 0):
            print(diffFailed/FailedBefore)
            break 

    Projects = os.listdir(pathOverall)
    ExecutionsDirNameCurrent = ExecutionsDirName+str(counter)
    for entry in Projects:          
        destination_dir = os.path.join(pathOverall, entry, ExecutionsDirNameCurrent)          
        initialDir_Dir = os.path.join(pathOverall, entry, initialDir)  
        if not os.path.exists(destination_dir): 
            os.rename(initialDir_Dir, destination_dir) 

    # LogsDirNameCurrent = LogsDirName+str(counter)
    # Logsdestination_dir = os.path.join(pathOverall, "..", LogsDirNameCurrent)    
    # if not os.path.exists(Logsdestination_dir): 
    #     os.rename(source_dirLogs, Logsdestination_dir) 

def getNumberOfFails():
    failed_translations = 0
    with open('retranslate.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            if row['ErrorType'] in ['TestFailed', 'RuntimeFailed', 'CompilationFailed', 'InfiniteLoop']:
                failed_translations += 1
    return failed_translations

def copyToNewDirQuant(newDirName, Path, flagObject):
    newPath = os.path.join(Path, newDirName)
    basisPath = os.path.join(Path, flagObject.reTranslateFrom)
    shutil.copytree(basisPath, newPath)

def saveJsonVariables(experimentDataJsonFile): 
    jsonData = {
    "currentProjectDir" : 'Projects/HumanEvalX/142' ,
    "WithTestsFlag" : True,
    "numberOfRuns" : 5,
    "HaskellAddImportsFlag": True,
    "PascallAddCompileOptionFlag": True,
    "JavascriptNodeJS": True,
    "removeAfterBackTicks": True,
    "reTranslate": True,
    "Message": "{SOURCE_CODE}\nTranslate the above {TEXT_SOURCE_LANG} code to {TEXT_TARGET_LANG}.\nProvide the complete program, including any necessary class definitions and main method or equivalent, ensuring that it works correctly with the provided input arguments.\nBe aware of the properties of the data types in {TEXT_SOURCE_LANG} and accurately translate the functionality into {TEXT_TARGET_LANG}.\nThe translated code must be able to handle the following test values without modification:\n{test_cases_string}\nEnsure that the code is compilable, syntactically correct, and does not use example or placeholder values in the main function or elsewhere.\nInput values should be passed directly from the function arguments, not hard-coded.\nDo not include any extra function calls or print statements beyond what is required to correctly implement the code in {TEXT_TARGET_LANG}.\nEnsure that variables are defined before use, and methods are defined before being invoked.\nAvoid naming conflicts by ensuring unique names for variables and methods.\nPrint only the {TEXT_TARGET_LANG} code.\n",
    "SystemRole": "You will be provided with a piece of code, and your task is to translate it into a given programming language so that it is compilable.",
    "reTranslateTestFailed" : """
You were asked to translate the following {SOURCE_LANG} code to {TARGET_LANG}:
{SOURCE_CODE}

Your response was the following {TARGET_LANG} code:
{TRANSLATED_CODE}

Executing your generated code gives the following output:
{GENERATED_OUTPUT}

instead of the following expected output:
{EXPECTED_OUTPUT}

Can you re-generate your response and translate the above {SOURCE_LANG} code to {TARGET_LANG}. Print only the {TARGET_LANG} code and do not add any other natural language description in your output. Make sure your generated code is syntactically correct. Your generated {TARGET_LANG} code should take the following input and generate the expected output:

Input:
{TEST_INPUT}

Expected Output:
{EXPECTED_OUTPUT} 
""",
    "reTranslateError" :"""
You were asked to translate the following {SOURCE_LANG} code to {TARGET_LANG}:
{SOURCE_CODE}

Your response was the following {TARGET_LANG} code:
{TRANSLATED_CODE}

Executing your generated code gives the following error because it is syntactically incorrect:
{STDERR}

Can you re-generate your response and translate the above {SOURCE_LANG} code to {TARGET_LANG}. Print only the {TARGET_LANG} code and do not add any other natural language description in your output, and do not change the method signature from incorrect translation. Make sure your generated code is syntactically correct.
"""
    }
    
    
    # Write the dictionary to a JSON file
    with open(experimentDataJsonFile, 'w') as json_file:
        json.dump(jsonData, json_file, indent=4)  

def count_generated_files(flag_object, experiment, run):
    total_files = 0

    projects = os.listdir(flag_object.currentProjectDir)

    for entry in projects:
        projectDir = os.path.join(flag_object.currentProjectDir, entry)
        dirname = os.path.dirname(__file__)
        fullProjectDir = os.path.join(dirname, projectDir)

        executionDir = os.path.join(
            fullProjectDir,
            f'ExecutionsExp{experiment}Run{run}'
        )

        if not os.path.exists(executionDir):
            continue

        # count files across all timestamps
        for timestamp_dir in os.listdir(executionDir):
            full_timestamp_dir = os.path.join(executionDir, timestamp_dir)

            if not os.path.isdir(full_timestamp_dir):
                continue

            for f in os.listdir(full_timestamp_dir):
                full_file = os.path.join(full_timestamp_dir, f)
                if os.path.isfile(full_file):
                    total_files += 1

    return total_files
class FlagObject:
    def __init__(self, data):
        self.currentProjectDir = data.get("currentProjectDir")
        self.WithTestsFlag = data.get("WithTestsFlag")
        self.numberOfRuns = data.get("numberOfRuns")
        self.HaskellAddImportsFlag = data.get("HaskellAddImportsFlag")
        self.PascallAddCompileOptionFlag = data.get("PascallAddCompileOptionFlag")
        self.JavascriptNodeJS = data.get("JavascriptNodeJS")
        self.removeAfterBackTicks = data.get("removeAfterBackTicks")
        self.Message = data.get("Message")
        self.SystemRole = data.get("SystemRole")
        self.reTranslateTestFailed = data.get("reTranslateTestFailed")
        self.reTranslateError = data.get("reTranslateError")
        self.SystemRoleExplanation = data.get("SystemRoleExplanation")
        self.MessageExplanation = data.get("MessageExplanation")
        self.WithExplanation = data.get("WithExplanation")
        self.MessageFunctionTranslate = data.get("MessageFunctionTranslate")
        self.SystemRoleFunctionTranslate = data.get("SystemRoleFunctionTranslate")
        self.addLibarys = data.get("addLibarys")
        self.reTranslateFunctionWithSourceCode = data.get("reTranslateFunctionWithSourceCode")
        self.MessageFunctionAgain = data.get("MessageFunctionAgain")
        self.SystemRoleFunctionTranslateAgain = data.get("SystemRoleFunctionTranslateAgain")
        self.buildProgramManuly = data.get("buildProgramManuly")
        self.WithExplanationFunctions = data.get("WithExplanationFunctions")
        self.SystemRoleFunctionExplanation = data.get("SystemRoleFunctionExplanation")
        self.MessageFunctionExplanation = data.get("MessageFunctionExplanation")
        self.reTranslateFrom = data.get("reTranslateFrom")
        self.notJavaClassNameChange = data.get("notJavaClassNameChange")
        self.notRemoveBackTicks = data.get("notRemoveBackTicks")
        self.NotCScharfAenderung = data.get("NotCScharfAenderung")
        self.notRmeoveCRTlib = data.get("notRmeoveCRTlib")
        self.modelName = data.get("modelName")
        self.reTranslate = data.get("reTranslate")
        

        
if __name__ == "__main__":  
    experiment = 23
    run = 1
    experimentDataJsonFile = f"./RunsJsonData/Experiment{experiment}Run{run}.json"

    with open(experimentDataJsonFile, 'r') as file:
        jsonData = json.load(file)
        
    flag_object = FlagObject(jsonData)
    
    
    # file_count = count_generated_files(flag_object, experiment, run)

    # while file_count < 3500:        
    #     file_count = count_generated_files(flag_object, experiment, run)
    #     translateInititialyQuant(flag_object, experiment=experiment, run=run)
    #     print(f"Current generated files: {file_count}")

    # compile_all_Quant(flag_object, True, experiment,run, f'ExecutionsExp{experiment}Run{run}', f'../../logsHumanEvalXExp{experiment}Run{run}')
       
   
    # translateInititialy(flag_object)
    # compile_all_Quant(flag_object)
    # compile_all(flag_object)

    # if flag_object.reTranslate: 
    #     reTranslate()
    #     compile_all(flag_object)


    # reTranslateRun(flag_object, experiment, run)
    reTranslateRunQuant(flag_object, experiment, run)

    # compile_all(flag_object, True)

    # compile_all_Quant(flag_object, True, 9,14, "ExecutionsExp9Run14", "../../logsHumanEvalXExp9Run14")

