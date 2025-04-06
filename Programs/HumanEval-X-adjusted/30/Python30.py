import ast
import sys
def get_positive(l: list):
    return [e for e in l if e > 0]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = get_positive(n)
    result = list(result)
    print(result)
