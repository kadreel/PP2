class Shape:
    def __init__(self):
        self._area = 0                          #Creates _area and defaults it to 0
    
    def area(self):                             #Outputs area
        print(f"Area of shape: {self._area}")

class Square(Shape):
    def __init__(self, length):                 #Gets length, calls for calculation
        super().__init__()                      #Call the init method of the parent class (Shape) to create variable _area with default of 0
        self.length = length
        self.areaCalc()

    def areaCalc(self):                         #Calculates area. You can just put it __init__ but it's more organized this way imo
        self._area = self.length ** 2

    def area(self):                             #Since Shape already has area method, this one can be removed without an issue - but task requires they both have it so uh
        print(f"Area of square: {self._area}")

# EXAMPLE:

shape = Shape()
shape.area()                                    #As of default, prints: Area of shape: 0

square = Square(5)
square.area()                                   #Prints: Area of square: 25