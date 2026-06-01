# create a python function that takes a list as input 
# and returns the minimum element in the list

# create a python function that takes a list 
# as input and returns the maximum element in the list

# call these two functions and create one list in ascending 
# order and another list in descending order by taking the list i

# eg : [1,22,32,12,42,15]
# Function to find minimum
def find_min(lst):
    return min(lst)

# Function to find maximum
def find_max(lst):
    return max(lst)

# Given list
i = [1, 22, 32, 12, 42, 15]

# Calling functions
print("Minimum:", find_min(i))
print("Maximum:", find_max(i))

# Ascending order
ascending = sorted(i)

# Descending order
descending = sorted(i, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)
