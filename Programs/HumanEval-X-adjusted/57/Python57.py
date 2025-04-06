import ast
import sys
def monotonic(l: list):
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = monotonic(n)
    print(result)
