# Шифр Цезаря
# Дана строка, каждая буква должна замениться на следующую по алфавиту

def nextLetter(letter: str) -> str:
    if letter == 'z':
        return 'a'
    return chr(ord(letter) + 1)

# "a" + ("z" - "a" + 1) % 26

def ceaser(text: str) -> str:
    result = ""

    for letter in text:
        result += nextLetter(letter)
    return result
