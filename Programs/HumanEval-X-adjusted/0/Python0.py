import ast
import sys
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = float(sys.argv[2])
    result = has_close_elements(n, o)
    print(result)
