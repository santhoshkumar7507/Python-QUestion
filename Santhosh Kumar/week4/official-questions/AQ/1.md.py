# class should have numbers which are not perfect squares. Do you observe any pattern?

x=int(input("Enter the number:"))
count=0
for i in range(1,x+1):
    if x%i==0:
        count+=1
print("count",count)

if (x**0.5) * (x**0.5)==x:
    print("perfect square")
else:
    print("Not a perfect square")
    