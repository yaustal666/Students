# Сокращение словаря
# Дан словарь с набором пар ключ-значение
# Необходимо изменить его следующим образом

# {1: "one", 2: "two", 3: "three"} -> {6: ["one", "two", "three"]}

# То есть нужно суммировать ключи, а все значения преобразовать в список
# Можно создать новый словарь, а можно попробовать обработать уже существующий

d = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}

def summation(dic : dict):
    typed_nums = []
    total = 0 
    for i in dic: # Gemini assist in 'in dic logic' instead of range 
        total += i
    for j in range(1, len(dic) + 1): # got 0 error and then undestood by experiecne that there is no 0 key.WOnder how else i could fix it without a "crutch"
        typed_nums.append(dic[j]) 
    return total, typed_nums
print(summation(d))

#--------------- Все супер *_*
            