import ast
import sys
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
if __name__ == "__main__":
    n = sys.argv[1]
    result = count_distinct_characters(n)
    print(result)
