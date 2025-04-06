import ast
import sys
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = mean_absolute_deviation(n)
    print(result)
