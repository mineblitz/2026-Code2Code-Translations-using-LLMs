import ast
import sys
def sum_squares(lst):
    
    result =[]
    for i in range(len(lst)):
        if i %3 == 0:
            result.append(lst[i]**2)
        elif i % 4 == 0 and i%3 != 0:
            result.append(lst[i]**3)
        else:
            result.append(lst[i])
    return sum(result)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sum_squares(n)
    print(result)
