import ast
import sys
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    running_max = None
    result = []

    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)

        result.append(running_max)

    return result
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = rolling_max(n)
    result = list(result)
    print(result)
