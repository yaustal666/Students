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
    
    def delete_item(self, id_item: int):
        self.cursor.execute(
            """
            DELETE from menu
            WHERE id = ?
            """,
            (id_item,)
        )
        
        self.database.commit()
    
    def update_item(self, id_item, object_to_insert):
        self.cursor.execute(
            
            """
            UPDATE menu
            SET name = ?, description =?, price = ?, category = ?
            WHERE id = ?
            """,
            (object_to_insert.name, object_to_insert.description, object_to_insert.price, object_to_insert.category, id_item)
        )
        self.database.commit()
    
    def get_item_id(self, id_item):
        self.cursor.execute(
            """
            SELECT name, description, price, category
            FROM menu
            WHERE id = ?
            """,
            (id_item ,)
        )
        store = self.cursor.fetchone()
        return store