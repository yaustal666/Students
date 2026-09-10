from random import choice
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"

word_bank = []

with open("words.txt", "r") as file:
    word = file.readline().strip()
    word_bank.append(word)

guess_word = choice(word_bank)
attempts = len(guess_word)
j = 0
while j < attempts:
    guess = input('Write down the word\n')

    if len(guess) != len(guess_word):
        print(f'the amount of letters must match {len(guess_word)}')
        j -= 1

    if guess == guess_word:
        print("Win!!!")
        exit(0)

    result = ""
    for i, letter in enumerate(guess):
        if letter in guess_word:
            if letter == guess_word[i]:
                result += green + letter
            else:
                result += yellow + letter
        else:
            result += red + letter
    print(result)
    j += 1

print("You lost")