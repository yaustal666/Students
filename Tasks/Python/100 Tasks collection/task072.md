### Question 72 | Level 1

### EN
***
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

<br><br>

### RU
***
Пожалуйста, напишите функцию бинарного поиска, которая ищет элемент в отсортированном списке. Функция должна возвращать индекс искомого элемента в списке.

<br><br>

<details>
<summary>Solution/Решение</summary>

```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

</details>

