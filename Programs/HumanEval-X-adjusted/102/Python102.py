import ast
import sys
def choose_num(x, y):
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = choose_num(n, o)
    print(result)
