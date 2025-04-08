import ast
import json
import math
import os
import re
from datasets import load_dataset

languageDict = {}
languageDict['CPP'] = 'c++'
languageDict['Java'] = 'java'
languageDict['JavaScript'] = 'js'
languageDict['Python'] = 'py'

def processDataset(datasets):
    counter = 0
    sumJava = []
    sumCPP = []
    sumJavascript = []
    sumPython = []
    for i in range(len(datasets[0])):
        # if counter > 4: break:
        # problems to skip   
        if i in {12, 22, 32, 33, 37,38, 44, 50,51, 52, 53, 61, 72, 77,78,90, 92, 95, 97, 103, 107,112, 114, 117, 125, 128, 136, 137, 144, 148, 151, 154, 155, 160, 162, 115, 111, 87, 129}: continue    
        # to fix 115, 111, 87, 129 for java there needs to be the input and oupt of array of arrays allowed and implemented
        # 12 OPtional needs to be supported
        # 22 co complex parameter, 33 test is with touple not parseable 37, same; 38 uses random, 50 uses random
        # 51 because it uses \n that are not printed by some languages
        # 77 wrong parsed tests 78 same 95 same 97 same 90 uses java optinal 92 wierd mix of in and float
        # 103 java would need special parsing 107 javascript would need to be adjusted to print tupel
        # 114 muss in c++ bei return umgestellt werden auf vector, und andere fehler noch
        # 112 list object in java 117 not parseable 
        # 125 java object 128 java optional 136 optional java 137 optional java
        # 144 because of 1/5 as input value 155 javascript tupel problem
        # 160 different test values for different languages
        # 162 different hash values for each language
         
        for dataset in datasets:                    
            id = dataset[i]['task_id']
            problemNumber = id.split('/')[-1]
            language = id.split('/')[0]

            functionName = get_function_name(dataset[i]['declaration'], language, problemNumber)  
            if id == "Java/10" or id == "JavaScript/10": functionName = "makePalindrome"
            if id == "CPP/10" or id == "Python/10": functionName = "make_palindrome"
            
            sampleProgramm = dataset[i]['canonical_solution']
            test = dataset[i]['test']
            declaration = dataset[i]['declaration']
            
            path = createDir(id)
            createTestData(test, id, path)

    

            with open(os.path.join(path, "TestData.json"), 'r') as file:
                testData = json.load(file)
            # print(testData)
            codelength = createSampleProgramm(path,id, sampleProgramm, declaration, functionName, testData[0]['input'], testData)


            if  language == "Java":
                sumJava.append(codelength)
            elif language == "CPP":
                sumCPP.append(codelength)
            elif language == "JavaScript":
                sumJavascript.append(codelength)
            elif language == "Python":
                sumPython.append(codelength)            
            
        counter = counter + 1

    mean_lengthJava = sum(sumJava) / len(sumJava)
    varianceJava = sum((length - mean_lengthJava) ** 2 for length in sumJava) / len(sumJava)
    std_deviationJava = math.sqrt(varianceJava)
    print(f"Java Mean: {mean_lengthJava:.6f} Standard deviation: {std_deviationJava:.6f}")

    mean_lengthCPP = sum(sumCPP) / len(sumCPP)
    varianceCPP = sum((length - mean_lengthCPP) ** 2 for length in sumCPP) / len(sumCPP)
    std_deviationCPP = math.sqrt(varianceCPP)
    print(f"CPP Mean: {mean_lengthCPP:.6f} Standard deviation: {std_deviationCPP:.6f}")

    mean_lengthPython = sum(sumPython) / len(sumPython)
    variancePython = sum((length - mean_lengthPython) ** 2 for length in sumPython) / len(sumPython)
    std_deviationPython = math.sqrt(variancePython)
    print(f"Python Mean: {mean_lengthPython:.6f} Standard deviation: {std_deviationPython:.6f}")

    mean_lengthJavaScript = sum(sumJavascript) / len(sumJavascript)
    varianceJavaScript = sum((length - mean_lengthJavaScript) ** 2 for length in sumJavascript) / len(sumJavascript)
    std_deviationJavaScript = math.sqrt(varianceJavaScript)
    print(f"Javascript Mean: {mean_lengthJavaScript:.6f} Standard deviation: {std_deviationJavaScript:.6f}")



    




def createDir(id):
    problemNumber = id.split('/')[-1]
    basePath = './Projects/HumanEvalX'
    newPath = os.path.join(basePath , problemNumber)
    if(not os.path.exists(newPath)):
        os.makedirs(newPath)
    return newPath

def get_function_name(s, language, problemNumber):
    patternJavascript = r'const\s+(\w+)\s*=\s*\([^)]*\)\s*=>\s*\{'
    patternJava = r'\bpublic\s+\w+(\s*<[^>]*>)?\s+(\w+)\s*\([^)]*\)\s*(throws\s+\w+(\s+\w+)*)?\s*\{'
    patternPython = r'\bdef\s+(\w+)\s*\(.*?\)\s*(?:->\s*.*)?\s*:'
    patternCPP = r'\b[\w<>]+\s+(\w+)\s*\([^)]*\)\s*(?=\{|\s*$)'

    if language == "JavaScript":
        pattern = patternJavascript
    elif language == "Python":
        pattern = patternPython
    elif language == "Java":
        pattern = patternJava
    elif language == "CPP":
        pattern = patternCPP
    else:
        return None
    
    match = re.search(pattern, s)
    if match:
        if language == "Java":
            return match.group(2)
        else:
            return match.group(1)
    
    # Only execute the following if no match is found
    if problemNumber == "136" and language == "Java":
        return "largestSmallestIntegers"
    
    return None


