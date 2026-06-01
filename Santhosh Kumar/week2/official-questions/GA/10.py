a=True
b=True
c=True
if a:
    if b:
        print('OK')
    if c:
        print('OK')

if a and b or c:
    print('OK')

# # output:
# option 3 and 5
