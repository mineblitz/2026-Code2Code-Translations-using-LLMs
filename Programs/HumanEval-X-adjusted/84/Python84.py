import ast
import sys
def solve(N):
    return bin(sum(int(i) for i in str(N)))[2:]
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = solve(n)
    print(result)
