import pandas as pd
import numpy as np
import os

COST_OF_GPT_IN = 0.15 / 1000000
COST_OF_GPT_OUT = 0.6 / 1000000
COST_OF_CLAUDE_IN = 3 / 1000000
COST_OF_CLAUDE_OUT = 15 / 1000000
TOKEN_GPT_IN = 694.763524
TOKEN_GPT_OUT = 311.4600721
TOKEN_CLAUDE_IN = 859.0216383
TOKEN_CLAUDE_OUT = 394.6321484

NUMBER_OF_PROBLEMS = 125
NUMBER_OF_GPT_ITERATIONS = 44
NUMBER_OF_CLAUDE_ITERATIONS = 18
NUMBER_OF_TOTAL_TRANSLATION = 3500

PATH_TO_CLAUDE_RETRANS = "./data/RetranslateClaude/logsHumanEvalXExp14Run1_"
PATH_TO_GPT_RETRANS = "./data/RetranslateGPT/logsHumanEvalXExp6Run2_"
FROM_LANGUAGES = ["C++", "Java", "Javascript", "Python"]
TO_LANGUAGES = ["C", "C++", "C#", "Java", "Javascript", "Pascal", "Python", "Haskell"]


def load_and_get_mean(folder_name: str):
    path = f"../data/{folder_name}/compilation_matrix_avg"
    df = pd.read_csv(path, index_col=0)
    values = df.to_numpy().flatten()
    non_nan = values[~np.isnan(values)]
    return non_nan.sum() / len(non_nan)


def sum_all_csvs(folder_path: str):
    total_sum = 0.0
    for i in range(125):  # 0 to 124
        file_path = os.path.join(folder_path, f"compilation_matrix{i}")
        df = pd.read_csv(file_path, index_col=0)
        values = df.to_numpy().flatten()
        non_nan = values[~np.isnan(values)]
        total_sum += non_nan.sum()
    return total_sum

def loadDataframe(folder_path: str):    
    df = pd.read_csv(folder_path, index_col=0)    
    return df



def getCostAndQuality(breakPercentage):

    remaingProblems = list(range(NUMBER_OF_PROBLEMS))

    if(breakPercentage == 1):
        gptCostCounter = 0
        remaingProblems = initialiseRemaingProblems(0) 
        for key, df in remaingProblems.items():
            for languageFrom in FROM_LANGUAGES:
                for languageTO in TO_LANGUAGES:
                    if(df.loc[languageFrom, languageTO] == 1):
                        df.loc[languageFrom, languageTO] = 0    

    elif(breakPercentage == -1):
        gptQuality, gptCostCounter, remaingProblems = getGPTQuality(remaingProblems, 0)
    else:
        gptQuality, gptCostCounter, remaingProblems = getGPTQuality(remaingProblems, breakPercentage)

    
    totalQuality, claudeCostCunter = getClaudeQuality(remaingProblems)

    gptCost = gptCostCounter * (COST_OF_GPT_IN * TOKEN_GPT_IN + COST_OF_GPT_OUT * TOKEN_GPT_OUT)
    claudeCost = claudeCostCunter * (COST_OF_CLAUDE_IN * TOKEN_CLAUDE_IN + COST_OF_CLAUDE_OUT * TOKEN_CLAUDE_OUT)
    totalCost = gptCost + claudeCost

    if (breakPercentage == -1):
        return gptCost, gptQuality
    
    return totalCost, totalQuality



def getGPTQuality(remaingProblems, breakPercentage):
    gptCostCounter = 0
    previousQuality = 0

    iterations = list(range(NUMBER_OF_GPT_ITERATIONS))
    lastIteration = 0


    for iteration in iterations:


        currentQuality, currentGPTCostCounter = getQualityGPTPerIteration(iteration)
        gptCostCounter += currentGPTCostCounter


        if (currentQuality - previousQuality) <= breakPercentage:
            gptQuality = currentQuality
            lastIteration = iteration
            break
        else:
            previousQuality = currentQuality
            gptQuality = currentQuality
            lastIteration = iteration

    remaingProblems = initialiseRemaingProblems(lastIteration)

    return gptQuality, gptCostCounter, remaingProblems



def getQualityGPTPerIteration(iteration):
    currentQuality = sum_all_csvs(PATH_TO_GPT_RETRANS + str(iteration)) / NUMBER_OF_TOTAL_TRANSLATION
    
    currentGPTCostCounter = 0
    if(iteration == 0):
        currentGPTCostCounter = NUMBER_OF_TOTAL_TRANSLATION
    else:
        currentGPTCostCounter = NUMBER_OF_TOTAL_TRANSLATION - sum_all_csvs(PATH_TO_GPT_RETRANS + str(iteration-1))

    return currentQuality, currentGPTCostCounter


def getClaudeQuality(remaingProblems):
    claudeCostCunter = 0
    iteration = 0

    for iteration in list(range(NUMBER_OF_CLAUDE_ITERATIONS)):
        sumOverAllProblems = 0
        for problemNumber, RemaingProblemsDF in remaingProblems.items():
            SolvedInIterationDataframe = loadDataframe(os.path.join(PATH_TO_CLAUDE_RETRANS + str(iteration), f"compilation_matrix{problemNumber}"))

            for languageFrom in FROM_LANGUAGES:
                for languageTO in TO_LANGUAGES:
                    if (RemaingProblemsDF.loc[languageFrom, languageTO] == 1):
                        continue 
                    if (np.isnan(RemaingProblemsDF.loc[languageFrom, languageTO]) ):
                        continue 
                    if (languageFrom == languageTO):
                        continue
                    
                    claudeCostCunter += 1

                    if(not SolvedInIterationDataframe.loc[languageFrom, languageTO] == 1):
                        continue
                    else:
                        RemaingProblemsDF.loc[languageFrom, languageTO] = 1

            if(SolvedInIterationDataframe.sum().sum() > RemaingProblemsDF.sum().sum()):
                print("test")
            sumOverAllProblems += RemaingProblemsDF.sum().sum()
                    
   
    claudeQuality = sumOverAllProblems / NUMBER_OF_TOTAL_TRANSLATION

    return claudeQuality, claudeCostCunter

def initialiseRemaingProblems(lastIteration):
    remaingProblems = {}
    for problemNumber in list(range(NUMBER_OF_PROBLEMS)):
        df = loadDataframe(os.path.join(PATH_TO_GPT_RETRANS + str(lastIteration), f"compilation_matrix{problemNumber}"))
        remaingProblems.update({problemNumber: df})

    return remaingProblems


def save_results(df: pd.DataFrame, filename: str):
    df.to_csv(filename, index=False)

def load_results(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def run_experiments():
    break_percentages = [0, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 0.75, 1]
    results = []

    for bp in break_percentages:
        cost, quality = getCostAndQuality(bp)
        results.append((bp, cost, quality))
        

    cost, quality = getCostAndQuality(-1)
    results.append(("GPTOnly", cost, quality))

    df = pd.DataFrame(results, columns=["breakPercentage", "cost", "quality"])
    return df

df = run_experiments()
save_results(df, "results.csv")
loaded = load_results("results.csv")
print(loaded)
