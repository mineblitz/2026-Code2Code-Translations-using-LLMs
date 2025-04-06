import ast
import sys
def is_bored(S):
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)
if __name__ == "__main__":
    n = sys.argv[1]
    result = is_bored(n)
    print(result)
