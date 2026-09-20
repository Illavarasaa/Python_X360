import tkinter as tk
from tkinter import messagebox


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Contact & Phone Directory")
root.geometry("850x700")


# ============================================================
# CONTACT DICTIONARY
# ============================================================

# Main dictionary
#
# Each contact name is the KEY.
#
# The contact information is stored
# inside another dictionary.
#
# Example:
#
# contacts = {
#     "Arun": {
#         "phone": "9876543210",
#         "email": "arun@gmail.com",
#         "city": "Madurai"
#     }
# }

contacts = {}


# ============================================================
# FUNCTION 1: VALIDATE CONTACT DETAILS
# ============================================================

def validate_contact(name, phone, email, city):

    # Check whether any field is empty
    if not name or not phone or not email or not city:

        messagebox.showwarning(
            "Missing Information",
            "Please enter all contact details."
        )

        return False

    # Check phone number
    if not phone.isdigit():

        messagebox.showerror(
            "Invalid Phone",
            "Phone number should contain only numbers."
        )

        return False

    # Check phone number length
    if len(phone) != 10:

        messagebox.showerror(
            "Invalid Phone",
            "Phone number must contain 10 digits."
        )

        return False

    # Basic email validation
    if "@" not in email or "." not in email:

        messagebox.showerror(
            "Invalid Email",
            "Please enter a valid email address."
        )

        return False

    return True


# ============================================================
# FUNCTION 2: ADD CONTACT
# ============================================================

def add_contact():

    # Get values from Entry widgets
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    city = city_entry.get().strip()

    # Validate input
    if not validate_contact(name, phone, email, city):
        return

    # Check whether contact already exists
    if name in contacts:

        messagebox.showerror(
            "Duplicate Contact",
            "Contact already exists."
        )

        return

    # Store contact information
    # using a nested dictionary

    contacts[name] = {

        "phone": phone,

        "email": email,

        "city": city
    }

    messagebox.showinfo(
        "Success",
        f"Contact '{name}' added successfully."
    )

    # Display updated contact list
    display_all_contacts()


# ============================================================
# FUNCTION 3: SEARCH CONTACT
# ============================================================

def search_contact():

    # Get contact name
    name = name_entry.get().strip()

    # Check empty name
    if not name:

        messagebox.showwarning(
            "Missing Name",
            "Please enter a contact name."
        )

        return

    # --------------------------------------------------------
    # .get() IS USED FOR SAFE SEARCHING
    # --------------------------------------------------------

    contact = contacts.get(name)

    # If contact doesn't exist
    if contact is None:

        messagebox.showerror(
            "Contact Not Found",
            f"No contact found for '{name}'."
        )

        return

    # Clear display area
    contact_display.delete("1.0", tk.END)

    # Display contact details
    contact_display.insert(
        tk.END,
        "CONTACT FOUND\n"
    )

    contact_display.insert(
        tk.END,
        "=" * 55 + "\n"
    )

    contact_display.insert(
        tk.END,
        f"Name  : {name}\n"
    )

    contact_display.insert(
        tk.END,
        f"Phone : {contact.get('phone')}\n"
    )

    contact_display.insert(
        tk.END,
        f"Email : {contact.get('email')}\n"
    )

    contact_display.insert(
        tk.END,
        f"City  : {contact.get('city')}\n"
    )


# ============================================================
# FUNCTION 4: UPDATE CONTACT
# ============================================================

def update_contact():

    # Get values from Entry widgets
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    city = city_entry.get().strip()

    # Check whether contact exists
    contact = contacts.get(name)

    if contact is None:

        messagebox.showerror(
            "Contact Not Found",
            f"Cannot update '{name}'. Contact does not exist."
        )

        return

    # Validate new information
    if not validate_contact(name, phone, email, city):
        return

    # Update existing nested dictionary
    contacts[name]["phone"] = phone
    contacts[name]["email"] = email
    contacts[name]["city"] = city

    messagebox.showinfo(
        "Updated",
        f"Contact '{name}' updated successfully."
    )

    # Display updated contacts
    display_all_contacts()