def createSampleProgramm(dirPath, id,  sampleProgramm, declaration, functionName, exampleInput, testData):
    if sampleProgramm is None: return None


    firstPart = id.split('/')[0]
    language = languageDict[firstPart]
    id_clean = id.replace("/", "")
    if not os.path.exists(os.path.join(dirPath, 'Code_Input')):
        os.mkdir(os.path.join(dirPath, 'Code_Input'))

    if not os.path.exists(os.path.join(dirPath, 'Code_InputFunctions')):
        os.mkdir(os.path.join(dirPath, 'Code_InputFunctions'))    
    pathFunctions1 = os.path.join(dirPath, 'Code_InputFunctions',firstPart+"1" )
    pathFunctions2 = os.path.join(dirPath, 'Code_InputFunctions',firstPart+"2" )

    path = os.path.join(dirPath, 'Code_Input',id_clean + "." + language )

    if id == "Python/142":
        declaration = declaration.replace("\"", "")
    code = declaration + sampleProgramm

    if id == "CPP/30": code = code.replace("float", "int")

    if firstPart == "JavaScript" or firstPart == "Python":
        with open(pathFunctions1, 'w') as file:
            file.write(code)

    if firstPart == "JavaScript":
        code = adjustToJavascript(code, functionName, exampleInput, pathFunctions2)
    if firstPart == "Python":
        code = adjustToPython(code, functionName, exampleInput, testData, pathFunctions2)
    if firstPart == "Java":
        code = adjustToJava(code, functionName, exampleInput, testData, id, pathFunctions2)
    if firstPart == "CPP":
        code = adjustToCPP(code, functionName, exampleInput, testData, id, pathFunctions2)

    with open(path, 'w') as file:
            file.write(code)


    if firstPart == "Java":
        marker = "class Solution {"
        start_index = declaration.find(marker)
        start_index += len(marker)
        shortDeclaration = declaration[start_index:].strip()
        tempCode = shortDeclaration + sampleProgramm
        tempCode = tempCode[:-1]
        with open(pathFunctions1, 'w') as file:
            file.write(tempCode)
    elif firstPart == "CPP":
        include_marker = "#include<"
        last_index = declaration.rfind(include_marker)
        end_of_include = declaration.find('>', last_index)
        start_index = end_of_include + 1
        shortDeclaration = declaration[start_index:].strip()
        tempCode = shortDeclaration + sampleProgramm
        with open(pathFunctions1, 'w') as file:
            file.write(tempCode)
    return len(code)

def adjustToJavascript(code, functionName, exampleInput, pathFunctions2):
    tempCode = ""
    code = code + f"""// Get the command-line arguments
const args = process.argv.slice(2);\n"""
    tempCode = tempCode + f"""// Get the command-line arguments
const args = process.argv.slice(2);\n"""
    for i in range(len(exampleInput)):
        if isinstance(exampleInput[i], int):
            code = code +f"args[{i}] = parseInt(args[{i}]);\n"
            tempCode = tempCode +f"args[{i}] = parseInt(args[{i}]);\n"
        if isinstance(exampleInput[i], float):
            code = code +f"args[{i}] = parseFloat(args[{i}]);\n"
            tempCode = tempCode +f"args[{i}] = parseFloat(args[{i}]);\n"
        if isinstance(exampleInput[i], bool):
            code = code +f"args[{i}] = JSON.parse(args[{i}].toLowerCase());\n"
            tempCode = tempCode +f"args[{i}] = JSON.parse(args[{i}].toLowerCase());\n"
        if isinstance(exampleInput[i], list):
            code = code +f"args[{i}] = args[{i}].replace(/'/g, '\"');\n"
            code = code +f"args[{i}] = JSON.parse(args[{i}]);\n"
            tempCode = tempCode +f"args[{i}] = args[{i}].replace(/'/g, '\"');\n"
            tempCode = tempCode +f"args[{i}] = JSON.parse(args[{i}]);\n"
        if isinstance(exampleInput[i], dict):
            print("dict")
    
    code = code + f"""// Call the function and print the result
const result = {functionName}(...args);
console.log(result);"""
    tempCode = tempCode + f"""// Call the function and print the result
const result = {functionName}(...args);
console.log(result);"""
    
    with open(pathFunctions2, 'w') as file:
        file.write(tempCode)
    return code

