today_discounts = {
    "Bread": {
        2: 0.2,
        5: 0.5
    },
    "Milk": {
        3: 0.1
    }
}

class ShoppingCart:
    def __init__(self):
        self.products = []

    def addItem(self, name: str, amount: int):
        self.products.append((name, amount))

shopping_cart = ShoppingCart()
shopping_cart.addItem("Bread", 10)

# Необходимо написать функцию рассчета стоимости корзины с учетом скидок
def calculateCart(cart: ShoppingCart, discounts: dict):
    pass

print(calculateCart(shopping_cart, today_discounts))