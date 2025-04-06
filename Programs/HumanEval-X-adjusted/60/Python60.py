import ast
import sys
def sum_to_n(n: int):
    return sum(range(n + 1))
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = sum_to_n(n)
    print(result)
