num=123456
op=num%10
num=num//10

while num>0:
    digit=num%10 #5 4 3 2 1
    op=op*10+digit #65 654 6543 65432 654321
    num=num//10#1234 123 12 1 
print(op)

