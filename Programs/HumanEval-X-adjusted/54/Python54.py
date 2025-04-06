import ast
import sys
def same_chars(s0: str, s1: str):
    return set(s0) == set(s1)
if __name__ == "__main__":
    n = sys.argv[1]
    o = sys.argv[2]
    result = same_chars(n, o)
    print(result)
