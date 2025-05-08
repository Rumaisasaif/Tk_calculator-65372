import tkinter as tk
import math

# Function to perform basic arithmetic operations
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result.set(num1 + num2)
        elif operation == "subtract":
            result.set(num1 - num2)
        elif operation == "multiply":
            result.set(num1 * num2)
        elif operation == "divide":
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Divide by 0")
    except ValueError:
        result.set("Invalid input")

def square():
    try:
        num = float(entry1.get())
        result.set(num ** 2)
    except ValueError:
        result.set("Invalid input")

def square_root():
    try:
        num = float(entry1.get())
        if num >= 0:
            result.set(math.sqrt(num))
        else:
            result.set("Error: Negative input")
    except ValueError:
        result.set("Invalid input")

# ----- GUI Setup -----
root = tk.Tk()
root.title("🧮 Simple GUI Calculator")
root.geometry("400x400")
root.configure(bg="#1e1e2f")  # Dark background

# Styles
label_style = {"bg": "#1e1e2f", "fg": "white", "font": ("Segoe UI", 11)}
entry_style = {"font": ("Segoe UI", 11), "bg": "#2e2e3f", "fg": "white", "insertbackground": "white"}
button_style = {"bg": "#007acc", "fg": "white", "font": ("Segoe UI", 10, "bold"), "width": 15, "relief": "flat", "padx": 5, "pady": 5}

# Title
tk.Label(root, text="Simple Calculator", font=("Segoe UI", 16, "bold"), fg="#00ffff", bg="#1e1e2f").pack(pady=15)

# Entry Fields
tk.Label(root, text="Enter first number:", **label_style).pack()
entry1 = tk.Entry(root, **entry_style)
entry1.pack(pady=5)

tk.Label(root, text="Enter second number:", **label_style).pack()
entry2 = tk.Entry(root, **entry_style)
entry2.pack(pady=5)

# Result Field
tk.Label(root, text="Result:", **label_style).pack(pady=(10, 0))
result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, font=("Segoe UI", 14, "bold"),
                        bg="#202030", fg="#00ffcc", state="readonly", relief="flat",
                        justify="center", readonlybackground="#202030", bd=2,
                        highlightthickness=1, highlightbackground="#00ffcc")
result_entry.pack(ipady=10, padx=30, pady=5, fill="x")

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Add", command=lambda: calculate("add"), **button_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Subtract", command=lambda: calculate("subtract"), **button_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Multiply", command=lambda: calculate("multiply"), **button_style).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Divide", command=lambda: calculate("divide"), **button_style).grid(row=1, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Square", command=square, **button_style).grid(row=2, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Square Root", command=square_root, **button_style).grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
