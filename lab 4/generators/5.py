n = int(input("Enter a number: "))
resL = []
for i in range(n, 0, -1):
    if i != 1:
        print(i, end = ", ")
    else:
        print(i)

#with n = 10, output is "10, 9, 8, 7, 6, 5, 4, 3, 2, 1"