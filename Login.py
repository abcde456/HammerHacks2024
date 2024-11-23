import json
import tkinter as tk
from tkinter import messagebox

# File to store user credentials
CREDENTIALS_FILE = "users.json"

# Load or create the credentials file
def load_credentials():
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # If the file doesn't exist, return an empty dictionary

def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file)

# Register a new user
def register_user(email, password):
    credentials = load_credentials()
    if email in credentials:
        messagebox.showerror("Error", "Email already exists. Please use a different email.")
    else:
        credentials[email] = password  # Save plain text password (not recommended for real apps)
        save_credentials(credentials)
        messagebox.showinfo("Success", "Registration successful!")

# Verify user login
def verify_user_login(email, password):
    credentials = load_credentials()
    if credentials.get(email) == password:
        messagebox.showinfo("Welcome", f"Welcome back, {email}!")
    else:
        messagebox.showerror("Error", "Invalid email or password.")

# Functionality for login button
def login_action():
    email = email_var.get()
    password = password_var.get()
    if email and password:
        verify_user_login(email, password)
    else:
        messagebox.showerror("Error", "Please enter both email and password.")

# Functionality for register button
def register_action():
    email = email_var.get()
    password = password_var.get()
    if email and password:
        register_user(email, password)
    else:
        messagebox.showerror("Error", "Please enter both email and password.")

# Tkinter setup
app = tk.Tk()
app.title("SchoolMaster Login")
app.geometry("400x500")

# Display the image using PhotoImage with resizing
try:
    img = tk.PhotoImage(file="SchoolMaster.png")
    img = img.subsample(2, 2)  # Reduce the image size by a factor of 2 (adjust as needed)
    img_label = tk.Label(app, image=img)
    img_label.pack(pady=10)
except tk.TclError:
    messagebox.showwarning("Warning", "Image file 'SchoolMaster.png' not found or unsupported format.")

# Add labels and entry fields
email_var = tk.StringVar()
password_var = tk.StringVar()

tk.Label(app, text="Email:", font=("Arial", 14)).pack(pady=(10, 5))
email_entry = tk.Entry(app, textvariable=email_var, width=30, font=("Arial", 12))
email_entry.pack(pady=5)

tk.Label(app, text="Password:", font=("Arial", 14)).pack(pady=(10, 5))
password_entry = tk.Entry(app, textvariable=password_var, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Add buttons
tk.Button(app, text="Login", command=login_action, font=("Arial", 14), bg="blue", fg="white").pack(pady=10)
tk.Button(app, text="Register", command=register_action, font=("Arial", 14), bg="green", fg="white").pack(pady=10)

# Run the application
app.mainloop()