def adjustToPython(code, functionName, exampleInput, exampleOutput, pathFunctions2):
    tempCode = ""
    for i in range(len(exampleOutput)):
        if exampleOutput[i]['expected']:
            exampleOutput = exampleOutput[i]['expected']
            break
        if i == len(exampleOutput)-1:
            exampleOutput = []

    code = "import sys\n" + code
    code = "import ast\n" + code
    code = code + 'if __name__ == "__main__":\n'
    tempCode = tempCode + 'if __name__ == "__main__":\n'
    # code = code + '    parser = argparse.ArgumentParser()\n'
    listOfArgs = []
    for i in range(len(exampleInput)):
        if isinstance(exampleInput[i], int):
            char = chr(110+i)
            code = code +f"    {char} = int(sys.argv[{i+1}])\n"
            tempCode = tempCode +f"    {char} = int(sys.argv[{i+1}])\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], float):
            char = chr(110+i)
            code = code +f"    {char} = float(sys.argv[{i+1}])\n"
            tempCode = tempCode +f"    {char} = float(sys.argv[{i+1}])\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], bool):
            char = chr(110+i)
            code = code +f"    {char} = bool(sys.argv[{i+1}])\n"
            tempCode = tempCode +f"    {char} = bool(sys.argv[{i+1}])\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], list):
            char = chr(110+i)
            code = code +f"    {char} = ast.literal_eval(sys.argv[{i+1}])\n"
            tempCode = tempCode +f"    {char} = ast.literal_eval(sys.argv[{i+1}])\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], str):
            char = chr(110+i)
            code = code +f"    {char} = sys.argv[{i+1}]\n"
            tempCode = tempCode +f"    {char} = sys.argv[{i+1}]\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], dict):
            print("dict")
    
    # code = code + "    args = parser.parse_args()\n"
    listOfArgsString = ", ".join(f"{arg}" for arg in listOfArgs)
    code = code + f"    result = {functionName}({listOfArgsString})\n"
    tempCode = tempCode + f"    result = {functionName}({listOfArgsString})\n"
    if isinstance(exampleOutput, list):
        code = code +f"    result = list(result)\n"    
        tempCode = tempCode +f"    result = list(result)\n"    
    code = code + "    print(result)\n"
    tempCode = tempCode + "    print(result)\n"

    with open(pathFunctions2, 'w') as file:
        file.write(tempCode)
    return code

def adjustToJava(code, functionName, exampleInput, testData, id, pathFunctions2):
    tempCode = ""
    code = code.replace("class Solution", "public " + "class Solution")
    
    code = code.rstrip()
    code = code[:-1] 

    code = code + "    public static void main(String[] args) {\n"
    tempCode = tempCode + "    public static void main(String[] args) {\n"
    
    code = code + "    Solution solution = new Solution();\n"
    tempCode = tempCode + "    Solution solution = new Solution();\n"

    listOfArgs = []
    for i in range(len(exampleInput)):
        if isinstance(exampleInput[i], int):
            char = chr(110+i)
            code = code +f"            int {char} = Integer.parseInt(args[{i}]);\n"
            tempCode = tempCode +f"            int {char} = Integer.parseInt(args[{i}]);\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], float):
            char = chr(110+i)
            code = code +f"            double {char} = Float.parseFloat(args[{i}]);\n"
            tempCode = tempCode +f"            double {char} = Float.parseFloat(args[{i}]);\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], bool):
            char = chr(110+i)
            code = code +f"            boolean {char} = Boolean.parseBoolean(args[{i}]);\n"
            tempCode = tempCode +f"            boolean {char} = Boolean.parseBoolean(args[{i}]);\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], list):
            char = chr(110+i)
            code = code + parseJavaList(char, testData, i, id)
            tempCode = tempCode + parseJavaList(char, testData, i, id)
            listOfArgs.append(char)
        if isinstance(exampleInput[i], str):
            char = chr(110+i)
            code = code +f"            String {char} = args[{i}];\n"
            tempCode = tempCode +f"            String {char} = args[{i}];\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], dict):
            print("dict")
    
    listOfArgsString = ", ".join(f"{arg}" for arg in listOfArgs)
    code = code + parseReturnValueJava(testData, functionName, listOfArgsString,id)
    tempCode = tempCode + parseReturnValueJava(testData, functionName, listOfArgsString,id)

    code = code + "    }\n"
    tempCode = tempCode + "    }\n"
    code = code + "}\n"

    with open(pathFunctions2, 'w') as file:
        file.write(tempCode)
    return code
    

def parseReturnValueJava(exampleOutput, functionName, listOfArgsString, id):
    returnString = "    "
    for i in range(len(exampleOutput)):
        if exampleOutput[i]['expected']:
            exampleOutput = exampleOutput[i]['expected']
            break
        if i == len(exampleOutput)-1:
            exampleOutput = []
    
    if isinstance(exampleOutput, int) and not isinstance(exampleOutput, bool) and not id == "Java/47" and not id == "Java/139":
        returnString = returnString + f"int result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, int) and id == "Java/139":
        returnString = returnString + f"long result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, float) or id == "Java/47":
        returnString = returnString + f"double result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, bool):
        returnString = returnString + f"boolean result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, list):
        if len(exampleOutput) == 0:
            print(exampleOutput)
        returnString = parseReturnListValueJava(exampleOutput[0], functionName, listOfArgsString)
    if isinstance(exampleOutput, str):
        returnString = returnString + f"String result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, dict):
        print("output dicts")

    return returnString

