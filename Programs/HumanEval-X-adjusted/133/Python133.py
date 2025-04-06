import ast
import sys
def sum_squares(lst):
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i)**2
    return squared
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sum_squares(n)
    print(result)
