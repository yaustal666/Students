# Словарь наизнанку
# Дан словарь, нужно создать новый словарь в котором все будет наоборот
# Значения станут ключами, а ключи значениями

d = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six"
}

def reversed(dic : dict) -> dict:
    reverse_d = {}
    for i in range(1, len(dic) + 1): #range(1, len(dic)) used instead of current,forgot +1 to len 
        reverse_d[dic[i]] = i #  reverse_d[dic[1]] = dic[0] i had had before upon GEMINI explanation fixed it 
    return reverse_d
print(reversed(d))

#--------------- Все супер *_*