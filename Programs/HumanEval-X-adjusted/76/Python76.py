import ast
import sys
def is_simple_power(x, n):
    if (n == 1): 
        return (x == 1) 
    power = 1
    while (power < x): 
        power = power * n 
    return (power == x) 
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = is_simple_power(n, o)
    print(result)
