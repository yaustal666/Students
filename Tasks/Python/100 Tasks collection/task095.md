### Question 95 | Level 1

### EN
***
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

<br><br>

### RU
***
Определите класс Person и его два дочерних класса: Male и Female. Все классы имеют метод "getGender", который может выводить "Male" для класса Male и "Female" для класса Female.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())
```

</details>

