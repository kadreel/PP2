#MIXING STRINGS AND INTS IS HERESY
"""
age = 36
txt = "anti-heresy"
txt = "My name is John, I am " + age
"""

#This is legal.
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Use of placeholder
price = 59
txt = f"The price is {price:.2f} dollars"  #price is a placeholder, and :.2f is a modifier that forces it to have 2 numbers after . which results in 59.00
print(txt)

txt = f"The price is {20 * 59} dollars" #similar
print(txt) #outputs 1180