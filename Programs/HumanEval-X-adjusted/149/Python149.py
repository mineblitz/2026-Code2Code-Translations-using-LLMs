import ast
import sys
def sorted_list_sum(lst):
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return sorted(new_lst, key=len)
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = sorted_list_sum(n)
    result = list(result)
    print(result)
