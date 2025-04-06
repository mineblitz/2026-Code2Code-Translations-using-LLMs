import ast
import sys
def count_up_to(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

if __name__ == "__main__":
    n = int(sys.argv[1])
    result = count_up_to(n)
    result = list(result)
    print(result)
