import tkinter as tk
from tkinter import messagebox


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Online Product & Billing System")
root.geometry("800x750")


# ============================================================
# DICTIONARIES
# ============================================================

# Dictionary to store all products
#
# Example:
#
# products = {
#     "Laptop": {
#         "price": 50000,
#         "stock": 10
#     },
#     "Mouse": {
#         "price": 1000,
#         "stock": 20
#     }
# }
#
# This is a NESTED DICTIONARY.

products = {}


# Dictionary to store shopping cart
#
# Example:
#
# cart = {
#     "Laptop": {
#         "price": 50000,
#         "quantity": 2,
#         "amount": 100000
#     }
# }

cart = {}


# ============================================================
# FUNCTION 1: ADD PRODUCT
# ============================================================

def add_product():

    # Get product name from Entry box
    product_name = product_name_entry.get().strip()

    # Get price from Entry box
    price_text = price_entry.get().strip()

    # Get stock from Entry box
    stock_text = stock_entry.get().strip()

    # Check whether all fields are entered
    if not product_name or not price_text or not stock_text:
        messagebox.showwarning(
            "Warning",
            "Please enter Product Name, Price and Stock."
        )
        return

    try:
        # Convert price into float
        price = float(price_text)

        # Convert stock into integer
        stock = int(stock_text)

        # Validate price
        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        # Validate stock
        if stock < 0:
            raise ValueError("Stock cannot be negative.")

    except ValueError as e:

        messagebox.showerror(
            "Invalid Input",
            str(e)
        )

        return

    # Check whether product already exists
    if product_name in products:

        messagebox.showerror(
            "Error",
            "Product already exists."
        )

        return

    # Store product details inside nested dictionary
    products[product_name] = {
        "price": price,
        "stock": stock
    }

    messagebox.showinfo(
        "Success",
        f"{product_name} added successfully."
    )

    # Clear product input fields
    product_name_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    stock_entry.delete(0, tk.END)

    # Display all products
    display_products()


# ============================================================
# FUNCTION 2: DISPLAY PRODUCTS
# ============================================================

def display_products():

    # Clear previous display
    product_display.delete("1.0", tk.END)

    product_display.insert(
        tk.END,
        "AVAILABLE PRODUCTS\n"
    )

    product_display.insert(
        tk.END,
        "-" * 50 + "\n"
    )

    # .items() gives product name and product details
    for product_name, details in products.items():

        # Get price and stock from nested dictionary
        price = details.get("price")
        stock = details.get("stock")

        product_display.insert(
            tk.END,
            f"Product : {product_name}\n"
        )

        product_display.insert(
            tk.END,
            f"Price   : ₹{price:.2f}\n"
        )

        product_display.insert(
            tk.END,
            f"Stock   : {stock}\n"
        )

        product_display.insert(
            tk.END,
            "-" * 50 + "\n"
        )


# ============================================================
# FUNCTION 3: ADD PRODUCT TO CART
# ============================================================

