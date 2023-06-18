import sqlite3

def database():
    connection = sqlite3.connect("Property_Management.db")
    connection_cursor = connection.cursor()

    #query 1: creating owner table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS owner(owner_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone_no INTEGER NOT NULL, aadhaar_no INTEGER NOT NULL UNIQUE, address TEXT, city TEXT, state TEXT, pincode INTEGER)")
    connection.commit()

    #query 2: creating property table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS property(property_id INTEGER PRIMARY KEY AUTOINCREMENT,owner_id INTEGER , bhk INTEGER NOT NULL, washrooms INTEGER NOT NULL, status TEXT NOT NULL, Address TEXT, city TEXT, state TEXT, pincode INTEGER, other_details TEXT,foreign key(owner_id) references owner(owner_id))")
    connection.commit()

    #query 3: creating tenant table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS tenant(tenant_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone_no INTEGER NOT NULL, aadhaar_no INTEGER NOT NULL UNIQUE, email TEXT)")
    connection.commit()

    #query 4: creating lease table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS lease(lease_id INTEGER PRIMARY KEY AUTOINCREMENT, owner_id INTEGER NOT NULL, property_id INTEGER NOT NULL, tenant_id INTEGER NOT NULL, start_date TEXT, end_date TEXT, security INTEGER, lease_amount INTEGER, rent_amount INTEGER, due_date TEXT)")
    connection.commit() 

    #query 5: creating owner table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS vendor(vendor_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, phone_no INTEGER NOT NULL, work TEXT NOT NULL , address TEXT, email TEXT)")
    connection.commit()

    #query 6: creating lease table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS request(request_id INTEGER PRIMARY KEY AUTOINCREMENT, vendor_id INTEGER NOT NULL, property_id INTEGER NOT NULL, tenant_id INTEGER NOT NULL, description TEXT, status TEXT, required_date TEXT, amount INTEGER, payment_status TEXT)")
    connection.commit()

    #query 7: creating payment table
    connection_cursor.execute("CREATE TABLE IF NOT EXISTS payment(payment_id INTEGER PRIMARY KEY AUTOINCREMENT, owner_id INTEGER NOT NULL, request_id INTEGER NOT NULL, tenant_id INTEGER NOT NULL, payment_date TEXT)")
    connection.commit()

database()