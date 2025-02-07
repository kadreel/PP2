def Bond(namesBond):
    success = 0
    for i in range(len(namesBond)):
        if namesBond[i] == 0 and success < 2:                       #finds the first 2 zeroes for "00x"
            success += 1
        elif namesBond[i] == 7:                                     #checks for the last element 7
            if success == 2:                                        #if it's the third in order, it passes the tests
                return True
            else:                                                   #if it appears too early, the success resets and stuff like "0707" doesnt pass the test
                success = 0
    return False

seq1 = [1,2,4,0,0,7,5]      #expected true, "007" works
seq2 = [1,0,2,4,0,5,7]      #expected true, "0--0-7" works
seq3 = [1,7,2,0,4,5,0]      #expected false, "7-0--0" is in incorrect order
seq4 = [0,7,0,7,0,7,0]      #expected false, "0707070" keeps resetting stuff and isnt strictly in sequence of "007"

print(Bond(seq1))           #Outputs True
print(Bond(seq2))           #Outputs True
print(Bond(seq3))           #Outputs False
print(Bond(seq4))           #Outputs False