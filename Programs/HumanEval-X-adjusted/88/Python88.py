import ast
import sys
def sort_array(array):
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 == 0) 
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sort_array(n)
    result = list(result)
    print(result)
