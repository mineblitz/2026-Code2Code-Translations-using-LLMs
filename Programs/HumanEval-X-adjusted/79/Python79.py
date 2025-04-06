import ast
import sys
def decimal_to_binary(decimal):
    return "db" + bin(decimal)[2:] + "db"
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = decimal_to_binary(n)
    print(result)
