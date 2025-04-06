import ast
import sys
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = remove_duplicates(n)
    result = list(result)
    print(result)
