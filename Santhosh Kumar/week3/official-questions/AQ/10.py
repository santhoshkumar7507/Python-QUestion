# Write a program to accept the name and age of a person and display the message
# "Hii,I am {}. I am {} is old." using string formatting.

name=input("Enter the name : ")
age=int(input("Enter the age : "))
message="Hii,I am {}. I am {} is old.".format(name,age)
print(message)
