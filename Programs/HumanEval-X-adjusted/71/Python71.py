import ast
import sys
def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)/2    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    p = int(sys.argv[3])
    result = triangle_area(n, o, p)
    print(result)
