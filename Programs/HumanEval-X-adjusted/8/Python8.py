import ast
import sys
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_value = 0
    prod_value = 1

    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sum_product(n)
    result = list(result)
    print(result)
