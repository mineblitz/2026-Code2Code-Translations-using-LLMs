import ast
import sys
def count_nums(arr):
    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = count_nums(n)
    print(result)
