def evenGen(nu):
    if nu % 2 == 1:
        return nu

n = int(input("Enter a number: "))
resL = []
for i in range(n):
    res = evenGen(i)
    if res != None:
        resL.append(str(res))

print(", ".join(resL))

#with n = 10, output is "1, 3, 5, 7, 9"