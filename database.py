import sqlite3

con = sqlite3.connect("shop.db")
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname VARCHAR(55) NOT NULL,
    phone_number VARCHAR(31) UNIQUE,
    chat_id BIGINTEGER UNIQUE NOT NULL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(55) NOT NULL,
    description VARCHAR(255),
    file_id VARCHAR(255) UNIQUE,
    price FLOAT,
    chat_id BIGINTEGER NOT NULL
    )""")

def update_product_name(product_id, new_name):
    query = "UPDATE products SET name = %s WHERE id = %s"
    params = (new_name, product_id)
    try:
        cur.execute(query, params)
        con.commit()
        return True
    except Exception as e:
        print(f"Error updating name: {e}")
        return False
    
def update_product_price(product_id, new_price):
    query = "UPDATE products SET price = %s WHERE id = %s"
    params = (new_price, product_id)
    try:
        cur.execute(query, params)
        con.commit()
        return True
    except Exception as e:
        print(f"Error updating price: {e}")
        return False


def update_product_description(product_id, new_description):
    query = "UPDATE products SET description = %s WHERE id = %s"
    params = (new_description, product_id)
    try:
        cur.execute(query, params)
        con.commit()
        return True
    except Exception as e:
        print(f"Error updating description: {e}")
        return False


def update_product_image(product_id, new_image):
    query = "UPDATE products SET image = %s WHERE id = %s"
    params = (new_image, product_id)
    try:
        cur.execute(query, params)
        con.commit()
        return True
    except Exception as e:
        print(f"Error updating image: {e}")
        return False
    

def insert_user(data: dict):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()
	try:
		cur.execute("INSERT INTO users(fullname,phone_number,chat_id) VALUES(?,?,?)"
		            , (data.get("fullname"), data.get("phone_number"), data.get("chat_id")))
		con.commit()
		return True

	except:
		return False

	finally:
		con.close()


def get_user(chat_id):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()

	user = cur.execute("SELECT * FROM users WHERE chat_id=?", (chat_id,)).fetchone()

	return user


def insert_product(data: dict):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()
	try:
		cur.execute("INSERT INTO products(name,description,file_id,price,chat_id) VALUES(?,?,?,?,?)"
		            , (data.get("name"), data.get("description"), data.get("file_id"), data.get("price"),
		               data.get("chat_id")))
		con.commit()
		return True
	except Exception as e:
		print(e)
		return False
	finally:
		con.close()


def get_my_products(chat_id):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()
	products = cur.execute("SELECT * FROM products WHERE chat_id=? LIMIT 5 OFFSET 0", (chat_id,)).fetchall()
	print(products)
	return products

def get_my_product(chat_id, product_id):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()
	product = cur.execute("SELECT * FROM products WHERE chat_id=? AND id=?", (chat_id, product_id)).fetchone()
	return product

def delete_product(product_id):
	con = sqlite3.connect("shop.db")
	cur = con.cursor()
	try:
		cur.execute("DELETE FROM products WHERE id=?", (product_id,))
		con.commit()
		return True
	except:
		return False
	finally:
		con.close()
 