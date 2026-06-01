# create an example while loop which will not terminate , and prints `hi` in each iteration
# and how will you stop the program manually?

while True:
    print('hi')

# ♾️ Non-Terminating while Loop Example
# A while loop that will not terminate, also known as an infinite loop,
#  is created when the condition it checks always evaluates to True.

# Here is a Python example that prints hi indefinitely:

# Python

# # The condition 'True' will never become False, so the loop runs forever.
# while True:
#     print('hi') 
# Explanation of Why it's Infinite
# In this example, the loop condition is simply the Boolean value True.
#  Since True is always True, the program never finds a reason to exit the loop,
#  and it will continue to execute the print('hi') command, consuming system resources,
#  until it is manually interrupted.