def add_to_cart():

    # Get customer name
    customer_name = customer_entry.get().strip()

    # Get product name
    product_name = cart_product_entry.get().strip()

    # Get quantity
    quantity_text = quantity_entry.get().strip()

    # Check customer name
    if not customer_name:
        messagebox.showwarning(
            "Warning",
            "Please enter customer name."
        )
        return

    # Check product name and quantity
    if not product_name or not quantity_text:
        messagebox.showwarning(
            "Warning",
            "Please enter product name and quantity."
        )
        return

    try:

        # Convert quantity to integer
        quantity = int(quantity_text)

        # Quantity must be greater than zero
        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than 0."
            )

    except ValueError as e:

        messagebox.showerror(
            "Invalid Quantity",
            str(e)
        )

        return

    # --------------------------------------------------------
    # SEARCH PRODUCT USING .get()
    # --------------------------------------------------------

    # .get() searches the dictionary
    # If product doesn't exist, it returns None

    product = products.get(product_name)

    if product is None:

        messagebox.showerror(
            "Error",
            "Product not found."
        )

        return

    # Get available stock
    available_stock = product.get("stock")

    # Check whether requested quantity is available
    if quantity > available_stock:

        messagebox.showerror(
            "Stock Error",
            f"Only {available_stock} items available."
        )

        return

    # Get product price
    price = product.get("price")

    # Calculate item amount
    item_amount = price * quantity

    # --------------------------------------------------------
    # ADD ITEM TO CART
    # --------------------------------------------------------

    # If product already exists in cart,
    # increase its quantity.

    if product_name in cart:

        old_quantity = cart[product_name].get("quantity")

        new_quantity = old_quantity + quantity

        # Check stock again
        if new_quantity > available_stock:

            messagebox.showerror(
                "Stock Error",
                f"Only {available_stock} items available."
            )

            return

        cart[product_name]["quantity"] = new_quantity

        cart[product_name]["amount"] = (
            price * new_quantity
        )

    else:

        # Add new product to cart
        cart[product_name] = {

            "price": price,

            "quantity": quantity,

            "amount": item_amount
        }

    # --------------------------------------------------------
    # UPDATE STOCK
    # --------------------------------------------------------

    product["stock"] = available_stock - quantity

    messagebox.showinfo(
        "Success",
        f"{quantity} {product_name}(s) added to cart."
    )

    # Clear product and quantity fields
    cart_product_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

    # Display cart
    view_cart()

    # Display updated products
    display_products()


# ============================================================
# FUNCTION 4: REMOVE PRODUCT FROM CART
# ============================================================

def remove_product():

    product_name = cart_product_entry.get().strip()

    if not product_name:

        messagebox.showwarning(
            "Warning",
            "Enter the product name to remove."
        )

        return

    # Search product in cart using .get()
    cart_item = cart.get(product_name)

    if cart_item is None:

        messagebox.showerror(
            "Error",
            "Product is not available in cart."
        )

        return

    # Get quantity being removed
    quantity = cart_item.get("quantity")

    # Return quantity back to product stock
    products[product_name]["stock"] += quantity

    # Remove product from cart
    del cart[product_name]

    messagebox.showinfo(
        "Removed",
        f"{product_name} removed from cart."
    )

    cart_product_entry.delete(0, tk.END)

    # Refresh displays
    view_cart()
    display_products()


# ============================================================
# FUNCTION 5: VIEW CART
# ============================================================

def view_cart():

    # Clear old cart display
    cart_display.delete("1.0", tk.END)

    cart_display.insert(
        tk.END,
        "SHOPPING CART\n"
    )

    cart_display.insert(
        tk.END,
        "=" * 60 + "\n"
    )

    if not cart:

        cart_display.insert(
            tk.END,
            "Cart is empty.\n"
        )

        return

    # .items() gives product name and details
    for product_name, details in cart.items():

        price = details.get("price")

        quantity = details.get("quantity")

        amount = details.get("amount")

        cart_display.insert(
            tk.END,
            f"Product  : {product_name}\n"
        )

        cart_display.insert(
            tk.END,
            f"Price    : ₹{price:.2f}\n"
        )

        cart_display.insert(
            tk.END,
            f"Quantity : {quantity}\n"
        )

        cart_display.insert(
            tk.END,
            f"Amount   : ₹{amount:.2f}\n"
        )

        cart_display.insert(
            tk.END,
            "-" * 60 + "\n"
        )


# ============================================================
# FUNCTION 6: CALCULATE TOTAL AND DISCOUNT
# ============================================================

def calculate_bill_total(cart_items):

    # Start total from zero
    total = 0

    # Go through every product in cart
    for product_name, details in cart_items.items():

        # Get item amount
        amount = details.get("amount")

        # Add amount to total
        total += amount

    # --------------------------------------------------------
    # DISCOUNT RULES
    # --------------------------------------------------------

    # Purchase ₹10,000 or more → 15% discount
    if total >= 10000:

        discount = total * 0.15

    # Purchase ₹5,000 or more → 10% discount
    elif total >= 5000:

        discount = total * 0.10

    # Purchase ₹2,000 or more → 5% discount
    elif total >= 2000:

        discount = total * 0.05

    # Less than ₹2,000 → no discount
    else:

        discount = 0

    # Calculate final amount
    final_amount = total - discount

    # Return all three values
    return total, discount, final_amount


