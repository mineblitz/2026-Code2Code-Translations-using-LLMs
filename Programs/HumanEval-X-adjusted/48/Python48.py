import ast
import sys
def is_palindrome(text: str):
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True
if __name__ == "__main__":
    n = sys.argv[1]
    result = is_palindrome(n)
    print(result)
