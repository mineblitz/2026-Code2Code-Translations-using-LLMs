import ast
import sys
def triples_sum_to_zero(l: list):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = triples_sum_to_zero(n)
    print(result)
