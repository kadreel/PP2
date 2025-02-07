def poormansmorse(peacekeeper):
    for i in range(len(peacekeeper)):
        for z in range(peacekeeper[i]):
            print("*", end="")
        print()

escalation = [4,9,5]
poormansmorse(escalation)