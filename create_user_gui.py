from tkinter import Entry, Label, Button
import database_operations as db_ops

def create_username():
  #retrieve entered data for the new user
  new_user = create_username_entry.get()
  new_password = create_password_entry.get()
  name = create_name_entry.get()
  lname = create_lname_entry.get()
  #create the new user in the db
  db_ops.create_user(new_user, new_password, name, lname)

def in_create_user_gui(root):   #create the gui for creating a new user
  global create_username_entry, create_password_entry, create_name_entry, create_lname_entry

  create_username_label = Label(root, text="Create Username:")
  create_username_label.grid(row=3, column=0)

  create_username_entry = Entry(root)
  create_username_entry.grid(row=3, column=1)

  create_password_label = Label(root, text="Create Password:")
  create_password_label.grid(row=4, column=0)

  create_password_entry = Entry(root)
  create_password_entry.grid(row=4, column=1)

  create_name_label = Label(root, text="First Name:")
  create_name_label.grid(row= 5, column=0)

  create_name_entry = Entry(root)
  create_name_entry.grid(row=5, column=1)

  create_lname_label = Label(root, text="Last Name:")
  create_lname_label.grid(row=6, column=0)

  create_lname_entry = Entry(root)
  create_lname_entry.grid(row=6, column=1)

  create_username_button = Button(root, text="Create", command=create_username)
  create_username_button.grid(row=7, column=0, columnspan=2)
