import ast
import sys
from typing import List


def below_zero(operations: List[int]) -> bool:
    balance = 0

    for op in operations:
        balance += op
        if balance < 0:
            return True

    return False
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = below_zero(n)
    print(result)
