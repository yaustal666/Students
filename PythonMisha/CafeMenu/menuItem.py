class MenuItem:
    category_list = ['soup', 'drink']

    def __init__(self, name: str, description: str, price: float, category: str):
        if not name:
            raise ValueError("Name must bot be empty")
        if not description:
            raise ValueError('Description must not be empty')
        if price <= 0:
            raise ValueError('Price must be greater than 0')
        if not category in MenuItem.category_list:
            raise ValueError('Product must be in the existing category')

        self.name = name
        self.description = description
        self.price = price
        self.category = category
