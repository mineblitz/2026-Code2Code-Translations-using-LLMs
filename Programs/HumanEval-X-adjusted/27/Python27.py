import ast
import sys
def flip_case(string: str) -> str:
    return string.swapcase()
if __name__ == "__main__":
    n = sys.argv[1]
    result = flip_case(n)
    print(result)
