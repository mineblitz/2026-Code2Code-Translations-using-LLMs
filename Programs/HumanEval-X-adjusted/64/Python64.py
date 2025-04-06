import ast
import sys
FIX = """
Add more test cases.
"""

def vowels_count(s):
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels
if __name__ == "__main__":
    n = sys.argv[1]
    result = vowels_count(n)
    print(result)
