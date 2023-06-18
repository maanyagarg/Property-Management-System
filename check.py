import sqlite3

def database():
    connection = sqlite3.connect("Property_Management.db")
    connection_cursor = connection.cursor()

    connection_cursor.execute("CREATE TABLE IF NOT EXISTS admin(admin_id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL, password TEXT)")
    connection.commit()

    connection_cursor.execute("INSERT INTO ADMIN (admin_id, name, email, password) VALUES (?, ?, ?,?)", (
        1001,
        "Manya",
        "dewanmanyagarg@gmail.com",
        12345
    ))
    
    connection_cursor.execute("INSERT INTO ADMIN (admin_id, name, email, password) VALUES (?,?, ?,?)", (
        1002,
        "Manav",
        "manavmittal.don@gmail.com",
        12347
    ))

    #query 1: creating owner table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS owner(owner_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone_no INTEGER NOT NULL, aadhaar_no INTEGER NOT NULL UNIQUE, address TEXT, city TEXT, state TEXT, pincode INTEGER)")
    connection.commit()

    #query 2: creating tenants table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS tenants(tenant_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, aadhaar_no INTEGER NOT NULL UNIQUE, email TEXT, phone_no INTEGER NOT NULL)")
    connection.commit()

    connection_cursor.execute("CREATE TABLE IF NOT EXISTS property(property_id INTEGER PRIMARY KEY AUTOINCREMENT,owner_id INTEGER , bhk INTEGER NOT NULL, washrooms INTEGER NOT NULL, status TEXT NOT NULL, Address TEXT, city TEXT, state TEXT, pincode INTEGER, other_details TEXT)")
    connection.commit()

database()
