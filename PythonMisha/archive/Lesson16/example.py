class Character:
    def __init__(self, name: str, age: int, hp: int, stamina: int):
        self.name = name
        self.age = age
        self.hp = hp
        self.stamina = stamina

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        
class InventorySlot:
    def __init__(self, item: Item, amount: int):
        self.item = item
        self.amount = amount

class Inventory:
    def __init__(self, items: list[InventorySlot] = []):
        self.items = items

    def add_item(self, item: Item, amount: int = 1):
        slot = InventorySlot(item, amount)
        self.items.append(slot)

    def __str__(self):
        res = []
        for slot in self.items:
            res.append(slot.item.name + " " + str(slot.amount))
        return "\n".join(res)

apple = Item("apple", 10)
stick = Item("stick", 10)
inv = Inventory()
inv.add_item(apple, 2)
inv.add_item(stick, 125)
print(inv)