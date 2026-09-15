import sqlite3
from menuItem import MenuItem

class MenuItemDao:
    def __init__(self, database: sqlite3.Connection):
        self.database = database
        self.cursor = database.cursor()

    def add_item(self, menuItem: MenuItem):
        self.cursor.execute(
            """
            INSERT into menu (name, description, price, category)
            VALUES (?, ?, ?, ?)
            """,
            (menuItem.name, menuItem.description, menuItem.price, menuItem.category)
        )

        self.database.commit()