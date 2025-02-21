def fourthreeGen(nu):
    if (nu % 3 == 0 or nu % 4 == 0) and nu >= 1:
        return nu

n = int(input("Enter a number: "))
resL = []
for i in range(n):
    res = fourthreeGen(i)
    if res != None:
        resL.append(str(res))

print(", ".join(resL))

#with n = 10, output is "3, 4, 6, 8, 9"