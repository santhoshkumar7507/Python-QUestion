E_1 = True
E_2 = False
E_3 = not (E_1 or E_2)
E_4 = (not E_1) and (not E_2)
print(E_3 == E_4)

# It is always True
