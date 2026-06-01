
x=int(input())
pre = None 
count = 0

while x!=-1:
    if pre!=x:
        count+=1
    pre=x
    x=int(input())
print(count)
       
   
        
            