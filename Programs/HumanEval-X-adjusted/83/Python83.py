import ast
import sys
def starts_one_ends(n):
    if n == 1: return 1
    return 18 * (10 ** (n - 2))
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = starts_one_ends(n)
    print(result)
