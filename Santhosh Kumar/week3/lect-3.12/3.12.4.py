days=int(input("enter days:"))
for i in range(1,days+1):
    total=0
    rainfall=int(input("Enter value:"))  
    while(rainfall!=-1):
     total=total+rainfall
     rainfall=int(input("Enter value:"))
    print(total)       