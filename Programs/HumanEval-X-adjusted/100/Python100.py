import ast
import sys
def make_a_pile(n):
    return [n + 2*i for i in range(n)]
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = make_a_pile(n)
    result = list(result)
    print(result)
