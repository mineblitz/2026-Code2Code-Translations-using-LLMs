import ast
import sys
def total_match(lst1, lst2):
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst1
    else:
        return lst2
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = ast.literal_eval(sys.argv[2])
    result = total_match(n, o)
    result = list(result)
    print(result)
