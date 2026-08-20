### Question 24 | Level 1

### EN
***
Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

And add document for your own function

<br><br>

### RU
***
В Python есть много встроенных функций, и если вы не знаете, как их использовать, вы можете прочитать документацию онлайн или найти книги. Но Python имеет встроенную функцию документации для каждой встроенной функции.

Пожалуйста, напишите программу, которая выводит документацию для некоторых встроенных функций Python, таких как abs(), int(), raw_input()

И добавьте документацию для своей собственной функции

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)
```

</details>