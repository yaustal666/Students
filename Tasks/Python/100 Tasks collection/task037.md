### Question 17 | Level 2

### EN
***
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500

<br><br>

### RU
***
Напишите программу, которая вычисляет итоговую сумму на банковском счете на основе журнала транзакций из консольного ввода. Формат журнала транзакций показан ниже:
D 100
W 200

D означает депозит (пополнение), а W означает снятие (вывод).
Предположим, что на вход программе подается:
D 300
D 300
W 200
D 100
Тогда вывод должен быть:
500

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)
```

</details>

