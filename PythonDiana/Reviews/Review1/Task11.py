# Все ок

j = input()    #11 question
count = 0
for letter in j:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        count += 1
print(count)

# Эту же проверку можно сделать следующим образом
# if letter in ['a', 'o', 'u', 'i', 'e']
