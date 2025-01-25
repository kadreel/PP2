#Creating variables
x = 5
y = "John"
print(x)
print(y)

#can change values and type after initial declaration
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

#Single and double quotes are treated equally
x = "John"
# is the same as
x = 'John'

#Values are case-sensitive
a = 4
A = "Sally"
#A will not overwrite a due to being uppercase and lowercase respectively