### Question 19 | Level 3

### EN
***
You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

<br><br>

### RU
***
Вам требуется написать программу для сортировки кортежей (имя, возраст, рост) в порядке возрастания, где имя — строка, возраст и рост — числа. Кортежи вводятся через консоль. Критерии сортировки:
1: Сортировка по имени;
2: Затем сортировка по возрасту;
3: Затем сортировка по росту.
Приоритет: имя > возраст > рост.
Если на вход программе поданы следующие кортежи:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Тогда вывод программы должен быть:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))

print(sorted(l, key=itemgetter(0,1,2)))
```

</details>

