## write a code for the below test cases

# print until you find @ in the string, using break statement
# TestCase 1
INPUT="abcd@gmail.com"
# OUTPUT:
'''
a
b
c
d
'''

num="santhosh@gmail.com"

for i in num:
    if i=="@":
        break
    print(i)