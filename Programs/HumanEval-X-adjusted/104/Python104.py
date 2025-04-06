import ast
import sys
def unique_digits(x):
    odd_digit_elements = []
    for i in x:
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
    return sorted(odd_digit_elements)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = unique_digits(n)
    result = list(result)
    print(result)
