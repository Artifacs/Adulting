# savers_gui.py

import tkinter as tk
from tkinter import messagebox
from logic import deposit, deduct

# Global variable for savings balance
money = 0

# Create the main window
root = tk.Tk()
root.title("Savers GUI")
root.geometry("350x250")

# Function to update the balance label
def update_balance():
    balance_label.config(text=f"Current Savings: ₱{money}")

# Function to handle deposit
def handle_deposit():
    global money
    try:
        amount = int(entry.get())
        money = deposit(money, amount)
        update_balance()
        messagebox.showinfo("Deposit", f"You deposited ₱{amount}!")
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Function to handle deduction
def handle_deduct():
    global money
    try:
        amount = int(entry.get())
        money = deduct(money, amount)
        update_balance()
        messagebox.showinfo("Deduct", f"You deducted ₱{amount}!")
        entry.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Balance display
balance_label = tk.Label(root, text=f"Current Savings: ₱{money}", font=("Arial", 14))
balance_label.pack(pady=10)

# Input field
entry = tk.Entry(root)
entry.pack(pady=5)

# Button container
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Deposit button
deposit_button = tk.Button(button_frame, text="Deposit", width=10, command=handle_deposit)
deposit_button.grid(row=0, column=0, padx=5)

# Deduct button
deduct_button = tk.Button(button_frame, text="Deduct", width=10, command=handle_deduct)
deduct_button.grid(row=0, column=1, padx=5)

# Exit button
exit_button = tk.Button(root, text="Exit", width=10, command=root.quit)
exit_button.pack(pady=10)

# Run the GUI loop
root.mainloop()

