import ast
import sys
def specialFilter(nums):
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 
if __name__ == "__main__":
    n = ast.literal_eval(sys.argv[1])
    result = specialFilter(n)
    print(result)
