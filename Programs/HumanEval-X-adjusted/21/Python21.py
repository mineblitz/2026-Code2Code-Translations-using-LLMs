import ast
import sys
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = rescale_to_unit(n)
    result = list(result)
    print(result)
