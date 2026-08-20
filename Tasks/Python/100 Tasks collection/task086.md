### Question 86 | Level 1

### EN
***
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

<br><br>

### RU
***
Пожалуйста, напишите программу для генерации всех предложений, где подлежащее находится в ["I", "You"], глагол в ["Play", "Love"], а объект в ["Hockey","Football"].

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
```

</details>

