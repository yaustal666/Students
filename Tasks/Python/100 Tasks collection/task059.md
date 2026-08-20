### Question 59 | Level 1

### EN
***
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

<br><br>

### RU
***
Предполагая, что у нас есть некоторые email-адреса в формате "username@companyname.com", напишите программу для вывода названия компании из заданного email-адреса. И имена пользователей, и названия компаний состоят только из букв.

Пример:
Если на вход программе подается следующий email-адрес:

john@google.com

Тогда вывод программы должен быть:

google

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2, emailAddress)
print(r2.group(2))
```

</details>

