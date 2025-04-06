import ast
import sys
def common(l1: list, l2: list):
    ret = set()
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.add(e1)
    return sorted(list(ret))
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = ast.literal_eval(sys.argv[2])
    result = common(n, o)
    result = list(result)
    print(result)
