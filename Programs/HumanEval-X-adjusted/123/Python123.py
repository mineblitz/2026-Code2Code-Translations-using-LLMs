import ast
import sys
def get_odd_collatz(n):
    if n%2==0:
        odd_collatz = [] 
    else:
        odd_collatz = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = n*3 + 1
            
        if n%2 == 1:
            odd_collatz.append(int(n))

    return sorted(odd_collatz)
if __name__ == "__main__":
    n = int(sys.argv[1])
    result = get_odd_collatz(n)
    result = list(result)
    print(result)
