def squares(nu):
    return nu ** 2

n = int(input("Enter a number: "))
resL = []
for i in range(n):
    res = squares(i)
    resL.append(str(res))

print(", ".join(resL))

#with n = 10, output is "0, 1, 4, 9, 16, 25, 36, 49, 64, 81"