import ast
import sys
def incr_list(l: list):
    return [(e + 1) for e in l]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = incr_list(n)
    result = list(result)
    print(result)
