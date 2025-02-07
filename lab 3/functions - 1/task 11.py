def panama(word):
    word = ''.join(e for e in word if e.isalnum()).lower()              #Necessary for the phrases, but solo words work without it
    return word == word[::-1]                                           #reverses and checks if true

print(panama("madam"))                                                  #Should be True, is true
print(panama("mademoiselle"))                                           #Should be False, is false
print(panama("I am at madam Tamai"))                                    #Should be True, is true