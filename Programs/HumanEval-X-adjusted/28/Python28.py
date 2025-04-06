import ast
import sys
from typing import List


def concatenate(strings: List[str]) -> str:
    return ''.join(strings)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = concatenate(n)
    print(result)
