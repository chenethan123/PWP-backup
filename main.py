import tkinter as tk
from login_gui import in_login_gui
from create_user_gui import in_create_user_gui
import database_operations as db_ops 
import requests

def in_main_gui():
  #set up the database
  db_ops.setup_database()
  #create the main tkinter window
  root = tk.Tk()
  root.title("Login and Create User")

  in_login_gui(root)
  in_create_user_gui(root)
  #start the tkinter main loop to display the window
  root.mainloop()



if __name__ == '__main__':
  in_main_gui()

