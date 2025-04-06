import ast
import sys
def generate_integers(a, b):
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = generate_integers(n, o)
    result = list(result)
    print(result)
