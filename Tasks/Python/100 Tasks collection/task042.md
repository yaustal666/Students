### Question 25 | Level 1

### EN
***
Define a class, which have a class parameter and have a same instance parameter.

<br><br>

### RU
***
Определите класс, который имеет параметр класса и такой же параметр экземпляра.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))
```

</details>

