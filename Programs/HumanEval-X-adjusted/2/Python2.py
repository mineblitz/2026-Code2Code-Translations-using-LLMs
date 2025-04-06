import ast
import sys
def truncate_number(number: float) -> float:
    return number % 1.0
if __name__ == "__main__":
    n = float(sys.argv[1])
    result = truncate_number(n)
    print(result)
