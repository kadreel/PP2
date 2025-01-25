#If you force int, it rounds it down
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#If you force float, it gives it at least 2 significant numbers
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#Strings are straight-forward and just convert into string without any alterations
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'