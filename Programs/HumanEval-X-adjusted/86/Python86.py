import ast
import sys
def anti_shuffle(s):
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])
if __name__ == "__main__":
    n = sys.argv[1]
    result = anti_shuffle(n)
    print(result)
