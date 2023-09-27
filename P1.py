# problem statement
# Knowing the durabilty of vechile
# to solve this we need to equ
# 2x+4y=6
# 3x+4y=8
#Write a progam to print reverse of each element the list
a = ["123","456","789"]
for i in a:
    print(int(str(i)[::-1]))

b = [int(str(x)[::-1]) for x in a]
print(b)