# ============================================================
# FUNCTION 7: GENERATE BILL
# ============================================================

def generate_bill():

    # Get customer name
    customer_name = customer_entry.get().strip()

    # Check customer name
    if not customer_name:

        messagebox.showwarning(
            "Warning",
            "Please enter customer name."
        )

        return

    # Check whether cart is empty
    if not cart:

        messagebox.showwarning(
            "Warning",
            "Cart is empty."
        )

        return

    # Calculate total, discount and final amount
    total, discount, final_amount = calculate_bill_total(cart)

    # Clear bill display
    bill_display.delete("1.0", tk.END)

    # --------------------------------------------------------
    # BILL HEADER
    # --------------------------------------------------------

    bill_display.insert(
        tk.END,
        "             ONLINE PRODUCT BILL\n"
    )

    bill_display.insert(
        tk.END,
        "=" * 60 + "\n"
    )

    bill_display.insert(
        tk.END,
        f"Customer Name : {customer_name}\n"
    )

    bill_display.insert(
        tk.END,
        "-" * 60 + "\n"
    )

    # --------------------------------------------------------
    # DISPLAY CART ITEMS
    # --------------------------------------------------------

    # .items() used to display cart products
    for product_name, details in cart.items():

        price = details.get("price")

        quantity = details.get("quantity")

        amount = details.get("amount")

        bill_display.insert(
            tk.END,
            f"Product  : {product_name}\n"
        )

        bill_display.insert(
            tk.END,
            f"Price    : ₹{price:.2f}\n"
        )

        bill_display.insert(
            tk.END,
            f"Quantity : {quantity}\n"
        )

        bill_display.insert(
            tk.END,
            f"Amount   : ₹{amount:.2f}\n"
        )

        bill_display.insert(
            tk.END,
            "-" * 60 + "\n"
        )

    # --------------------------------------------------------
    # BILL SUMMARY
    # --------------------------------------------------------

    bill_display.insert(
        tk.END,
        f"Total Amount  : ₹{total:.2f}\n"
    )

    bill_display.insert(
        tk.END,
        f"Discount      : ₹{discount:.2f}\n"
    )

    bill_display.insert(
        tk.END,
        f"Final Amount  : ₹{final_amount:.2f}\n"
    )

    bill_display.insert(
        tk.END,
        "=" * 60 + "\n"
    )

    bill_display.insert(
        tk.END,
        "        Thank you for shopping!\n"
    )

    # Display values in separate labels
    total_label.config(
        text=f"Total Amount: ₹{total:.2f}"
    )

    discount_label.config(
        text=f"Discount: ₹{discount:.2f}"
    )

    final_label.config(
        text=f"Final Amount: ₹{final_amount:.2f}"
    )


# ============================================================
# FUNCTION 8: CLEAR / RESET
# ============================================================

def clear_all():

    # Clear dictionaries
    products.clear()
    cart.clear()

    # Clear all Entry fields
    customer_entry.delete(0, tk.END)

    product_name_entry.delete(0, tk.END)

    price_entry.delete(0, tk.END)

    stock_entry.delete(0, tk.END)

    cart_product_entry.delete(0, tk.END)

    quantity_entry.delete(0, tk.END)

    # Clear display areas
    product_display.delete("1.0", tk.END)

    cart_display.delete("1.0", tk.END)

    bill_display.delete("1.0", tk.END)

    # Reset amount labels
    total_label.config(
        text="Total Amount: ₹0.00"
    )

    discount_label.config(
        text="Discount: ₹0.00"
    )

    final_label.config(
        text="Final Amount: ₹0.00"
    )


# ============================================================
# GUI - CUSTOMER DETAILS
# ============================================================

customer_frame = tk.LabelFrame(
    root,
    text="Customer Details",
    padx=10,
    pady=10
)

customer_frame.pack(
    fill="x",
    padx=10,
    pady=10
)


