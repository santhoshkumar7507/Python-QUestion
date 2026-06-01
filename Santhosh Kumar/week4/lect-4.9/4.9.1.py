# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# multiply these two matrices using for loops
# Create matrix A
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create matrix B
B = [
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
]

# Initialize result matrix C with zeros
C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Matrix multiplication using for loops
for i in range(len(A)):          # iterate through rows of A
    for j in range(len(B[0])):   # iterate through columns of B
        for k in range(len(B)):  # iterate through rows of B
            C[i][j] += A[i][k] * B[k][j]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix C (A x B):")
for row in C:
    print(row)