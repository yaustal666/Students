#Question Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program:
# Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT



def upp(a : str) -> str:
    y = []
    for i in a.split():
        s = i.upper()
        y.append(s)
    return ' '.join(y) 

print(upp("Hello world Practice makes perfect"))