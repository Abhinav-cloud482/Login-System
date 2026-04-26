import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import hashlib
import os
import uuid

USERS_FILE = 'users.pkl'
MAX_ATTEMPTS = 3

# Load users from file
def load_users():
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'rb') as f:
                return pickle.load(f)
        except:
            return {}
    return {}

# Save users to file
def save_users(users):
    with open(USERS_FILE, 'wb') as f:
        pickle.dump(users, f)

# Hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Generate session token
def generate_token():
    return str(uuid.uuid4())

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.users = load_users()
        self.session_token = None

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.status_label = tk.Label(self.frame, text="Welcome! Please log in or register.")
        self.status_label.grid(row=0, column=0, columnspan=2, pady=10)

        tk.Label(self.frame, text="Username:").grid(row=1, column=0, sticky='e')
        tk.Label(self.frame, text="Password:").grid(row=2, column=0, sticky='e')

        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1)

        self.login_btn = tk.Button(self.frame, text="Login", command=self.login)
        self.login_btn.grid(row=3, column=0, pady=5)
        self.register_btn = tk.Button(self.frame, text="Register", command=self.register)
        self.register_btn.grid(row=3, column=1, pady=5)
        self.reset_btn = tk.Button(self.frame, text="Reset Password", command=self.reset_password)
        self.reset_btn.grid(row=4, column=0, columnspan=2, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = self.users.get(username)

        if not user:
            messagebox.showerror("Error", "User not found.")
            return

        if user.get("locked", False):
            messagebox.showwarning("Account Locked", "Too many failed attempts. Account is locked.")
            return

        hashed = hash_password(password)

        if hashed == user["password"]:
            self.session_token = generate_token()
            self.users[username]["attempts"] = 0
            save_users(self.users)
            messagebox.showinfo("Success", f"Welcome {username}!\nSession Token: {self.session_token}")
        else:
            self.users[username]["attempts"] += 1
            if self.users[username]["attempts"] >= MAX_ATTEMPTS:
                self.users[username]["locked"] = True
                messagebox.showwarning("Account Locked", "Too many failed attempts. Account is now locked.")
            else:
                remaining = MAX_ATTEMPTS - self.users[username]["attempts"]
                messagebox.showerror("Error", f"Incorrect password. {remaining} attempts remaining.")
            save_users(self.users)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users:
            messagebox.showerror("Error", "Username already exists.")
            return
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return

        self.users[username] = {
            "password": hash_password(password),
            "attempts": 0,
            "locked": False
        }
        save_users(self.users)
        messagebox.showinfo("Success", "Registration successful!")

    def reset_password(self):
        username = self.username_entry.get()

        if username not in self.users:
            messagebox.showerror("Error", "Username not found.")
            return

        new_password = simpledialog.askstring("Reset Password", "Enter a new password:", show='*')
        if not new_password or len(new_password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return

        self.users[username]["password"] = hash_password(new_password)
        self.users[username]["attempts"] = 0
        self.users[username]["locked"] = False
        save_users(self.users)
        messagebox.showinfo("Success", "Password has been reset.")

if __name__ == '__main__':
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
