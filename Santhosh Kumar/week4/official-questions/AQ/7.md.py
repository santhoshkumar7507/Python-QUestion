x = 1
while (x ** 2 + x + 41) % 41 != 0:
    x += 1
print(x)
# check correctness of answer
# assert statement may be new to you
# assert False will throw an AssertionError
assert (x ** 2 + x + 41) % 41 == 0