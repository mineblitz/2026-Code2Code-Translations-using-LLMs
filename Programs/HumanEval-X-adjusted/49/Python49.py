import ast
import sys
def modp(n: int, p: int):
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = modp(n, o)
    print(result)
