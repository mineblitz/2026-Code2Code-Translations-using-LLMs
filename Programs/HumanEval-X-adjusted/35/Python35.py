import ast
import sys
def max_element(l: list):
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = max_element(n)
    print(result)
