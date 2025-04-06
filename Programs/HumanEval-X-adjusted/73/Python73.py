import ast
import sys
def smallest_change(arr):
    ans = 0
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - i - 1]:
            ans += 1
    return ans
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = smallest_change(n)
    print(result)
