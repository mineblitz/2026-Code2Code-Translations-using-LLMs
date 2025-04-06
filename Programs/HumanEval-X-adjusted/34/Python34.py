import ast
import sys
def unique(l: list):
    return sorted(list(set(l)))
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = unique(n)
    result = list(result)
    print(result)
