import ast
import sys
def prime_length(string):
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True
if __name__ == "__main__":
    n = sys.argv[1]
    result = prime_length(n)
    print(result)
