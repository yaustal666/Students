a = input()

digit = 0
letter = 0
for i in a:
    if i.isalpha() == True:
        letter += 1
    if i.isdigit() == True:
        digit += 1

print('DIGIT: ', digit, 'LETTER: ', letter)
print(f"DIGIT {digit} LETTER {letter}")