import ast
import sys
def maximum(arr, k):
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ans
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = int(sys.argv[2])
    result = maximum(n, o)
    result = list(result)
    print(result)
