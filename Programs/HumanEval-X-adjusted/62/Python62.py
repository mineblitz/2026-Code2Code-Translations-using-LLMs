import ast
import sys
def derivative(xs: list):
    return [(i * x) for i, x in enumerate(xs)][1:]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = derivative(n)
    result = list(result)
    print(result)
