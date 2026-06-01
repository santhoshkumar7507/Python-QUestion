# for i in range(5):
#     print(5*"*")


# for i in range(1,6):
#     print(i*"*")

# for i in range(5,0,-1):
#     print(i*"*")
# ````
#     1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
# ````

# op="" 
# for i in range(1,6):
#     op+=str(i)+" "
#     print(op)


    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *


# for i in range(1,6):
#     print(i*"*")
# for j in range(4,0,-1):
#     print(j*"*")  



    #     *
    #     **
    #    ***
    #   ****
    #  *****


# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)



# arr=[1,2,3,4,1,8,9,10,11]

# print(len(arr))

# max_lenght =1
# current_length =1

# for i in range (1,len(arr)):
#     if arr [i]>arr[i-1]:
#         current_length+=1
#         max_lenght+=1
#     else:
#         current_length=1
# print(max_lenght)


# 1.  *****
#     *****
#     *****
#     *****
#     *****


# for i in range(5):
#     print(5*"*")



# 2.  *
#     **
#     ***
#     ****
#     *****


# for i in range(1,6):
#     print(i*"*")



# 3.  *****
#     ****
#     ***
#     **
#     *

# for i in range(5,0,-1):
#     print(i*"*")


# 4.  1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3 4 5
# op=""
# for i in range(1,6):
#     op+=str(i)+" "
#     print(op)

# 5.  *
#     **
#     ***
#     ****
#     *****
#     ****
#     ***
#     **
#     *

# for i in range(1,6):
#     print(i*"*")
# for j in range(4,0,-1):
#     print(j*"*")    


# arr=[1,2,2,3,2,3,4,5,2,4,6,7,8,9,10]

# freq={}

# for i in arr:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)            

# sum of digits of a number


# num=int(input("Enter the number: "))
# total=0

# while num>0:
#     digit=num%10
#     total=total+digit
#     num//=10


# print(total)    

    #      *
    #     **
    #    ***
    #   ****
    #  *****


# for i in range(1,6):
#     print(" "*(5-i)+"*"*i)



    
# 7.   *****
#       ****
#        ***
#         **
#          *


# for i in range(5,0,-1):
#     print(" "*(5-i)+"*"*i)



# 8.      *
#        ***
#       *****
#      *******
#     *********

# power pf value

# num=2**5
# print(num)

# permutation of string

# import itertools

# string="abc"
# d=itertools.permutations(string)
# for i in d:
#     print("".join(i))


# palandromic substring
s="ababa"
n=len(s)
count=0         
for i in range(n):
    for j in range(i,n):
        substring=s[i:j+1]
        if substring==substring[::-1]:
            count+=1
            print(substring)
print("Total palandromic substring:         ",count)






# find the trailing  number of zero

# def trailing_zeros(n):
#     count=0

#     while n>=5:
#         n=n//5
#         count+=n
#     return count
# num=100   
# print("Trailing zeros in",num,"! is",trailing_zeros(num))



# matrix 90 degree rotation
# def rotate_matrix(matrix):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# rotated_matrix = rotate_matrix(matrix)
# for row in rotated_matrix:
#     print(row)