def parseReturnListValueJava(exampleOutput, functionName, listOfArgsString):
    returnString = "    "

    if isinstance(exampleOutput, int) and not isinstance(exampleOutput, bool):
        returnString = returnString + f"List<Integer> result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, float):
        returnString = returnString + f"List<Double> result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, bool):
        returnString = returnString + f"List<Boolean> result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"    System.out.println(result);\n"
    if isinstance(exampleOutput, list):
        print(exampleOutput)
        print("list of list output")
    if isinstance(exampleOutput, str):
        returnString = returnString + f"List<String> result = solution.{functionName}({listOfArgsString});\n"
        returnString = returnString + f"        System.out.print(\"[\");\n"  
        returnString = returnString + f"        if(result.size() > 0){"{"} System.out.print(\"'\");{"}"}\n"  

        # returnString = returnString + f'        for (int i = 0; i < result.size(); i++) {"{"}result.set(i, result.get(i).replace("\\"", ""));{"}"} \n'
        returnString = returnString + f"        String print = String.join(\"', '\", result);\n"
        returnString = returnString + f"        if (!print.equals(\"\")){"{"}System.out.print(print);{"}"}\n"   
        
        returnString = returnString + f"        if(result.size() > 0){"{"} System.out.print(\"'\");{"}"}\n"   
        returnString = returnString + f"        System.out.println(\"]\");\n"
    if isinstance(exampleOutput, dict):
        print("output list dicts")

    return returnString

def parseJavaList(char, exampleInput, j, id):    
    for i in range(len(exampleInput)):
        if exampleInput[i]['input'][j]:
            exampleInput = exampleInput[i]['input'][j][0]
            break
        if i == len(exampleInput)-1:
            exampleInput = []

    returnString = ""
    returnString = returnString + f"        String listString{j} = args[{j}];\n"


    if isinstance(exampleInput, int) and not id == "Java/133":  
        
        returnString = returnString +f"        List<Integer> {char} = new ArrayList<>();\n"
        returnString = returnString + f'        if (!listString{j}.equals("[]")) {"{"}\n'
        returnString = returnString + f'        listString{j} = listString{j}.replace("[", "").replace("]", "");\n'
        returnString = returnString + f'        String[] tempArray{j} = listString{j}.split(",");\n'
        returnString = returnString +f"        for (String value : tempArray{j}) {'{'}\n"
        returnString = returnString +f"            {char}.add(Integer.parseInt(value.trim()));\n"
        returnString = returnString +"        }\n"
        returnString = returnString +"        }\n"
    if isinstance(exampleInput, float) or id == "Java/133":
        returnString = returnString +f"        List<Double> {char} = new ArrayList<>();\n"
        returnString = returnString + f'        if (!listString{j}.equals("[]")) {"{"}\n'
        returnString = returnString + f'        listString{j} = listString{j}.replace("[", "").replace("]", "");\n'
        returnString = returnString + f'        String[] tempArray{j} = listString{j}.split(",");\n'
        returnString = returnString +f"        for (String value : tempArray{j}) {'{'}\n"
        returnString = returnString +f"            {char}.add(Double.parseDouble(value.trim()));\n"
        returnString = returnString +"        }\n"
        returnString = returnString +"        }\n"
    if isinstance(exampleInput, bool):
        returnString = returnString +f"        List<Boolean> {char} = new ArrayList<>();\n"
        returnString = returnString + f'        if (!listString{j}.equals("[]")) {"{"}\n'
        returnString = returnString + f'        listString{j} = listString{j}.replace("[", "").replace("]", "");\n'
        returnString = returnString + f'        String[] tempArray{j} = listString{j}.split(",");\n'
        returnString = returnString +f"        for (String value : tempArray{j}) {'{'}\n"
        returnString = returnString +f"            {char}.add(Boolean.parseBoolean(value.trim()));\n"
        returnString = returnString +"        }\n"
        returnString = returnString +"        }\n"
    if isinstance(exampleInput, list):
        print(exampleInput)
        print("list of list")
    if isinstance(exampleInput, str):
        returnString = returnString +f"        List<String> {char} = new ArrayList<>();\n"
        returnString = returnString +f"        listString{j} = listString{j}.replace(\"\\'\", \"\");\n"
        
        returnString = returnString + f'        if (!listString{j}.equals("[]")) {"{"}\n'
        returnString = returnString + f'        listString{j} = listString{j}.replace("[", "").replace("]", "");\n'
        returnString = returnString + f'        String[] tempArray{j} = listString{j}.split(",");\n'
        returnString = returnString +f"        for (String value : tempArray{j}) {'{'}\n"
        returnString = returnString +f"            {char}.add(value.trim());\n"
        returnString = returnString +"        }\n"
        returnString = returnString +"        }\n"
    if isinstance(exampleInput, dict):
        print("list of dicts")


    return returnString

def adjustToCPP(code, functionName, exampleInput, testData, id, pathFunctions2):
    tempCode = ""
    code = "#include <iostream>\n" + code
    code = "#include <vector>\n" + code
    code = "#include <string>\n" + code
    code = "#include <sstream>\n" + code

    code = code + "    int main(int argc, char *argv[]) {\n"
    tempCode = tempCode + "    int main(int argc, char *argv[]) {\n"

    listOfArgs = []
    for i in range(len(exampleInput)):
        if isinstance(exampleInput[i], int):
            char = chr(110+i)
            code = code +f"    int {char} = atoi(argv[{i+1}]);\n"
            tempCode = tempCode +f"    int {char} = atoi(argv[{i+1}]);\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], float):
            char = chr(110+i)
            code = code +f"    float {char} = atof(argv[{i+1}]);\n"
            tempCode = tempCode +f"    float {char} = atof(argv[{i+1}]);\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], list):
            char = chr(110+i)
            code = code + parseCPPList(char, testData, i, id)
            tempCode = tempCode + parseCPPList(char, testData, i, id)
            listOfArgs.append(char)
        if isinstance(exampleInput[i], str):
            char = chr(110+i)
            code = code +f"    string {char} = argv[{i+1}];\n"
            tempCode = tempCode +f"    string {char} = argv[{i+1}];\n"
            listOfArgs.append(char)
        if isinstance(exampleInput[i], dict):
            print("dict")
    
    listOfArgsString = ", ".join(f"{arg}" for arg in listOfArgs)
    code = code + parseReturnValueCPP(testData, functionName, listOfArgsString, id)
    tempCode = tempCode + parseReturnValueCPP(testData, functionName, listOfArgsString, id)

    tempCode = tempCode + "}\n"
    code = code + "}\n"

    with open(pathFunctions2, 'w') as file:
        file.write(tempCode)
    return code

