from fastapi import FastAPI, status
from MenuItem import MenuItem
from MenuService import MenuManager
import sqlite3

database = sqlite3.connect('database.db')
menuManager = MenuManager(database)

app = FastAPI()

@app.get("/items")
def get_menu():
    return menuManager.get_items()

@app.get("/items/{id}")
def get_menu_item(id: int):
    return menuManager.get_item_by_id(id)

@app.post('/items')
def add_menu(item: MenuItem):
    menuManager.add_item(item)

@app.patch("items/{id}")
def update_item(id: int, item: MenuItem):
    menuManager.update_item(item)

@app.delete('/items/{id}')
def delete_menu(id: int):
    menuManager.delete_item(id)