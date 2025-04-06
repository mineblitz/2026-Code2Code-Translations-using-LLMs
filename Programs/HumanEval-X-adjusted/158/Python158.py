import ast
import sys
def find_max(words):
    return sorted(words, key = lambda x: (-len(set(x)), x))[0]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = find_max(n)
    print(result)
