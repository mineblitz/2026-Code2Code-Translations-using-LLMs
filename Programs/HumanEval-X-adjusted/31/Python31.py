import ast
import sys
def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return True
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = is_prime(n)
    print(result)
