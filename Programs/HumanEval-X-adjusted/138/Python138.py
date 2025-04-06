import ast
import sys
def is_equal_to_sum_even(n):
    return n%2 == 0 and n >= 8
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = is_equal_to_sum_even(n)
    print(result)
