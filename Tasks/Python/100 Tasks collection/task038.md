### Question 18 | Level 3

### EN
***
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of transaction password: 6
6. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1

<br><br>

### RU
***
Веб-сайт требует от пользователей вводить имя пользователя и пароль для регистрации. Напишите программу для проверки валидности пароля, введенного пользователями.
Ниже приведены критерии проверки пароля:
1. Как минимум 1 буква в диапазоне [a-z]
2. Как минимум 1 цифра в диапазоне [0-9]
3. Как минимум 1 буква в диапазоне [A-Z]
4. Как минимум 1 символ из [$#@]
5. Минимальная длина пароля: 6
6. Максимальная длина пароля: 12
Ваша программа должна принимать последовательность паролей, разделенных запятыми, и проверять их по указанным выше критериям. Пароли, соответствующие критериям, должны быть выведены, каждый разделен запятой.
Пример
Если на вход программе поданы следующие пароли:
ABd1234@1,a F1#,2w3E*,2We3345
Тогда вывод программы должен быть:
ABd1234@1

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))
```

</details>

