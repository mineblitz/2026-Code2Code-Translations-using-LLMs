import ast
import sys
from typing import List


def string_xor(a: str, b: str) -> str:
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))
if __name__ == "__main__":
    n = sys.argv[1]
    o = sys.argv[2]
    result = string_xor(n, o)
    print(result)
