import tkinter as tk
import requests

def in_post_login_gui(first_name):
  def move(direction):
    try:
      response = requests.get(f"http://127.0.0.1:5000/navigate/{direction}")
      if response.status_code == 200:
        log_display.insert(tk.END, response.text + "\n")  # Display the response in the log display
      else:
        log_display.insert(tk.END, "Error from the server: " + response.text + "\n")
    except requests.RequestException:
        log_display.insert(tk.END, "API server connection error\n")

  post_login_window = tk.Toplevel()
  post_login_window.title(f"Welcome {first_name}")

  # Display Welcome Message
  welcome_label = tk.Label(post_login_window, text=f"Welcome {first_name}!")
  welcome_label.grid(row=0, column=0, columnspan=2)

  # Direction Buttons Frame
  buttons_frame = tk.Frame(post_login_window)
  buttons_frame.grid(row=1, column=0, pady=20)

  fwd_button = tk.Button(buttons_frame, text="FWD", command=lambda: move("FORWARD"))
  fwd_button.pack(side=tk.TOP)

  bkwd_button = tk.Button(buttons_frame, text="BKWD", command=lambda: move("BACKWARD"))
  bkwd_button.pack(side=tk.TOP)

  left_button = tk.Button(buttons_frame, text="LEFT", command=lambda: move("LEFT"))
  left_button.pack(side=tk.LEFT)

  right_button = tk.Button(buttons_frame, text="RIGHT", command=lambda: move("RIGHT"))
  right_button.pack(side=tk.RIGHT)

  stop_button = tk.Button(buttons_frame, text="STOP", command=lambda: move("STOP"))
  stop_button.pack(side=tk.TOP)

  # Log Display
  log_label = tk.Label(post_login_window, text="Log:")
  log_label.grid(row=1, column=1)

  log_display = tk.Text(post_login_window, height=10, width=30)
  log_display.grid(row=2, column=1, padx=20, pady=10)

  # Video Feed (Placeholder for now)
  video_label = tk.Label(post_login_window, text="Video Feed:")
  video_label.grid(row=3, column=0, columnspan=2)

  video_display = tk.Label(post_login_window, text="Video goes here", bg="black", width=40, height=10)
  video_display.grid(row=4, column=0, columnspan=2, padx=20, pady=10)

  # Blank Field for Later Use
  blank_field = tk.Text(post_login_window, height=5, width=40)
  blank_field.grid(row=5, column=0, columnspan=2, padx=20, pady=10)
