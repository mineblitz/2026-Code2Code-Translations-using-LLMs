import ast
import sys
def sort_array(arr):
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sort_array(n)
    result = list(result)
    print(result)
