import ast
import sys
def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = greatest_common_divisor(n, o)
    print(result)
