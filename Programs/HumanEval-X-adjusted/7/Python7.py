import ast
import sys
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = sys.argv[2]
    result = filter_by_substring(n, o)
    result = list(result)
    print(result)
