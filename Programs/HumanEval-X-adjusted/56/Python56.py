import ast
import sys
def correct_bracketing(brackets: str):
    depth = 0
    for b in brackets:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
if __name__ == "__main__":
    n = sys.argv[1]
    result = correct_bracketing(n)
    print(result)
