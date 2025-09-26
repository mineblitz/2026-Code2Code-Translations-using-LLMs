import pandas as pd
import numpy as np
import os

COST_OF_GPT_IN = 0.15
COST_OF_GPT_OUT = 0.6
COST_OF_CLAUDE_IN = 3
COST_OF_CLAUDE_OUT = 15
NUMBER_OF_PROBLEMS = 125
NUMBER_OF_GPT_ITERATIONS = 44
NUMBER_OF_TOTAL_TRANSLATION = 3500
PATH_TO_GPT_RETRANS = "./data/RetranslateGPT/logsHumanEvalXExp6Run2_"


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


# Ziel: Tupel: cost, qualität
# cost: counter der mitzählt wie oft man von claude oder gpt nimmt 
# (counter muss für jeden aufruf jedes programms hochgezählt werden)
# qualität: zählen wie viele erfolgreich übersetzt wurden


def getCostAndQuality(breakPercentage):

    remaingProblems = list(range(NUMBER_OF_PROBLEMS))

    gptQuality, gptCostCounter, remaingProblems = getGPTQuality(remaingProblems, breakPercentage)
    claudeQuality, claudeCostCunter = getClaudeQuality(remaingProblems)
    totalQuality = gptQuality + claudeQuality

    gptCost = gptCostCounter * (COST_OF_GPT_IN + COST_OF_GPT_OUT)
    claudeCost = claudeCostCunter * (COST_OF_CLAUDE_IN + COST_OF_CLAUDE_OUT)
    totalCost = gptCost + claudeCost

    return totalCost, totalQuality


# geht durch alles verbliebenen Probleme durch 
def getGPTQuality(remaingProblems, breakPercentage):
    gptCostCounter = 0
    previousQuality = 0

    iterations = list(range(NUMBER_OF_GPT_ITERATIONS))


    for iteration in iterations: # Scheife für Iterationen

        # Brauche:
        # wie viel prozent sind bisher richtig?
        # Wie viel mussten in der Iteration übersetzt werden
        # Welche Probleme bestehen noch?
        # Für:
        # Iteration
        currentQuality, currentGPTCostCounter, remaingProblems = getQualityGPT(iteration, remaingProblems)
        gptCostCounter += currentGPTCostCounter

        



        if (currentQuality - previousQuality) <= breakPercentage:
            gptQuality = currentQuality
            break
        else:
            previousQuality = currentQuality
            gptQuality = currentQuality

        if len(remaingProblems) == 0:
            gptQuality = currentQuality
            break
        

    return gptQuality, gptCostCounter, remaingProblems


# qulity = summe über alle ergebnisse
# costCounter = jetzt gelöste Probleme - vorherige Iteration gelöste Probleme 
# remaingproblems
# def getQualityGPT(iteration, remaingProblems):
#     currentQuality = sum_all_csvs(PATH_TO_GPT_RETRANS + str(iteration)) / NUMBER_OF_TOTAL_TRANSLATION
    
#     currentGPTCostCounter = 0
#     if(iteration == 0):
#         currentGPTCostCounter = NUMBER_OF_TOTAL_TRANSLATION
#     else:
#         currentGPTCostCounter = NUMBER_OF_TOTAL_TRANSLATION - sum_all_csvs(PATH_TO_GPT_RETRANS + str(iteration-1))

#     return currentQuality, currentGPTCostCounter, remaingProblems


def getClaudeQuality(remaingProblems):
    claudeCostCunter = 0
    iteration = 0

    for problem in remaingProblems[:]:  # iterate over a shallow copy so we can remove items
        # load dataframe for this problem (keep call as given)
        problemDataframe = loadDataframe(os.path.join(PATH_TO_GPT_RETRANS, str(iteration), f"compilation_matrix{1}"))

        # iterate over copies of keys/values so we can mutate the structure safely
        for languageFrom in list(problem):
            for languageTO in list(problem[languageFrom]):
                claudeCostCunter += 1

                # attempt safe access to the dataframe cell
                try:
                    cell = problemDataframe.loc[languageFrom, languageTO]
                except Exception:
                    try:
                        cell = problemDataframe[languageFrom][languageTO]
                    except Exception:
                        # if cell cannot be accessed treat as not successful
                        cell = None

                if cell == 1:
                    # remove languageTO from this languageFrom (support list or set)
                    val = problem[languageFrom]
                    if isinstance(val, set):
                        val.discard(languageTO)
                    else:
                        try:
                            val.remove(languageTO)
                        except Exception:
                            # fallback: if mapping-like, attempt pop
                            if isinstance(val, dict):
                                val.pop(languageTO, None)

                    # if that languageFrom has no targets left remove the key
                    if not problem[languageFrom]:
                        problem.pop(languageFrom, None)

        # if problem now empty remove it from remainingProblems
        if not problem:
            remaingProblems.remove(problem)

    # count remaining translation targets
    sumOfElementsRemainingInRemaingProblems = sum(
        len(targets) for prob in remaingProblems for targets in prob.values()
    )

    # proportion of solved translations
    claudeQuality = (NUMBER_OF_TOTAL_TRANSLATION - sumOfElementsRemainingInRemaingProblems) / NUMBER_OF_TOTAL_TRANSLATION

    return claudeQuality, claudeCostCunter



def getClaudeQuality(remaingProblems):

    iteration = 0 #TODO iteraation schleife einfügen
    claudeCostCunter = 0

    for problem in remaingProblems:
        problemDataframe = loadDataframe(PATH_TO_GPT_RETRANS + str(iteration) + f"compilation_matrix{IndexOfProblemInRemaingProblems}")
        for languageFrom in problem:
            for languageTO in languageFrom:
                claudeCostCunter += 1
                if problemDataframe[languageFrom][languageTO] == 1:
                    #TODO remove LanguageTO from this LanguageFrom if LanguageFrom after that is empty remove it aswell



    claudeQuality = NUMBER_OF_TOTAL_TRANSLATION - sumOfElementsRemainingInRemaingProblems / NUMBER_OF_TOTAL_TRANSLATION
    
    return claudeQuality, claudeCostCunter



print(getCostAndQuality(0))
print(getCostAndQuality(0.001))
print(getCostAndQuality(0.1))
print(getCostAndQuality(1))





# print(sum_all_csvs("..\data\RetranslateGPT\logsHumanEvalXExp6Run2_15"))
# print(sum_all_csvs("..\data\RetranslateGPT\logsHumanEvalXExp6Run2_16"))

# OneTurnGPT = load_and_get_mean("1TurnGPT/logsHumanEvalXQuant1")
# OneTurnClaude = load_and_get_mean("1TurnClaude/logsHumanEvalXExp13Run1")
# ExplanationGPT = load_and_get_mean("ExplanationGPT/logsHumanEvalXExp7Run4")
# ExplanationClaude = load_and_get_mean("ExplanationClaude/logsHumanEvalXExp15Run1")
# RetranslationGPT = load_and_get_mean("1TurnGPT/logsHumanEvalXQuant1")
# RetranslationClaude = load_and_get_mean("1TurnGPT/logsHumanEvalXQuant1")

# print(OneTurnGPT)
# print(OneTurnClaude)
# print(ExplanationGPT)
# print(ExplanationClaude)
# print(RetranslationGPT)
# print(RetranslationClaude)