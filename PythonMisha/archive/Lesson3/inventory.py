inventory = [
    ["Apple", 3],
    ["Stick", 15],
    ["Tomato", 5],
    ["Sword", 1],
    ["Wood", 38],
]

# Нас просят добавить в инвентарь
# 1 - проверяем есть ли в инвентаре хотя бы 1 такой предмет
# 2 - если есть, то просто прибавляем к счетчику
# 3 - если нет, то добавляем новый с заданным значением

def addItem(itemName: str, amount: int):
    for i in inventory:
        if i[0] == itemName:
            i[1] += amount
            return
            
    inventory.append([itemName, amount])
  
            
addItem("Shield", 10)

for i in inventory:
    print(*i)