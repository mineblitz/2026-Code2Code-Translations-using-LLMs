import ast
import sys
def right_angle_triangle(a, b, c):
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    p = int(sys.argv[3])
    result = right_angle_triangle(n, o, p)
    print(result)
