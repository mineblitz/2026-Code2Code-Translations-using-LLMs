import ast
import sys
def pluck(arr):
    if(len(arr) == 0): return []
    evens = list(filter(lambda x: x%2 == 0, arr))
    if(evens == []): return []
    return [min(evens), arr.index(min(evens))]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = pluck(n)
    result = list(result)
    print(result)
