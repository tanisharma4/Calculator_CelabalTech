import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

# Creating the main window
window = tk.Tk()
window.title('Calculator')

# Creating a frame within the window with purple background
frame = tk.Frame(master=window, bg="#7e57c2", padx=10, pady=10)
frame.pack()

# Creating an entry widget for displaying and entering numbers
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30, font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=4, ipady=8, pady=5)

# Function to append clicked number or operator to the entry widget
def add_to_display(value):
    current_value = entry.get()
    if current_value == 'Error':
        entry.delete(0, tk.END)
    entry.insert(tk.END, value)

# Function to evaluate the expression in the entry widget
def calculate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')
        print(f"Error: {e}")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to bind keyboard keys to calculator buttons
def key_press(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '.', '%']:
        add_to_display(key)
    elif key == '\r':
        calculate()
    elif key == '\x08':
        clear()

# Bind keyboard keys to the calculator functions
window.bind('<Key>', key_press)

# Creating number buttons using lambda functions to pass arguments
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('/', 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(master=frame, text=text, padx=15, pady=10, width=3, font=('Arial', 12),
                       bg="#9c27b0", fg="white", command=lambda text=text: add_to_display(text))
    button.grid(row=row, column=column, pady=3)

# Creating clear and equal buttons with purple background
button_clear = tk.Button(master=frame, text="Clear", padx=15, pady=10, width=12, font=('Arial', 12),
                         bg="#9c27b0", fg="white", command=clear)
button_clear.grid(row=5, column=0, columnspan=2, pady=3)
button_equal = tk.Button(master=frame, text="=", padx=15, pady=10, width=9, font=('Arial', 12),
                         bg="#9c27b0", fg="white", command=calculate)
button_equal.grid(row=5, column=2, columnspan=2, pady=3)

# Starts the main event loop
window.mainloop()
