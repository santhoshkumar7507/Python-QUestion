# Find smallest n such that a number with n repeated 7's is divisible by 2003

mod = 2003
remainder = 0

for n in range(1, 2003):   # upper bound is enough since 2003 is prime
    remainder = (remainder * 10 + 7) % mod
    if remainder == 0:
        print("Number of digits:", n)
        break

# l=[1,2,3,4,5]
# target=6
# for i in l:
#     if i == target:
#         print(i)
#         break
# else:
#     print("Not found")
# i=11
# while(i<10):
#     print(i)
#     i+=1
# else:
#     print("Loop ended")

# try:
#     print(1/0)
# except Exception as e:
#     print(e)
# else:
#     print("No error")
# finally:
#     print("Finally")

# l=1,3,4,5
# x,y,*a=l
# print(x,y,a)

# for i in range(1, 6):
#     for j in range(1, 6):
#         for k in range(1, 2):
#             if i == j:
#                 print("-")
#             else:
#                 print("*", end=" ")
#     print("+")

# for i in range(1, 5):
#     for j in range(1, 5):
#         if j == 3:
#             break
#         if i == 2:
#             continue
#         print(i, j)


def analyze(data): 
    result = [] 
    for item in data: 
        if isinstance(item, tuple): 
            total = 0
            for x in item: 
                if x % 2 == 0: 
                    total += x 
                    result.append(total) 
        elif isinstance(item, int) and item % 2 == 1: 
            result.append(item * 3) 
        else: 
            continue
    return result
sample = [(2, 5, 6), 7, (1, 3), 4, (8, 2, 1)] 
output = analyze(sample)


