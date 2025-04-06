import ast
import sys
def search(lst):
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = -1
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = search(n)
    print(result)