def parseReturnValueCPP(exampleOutput, functionName, listOfArgsString, id):
    returnString = ""
    for i in range(len(exampleOutput)):
        if exampleOutput[i]['expected']:
            exampleOutput = exampleOutput[i]['expected']
            break
        if i == len(exampleOutput)-1:
            exampleOutput = []
    

    if isinstance(exampleOutput, int) and not isinstance(exampleOutput, bool) and not id == "CPP/47" and not id == "CPP/139":
        returnString = returnString + f"    int result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f"    std::cout << result << std::endl;\n"
    if isinstance(exampleOutput, int) and id == "CPP/139":
        returnString = returnString + f"    long long result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f"    std::cout << result << std::endl;\n"
    if isinstance(exampleOutput, float) or id == "CPP/47":
        returnString = returnString + f"    float result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f"    std::cout << result << std::endl;\n"
    if isinstance(exampleOutput, bool):
        returnString = returnString + f"    bool result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f'    std::cout << (result ? "True" : "False") << std::endl;\n'
    if isinstance(exampleOutput, list):
        if len(exampleOutput) == 0:
            print(exampleOutput)
        returnString = parseReturnListValueCPP(exampleOutput[0], functionName, listOfArgsString, id)
    if isinstance(exampleOutput, str):
        returnString = returnString + f"    string result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f"    std::cout << result << std::endl;\n"
    if isinstance(exampleOutput, dict):
        print("output dicts")

    return returnString

