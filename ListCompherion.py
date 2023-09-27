l = [1,2,3,4,5,6,7,8,9,10]
l1 = [x**2 for x in l]
print(l1)
l2 = [x**3 for x in l  if (x & 1 == 0)]
print(l2)