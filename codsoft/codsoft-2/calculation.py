import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid input!")

root = tk.Tk()
root.title("Simple Calculator")

entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

operation_var = tk.StringVar()
operation_choices = ['+', '-', '*', '/']
operation_dropdown = tk.OptionMenu(root, operation_var, *operation_choices)
operation_dropdown.pack(pady=5)

entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
