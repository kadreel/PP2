def converdainhof(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    return celcius

fahr = float(input())
print(converdainhof(fahr))      #if input is 212F, then output is 100C