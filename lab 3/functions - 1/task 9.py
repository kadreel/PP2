import math                                     #needed for pi

def lol(R):
    return (math.pi * 4 * (R ** 3)) / 3         #formula

radius = int(input())                           #input is, say, 5
print(lol(radius))                              #with input 5, the output is 523.5987755982989