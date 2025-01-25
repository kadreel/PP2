#OH MY GOD STRINGS EXIST! NOT LIKE I USED THEM BEFORE A HUNDRED TIME! BUT WHERE ARE PERCUSSIONS, AND BRASS, AND WINDS, AND KEYS?!?!?!?
print("Double")
print('Single') #either work, as it had already been established in python variables

#if you use doubles, you can't use singles inside without breaking the string, and the opposite for singles
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
#print('He is called 'Johnny'') <- This is an open-and-shut case of murder

#strings can be variables... how wise
a = "Hoi!"
print(a)

#alike the freaky comments, strings can be done freaky alike
a = """Ash nazg durbatulûk,
ash nazg gimbatul,
Ash nazg thrakutulûk
agh burzum-ishi krimpatul."""
print(a)

#can use single quotes
a = '''Ash nazg durbatulûk,
ash nazg gimbatul,
Ash nazg thrakutulûk
agh burzum-ishi krimpatul.'''
print(a)

#can use strings as arrays, cuz they kinda are
a = "Hello, World!"
print(a[1]) #outputs "e"
for x in "banana":
    print(x) #outputs entire string "banana," albeit each letter gets a new line

#can check if sequence exists
txt = "The best things in life are free!"
print("free" in txt) #outputs "True"
#alternatively use if:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.") #outputs this, whatever is put after if check

#can be modified with not
txt = "The best things in life are free!"
print("expensive" not in txt) #outputs "True"
#again, can be used with if:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.") #outputs this, whatever is put after if check