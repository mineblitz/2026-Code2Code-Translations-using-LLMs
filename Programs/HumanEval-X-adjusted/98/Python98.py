import ast
import sys
def count_upper(s):
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count
if __name__ == "__main__":
    n = sys.argv[1]
    result = count_upper(n)
    print(result)
