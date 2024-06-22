import sqlite3
from datetime import datetime
connection=sqlite3.connect("kfc.db")
sql=connection.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER,name TEXT, phone_number TEXT,reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS products(PR_id INTEGER PRIMARY KEY AUTOINCREMENT,pr_name TEXT, price REAL,pr_des TEXT,pr_quantity INTEGER, pr_photo TEXT,reg_date DATETIME); ")
sql.execute("CREATE TABLE IF NOT EXISTS cart (user_id INTEGER, pr_id INTEGER, pr_count INTEGER, pr_name TEXT, total_price REAL); ")
connection.commit()

def add_users(user_id,name,phone_number):
    connection=sqlite3.connect("kfc.db")
    sql=connection.cursor()
    sql.execute("INSERT INTO users(user_id, name, phone_number, reg_date) VALUES(?,?,?,?);",(user_id, name, phone_number, datetime.now()))
    connection.commit()
def chek_user(user_id):
    connection=sqlite3.connect("kfc.db")
    sql=connection.cursor()
    checker=sql.execute("SELECT * FROM users WHERE user_id=?;", (user_id,)).fetchone()
    if checker:
        return True
    elif not checker:
        return False
def get_all_users():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_users=sql.execute("SELECT * FROM users;").fetchall()
    return all_users
#pr

def add_products(pr_name, price, pr_des, pr_quantity, pr_photo):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO products (pr_name, price, pr_des, pr_quantity, pr_photo, reg_date)" "VALUES(?,?,?,?,?,?);", (pr_name, price, pr_des, pr_quantity, pr_photo, datetime.now()))
    connection.commit()
def delete_product(pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products WHERE pr_id=?;", (pr_id,))
    connection.commit()
def get_all_products(pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_products = sql.execute("SELECT* FROM products").fetchall()
    return all_products
def get_exact_products(pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    exact_product=sql.execute("SELECT pr_name, price, pr_des, pr_photo FROM products WHERE pr_id=?;", (pr_id,)).fetchone()
    return exact_product
def get_pr_id_name():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_products=sql.execute("SELECT pr_id, pr_name, pr_quantity FROM products;").fetchall()
    actual_product=[(product[0], product[1])for product in all_products if product[2]>0 ]
    return actual_product
def delete_all_products():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("DELETE FROM products;")
    connection.commit()
def change_quantity(pr_id, new_quantity):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("UPDATE products SET pr_quantity=? WHERE pr_id=?;",(new_quantity, pr_id))
    connection.commit()
#cart
def add_to_cart(user_id, pr_id, pr_name, pr_count, pr_price):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    total_price=pr_price * pr_count
    sql.execute("INSERT INTO cart (user_id, pr_id, pr_name, pr_count, total_price) VALUES(?,?,?,?,?);",(user_id, pr_id, pr_name, pr_count, total_price))
    connection.commit()
def delete_axact_pr_from_cart(user_id, pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute('DELETE FROM cart WHERE pr_id=?;', (user_id, pr_id))
    connection.commit()
def delete_exact_user_cart(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute('DELETE FROM cart;')
    connection.commit()
def get_cart_id_name(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    cart_1= sql.execute('SELECT pr_name, pr_id FROM cart;').fetchall()
    return cart_1
