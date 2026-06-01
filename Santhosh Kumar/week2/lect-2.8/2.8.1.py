# take salary as input, if the person salary is above 100000
# then print "eligible" else print "not eligible"

# TestCase 1
'''
INPUT: 90000
OUTPUT: 'not eligible'
'''

# TestCase 2
'''
INPUT: 120000
OUTPUT: 'eligible'
'''
number=int(input("Enter the number:"))
if number > 100000:
    print("eligible")
else:
    print("not eligible")