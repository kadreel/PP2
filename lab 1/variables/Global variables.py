#For functions, variables outside of functions are global. Inside are not
#Global variables are persistent and work everywhere
#Local only exist within their own function

x = "I AM EVERYWHERE"

def func():
    print(x)

func() #outputs "I AM EVERYWHERE"

#but if we declare variable inside function, it isn't everywhere. Can be averted with global keyword

def secondFunc():
    x = "I AM A FAILURE"
    print(x)
    y = "I AM NEW HERE!"
    global z
    z = "Miguel"

secondFunc() #Outputs "I AM A FAILURE"
print(x) #reverts back and outputs "I AM EVERYWHERE"
#print(y) <- Outputs error since Y does not exist in current scope
print(z) #outputs "Miguel"

def xChanger():
    global x
    x = "NOW, I AM, INDEED, A FAILURE"

xChanger()
print(x) #Outputs "NOW, I AM, INDEED, A FAILURE"