import sqlite3
from tkinter import messagebox

def login(username, password):
  conn = sqlite3.connect('sql.db') #connect to the sqlite3 db
  cur = conn.cursor()

  # Checking credentials
  cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
  row = cur.fetchone()
  conn.close()
  if row:
      messagebox.showinfo("Login Info", "Login Successful!")
      return row[3]  # Return the First_name of the user
  else:
      messagebox.showerror("Login Info", "Login Failed!")
      return False

  conn.close() #close the db connection


def create_user(username, password, first_name, last_name):
  conn = sqlite3.connect('sql.db')
  cur = conn.cursor()

  cur.execute("Insert into users(Username, Password, First_name, Last_name) values(?,?,?,?)", (username, password, first_name, last_name))
  conn.commit()
  conn.close()

  messagebox.showinfo("Creation Info", f"Created user with Username: {username}\nPassword: {password}\nName: {first_name}\nLast Name: {last_name}")


def list_users(): #function for listing all the users
  conn = sqlite3.connect('sql.db')
  cur = conn.cursor()

  cur.execute("SELECT * FROM users")
  for user in cur.fetchall():
    print(user)

  conn.close()


def delete_all_users():  #function to delete all users
  conn = sqlite3.connect('sql.db')
  cur = conn.cursor()

  cur.execute("DELETE FROM users")
  conn.commit()
  conn.close()

def setup_database():  #Function to create a db
  conn = sqlite3.connect('sql.db')
  cur = conn.cursor()

  cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    Password TEXT NOT NULL,
    First_name TEXT,
    Last_name TEXT)''')

  conn.commit()
  conn.close()
