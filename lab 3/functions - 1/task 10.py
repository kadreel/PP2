def unique_elements(input_list):
    unique_list = []                            #empty list
    for item in input_list:
        if item not in unique_list:             #adds only unique items
            unique_list.append(item)
    return unique_list                          #gives us that unique list back, duh

list1 = [1, 2, 3, 2, 4, 5, 1]                   #repeats 1, 2
list2 = ['apple', 'banana', 'apple', 'cherry']  #repeats 'apple'
list3 = [7, 8, 9, 8, 7, 10]

print(unique_elements(list1))                   #Outputs [1, 2, 3, 4, 5]
print(unique_elements(list2))                   #Outputs ['apple', 'banana', 'cherry']
print(unique_elements(list3))                   #Outputs [7, 8, 9, 10]