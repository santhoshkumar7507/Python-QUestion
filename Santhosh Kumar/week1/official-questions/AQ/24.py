# Accept a two digit number as input and print the sum of its digits.
# What about a three digit number?

# input = 256
# ouput = 265

n = int(input())
fir = n // 100
print(fir)
thir = n % 10
print(thir)
sec = (n // 10)%10
print(sec)
print(fir,thir,sec)
# print(fir+sec+thir)
































