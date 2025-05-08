import tkinter as tk
from tkinter import messagebox

# Function to perform calculations
def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result.set(f"{num1 + num2:.2f}")
        elif operation == "subtract":
            result.set(f"{num1 - num2:.2f}")
        elif operation == "multiply":
            result.set(f"{num1 * num2:.2f}")
        elif operation == "divide":
            if num2 != 0:
                result.set(f"{num1 / num2:.2f}")
            else:
                result.set("❌ Cannot divide by 0")
    except ValueError:
        result.set("⚠️ Invalid input")

# GUI Setup
root = tk.Tk()
root.title("🧮 Professional Calculator")
root.geometry("380x280")
root.configure(bg="#1e1e2f")

# --- Theme Colors and Fonts ---
LABEL_COLOR = "#e0e0e0"
ENTRY_BG = "#2e2e3f"
ENTRY_FG = "#ffffff"
BTN_BG = "#0077b6"
BTN_FG = "#ffffff"
RESULT_FG = "#00ffcc"
FONT_MAIN = ("Segoe UI", 11)

# --- Title ---
tk.Label(root, text="Simple Calculator", font=("Segoe UI", 16, "bold"), bg="#1e1e2f", fg="#00ffcc").pack(pady=10)

# --- Input Frame ---
input_frame = tk.Frame(root, bg="#1e1e2f")
input_frame.pack(pady=10)

tk.Label(input_frame, text="First Number:", font=FONT_MAIN, bg="#1e1e2f", fg=LABEL_COLOR).grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry1 = tk.Entry(input_frame, font=FONT_MAIN, bg=ENTRY_BG, fg=ENTRY_FG, relief="flat", insertbackground=ENTRY_FG)
entry1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(input_frame, text="Second Number:", font=FONT_MAIN, bg="#1e1e2f", fg=LABEL_COLOR).grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry2 = tk.Entry(input_frame, font=FONT_MAIN, bg=ENTRY_BG, fg=ENTRY_FG, relief="flat", insertbackground=ENTRY_FG)
entry2.grid(row=1, column=1, padx=5, pady=5)

# --- Result Display ---
result_frame = tk.Frame(root, bg="#1e1e2f")
result_frame.pack(pady=(5, 15))

tk.Label(result_frame, text="Result:", font=("Segoe UI", 12, "bold"),
         bg="#1e1e2f", fg="#ffffff").pack(anchor="w")

result = tk.StringVar()
result_entry = tk.Entry(result_frame, textvariable=result,
                        font=("Segoe UI", 14, "bold"), state="readonly",
                        bg="#202030", fg="#00ffcc", relief="flat", justify="center",
                        readonlybackground="#202030", bd=2, highlightthickness=1, highlightbackground="#00ffcc")
result_entry.pack(ipady=10, padx=10, fill="x")

# --- Button Frame ---
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="➕ Add", command=lambda: calculate("add"),
          bg=BTN_BG, fg=BTN_FG, font=FONT_MAIN, relief="flat", width=14).grid(row=0, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="➖ Subtract", command=lambda: calculate("subtract"),
          bg=BTN_BG, fg=BTN_FG, font=FONT_MAIN, relief="flat", width=14).grid(row=0, column=1, padx=5, pady=5)

tk.Button(btn_frame, text="✖ Multiply", command=lambda: calculate("multiply"),
          bg=BTN_BG, fg=BTN_FG, font=FONT_MAIN, relief="flat", width=14).grid(row=1, column=0, padx=5, pady=5)

tk.Button(btn_frame, text="➗ Divide", command=lambda: calculate("divide"),
          bg=BTN_BG, fg=BTN_FG, font=FONT_MAIN, relief="flat", width=14).grid(row=1, column=1, padx=5, pady=5)

# Run the GUI
root.mainloop()
