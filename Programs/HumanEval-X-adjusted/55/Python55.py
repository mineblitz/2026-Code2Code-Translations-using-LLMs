import ast
import sys
def fib(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = fib(n)
    print(result)
