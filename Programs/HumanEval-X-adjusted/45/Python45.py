import ast
import sys
def triangle_area(a, h):
    return a * h / 2.0
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = triangle_area(n, o)
    print(result)
