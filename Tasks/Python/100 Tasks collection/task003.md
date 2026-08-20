### Question 22 | Level 3

### EN
***
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

<br><br>

### RU
***
Напишите программу для подсчета частоты слов во входном тексте. Вывод должен быть отсортирован по ключам в алфавитно-цифровом порядке.
Предположим, что на вход программе подается:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Тогда вывод должен быть:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print("%s:%d" % (w,freq[w]))
```

</details>

