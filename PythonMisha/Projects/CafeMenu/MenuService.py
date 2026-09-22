from MenuItem import MenuItem
from MenuItemDao import MenuItemDao
import sqlite3

class MenuManager:
    def __init__(self, database: sqlite3.Connection):
        self.menuItemDao = MenuItemDao(database)

    def add_item(self, name, description, price, category):
        dish = MenuItem(name, description, price, category)
        self.menuItemDao.add_item(dish)

    def delete_item(self, item_to_delete : int):
        self.menuItemDao.delete_item(item_to_delete)
    
    def update_item(self, item_to_change: int):
        self.menuItemDao.update_item(item_to_change)

    def get_item_by_id(self, item_name):
        self.menuItemDao.get_item_id(item_name)