def yoda(inpetta):
    inpetta = inpetta[::-1]                 #Reverses list
    inpetta = ' '.join(inpetta)             #Turns list into string
    print(inpetta)

splitoon = input().split()                  #Gets input while turning it into list
yoda(splitoon)                              #With input of "that is why you fail", the output is "fail you why is that"