### Question 10 | Level 2

### EN
***
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

<br><br>

### RU
***
Напишите программу, которая принимает последовательность слов, разделенных пробелами, в качестве входных данных и выводит слова после удаления всех дубликатов и сортировки в алфавитно-цифровом порядке.
Предположим, что на вход программе подается:
hello world and practice makes perfect and hello world again
Тогда вывод должен быть:
again and hello makes perfect practice world

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
s = input()
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))
```

</details>

