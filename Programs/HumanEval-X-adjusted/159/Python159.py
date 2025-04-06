import ast
import sys
def eat(number, need, remaining):
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]
if __name__ == "__main__":
    n = int(sys.argv[1])
    o = int(sys.argv[2])
    p = int(sys.argv[3])
    result = eat(n, o, p)
    result = list(result)
    print(result)
