#Point is a point on the map lol. X and Y represent coordinates of this point
import math

class Point:
    def __init__(self, x, y):                       #Creates defaults for distance calculations and calls for set of initial position
        self.prevY = 0
        self.prevX = 0
        self.set(x, y)
    
    def set(self, x, y):                            #Creates or moves point position
        self.x = x
        self.y = y
    
    def show(self):                                 #Outputs current position
        print(self.x, self.y, sep=", ")

    def move(self, x, y):                           #Memorizes the previous position and calls for movement of the current point to new position
        self.prevX = self.x
        self.prevY = self.y
        self.set(x, y)

    def dist(self):                                 #Calculates distance between old and new points
        print(math.sqrt((self.prevX - self.x)**2 + (self.prevY - self.y)**2))

# EXAMPLE:

treasure = Point(30, 40)
treasure.show()                                     #Output: 30, 40
treasure.dist()
treasure.move(60, 80)
treasure.show()                                     #Output: 60, 80
treasure.dist()                                     #Output: 50.0