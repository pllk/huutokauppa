import db

def add_item(title, description, start_price, user_id):
    sql = """INSERT INTO items (title, description, start_price, user_id)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, description, start_price, user_id])
