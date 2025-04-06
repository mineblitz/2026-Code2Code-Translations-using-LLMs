import ast
import sys
def pairs_sum_to_zero(l):
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = pairs_sum_to_zero(n)
    print(result)
