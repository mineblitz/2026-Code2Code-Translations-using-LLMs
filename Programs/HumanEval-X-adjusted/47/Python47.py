import ast
import sys
def median(l: list):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = median(n)
    print(result)
