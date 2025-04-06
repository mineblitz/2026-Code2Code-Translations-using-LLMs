import ast
import sys
def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    result = circular_shift(n, o)
    print(result)
