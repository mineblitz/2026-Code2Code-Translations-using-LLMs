import ast
import sys
def strlen(string: str) -> int:
    return len(string)
if __name__ == "__main__":
    n = sys.argv[1]
    result = strlen(n)
    print(result)
