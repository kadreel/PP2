#exists solely for task 14

def palindr(word):
    word = ''.join(e for e in word if e.isalnum()).lower()              #Necessary for the phrases, but solo words work without it
    return word == word[::-1]                                           #reverses and checks if true