# ============================================================
# FUNCTION 5: DELETE CONTACT
# ============================================================

def delete_contact():

    # Get contact name
    name = name_entry.get().strip()

    # Check empty name
    if not name:

        messagebox.showwarning(
            "Missing Name",
            "Please enter a contact name."
        )

        return

    # Safe searching using .get()
    contact = contacts.get(name)

    # Contact does not exist
    if contact is None:

        messagebox.showerror(
            "Contact Not Found",
            f"Cannot delete '{name}'. Contact does not exist."
        )

        return

    # Ask for confirmation
    answer = messagebox.askyesno(
        "Confirm Delete",
        f"Are you sure you want to delete '{name}'?"
    )

    if answer:

        # Delete contact
        del contacts[name]

        messagebox.showinfo(
            "Deleted",
            f"Contact '{name}' deleted successfully."
        )

        # Refresh display
        display_all_contacts()


# ============================================================
# FUNCTION 6: DISPLAY ALL CONTACTS
# ============================================================

def display_all_contacts():

    # Clear display area
    contact_display.delete("1.0", tk.END)

    contact_display.insert(
        tk.END,
        "ALL CONTACTS\n"
    )

    contact_display.insert(
        tk.END,
        "=" * 65 + "\n"
    )

    # Check whether dictionary is empty
    if not contacts:

        contact_display.insert(
            tk.END,
            "No contacts available.\n"
        )

        return

    # --------------------------------------------------------
    # .items() IS USED TO DISPLAY ALL CONTACTS
    # --------------------------------------------------------

    for name, details in contacts.items():

        # Get values from nested dictionary
        phone = details.get("phone")
        email = details.get("email")
        city = details.get("city")

        contact_display.insert(
            tk.END,
            f"Name  : {name}\n"
        )

        contact_display.insert(
            tk.END,
            f"Phone : {phone}\n"
        )

        contact_display.insert(
            tk.END,
            f"Email : {email}\n"
        )

        contact_display.insert(
            tk.END,
            f"City  : {city}\n"
        )

        contact_display.insert(
            tk.END,
            "-" * 65 + "\n"
        )


# ============================================================
# BONUS 1: *args
# ============================================================

def show_message(*args):

    # *args allows the function
    # to accept any number of arguments.

    message = " ".join(args)

    messagebox.showinfo(
        "Information",
        message
    )


# ============================================================
# BONUS 2: **kwargs
# ============================================================

def create_contact_text(**kwargs):

    # **kwargs receives data in
    # key=value format.

    result = ""

    for key, value in kwargs.items():

        result += f"{key}: {value}\n"

    return result


# ============================================================
# BONUS 3: DICTIONARY COMPREHENSION
# ============================================================

def filter_contacts_by_city():

    city = city_entry.get().strip()

    if not city:

        messagebox.showwarning(
            "Missing City",
            "Please enter a city."
        )

        return

    # Dictionary comprehension
    #
    # Creates a new dictionary containing
    # only contacts from the selected city.

    filtered_contacts = {
        name: details
        for name, details in contacts.items()
        if details.get("city", "").lower() == city.lower()
    }

    # Clear display
    contact_display.delete("1.0", tk.END)

    contact_display.insert(
        tk.END,
        f"CONTACTS FROM {city.upper()}\n"
    )

    contact_display.insert(
        tk.END,
        "=" * 65 + "\n"
    )

    if not filtered_contacts:

        contact_display.insert(
            tk.END,
            f"No contacts found in {city}.\n"
        )

        return

    # Display filtered dictionary
    for name, details in filtered_contacts.items():

        contact_display.insert(
            tk.END,
            f"Name  : {name}\n"
        )

        contact_display.insert(
            tk.END,
            f"Phone : {details.get('phone')}\n"
        )

        contact_display.insert(
            tk.END,
            f"Email : {details.get('email')}\n"
        )

        contact_display.insert(
            tk.END,
            f"City  : {details.get('city')}\n"
        )

        contact_display.insert(
            tk.END,
            "-" * 65 + "\n"
        )


# ============================================================
# FUNCTION 7: CLEAR / RESET
# ============================================================

