# Напиши функцию, которая сравнивает два списка
# Два списка равны если все элементы списков равны
# Вообще можно сделать просто вот так list1 == list2
# Операция сравнения для списков сравнивает их по значениям
# Но мы не будем этим пользоваться в этом задании

def comparelists( list1: list, list2: list) -> bool:
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False 

    return True 
