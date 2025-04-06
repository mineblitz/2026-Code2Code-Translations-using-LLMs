import ast
import sys
def x_or_y(n, x, y):
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    p = int(sys.argv[3])
    result = x_or_y(n, o, p)
    print(result)
