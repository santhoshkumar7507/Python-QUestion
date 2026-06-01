# write a code to find whether the given number is prime or not
num=int(input())
if(num>2):
    print(2,end=" ")
    for i in range(3,num):
        a=False
        for j in range(2,i):
            if(i%j == 0):
                a=False
                break
            else:
                a=True
        if(a):
            print(i, end=" ")




