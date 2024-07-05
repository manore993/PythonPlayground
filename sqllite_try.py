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

create_table()

register("fulu", "fulu@gmail.com", "fulu45")

print_table()
