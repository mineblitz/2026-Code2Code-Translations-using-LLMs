import ast
import sys
def how_many_times(string: str, substring: str) -> int:
    times = 0

    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            times += 1

    return times
if __name__ == "__main__":
    n = sys.argv[1]
    o = sys.argv[2]
    result = how_many_times(n, o)
    print(result)
