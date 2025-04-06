import ast
import sys
def add_elements(arr, k):
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = int(sys.argv[2])
    result = add_elements(n, o)
    print(result)
