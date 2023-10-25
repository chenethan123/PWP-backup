from tkinter import Entry, Label, Button
import database_operations as db_ops
from post_login_gui import in_post_login_gui

def login():
  #retrieve entered username and password
  user = username_entry.get()
  pwd = password_entry.get()
  first_name = db_ops.login(user, pwd) #check credentials and login
  if first_name:
    in_post_login_gui(first_name)

def in_login_gui(root):
  global username_entry, password_entry
  #setting up the username label and entry
  username_label = Label(root, text="Username:")
  username_label.grid(row=0, column=0)

  username_entry = Entry(root)
  username_entry.grid(row=0, column=1)
  #setting up the password label and entry
  password_label = Label(root, text="Password:")
  password_label.grid(row=1, column=0)

  password_entry = Entry(root, show='*')
  password_entry.grid(row=1, column=1)
  #setting up the login button
  login_button = Button(root, text="Login", command=login)
  login_button.grid(row=2, column=0, columnspan=2)
