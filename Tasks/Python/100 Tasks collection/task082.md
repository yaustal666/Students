### Question 82 | Level 1

### EN
***
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

<br><br>

### RU
***
Пожалуйста, напишите программу для сжатия и распаковки строки "hello world!hello world!hello world!hello world!".

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
```

</details>

