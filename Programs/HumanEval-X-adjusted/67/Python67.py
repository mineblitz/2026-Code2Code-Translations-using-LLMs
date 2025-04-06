import ast
import sys
def fruit_distribution(s,n):
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis)
if __name__ == "__main__":
    n = sys.argv[1]
    o = int(sys.argv[2])
    result = fruit_distribution(n, o)
    print(result)
