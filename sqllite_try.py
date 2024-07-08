import sqlite3 as sql
# database name
dbname = "database.db"
# # Secret for session management
# SECRET_KEY = "SECRET_KEY"

def create_table():
    """This function will create users table in database if it does not exists"""
    query = """CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Email TEXT NOT NULL UNIQUE,
                PASSWORD TEXT NOT NULL
            )"""
    
    conn = sql.connect(dbname)
    try:
        conn.execute
    except:
         pass 
    conn.close()

    with sql.connect(dbname) as conn:
        conn.execute(query)
        

def register(name, email, password):
        """Register user or return None if fails"""
        query = "INSERT INTO Users(Name, Email, Password) VALUES(?, ?, ?)"
        
        with sql.connect(dbname) as conn:
            cur = conn.cursor()
            cur.execute(
                query,
                (
                    name,
                    email,
                    password,
                ),
            )
            conn.commit()
        
def print_table():
    conn = sql.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Users")
    conn.commit()
    print (cur.fetchall())

def login(email, password):
        """Login user function or return None if fails"""
        query = "SELECT ID, Name FROM Users WHERE Email=? AND Password=?"
        print(email)
        print(password)
        with sql.connect(dbname) as conn:
            cur = conn.cursor()
            cur.execute(
                query,
                (
                    email,
                    password,
                ),
            )
            rows = list(cur.fetchall())
            print(len(rows))
            if len(rows) == 1:
                print(rows[0])
                return rows[0]
            else:
                return None

def clear():
    """This function will remove all records"""
    query = "DELETE FROM Users"
    
    with sql.connect(dbname) as conn:
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        
create_table()

register("fulu", "fulu@gmail.com", "fulu45")

print_table()

print (login("tulu@gmail.com", "tulu45"))

clear()
print_table()