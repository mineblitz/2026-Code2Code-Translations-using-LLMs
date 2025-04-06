import ast
import sys
def string_sequence(n: int) -> str:
    return ' '.join([str(x) for x in range(n + 1)])
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = string_sequence(n)
    print(result)
