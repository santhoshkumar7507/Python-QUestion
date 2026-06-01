# compute the compound interest by taking in p,n as arguments and interest rate = 10%
# p-> principal amount, n-> number of years

def compound_interest(p, n):
    if n == 0:
        return p
    else:
        return compound_interest(p * 1.1, n - 1)
print(compound_interest(1000, 2))  # Output: 1210.0