tk.Label(
    customer_frame,
    text="Customer Name"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


customer_entry = tk.Entry(
    customer_frame,
    width=30
)

customer_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# GUI - PRODUCT DETAILS
# ============================================================

product_frame = tk.LabelFrame(
    root,
    text="Product Management",
    padx=10,
    pady=10
)

product_frame.pack(
    fill="x",
    padx=10,
    pady=5
)


# Product Name

tk.Label(
    product_frame,
    text="Product Name"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


product_name_entry = tk.Entry(
    product_frame,
    width=20
)

product_name_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Product Price

tk.Label(
    product_frame,
    text="Product Price"
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


price_entry = tk.Entry(
    product_frame,
    width=15
)

price_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# Stock

tk.Label(
    product_frame,
    text="Stock"
).grid(
    row=0,
    column=4,
    padx=5,
    pady=5
)


stock_entry = tk.Entry(
    product_frame,
    width=10
)

stock_entry.grid(
    row=0,
    column=5,
    padx=5,
    pady=5
)


# Add Product Button

tk.Button(
    product_frame,
    text="Add Product",
    command=add_product
).grid(
    row=1,
    column=0,
    columnspan=2,
    pady=10
)


# Display Products Button

tk.Button(
    product_frame,
    text="View Products",
    command=display_products
).grid(
    row=1,
    column=2,
    columnspan=2,
    pady=10
)


# ============================================================
# PRODUCT DISPLAY AREA
# ============================================================

product_display = tk.Text(
    root,
    height=7,
    width=80
)

product_display.pack(
    padx=10,
    pady=5
)


# ============================================================
# GUI - SHOPPING CART
# ============================================================

cart_frame = tk.LabelFrame(
    root,
    text="Shopping Cart",
    padx=10,
    pady=10
)

cart_frame.pack(
    fill="x",
    padx=10,
    pady=5
)


# Product Name

tk.Label(
    cart_frame,
    text="Product Name"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


cart_product_entry = tk.Entry(
    cart_frame,
    width=20
)

cart_product_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Quantity

tk.Label(
    cart_frame,
    text="Quantity"
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


quantity_entry = tk.Entry(
    cart_frame,
    width=10
)

quantity_entry.grid(
    row=0,
    column=3,
    padx=5,
    pady=5
)


# Add to Cart Button

tk.Button(
    cart_frame,
    text="Add to Cart",
    command=add_to_cart
).grid(
    row=1,
    column=0,
    padx=5,
    pady=10
)


# Remove Product Button

tk.Button(
    cart_frame,
    text="Remove Product",
    command=remove_product
).grid(
    row=1,
    column=1,
    padx=5,
    pady=10
)


# View Cart Button

tk.Button(
    cart_frame,
    text="View Cart",
    command=view_cart
).grid(
    row=1,
    column=2,
    padx=5,
    pady=10
)


# ============================================================
# CART DISPLAY AREA
# ============================================================

cart_display = tk.Text(
    root,
    height=8,
    width=80
)

cart_display.pack(
    padx=10,
    pady=5
)


# ============================================================
# BILL DISPLAY AREA
# ============================================================

bill_display = tk.Text(
    root,
    height=10,
    width=80
)

bill_display.pack(
    padx=10,
    pady=5
)


# ============================================================
# TOTAL / DISCOUNT / FINAL AMOUNT
# ============================================================

total_label = tk.Label(
    root,
    text="Total Amount: ₹0.00",
    font=("Arial", 11, "bold")
)

total_label.pack()


discount_label = tk.Label(
    root,
    text="Discount: ₹0.00",
    font=("Arial", 11, "bold")
)

discount_label.pack()


final_label = tk.Label(
    root,
    text="Final Amount: ₹0.00",
    font=("Arial", 12, "bold")
)

final_label.pack()


# ============================================================
# BUTTONS
# ============================================================

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)


tk.Button(
    button_frame,
    text="Generate Bill",
    command=generate_bill,
    width=15
).grid(
    row=0,
    column=0,
    padx=10
)


tk.Button(
    button_frame,
    text="Clear / Reset",
    command=clear_all,
    width=15
).grid(
    row=0,
    column=1,
    padx=10
)


# ============================================================
# START THE APPLICATION
# ============================================================

root.mainloop()