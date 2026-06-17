import sqlite3
from database import initialize_database

initialize_database()

def add_user(email, password):
    conn = sqlite3.connect("email_system.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (email, password) VALUES (?, ?)",
            (email, password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(email, password):
    conn = sqlite3.connect("email_system.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email=? AND password=?",
        (email, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user is not None

# Test
email = input("Enter Email: ")
password = input("Enter Password: ")

if add_user(email, password):
    print("User Registered Successfully")
else:
    print("User Already Exists")