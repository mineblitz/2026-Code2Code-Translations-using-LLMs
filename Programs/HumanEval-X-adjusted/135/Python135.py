import ast
import sys
def can_arrange(arr):
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
    return ind
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = can_arrange(n)
    print(result)
