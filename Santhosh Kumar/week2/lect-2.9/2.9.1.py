# find whether the given number is even or odd

# number=int(input("Enter the number:"))
# if number % 2 ==0:
#     print("Even")
# else:
#     print("odd")

# number=int(input("ENter the number:"))
# a=number % 10

# if a==0:
#     print(0)
# elif a ==5:
#     print(5)
# else:
#     print("other")

mark=int(input("Enter the mark:"))

if mark<0 or mark >100:
    print("invalid")
elif mark>100:
    print("A")
elif mark>90:
    print("B")
elif mark >80:
    print("c")
elif mark>70:
    print("D")
elif mark>60:
    print("e")

else:
    print("invalid ")
