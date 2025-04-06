import ast
import sys
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = sys.argv[2]
    result = filter_by_prefix(n, o)
    result = list(result)
    print(result)
