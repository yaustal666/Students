# Шифр Цезаря
# Дана строка, каждая буква должна замениться на следующую по алфавиту

def nextLetter(letter: str) -> str:
    if letter == 'z':
        return 'a'
    return chr(ord(letter) + 1) 

def cypher(text: str) -> str:
    result = ""          #texts are immutable
    for i in range(len(text)):
        result += nextLetter(text[i])
    return result

print(cypher("hello world"))