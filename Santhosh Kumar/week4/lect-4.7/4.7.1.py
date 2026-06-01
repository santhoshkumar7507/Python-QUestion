# create the below matrix A and B with python
# A = 1 2 3
#     4 5 6
#     7 8 9 
# 
# B = 1 2 1
#     6 2 3
#     4 2 1 
# 
# 
import numpy as np

# Create matrix A
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Create matrix B
B = np.array([
    [1, 2, 1],
    [6, 2, 3],
    [4, 2, 1]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)