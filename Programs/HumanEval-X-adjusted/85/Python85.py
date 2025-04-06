import ast
import sys
def add(lst):
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = add(n)
    print(result)
