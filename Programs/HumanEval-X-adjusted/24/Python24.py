import ast
import sys
def largest_divisor(n: int) -> int:
    for i in reversed(range(n)):
        if n % i == 0:
            return i
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = largest_divisor(n)
    print(result)
