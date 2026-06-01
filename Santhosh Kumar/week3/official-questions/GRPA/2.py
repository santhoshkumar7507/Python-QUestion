
num = 50
for j in range(2,num):
    n=j
    flag=True
    for i in range(2,n):
        if n % i == 0:
            flag=False
    if flag == True and num % n==0:
        print(n)       
