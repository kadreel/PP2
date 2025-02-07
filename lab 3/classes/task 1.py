class Strigoi:
    def __init__(self):
        self.recirra = ""
    
    def getString(self):
        self.recirra = input("Enter a string: ")        #Receives input
    
    def printString(self):
        print(self.recirra.upper())                     #Prints input in uppercase

# EXAMPLE:

a = Strigoi()
a.getString()   #Gets input from user. For example, input is "lAb"
a.printString()  #Prints the string in uppercase. For input "lAb", output is "LAB"