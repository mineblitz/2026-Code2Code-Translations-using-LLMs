import ast
import sys
def solution(lst):
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = solution(n)
    print(result)
