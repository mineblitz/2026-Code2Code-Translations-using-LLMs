import ast
import sys
def check_if_last_char_is_a_letter(txt):
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False
if __name__ == "__main__":
    n = sys.argv[1]
    result = check_if_last_char_is_a_letter(n)
    print(result)
