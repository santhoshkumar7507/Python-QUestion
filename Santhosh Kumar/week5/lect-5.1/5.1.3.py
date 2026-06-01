# create a function discount that takes two arguments cost and d
#  'discount percentage' as input,and it should return the cost
#  after reducing 
# the discounted price from the original price

# Test cases
# ip : discount(100,50)
# op : 50

# ip : discount(200,20)
# op: 160
def discount(cost, d):
    discounted_amount = cost * (d / 100)
    final_price = cost - discounted_amount
    return final_price
# Test cases
print(discount(100, 50))   # Expected output: 50
print(discount(200, 20))   # Expected output: 160