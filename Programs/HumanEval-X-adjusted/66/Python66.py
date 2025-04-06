import ast
import sys
def digitSum(s):
    if s == "": return 0
    return sum(ord(char) if char.isupper() else 0 for char in s)
if __name__ == "__main__":
    n = sys.argv[1]
    result = digitSum(n)
    print(result)
