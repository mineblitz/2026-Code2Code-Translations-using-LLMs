import ast
import sys
def compare(game,guess):
    return [abs(x-y) for x,y in zip(game,guess)]
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    o = ast.literal_eval(sys.argv[2])
    result = compare(n, o)
    result = list(result)
    print(result)
