import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Shopping Cart")
root.geometry("600x500")

products = []
prices = []

def refresh_cart():
    cart_list.delete(0, tk.END)

    for i in range(len(products)):
        cart_list.insert(
            tk.END,
            f"{products[i]} - ${prices[i]:.2f}"
        )

def add_product():
    name = product_entry.get().strip()

    try:
        price = float(price_entry.get())
        if price < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid product price.")
        return

    if name == "":
        messagebox.showerror("Error", "Enter a product name.")
        return

    products.append(name)
    prices.append(price)

    refresh_cart()

    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def remove_selected():
    selected = cart_list.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a product to remove.")
        return

    index = selected[0]
    products.pop(index)
    prices.pop(index)

    refresh_cart()

def sort_products():
    combined = list(zip(products, prices))
    combined.sort(key=lambda item: item[0].lower())

    products.clear()
    prices.clear()

    for name, price in combined:
        products.append(name)
        prices.append(price)

    refresh_cart()

def generate_bill():
    total = 0

    for price in prices:
        total += price

    if total >= 1000:
        discount = total * 0.10
    elif total >= 500:
        discount = total * 0.05bill_text.set(
        f"Total: ${total:.2f}\n"
        f"Discount: ${discount:.2f}\n"
        f"Final Amount: ${final_amount:.2f}"
    )

def clear_all():
    products.clear()
    prices.clear()
    cart_list.delete(0, tk.END)
    bill_text.set("")
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

tk.Label(root, text="Shopping Cart",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label
    else:
        discount = 0

    final_amount = total - discount

    (root, text="Product Name").pack()
product_entry = tk.Entry(root)
product_entry.pack()

tk.Label(root, text="Product Price").pack()
price_entry = tk.Entry(root)
price_entry.pack()

tk.Button(root, text="Add Product",
          command=add_product).pack(pady=5)

cart_list = tk.Listbox(root, width=50, height=10)
cart_list.pack(pady=10)

tk.Button(root, text="Remove Selected",
          command=remove_selected).pack(pady=3)

tk.Button(root, text="Sort Products",
          command=sort_products).pack(pady=3)

tk.Button(root, text="Generate Bill",
          command=generate_bill).pack(pady=3)

bill_text = tk.StringVar()
tk.Label(root, textvariable=bill_text,
         justify="left", font=("Arial", 11)).pack(pady=10)

tk.Button(root, text="Clear / Reset",
          command=clear_all).pack(pady=5)

root.mainloop()
