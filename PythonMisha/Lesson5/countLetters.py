# You are given some text
# calculate and show text analitics - amount of each letter in a text
message = input()

letters = {}

for i in message:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1

print(letters)