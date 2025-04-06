import ast
import sys
def encode(message):
    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])
if __name__ == "__main__":
    n = sys.argv[1]
    result = encode(n)
    print(result)
