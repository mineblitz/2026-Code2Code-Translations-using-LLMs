import ast
import sys
def strange_sort_list(lst):
    res, switch = [], True
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = strange_sort_list(n)
    result = list(result)
    print(result)
