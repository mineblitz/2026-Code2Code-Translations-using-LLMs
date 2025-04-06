import ast
import sys
def f(n):
    ret = []
    for i in range(1,n+1):
        if i%2 == 0:
            x = 1
            for j in range(1,i+1): x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1,i+1): x += j
            ret += [x]
    return ret
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = f(n)
    result = list(result)
    print(result)
