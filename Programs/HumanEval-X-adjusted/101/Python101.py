import ast
import sys
def words_string(s):
    if not s:
        return []

    s_list = []

    for letter in s:
        if letter == ',':
            s_list.append(' ')
        else:
            s_list.append(letter)

    s_list = "".join(s_list)
    return s_list.split()
if __name__ == "__main__":
    n = sys.argv[1]
    result = words_string(n)
    result = list(result)
    print(result)