def parseReturnListValueCPP(exampleOutput, functionName, listOfArgsString, id):
    returnString = "    "

    intButNeedsFloat = {"CPP/35", "CPP/62"}
    if isinstance(exampleOutput, int) and not isinstance(exampleOutput, bool) and not id in intButNeedsFloat:
        returnString = returnString + f"vector<int> result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f'    cout << "[";\n'
        returnString = returnString + f'    for (size_t i = 0; i < result.size(); ++i) {"{"}\n'
        returnString = returnString + f'        cout << result[i];\n'
        returnString = returnString + f'        if (i != result.size() - 1) {"{"}\n'
        returnString = returnString + f'            std::cout << ", ";\n'
        returnString = returnString + f'        {"}"}\n'
        returnString = returnString + f'    {"}"}\n'
        returnString = returnString + f'    cout << "]" << endl;\n'
    if isinstance(exampleOutput, float) or id in intButNeedsFloat:
        returnString = returnString + f"vector<float> result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f'cout << "[";\n'
        returnString = returnString + f'for (size_t i = 0; i < result.size(); ++i) {"{"}\n'
        returnString = returnString + f'    cout << result[i];\n'
        returnString = returnString + f'    if (i != result.size() - 1) {"{"}\n'
        returnString = returnString + f'        std::cout << ", ";\n'
        returnString = returnString + f'    {"}"}\n'
        returnString = returnString + f'{"}"}\n'
        returnString = returnString + f'cout << "]" << endl;\n'
    if isinstance(exampleOutput, bool):
        returnString = returnString + f"vector<bool> result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f'cout << "[";\n'
        returnString = returnString + f'for (size_t i = 0; i < result.size(); ++i) {"{"}\n'
        returnString = returnString + f'    cout << result[i];\n'
        returnString = returnString + f'    if (i != result.size() - 1) {"{"}\n'
        returnString = returnString + f'        std::cout << ", ";\n'
        returnString = returnString + f'    {"}"}\n'
        returnString = returnString + f'{"}"}\n'
        returnString = returnString + f'cout << "]" << endl;\n'
    if isinstance(exampleOutput, list):
        print(exampleOutput)
        print("list of list output")
    if isinstance(exampleOutput, str):
        returnString = returnString + f"vector<string> result = {functionName}({listOfArgsString});\n"
        returnString = returnString + f'cout << "[";\n'
        returnString = returnString + f'for (size_t i = 0; i < result.size(); ++i) {"{"}\n'        
        returnString = returnString + f"result[i].erase(std::remove(result[i].begin(), result[i].end(), '\\''), result[i].end());\n"
        returnString = returnString + f'    cout << "\'" << result[i] << "\'";\n'
        returnString = returnString + f'    if (i != result.size() - 1) {"{"}\n'
        returnString = returnString + f'        std::cout << ", ";\n'
        returnString = returnString + f'    {"}"}\n'
        returnString = returnString + f'{"}"}\n'
        returnString = returnString + f'cout << "]" << endl;\n'
    if isinstance(exampleOutput, dict):
        print("output list dicts")

    return returnString

def parseCPPList(char, exampleInput, j, id):
    intButNeedsFloat = {"CPP/35", "CPP/47", "CPP/57", "CPP/62", "CPP/133"}    
    for i in range(len(exampleInput)):
        if exampleInput[i]['input'][j]:
            exampleInput = exampleInput[i]['input'][j][0]
            break
        if i == len(exampleInput)-1:
            exampleInput = []

    returnString = ""
    returnString = returnString + f"    string input{j} = argv[{j+1}];\n"
    returnString = returnString + f"    if (input{j}.front() == '[') input{j}.erase(0, 1);\n"
    returnString = returnString + f"    if (input{j}.back() == ']') input{j}.pop_back();\n"
    returnString = returnString + f"    input{j}.erase(std::remove(input{j}.begin(), input{j}.end(), ','), input{j}.end());\n"
    returnString = returnString + f"    std::stringstream iss{j}( input{j} );\n"

    if isinstance(exampleInput, int) and not id in intButNeedsFloat:
        returnString = returnString +f"    int myValue{j};\n"
        returnString = returnString +f"    std::vector<int> {char};\n"
        returnString = returnString +f"    while ( iss{j} >> myValue{j} )\n"
        returnString = returnString +f"        {char}.push_back( myValue{j} );\n"
    if isinstance(exampleInput, float) or id in intButNeedsFloat:
        returnString = returnString +f"    float myValue{j};\n"
        returnString = returnString +f"    std::vector<float> {char};\n"
        returnString = returnString +f"    while ( iss{j} >> myValue{j} )\n"
        returnString = returnString +f"        {char}.push_back( myValue{j} );\n"
    if isinstance(exampleInput, list):
        print(exampleInput)
        print("list of list")
    if isinstance(exampleInput, str):
        returnString = returnString +f"    string myValue{j};\n"
        returnString = returnString +f"    std::vector<string> {char};\n"
        returnString = returnString +f"    while ( iss{j} >> myValue{j} ){"{"}\n"
        returnString = returnString +f"         myValue{j}.erase(std::remove(myValue{j}.begin(), myValue{j}.end(), '\\''), myValue{j}.end());   \n"
        returnString = returnString +f"        {char}.push_back( myValue{j} ); {"}"}\n"
    if isinstance(exampleInput, dict):
        print("list of dicts")


    return returnString


def createTestData(test, id, path):
    if "Python" in id:        
        print(id)
        # extracted_data = extract_relevant_substrings(test)
        extracted_data = findSpecialOperation(test)

        lines = test.split('assert')
        del lines[0]
        lines[-1] = lines[-1].split('check')[0]

        testData = []
        for line in lines:
            newTestData = (processLine(line, id))
            if newTestData: testData.append(newTestData)

        with open(os.path.join(path, "TestData.json"), 'w') as file:
            json.dump(testData, file)  
        
        return testData
    
def processLine(line, id):
    line = line.strip()  
    newTestData = {} 

   
    if "#" in line: line = line.split("#")[0].rstrip()
    position_T = line.lower().find(', "t')
    position_E = line.find(', "E')
    if position_T != -1 and not "]" in line[position_T:]: line = line.split(', "T')[0].rstrip()
    if position_E != -1 and not "]" in line[position_E:]: line = line.split(', "E')[0].rstrip()
    if line.strip() == "True": return False
    if not any(sub in line for sub in {"==", "<", ">", "<=", ">=", "!="}): return False

    if "abs" in line:
        inputParams = extract_function_argsABS(line)            
        newTestData['input'] = inputParams
        operator = extract_comparison_operators(line)
        if len(operator) == 0: return False
        newTestData['operator'] = operator[0]
        newTestData['expected'] = evaluteValue(extract_ExpectedResult(line, newTestData['operator'])[0])
        
        postPros = findSpecialOperation(line)[0]
        PostOperator, PostValue = postPros.split(" ")
        newTestData['postProcessingValue'] = evaluteValue(PostValue)
        newTestData['postProcessingOperator'] = evaluteValue(PostOperator) 
    else: 
        inputParams = extract_function_params(line)   
        if isinstance(inputParams[0], str) and "Mult()" in inputParams[0]: 
            inputParams[0] = inputParams[0].replace("(", "").replace(")", "")
            split_strings = inputParams[0].split("Mult")
            split_strings = [re.sub(r'\s+', '', part) for part in split_strings]
            inputParams[0] = math.prod(int(num) for num in split_strings)
        newTestData['input'] = inputParams
        operator = extract_comparison_operators(line)
        if len(operator) == 0: return False
        newTestData['operator'] = operator[0]
        line = line.replace(newTestData['operator'], newTestData['operator'] + ' ')
        newTestData['expected'] = evaluteValue(extract_ExpectedResult(line, newTestData['operator'])[0])
        newTestData['postProcessingValue'] = ""
        newTestData['postProcessingOperator'] = ""

    if len(newTestData) < 2: print("wenig Daten in ", id)

    if newTestData['input'] == [123.456] and id == "Python/2": newTestData['expected'] = 1e-05
    if newTestData['expected'] == "(3 + 5 + 7, 3 * 5 * 7)" and id == "Python/8": newTestData['expected'] = [15, 105]
    if newTestData['expected'] == "0" and id == "Python/11": newTestData['expected'] = 0
    if newTestData['input'] == ['((abcde Add() cade) Add() CADE)'] and id == "Python/16": newTestData['input'] = ['abcdecadeCADE']
    if newTestData['input'] == ['<>'] and id == "Python/56": 
        newTestData['expected'] = True
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<<><>>'] and id == "Python/56": 
        newTestData['expected'] = True
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<><><<><>><>'] and id == "Python/56": 
        newTestData['expected'] = True
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<><><<<><><>><>><<><><<>>>'] and id == "Python/56": 
        newTestData['expected'] = True
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<<<><>>>>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['><<>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<<<<'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<<>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<><><<><>><>><<>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    if newTestData['input'] == ['<><><<><>><>>><>'] and id == "Python/56": 
        newTestData['expected'] = False
        newTestData['operator'] = "=="
    
    if newTestData['expected'] == 8.18 and id == "Python/71": 
        newTestData['expected'] = 0.01
        newTestData['operator'] = "<"
        newTestData['postProcessingValue'] = 8.18
        newTestData['postProcessingOperator'] = "-"
    if newTestData['expected'] == 1.73 and id == "Python/71": 
        newTestData['expected'] = 0.01
        newTestData['operator'] = "<"
        newTestData['postProcessingValue'] = 1.73
        newTestData['postProcessingOperator'] = "-"        
    if newTestData['expected'] == 16.25 and id == "Python/71": 
        newTestData['expected'] = 0.01
        newTestData['operator'] = "<"
        newTestData['postProcessingValue'] = 16.25
        newTestData['postProcessingOperator'] = "-"
    if newTestData['expected'] == 0.43 and id == "Python/71": 
        newTestData['expected'] = 0.01
        newTestData['operator'] = "<"
        newTestData['postProcessingValue'] = 0.43
        newTestData['postProcessingOperator'] = "-"

    if newTestData['input'] == ['a'] and id == "Python/80": newTestData['expected'] = False
    if newTestData['input'] == ['aa'] and id == "Python/80": newTestData['expected'] = False
    if newTestData['input'] == ['abcd'] and id == "Python/80": newTestData['expected'] = True
    if newTestData['input'] == ['aabb'] and id == "Python/80": newTestData['expected'] = False
    if newTestData['input'] == ['adb'] and id == "Python/80": newTestData['expected'] = True
    if newTestData['input'] == ['xyy'] and id == "Python/80": newTestData['expected'] = False
    if newTestData['input'] == ['iopaxpoi'] and id == "Python/80": newTestData['expected'] = True
    if newTestData['input'] == ['iopaxioi'] and id == "Python/80": newTestData['expected'] = False

    if newTestData['input'] == [[0, '(1 Pow() 0)']] and id == "Python/108": newTestData['input'] = [[0, 1]]

    if newTestData['input'] == [['3', '11111111']] and id == "Python/113": newTestData['expected'] = ["the number of odd elements 1n the str1ng 1 of the 1nput.", "the number of odd elements 8n the str8ng 8 of the 8nput."]
 
    if newTestData['input'] == [["name", "of", "string"]] and id == "Python/158": newTestData['expected'] = "string"
    if newTestData['input'] == [["name", "enam", "game"]] and id == "Python/158": newTestData['expected'] = "enam"
    if newTestData['input'] == [["aaaaaaa", "bb", "cc"]] and id == "Python/158": newTestData['expected'] = "aaaaaaa"
    if newTestData['input'] == [["abc", "cba"]] and id == "Python/158": newTestData['expected'] = "abc"
    if newTestData['input'] == [["play", "this", "game", "of", "footbott"]] and id == "Python/158": newTestData['expected'] = "footbott"
    if newTestData['input'] == [["we", "are", "gonna", "rock"]] and id == "Python/158": newTestData['expected'] = "gonna"
    if newTestData['input'] == [["we", "are", "a", "mad", "nation"]] and id == "Python/158": newTestData['expected'] = "nation"
    if newTestData['input'] == [["this", "is", "a", "prrk"]] and id == "Python/158": newTestData['expected'] = "this"
    if newTestData['input'] == [["b"]] and id == "Python/158": newTestData['expected'] = "b"
    if newTestData['input'] == [["play", "play", "play"]] and id == "Python/158": newTestData['expected'] = "play"

    return newTestData

            


def evaluteValue(value):
        # Use ast.literal_eval to safely evaluate the expression
    try:
        result = ast.literal_eval(value.strip())
    except (ValueError, SyntaxError):
        result = value.strip()  # If evaluation fails, return the string itself
    return result


def extract_function_argsABS(expr):
    # Parse the expression into an AST
    tree = ast.parse(expr, mode='eval')
    
    class FunctionCallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.args = []
        
        def visit_Call(self, node):
            # Extract arguments from the function call
            self.args.extend(self._extract_value(arg) for arg in node.args)
            self.generic_visit(node)
        
        def _extract_value(self, node):
            if isinstance(node, ast.Constant):
                return node.value
            elif isinstance(node, ast.List):
                return [self._extract_value(el) for el in node.elts]
            elif isinstance(node, ast.Tuple):
                return tuple(self._extract_value(el) for el in node.elts)
            elif isinstance(node, ast.Name):
                return node.id
            elif isinstance(node, ast.BinOp):
                # Recursively extract values from binary operations
                left = self._extract_value(node.left)
                right = self._extract_value(node.right)
                return [left, right]
            elif isinstance(node, ast.Call):
                # Recursively extract values from nested function calls
                return [self._extract_value(arg) for arg in node.args]
            elif isinstance(node, ast.UnaryOp):
                # Handle unary operations, e.g., -1
                operand = self._extract_value(node.operand)
                if isinstance(node.op, ast.USub):
                    return -operand
                return operand
            # Handle other node types if needed
            return []

    # Create and run the visitor
    visitor = FunctionCallVisitor()
    visitor.visit(tree)
    
    # Return only the flattened list of arguments
    return [item for sublist in visitor.args for item in (sublist if isinstance(sublist, list) else [sublist])][0]


def extract_function_params(expr):
    # Parse the expression into an AST
    tree = ast.parse(expr, mode='eval')
    
    class FunctionCallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.args = []
        
        def visit_Call(self, node):
            # Extract arguments
            self.args.extend(self._extract_value(arg) for arg in node.args)
            self.generic_visit(node)
        
        def _extract_value(self, node):
            if isinstance(node, ast.Constant):  # Handles Python 3.8+
                return node.value
            elif isinstance(node, ast.Num):  # Handles Python < 3.8
                return node.n
            elif isinstance(node, ast.Str):  # Handles strings in older versions of Python
                return node.s
            elif isinstance(node, ast.List):
                return [self._extract_value(el) for el in node.elts]
            elif isinstance(node, ast.Tuple):
                return tuple(self._extract_value(el) for el in node.elts)
            elif isinstance(node, ast.Name):
                return node.id
            elif isinstance(node, ast.BinOp):
                left = self._extract_value(node.left)
                right = self._extract_value(node.right)
                return f'({left} {ast.dump(node.op)} {right})'
            elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
                return -self._extract_value(node.operand)
            # Add more node types as needed
            return None

    # Create and run the visitor
    visitor = FunctionCallVisitor()
    visitor.visit(tree)
    
    # Return only the list of arguments
    return visitor.args


def findSpecialOperation(code):    
    pattern = r'\)\s*([+\-*/]\s*[^)]*)\)'

    # Find matches
    matches = re.findall(pattern, code)
    return matches

def preprocess_text(text):
    # Replace all new lines with spaces
    return text.replace('\n', ' ')

def extract_ExpectedResult(text, operator):
    # Preprocess the text to remove new lines
    preprocessed_text = preprocess_text(text)
    # Escape the operator to handle special characters
    escaped_operator = re.escape(operator)
    
    # Define the regex pattern
    pattern = rf'{escaped_operator}\s+(.*)'
    
    # Compile the regex pattern with re.IGNORECASE
    regex = re.compile(pattern, re.IGNORECASE)
    
    # Find all matches
    matches = regex.findall(preprocessed_text)
    
    # Remove all whitespaces from the matches
    cleaned_matches = [re.sub(r'\s+', ' ', match).strip() for match in matches]
    
    return cleaned_matches

def all_elements_same(arr):
    # Check if the array is empty or has only one element
    if not arr:
        return True  # Or return False if you prefer an empty array to be considered as having different elements
    if len(arr) == 1:
        return True

    # Get the first element
    first_element = arr[0]

    # Check if all elements are the same as the first element
    for element in arr:
        if element != first_element:
            return False

    return True

def extract_comparison_operators(input_string):
    # Define the comparison operators
    operators = ['==', '!=', '<=', '>=', '<', '>']
    # Create a regex pattern to match any of these operators
    pattern = '|'.join(map(re.escape, operators))
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    return matches

def extract_relevant_substrings(input_string):
    # Define the pattern to match the relevant substrings
    pattern = r'console\.assert\((\w+)\(([^\)]+)\)\s*===\s*(true|false|\'[^\']*\'|\d+|[\[\]\d\s,\.]+)\)'
    
    # Find all matches in the input string
    matches = re.findall(pattern, input_string)
    
    # Extract and parse the relevant parts
    extracted_data = []
    for match in matches:
        function_name = match[0]
        parametersRaw = match[1]
        result_str = match[2]
        
        parameters = parseStringToValue(parametersRaw)
        expected_result = parseStringToValue(result_str)
        
        extracted_data.append([function_name, parameters, expected_result])
    
    return extracted_data

def parseStringToValue(result_str):
        # Parse the result string into an appropriate Python data type
    if result_str == 'true':
        expected_result = True
    elif result_str == 'false':
        expected_result = False
    elif result_str.startswith('\'') and result_str.endswith('\''):
        expected_result = result_str[1:-1]  # Remove the surrounding quotes
    elif result_str.isdigit():
        expected_result = int(result_str)
    else:
        try:
            # Use ast.literal_eval to safely evaluate lists or other complex literals
            expected_result = ast.literal_eval(result_str)
        except:
            expected_result = result_str  # Fallback to the raw string if parsing fails
    return expected_result


def format_output(extracted_data):
    result = []
    for test in extracted_data:
        newTestData = {}        
        if is_iterable(test[1]):
            inputValues = []
            for param in test[1]:
                inputValues.append(param)
            newTestData["input"] = inputValues
        else: newTestData["input"] = test[1]        

        newTestData["expected"] = test[2]           
        result.append(newTestData)
    return result

def safe_eval(expr):
    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return expr
    
def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

javascript = load_dataset("THUDM/humaneval-x", "js")['test']
java = load_dataset("THUDM/humaneval-x", "java")['test']
cpp = load_dataset("THUDM/humaneval-x", "cpp")['test']
python = load_dataset("THUDM/humaneval-x", "python")['test']

all = [javascript, java, cpp, python]
# all = [python]

processDataset(all)