import ast
import sys
def odd_count(lst):
    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = odd_count(n)
    result = list(result)
    print(result)
