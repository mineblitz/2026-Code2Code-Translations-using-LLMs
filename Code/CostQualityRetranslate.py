import os
import json
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Tuple, List
import tiktoken

from SourceCodeTranslatorParallel import FlagObject
from SourceCodeTranslatorParallel import evaluate_string

languageDict = {}
languageDict['c'] = 'C'
languageDict['c++'] = 'C++'
languageDict['cs'] = 'C#'
languageDict['java'] = 'Java'
languageDict['js'] = 'Javascript'
languageDict['pas'] = 'Pascal'
languageDict['py'] = 'Python'
languageDict['hs'] = 'Haskell'

languages = ['C', 'C++', 'C#', 'Java', 'Javascript', 'Pascal', 'Python', 'Haskell']

folder = "./Projects"
logBaseName = "logsHumanEvalXExp{EXPERIMENT}Run{RUN}_{ITERATION}"


def get_token_count(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    Calculate token count for a given text using tiktoken.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    
    tokens = encoding.encode(text)
    return len(tokens)


def extract_lang_from_filename(filename: str) -> Tuple[str, str]:
    """
    Extract source and target language from filename format: FromToInto.ext
    Returns (SOURCE_LANG, TARGET_LANG)
    """
    base_name = os.path.splitext(filename)[0]
    parts = base_name.split("To")
    
    if len(parts) >= 2:
        source_lang = parts[0]
        target_lang = parts[1]
        return source_lang, target_lang
    return None, None


def get_retranslate_files(experiment: int) -> List[str]:
    """
    Get all retranslate CSV files for a given experiment.
    """
    retranslate_dir = f"./RetranslateCSVExp{experiment}"
    
    if not os.path.exists(retranslate_dir):
        return []
    
    files = []
    for file in os.listdir(retranslate_dir):
        if file.startswith("reTranslate.csv"):
            files.append(os.path.join(retranslate_dir, file))
    
    return sorted(files)


def load_flag_object(experiment: int, run: int = 1) -> Dict:
    """
    Load FlagObject from JSON file to get prompt templates.
    """
    experiment_json_file = f"./RunsJsonData/Experiment{experiment}Run{run}.json"
    
    with open(experiment_json_file, 'r') as file:
        jsonData = json.load(file)
        
    flag_object = FlagObject(jsonData)
    return flag_object


def get_source_code(file_path: str, source_lang: str) -> str:
    """
    Get source code from Code_Input directory.
    """
    extension = next((k for k, v in languageDict.items() if v == source_lang), None)
    
    source_code_dir = os.path.join(os.path.dirname(file_path), "..", "..", "Code_Input")
    
    if not os.path.exists(source_code_dir):
        return ""
    
    for file in os.listdir(source_code_dir):
        if file.endswith(f".{extension}"):
            with open(os.path.join(source_code_dir, file), 'r', encoding='utf-8') as f:
                return f.read()
    
    return ""


def generate_prompt_for_retranslate(flag_object: Dict, row: dict, source_lang: str, target_lang: str, 
                                    source_code: str, translated_code: str) -> str:
    """
    Generate the same prompt as in SourceCodeTranslatorParallel.py
    """
    error_type = str(row.get("ErrorType", "")).strip()
    
    if error_type == "TestFailed":
        user_message = flag_object.reTranslateTestFailed.format(
            SOURCE_LANG=source_lang,
            TARGET_LANG=target_lang,
            SOURCE_CODE=source_code,
            TRANSLATED_CODE=translated_code,
            TEST_INPUT=row.get("TestInput", ""),
            EXPECTED_OUTPUT=row.get("TestOutput", ""),
            GENERATED_OUTPUT=row.get("GeneratedOutput", "")
        )
    else:
        # CompilationFailed, RuntimeFailed, or InfiniteLoop
        if error_type == "CompilationFailed":
            stderr = row.get("stdErr", "")
            if stderr in ["", "b''"]:
                stderr = row.get("Output", "")
        elif error_type == "RuntimeFailed":
            stderr = row.get("StackTrace", "")
        elif error_type == "InfiniteLoop":
            stderr = "the program enters infinite loop"
        else:
            stderr = ""
        
        user_message = flag_object.reTranslateError.format(
            SOURCE_LANG=source_lang,
            TARGET_LANG=target_lang,
            SOURCE_CODE=source_code,
            TRANSLATED_CODE=translated_code,
            STDERR=stderr
        )
    
    return user_message


def calculate_input_output_tokens(experiment: int, run: int = 1, model: str = "gpt-3.5-turbo") -> Dict:
    """
    Calculate input and output tokens for all retranslated programs in an experiment.
    Returns dictionary with detailed translation data and summary for each iteration.
    """
    # Load flag object for prompt templates
    flag_object = load_flag_object(experiment, run)
    
    # Get system role
    system_role = flag_object.SystemRole
    
    # Get all retranslate CSV files
    retranslate_files = get_retranslate_files(experiment)
    
    if not retranslate_files:
        print(f"No retranslate files found for experiment {experiment}")
        return {}
    
    results = {}
    summary_data = []
    
    for csv_file in retranslate_files:
        print(f"Processing: {csv_file}")
        
        # Extract iteration number from CSV filename (e.g., "reTranslate.csv0" -> "0")
        base_name = os.path.basename(csv_file)
        iteration_number = base_name.replace("reTranslate.csv", "")
        
        try:
            df = pd.read_csv(csv_file)
        except Exception as e:
            print(f"Error reading CSV file {csv_file}: {e}")
            continue
        
        # Store detailed data for each translation
        detailed_data = []
        total_input_iteration = 0
        total_output_iteration = 0
        translation_count = 0
        
        for index, row in df.iterrows():
            try:
                file_path = row.get('dirPath', '')
                
                # Insert _IterationNumber after ExecutionsExp{exp}Run{run}
                if file_path and iteration_number:
                    file_path = file_path.replace(
                        f"ExecutionsExp{experiment}Run{run}",
                        f"ExecutionsExp{experiment}Run{run}_{iteration_number}"
                    )

                if not file_path or not os.path.exists(file_path):
                    continue
                
                # Extract languages from filename
                file_name = os.path.basename(file_path)
                source_lang, target_lang = extract_lang_from_filename(file_name)
                
                if source_lang is None or target_lang is None:
                    continue
                
                # Map to full language names
                source_lang_full = languageDict.get(source_lang, source_lang)
                target_lang_full = languageDict.get(target_lang, target_lang)
                
                # Read translated code
                with open(file_path, 'r', encoding='utf-8') as f:
                    translated_code = f.read()
                
                # Get source code
                source_code = get_source_code(file_path, source_lang_full)
                
                # Generate the prompt
                user_message = generate_prompt_for_retranslate(
                    flag_object, row, source_lang_full, target_lang_full, 
                    source_code, translated_code
                )
                
                # Calculate tokens
                system_tokens = get_token_count(system_role, model)
                user_tokens = get_token_count(user_message, model)
                total_input_tokens = system_tokens + user_tokens
                
                # For output tokens, we estimate based on the translated code
                output_tokens = get_token_count(translated_code, model)
                
                # Accumulate totals for this iteration
                total_input_iteration += total_input_tokens
                total_output_iteration += output_tokens
                translation_count += 1
                
                # Add to detailed data
                detailed_data.append({
                    'Source_Language': source_lang_full,
                    'Target_Language': target_lang_full,
                    'Input_Tokens': total_input_tokens,
                    'Output_Tokens': output_tokens,
                    'Total_Tokens': total_input_tokens + output_tokens
                })
                
            except Exception as e:
                print(f"Error processing row {index}: {e}")
                continue
        
        results[csv_file] = {
            'detailed_data': pd.DataFrame(detailed_data)
        }
        
        # Add summary for this iteration
        summary_data.append({
            'Iteration': str(int(iteration_number) + 1),
            'Input_Tokens': total_input_iteration,
            'Output_Tokens': total_output_iteration,
            'Total_Tokens': total_input_iteration + total_output_iteration,
            'Translation_Count': translation_count
        })

    init_program_tokens_input, init_program_tokens_output = get_tokens_inital_trans(flag_object, experiment, run, model)

    summary_data.append({
            'Iteration': 0,
            'Input_Tokens': init_program_tokens_input,
            'Output_Tokens': init_program_tokens_output,
            'Total_Tokens': init_program_tokens_input + init_program_tokens_output,
            'Translation_Count': 3500
                })

    results['summary'] = pd.DataFrame(summary_data)
    return results


def save_token_matrices(experiment: int, run: int = 1, model: str = "gpt-3.5-turbo"):
    """
    Calculate and save detailed token lists for each iteration.
    """
    results = calculate_input_output_tokens(experiment, run, model)

    if not results:
        print("No results to save")
        return
    
    # Create output directory
    output_dir = f"./TokenAnalysis/Exp{experiment}Run{run}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract and save summary
    summary_df = results.pop('summary', None)
    if summary_df is not None:
        summary_file = os.path.join(output_dir, "token_summary.csv")
        summary_df.to_csv(summary_file, index=False)
        print(f"\nSummary saved to: {summary_file}")
        print("\nToken Summary per Iteration:")
        print(summary_df.to_string(index=False))
    
    # Save detailed data for each iteration
    for csv_file, data in results.items():
        # Extract iteration number from csv file name
        base_name = os.path.basename(csv_file)
        iteration = base_name.replace("reTranslate.csv", "")
        
        # Save detailed data
        detailed_file = os.path.join(output_dir, f"iteration_{iteration}_tokens.csv")
        data['detailed_data'].to_csv(detailed_file, index=False)
        print(f"Saved: {detailed_file}")


def calculate_cost_and_quality(experiment: int, run: int = 1):
    """
    Calculate cost (tokens) and quality metrics by comparing with compilation matrix.
    """
    # Load token matrices
    results = calculate_input_output_tokens(experiment, run)
    
    # Load compilation matrices
    logs_dir = f"./Projects/HumanEvalX/0/logsHumanEvalXExp{experiment}Run{run}_0"
    
    if not os.path.exists(logs_dir):
        print(f"Logs directory not found: {logs_dir}")
        return
    
    # Read compilation matrix
    compilation_matrix_file = os.path.join(logs_dir, "compilation_matrix0")
    if not os.path.exists(compilation_matrix_file):
        print(f"Compilation matrix not found: {compilation_matrix_file}")
        return
    
    try:
        compilation_matrix = pd.read_csv(compilation_matrix_file, index_col=0)
    except Exception as e:
        print(f"Error reading compilation matrix: {e}")
        return
    
    print(f"\nCost-Quality Analysis for Experiment {experiment} Run {run}:")
    print(f"Compilation Success Rate:\n{compilation_matrix}\n")
    
    for csv_file, matrices in results.items():
        input_tokens = matrices['input_tokens']
        output_tokens = matrices['output_tokens']
        
        total_input = input_tokens.sum().sum()
        total_output = output_tokens.sum().sum()
        total_tokens = total_input + total_output
        
        print(f"File: {csv_file}")
        print(f"  Total Input Tokens: {total_input}")
        print(f"  Total Output Tokens: {total_output}")
        print(f"  Total Tokens: {total_tokens}")
        print()



def get_tokens_inital_trans(flag_object, experiment, run, model: str = "gpt-3.5-turbo"):
    all_program_tokens_input = 0
    all_program_tokens_output = 0

    Projects = os.listdir(flag_object.currentProjectDir)
    for entry in Projects:

        projectDir = os.path.join(flag_object.currentProjectDir, entry)
        dirname = os.path.dirname(__file__)
        fullProjectDir = os.path.join(dirname, projectDir)
        codesnipetDir = os.path.join(fullProjectDir,'Code_Input')
        executionDir = os.path.join(fullProjectDir, f'ExecutionsExp{experiment}Run{run}_0')

        existing_runs = [
            d for d in os.listdir(executionDir)
            if os.path.isdir(os.path.join(executionDir, d))
        ]
        if existing_runs:
            latest_timestamp = sorted(existing_runs)[-1]
            currentExecutionDir = os.path.join(executionDir, latest_timestamp)


        filenames = os.listdir(codesnipetDir)

        for languageFile in filenames:
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
                    
                userContentMessage = flag_object.Message.format(
                    SOURCE_CODE=SOURCE_CODE,
                    TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                    TEXT_TARGET_LANG=TEXT_TARGET_LANG,
                    test_cases_string=test_cases_string
                        )  
                SystemRole = flag_object.SystemRole.format(
                    TEXT_SOURCE_LANG=TEXT_SOURCE_LANG,
                    TEXT_TARGET_LANG=TEXT_TARGET_LANG)
                
                system_role_tokens = get_token_count(SystemRole, model)
                user_message_tokens = get_token_count(userContentMessage, model)
                all_program_tokens_input = all_program_tokens_input +system_role_tokens + user_message_tokens                
            
                try:  
                    with open(newSaveFile, "r") as lang_file:
                        translated_code = lang_file.read()
                        output_tokens = get_token_count(translated_code, model)
                        all_program_tokens_output = all_program_tokens_output + output_tokens

                except UnicodeEncodeError as e:
                    print(f"Unicode encoding error: {e}")
    return (all_program_tokens_input, all_program_tokens_output)



if __name__ == "__main__":
    # Example usage
    experiment = 23
    run = 1
    
    # Save token matrices to files
    save_token_matrices(experiment, run, model="gpt-3.5-turbo")
    
    # Analyze cost and quality
    # calculate_cost_and_quality(experiment, run)
