# Import
import sqlite3



def initiate_db():
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
  ''')

  connection.commit()
  connection.close()



def get_all_products():
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  cursor.execute('SELECT * FROM Products')
  products = cursor.fetchall()

  cursor.close()
  connection.close()

  return products



def insert_products():
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  products = [
    ('Продукт 1', 'Описание 1', 100),
    ('Продукт 2', 'Описание 2', 200),
    ('Продукт 3', 'Описание 3', 300),
    ('Продукт 4', 'Описание 4', 400)
  ]

  cursor.executemany('INSERT OR IGNORE INTO Products(title, description, price) VALUES(?, ?, ?)', products)

  connection.commit()
  connection.close()

if __name__ = '__main__'
  insert_products()
  initiate_db()
