import random   #sixth question and also i have done this qustion with chatgpt

# Ну, не знаю насколько тут помог llm, но все ок
# Правильно использовала continue

count = 0
while True:
    a = random.randint(0, 1000)
    
    # но можно было еще вот так это сделать

    # if not a % 3 == 0:
    #     count += 1

    if a % 3 == 0:
        continue
    count += 1

    if a * a > 100000:
        break

print(count)
