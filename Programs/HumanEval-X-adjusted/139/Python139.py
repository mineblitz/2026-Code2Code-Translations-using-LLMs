import ast
import sys
def special_factorial(n):
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = special_factorial(n)
    print(result)
