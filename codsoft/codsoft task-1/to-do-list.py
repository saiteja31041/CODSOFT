import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def mark_task_complete():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        messagebox.showinfo("Task Completed", "Task marked as completed.")
    else:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List App")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=30, height=10)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_task_complete)
complete_button.pack()

root.mainloop()
