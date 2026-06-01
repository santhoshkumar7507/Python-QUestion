#  create a recursive function to return the sum  numbers from 1 to n, take  n as an argument
def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n - 1)
    
print(sum_of_numbers(5))  # Output: 15