class Shape:
    def __init__(self):
        self._area = 0                          #Creates _area and defaults it to 0
    
    def area(self):                             #Outputs area
        print(f"Area of shape: {self._area}")

class Rectangle(Shape):
    def __init__(self, length, width):          #Gets length and width, calls for calculation
        super().__init__()                      #Call the init method of the parent class (Shape) to create variable _area with default of 0
        self.length = length
        self.width = width
        self.areaCalc()

    def areaCalc(self):                         #Calculates area
        self._area = self.length * self.width

# EXAMPLE:

shape = Shape()
shape.area()                                    #As of default, it still prints: Area of shape: 0

receran = Rectangle(5, 2)                       #Creates rectangle with dimensions of 5 and 2
receran.area()                                  #As of non-default, it prints: Area of shape: 10