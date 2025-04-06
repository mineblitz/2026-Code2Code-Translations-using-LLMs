import ast
import sys
def encrypt(s):
    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c)+2*2) % 26]
        else:
            out += c
    return out
if __name__ == "__main__":
    n = sys.argv[1]
    result = encrypt(n)
    print(result)