def clear_all():

    # Clear all stored contacts
    contacts.clear()

    # Clear Entry fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)

    # Clear display area
    contact_display.delete("1.0", tk.END)

    contact_display.insert(
        tk.END,
        "Contact Manager Reset.\n"
    )


# ============================================================
# FUNCTION 8: HELP / ABOUT
# ============================================================

def show_help():

    help_text = """
CONTACT & PHONE DIRECTORY

How to use:

1. Enter contact name.
2. Enter 10-digit phone number.
3. Enter email address.
4. Enter city.
5. Click Add Contact.

Search:
Enter the contact name and click Search Contact.

Update:
Enter the existing contact name
and the new phone, email and city.
Then click Update Contact.

Delete:
Enter the contact name and click
Delete Contact.

Display All:
Click Display All Contacts.

Filter:
Enter a city and click
Contacts by City.

Clear / Reset:
Clears all contacts and input fields.
"""

    messagebox.showinfo(
        "Help / About",
        help_text
    )


# ============================================================
# GUI - TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="📱 CONTACT & PHONE DIRECTORY",
    font=("Arial", 18, "bold")
)

title_label.pack(
    pady=10
)


# ============================================================
# CONTACT DETAILS FRAME
# ============================================================

details_frame = tk.LabelFrame(
    root,
    text="Contact Details",
    padx=10,
    pady=10
)

details_frame.pack(
    fill="x",
    padx=15,
    pady=5
)


# ============================================================
# NAME
# ============================================================

tk.Label(
    details_frame,
    text="Contact Name"
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)


name_entry = tk.Entry(
    details_frame,
    width=30
)

name_entry.grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# PHONE
# ============================================================

tk.Label(
    details_frame,
    text="Phone Number"
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)


phone_entry = tk.Entry(
    details_frame,
    width=30
)

phone_entry.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# EMAIL
# ============================================================

tk.Label(
    details_frame,
    text="Email"
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)


email_entry = tk.Entry(
    details_frame,
    width=30
)

email_entry.grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# CITY
# ============================================================

tk.Label(
    details_frame,
    text="City"
).grid(
    row=3,
    column=0,
    padx=5,
    pady=5,
    sticky="w"
)


city_entry = tk.Entry(
    details_frame,
    width=30
)

city_entry.grid(
    row=3,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# BUTTON FRAME
# ============================================================

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)


# Add Contact

tk.Button(
    button_frame,
    text="Add Contact",
    width=18,
    command=add_contact
).grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


# Search Contact

tk.Button(
    button_frame,
    text="Search Contact",
    width=18,
    command=search_contact
).grid(
    row=0,
    column=1,
    padx=5,
    pady=5
)


# Update Contact

tk.Button(
    button_frame,
    text="Update Contact",
    width=18,
    command=update_contact
).grid(
    row=0,
    column=2,
    padx=5,
    pady=5
)


# Delete Contact

tk.Button(
    button_frame,
    text="Delete Contact",
    width=18,
    command=delete_contact
).grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


# Display All

tk.Button(
    button_frame,
    text="Display All Contacts",
    width=18,
    command=display_all_contacts
).grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# Filter by City

tk.Button(
    button_frame,
    text="Contacts by City",
    width=18,
    command=filter_contacts_by_city
).grid(
    row=1,
    column=2,
    padx=5,
    pady=5
)


# Help

tk.Button(
    button_frame,
    text="Help / About",
    width=18,
    command=show_help
).grid(
    row=2,
    column=0,
    padx=5,
    pady=5
)


# Clear / Reset

tk.Button(
    button_frame,
    text="Clear / Reset",
    width=18,
    command=clear_all
).grid(
    row=2,
    column=1,
    padx=5,
    pady=5
)


# ============================================================
# CONTACT DISPLAY AREA
# ============================================================

tk.Label(
    root,
    text="Contact Information",
    font=("Arial", 12, "bold")
).pack(
    pady=5
)


contact_display = tk.Text(
    root,
    width=90,
    height=18
)

contact_display.pack(
    padx=15,
    pady=5
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()