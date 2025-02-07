def solve(numheads, numlegs):
    rabbies = numheads                                                              #Starts with 0 chickens and numheads (35) rabbits to clear
    chicks = 0
    for i in range(numheads):
        chicks += 1
        rabbies -= 1
        if (chicks * 2 + rabbies * 4 == numlegs and chicks + rabbies == numheads):  #If number of legs and heads matches the correct values, outputs results                           
            print(f"There are {chicks} chickens and {rabbies} rabbits")

solve(35,94)                                                                        #Output: There are 23 chickens and 12 rabbits