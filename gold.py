import tkinter as tk
from tkinter import messagebox, ttk
import random

# Simulated live gold price function
def get_live_gold_price():
    return round(random.uniform(4500, 5000), 2)  # Example price per gram

# Dummy previous orders
previous_orders = {
    "surendarkarnati3@gmail.com": [
        {"item": "Gold Ring", "weight": "5g", "date": "2026-01-10"},
        {"item": "Gold Chain", "weight": "10g", "date": "2026-01-15"}
    ]
}

# Login credentials (not safe for real apps!)
users = {
    "surendarkarnati3@gmail.com": {"password": "Surendar@1", "role": "user"},
    "admin": {"password": "admin123", "role": "admin"}
}

# Login Window
def login():
    email = email_entry.get()
    pwd = password_entry.get()
    
    if email in users and users[email]["password"] == pwd:
        messagebox.showinfo("Login", f"Welcome {users[email]['role']}!")
        login_window.destroy()
        main_window(email, users[email]["role"])
    else:
        messagebox.showerror("Login", "Invalid credentials")

# Main App Window
def main_window(user_email, role):
    app = tk.Tk()
    app.title("Sihvaskhati Jewellery - Achampet, Telangana")
    app.geometry("800x600")
    
    tk.Label(app, text="Sihvaskhati Jewellery - Achampet, Telangana", font=("Arial", 16)).pack(pady=10)
    tk.Label(app, text=f"Phone: 83095494", font=("Arial", 12)).pack(pady=5)
    
    # Live gold price
    gold_price_var = tk.StringVar()
    gold_price_var.set(f"Live Gold Price: ₹{get_live_gold_price()} per gram")
    tk.Label(app, textvariable=gold_price_var, font=("Arial", 14), fg="gold").pack(pady=10)
    
    def refresh_price():
        gold_price_var.set(f"Live Gold Price: ₹{get_live_gold_price()} per gram")
    
    tk.Button(app, text="Refresh Price", command=refresh_price).pack(pady=5)
    
    # Booking Section
    tk.Label(app, text="Book/Exchange Items", font=("Arial", 14)).pack(pady=10)
    
    tk.Label(app, text="Select Item Type:").pack()
    item_type = ttk.Combobox(app, values=["Ring", "Chain", "Bracelet"])
    item_type.pack(pady=5)
    
    tk.Label(app, text="Select Design:").pack()
    design_var = ttk.Combobox(app, values=["Design 1", "Design 2", "Design 3"])
    design_var.pack(pady=5)
    
    tk.Label(app, text="Weight (grams):").pack()
    weight_entry = tk.Entry(app)
    weight_entry.pack(pady=5)
    
    def book_item():
        item = item_type.get()
        design = design_var.get()
        weight = weight_entry.get()
        if not item or not design or not weight:
            messagebox.showerror("Error", "Please fill all fields")
            return
        if user_email not in previous_orders:
            previous_orders[user_email] = []
        previous_orders[user_email].append({"item": f"{item} ({design})", "weight": f"{weight}g", "date": "2026-02-15"})
        messagebox.showinfo("Success", f"{item} booked successfully!")
    
    tk.Button(app, text="Book Item", command=book_item).pack(pady=10)
    
    # Previous Orders
    tk.Label(app, text="Previous Orders:", font=("Arial", 14)).pack(pady=10)
    orders_frame = tk.Frame(app)
    orders_frame.pack()
    
    columns = ("Item", "Weight", "Date")
    tree = ttk.Treeview(orders_frame, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
    tree.pack()
    
    if user_email in previous_orders:
        for order in previous_orders[user_email]:
            tree.insert("", tk.END, values=(order["item"], order["weight"], order["date"]))
    
    app.mainloop()

# Login GUI
login_window = tk.Tk()
login_window.title("Login - Sihvaskhati Jewellery")
login_window.geometry("400x300")

tk.Label(login_window, text="Email:", font=("Arial", 12)).pack(pady=10)
email_entry = tk.Entry(login_window, width=30)
email_entry.pack()

tk.Label(login_window, text="Password:", font=("Arial", 12)).pack(pady=10)
password_entry = tk.Entry(login_window, show="*", width=30)
password_entry.pack()

tk.Button(login_window, text="Login", command=login).pack(pady=20)

login_window.mainloop()
