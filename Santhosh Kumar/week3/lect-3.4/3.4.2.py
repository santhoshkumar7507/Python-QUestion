num=int(abs(int(input()))) #1234
count=0                 

while num>0:     #123>0       12>0     1>0      0>0
    num=num//10   #123//10=12 12//10=1  1//10=0
    count=count+1 #3
print(count)

