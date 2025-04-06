import ast
import sys
from typing import List


def all_prefixes(string: str) -> List[str]:
    result = []

    for i in range(len(string)):
        result.append(string[:i+1])
    return result
if __name__ == "__main__":
    n = sys.argv[1]
    result = all_prefixes(n)
    result = list(result)
    print(result)
