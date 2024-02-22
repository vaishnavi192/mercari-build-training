import hashlib
import os
import logging
import pathlib
import sqlite3
from click import File
from fastapi import FastAPI, Form, Query, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
db = "mercari.sqlite3"
logger = logging.getLogger("uvicorn")
logger.level = logging.INFO
images = pathlib.Path(__file__).parent.resolve() / "images"
db = pathlib.Path(__file__).parent.parent.resolve() / "db"
origins = [os.environ.get("FRONT_URL", "http://localhost:3000")]
app.add_middleware(
    CORSMiddleware,
    with open(file_path, "r") as file:
        items_data = json.load(file)

    logger.info(f"Receive items: {items_data}")
    return select_join_items())



@app.post("/items")
async def create_item(item: dict):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('''INSERT INTO items (name, category, image_name) VALUES (?, ?, ?)''', (item['name'], item['category'], item['image_name']))
    conn.commit()
    conn.close()
    return {"message": "item created"}

@app.get("/search")
async def get_search_items(keyword: str = Query(...)):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + keyword + '%',))
    items = cur.fetchall()
    conn.close()
    return items
@app.post("/items")
async def add_item(name: str = Form(...), category: str = Form(...), image: UploadFile = File(...)):
    image_filename = await store_image(image)

    new_item = {"name": name, "category": category, "image_name": image_filename}
    add_item_to_json(new_item)

    logger.info(f"Receive item: {name}, {category}, {image_filename}")
    return {"message": f"item received: {name}, {category}, {image_filename}"}

    return FileResponse(image)

@app.get("/search")
def get_search_items(keyword: str = Query(...)):
    return search_items(keyword)
async def store_image(image):
    image_bytes = await image.read()
    image_hash = hashlib.sha256(image_bytes).hexdigest()
    image_filename = f"{image_hash}.jpg"

    with open(images / image_filename, "wb") as image_file:
        image_file.write(image_bytes)

    logger.info(f"Receive name: {image_filename}")
    return image_filename


def add_item_to_json(new_item):
    image_file.write(image_bytes)

    logger.info(f"Receive name: {image_filename}")
    return image_filename


def insert_items(new_item):
    conn = sqlite3.connect(db/"items.db")
    cur = conn.cursor()

   
    cur.execute('''CREATE TABLE IF NOT EXISTS items
                (id INTEGER PRIMARY KEY,
                name TEXT,
                category TEXT,
                image_name TEXT)''')

    data = [new_item["name"], new_item["category"], new_item["image_name"]]
    sql = 'INSERT INTO items (name, category, image_name) VALUES (?, ?, ?)'
    cur.execute(sql,data)

    conn.commit()
    conn.close()

def select_items():
    conn = sqlite3.connect(db/"items.db")
    cur = conn.cursor()

    cur.execute('SELECT * FROM items')
    item_list = cur.fetchall()

    conn.close()

    return item_list

def search_items(keyword):
    conn = sqlite3.connect(db/"items.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM items WHERE name LIKE ?", ('%' + keyword + '%',))
    item_list = cur.fetchall()

    conn.close()

    return item_list

def split_tables():
    conn = sqlite3.connect(db/"items.db")
    cur = conn.cursor()

   
    cur.execute('''CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT)''')

    
    cur.execute('''INSERT OR IGNORE INTO categories (name) 
                SELECT DISTINCT category FROM items''')

    
    cur.execute('''CREATE TABLE IF NOT EXISTS new_items (
                id INTEGER PRIMARY KEY,
                name TEXT,
                category_id INTEGER,
                image_name TEXT,
                FOREIGN KEY (category_id) REFERENCES categories (id))''')

   
    cur.execute('''INSERT INTO new_items (id, name, category_id, image_name) 
                SELECT id, name, (SELECT id FROM categories WHERE categories.name = items.category), image_name FROM items''')

   
    cur.execute('''DROP TABLE items''')

    
    cur.execute('''ALTER TABLE new_items RENAME TO items''')

   
    cur.execute('SELECT * from categories')
    categories_list = cur.fetchall()
    logger.info(categories_list)

    
    cur.execute('SELECT * from items')
    items_list = cur.fetchall()
    logger.info(items_list)

    conn.commit()
    conn.close()

def select_join_items():
    conn = sqlite3.connect(db/"items.db")
    cur = conn.cursor()


    cur.execute("SELECT items.id, items.name, categories.name AS category, items.image_name FROM items INNER JOIN categories ON items.category_id = categories.id")
    items_list = cur.fetchall()

    conn.close()

    return items_list

