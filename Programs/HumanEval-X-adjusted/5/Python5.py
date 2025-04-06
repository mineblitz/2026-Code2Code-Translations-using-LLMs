import ast
import sys
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if not numbers:
        return []

    result = []

    for n in numbers[:-1]:
        result.append(n)
        result.append(delimeter)

    result.append(numbers[-1])

    return result
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = int(sys.argv[2])
    result = intersperse(n, o)
    result = list(result)
    print(result)
