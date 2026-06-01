num=int(input())
n=num
reverse=0

while num>0:
    digits=num%10
    reverse=reverse*10+digits
    num=num//10
print(reverse)

if n == reverse:
    print("palindrome")
else:
    print("not a palindrome")