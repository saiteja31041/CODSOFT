import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Invalid length. Please enter a positive integer.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer for the length.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(root, text="")
password_label.pack()

root.mainloop()
