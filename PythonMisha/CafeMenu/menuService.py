from menuItem import MenuItem
from menuItemDao import MenuItemDao
import sqlite3

class MenuManager:
    
    def __init__(self, database: sqlite3.Connection):
        self.menuItemDao = MenuItemDao(database)

    def add_item(self, name, description, price, category):
        dish = MenuItem(name, description, price, category)
        self.menuItemDao.add_item(dish)

    def delete_item():
        pass
    
    def update_item():
        pass

    def get_item_by_id():
        pass

