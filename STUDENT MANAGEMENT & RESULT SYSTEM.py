# STUDENT MANAGEMENT & RESULT SYSTEM

import tkinter as tk
from tkinter import messagebox


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("Student Management & Result System")
root.geometry("700x700")


# =========================================================
# DATA STORAGE
# =========================================================

# Main dictionary for storing student information
#
# Example structure:
#
# students = {
#     "101": {
#         "name": "Arun",
#         "department": "Computer Science",
#         "marks": {
#             "Python": 85,
#             "SQL": 90
#         }
#     }
# }

students = {}


# =========================================================
# ADD STUDENT
# =========================================================

def add_student():

    # Get values from Entry boxes
    roll = roll_entry.get().strip()
    name = name_entry.get().strip()
    department = dept_entry.get().strip()


    # Check whether any field is empty
    if not roll or not name or not department:

        messagebox.showerror(
            "Error",
            "Please enter Roll Number, Name and Department."
        )

        return


    # Check whether student already exists
    if roll in students:

        messagebox.showwarning(
            "Warning",
            "Student with this Roll Number already exists."
        )

        return


    # Create student record using a nested dictionary
    students[roll] = {
        "name": name,
        "department": department,
        "marks": {}
    }


    # Display confirmation
    messagebox.showinfo(
        "Success",
        "Student added successfully."
    )


    # Clear input fields
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)


# =========================================================
# ADD MARK
# =========================================================

def add_mark():

    # Get roll number, subject and mark
    roll = roll_entry.get().strip()
    subject = subject_entry.get().strip()
    mark_text = mark_entry.get().strip()


    # Check whether all fields are entered
    if not roll or not subject or not mark_text:

        messagebox.showerror(
            "Error",
            "Enter Roll Number, Subject and Mark."
        )

        return


    # Search student using dictionary
    student = students.get(roll)


    # Check whether student exists
    if student is None:

        messagebox.showerror(
            "Error",
            "Student not found. Add the student first."
        )

        return


    # Convert mark to float
    try:

        mark = float(mark_text)

        # Mark must be between 0 and 100
        if mark < 0 or mark > 100:
            raise ValueError

    except ValueError:

        messagebox.showerror(
            "Error",
            "Enter a valid mark between 0 and 100."
        )

        return


    # Store subject and mark
    # inside the nested marks dictionary
    students[roll]["marks"][subject] = mark


    # Display confirmation
    messagebox.showinfo(
        "Success",
        "Mark added successfully."
    )


    # Clear subject and mark fields
    subject_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)


# =========================================================
# SEARCH STUDENT
# =========================================================

def search_student():

    # Get roll number
    roll = roll_entry.get().strip()


    # Use .get() to search for the student
    student = students.get(roll)


    # Check whether student exists
    if student is None:

        messagebox.showerror(
            "Error",
            "Student not found."
        )

        return


    # Clear student details area
    details_text.delete("1.0", tk.END)


    # Display student information
    details_text.insert(
        tk.END,
        f"Roll Number: {roll}\n"
        f"Name: {student['name']}\n"
        f"Department: {student['department']}\n\n"
        f"Subjects and Marks:\n"
    )


    # Use .items() to display subject and mark
    for subject, mark in student["marks"].items():

        details_text.insert(
            tk.END,
            f"{subject}: {mark}\n"
        )


# =========================================================
# CALCULATE TOTAL
# =========================================================

def calculate_total(marks):

    # Start total at zero
    total = 0

    # Use .values() to get all marks
    for mark in marks.values():

        total += mark

    # Return calculated total
    return total


# =========================================================
# CALCULATE AVERAGE
# =========================================================

def calculate_average(marks):

    # If there are no marks
    if not marks:
        return 0


    # Calculate total using function
    total = calculate_total(marks)


    # Calculate average
    average = total / len(marks)


    # Return average
    return average


# =========================================================
# DETERMINE GRADE
# =========================================================

def determine_grade(average):

    # Determine grade based on average

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    elif average >= 40:
        return "E"

    else:
        return "F"


# =========================================================
# GENERATE RESULT
# =========================================================

def generate_result():

    # Get roll number
    roll = roll_entry.get().strip()


    # Search student using .get()
    student = students.get(roll)


    # Check whether student exists
    if student is None:

        messagebox.showerror(
            "Error",
            "Student not found."
        )

        return


    # Get marks dictionary
    marks = student["marks"]


    # Check whether marks have been entered
    if not marks:

        messagebox.showwarning(
            "Warning",
            "No marks available for this student."
        )

        return


    # Calculate total
    total = calculate_total(marks)


    # Calculate average
    average = calculate_average(marks)


    # Determine grade
    grade = determine_grade(average)


    # -----------------------------------------------------
    # DISPLAY RESULT
    # -----------------------------------------------------

    result_text.delete("1.0", tk.END)


    result_text.insert(
        tk.END,
        f"STUDENT RESULT\n"
        f"-----------------------------\n"
        f"Roll Number : {roll}\n"
        f"Name        : {student['name']}\n"
        f"Department  : {student['department']}\n"
        f"Total       : {total:.2f}\n"
        f"Average     : {average:.2f}\n"
        f"Grade       : {grade}\n"
    )


    # Display each subject and mark
    result_text.insert(
        tk.END,
        "\nSubject Marks\n"
        f"-----------------------------\n"
    )


    # Use .items() to display subjects and marks
    for subject, mark in marks.items():

        result_text.insert(
            tk.END,
            f"{subject}: {mark}\n"
        )


# =========================================================
# DISPLAY ALL STUDENTS
# =========================================================

def display_all_students():

    # Clear result area
    result_text.delete("1.0", tk.END)


    # Check whether dictionary is empty
    if not students:

        result_text.insert(
            tk.END,
            "No students available."
        )

        return


    # Use .items() to get roll number and student details
    for roll, student in students.items():

        result_text.insert(
            tk.END,
            f"Roll: {roll}\n"
            f"Name: {student['name']}\n"
            f"Department: {student['department']}\n"
            f"Subjects: {len(student['marks'])}\n"
            f"-----------------------------\n"
        )


# =========================================================
# CLEAR / RESET
# =========================================================

def clear_all():

    # Clear the entire students dictionary
    students.clear()


    # Clear all Entry boxes
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    dept_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    mark_entry.delete(0, tk.END)


    # Clear text areas
    details_text.delete("1.0", tk.END)
    result_text.delete("1.0", tk.END)


# =========================================================
# GUI DESIGN
# =========================================================

# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

tk.Label(
    root,
    text="Student Management & Result System",
    font=("Arial", 18, "bold")
).pack(pady=10)


# ---------------------------------------------------------
# STUDENT DETAILS FRAME
# ---------------------------------------------------------

student_frame = tk.LabelFrame(
    root,
    text="Student Details",
    padx=10,
    pady=10
)

student_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


# Roll Number
tk.Label(
    student_frame,
    text="Roll Number"
).grid(row=0, column=0, padx=5, pady=5)

roll_entry = tk.Entry(student_frame)
roll_entry.grid(row=0, column=1, padx=5, pady=5)


# Student Name
tk.Label(
    student_frame,
    text="Student Name"
).grid(row=1, column=0, padx=5, pady=5)

name_entry = tk.Entry(student_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)


# Department
tk.Label(
    student_frame,
    text="Department"
).grid(row=2, column=0, padx=5, pady=5)

dept_entry = tk.Entry(student_frame)
dept_entry.grid(row=2, column=1, padx=5, pady=5)


# Add Student button
tk.Button(
    student_frame,
    text="Add Student",
    command=add_student
).grid(row=0, column=2, padx=10)


# Search Student button
tk.Button(
    student_frame,
    text="Search Student",
    command=search_student
).grid(row=1, column=2, padx=10)


# Display All Students button
tk.Button(
    student_frame,
    text="Display All",
    command=display_all_students
).grid(row=2, column=2, padx=10)


# ---------------------------------------------------------
# MARK DETAILS FRAME
# ---------------------------------------------------------

mark_frame = tk.LabelFrame(
    root,
    text="Subject Marks",
    padx=10,
    pady=10
)

mark_frame.pack(
    fill="x",
    padx=20,
    pady=5
)


# Subject
tk.Label(
    mark_frame,
    text="Subject"
).grid(row=0, column=0, padx=5, pady=5)

subject_entry = tk.Entry(mark_frame)
subject_entry.grid(row=0, column=1, padx=5, pady=5)


# Mark
tk.Label(
    mark_frame,
    text="Mark"
).grid(row=1, column=0, padx=5, pady=5)

mark_entry = tk.Entry(mark_frame)
mark_entry.grid(row=1, column=1, padx=5, pady=5)


# Add Mark button
tk.Button(
    mark_frame,
    text="Add Mark",
    command=add_mark
).grid(row=0, column=2, rowspan=2, padx=10)


# ---------------------------------------------------------
# STUDENT DETAILS DISPLAY
# ---------------------------------------------------------

tk.Label(
    root,
    text="Student Details",
    font=("Arial", 12, "bold")
).pack(pady=5)


details_text = tk.Text(
    root,
    width=65,
    height=8
)

details_text.pack(pady=5)


# ---------------------------------------------------------
# GENERATE RESULT BUTTON
# ---------------------------------------------------------

tk.Button(
    root,
    text="Generate Result",
    command=generate_result,
    font=("Arial", 11, "bold")
).pack(pady=5)


# ---------------------------------------------------------
# RESULT DISPLAY
# ---------------------------------------------------------

tk.Label(
    root,
    text="Result",
    font=("Arial", 12, "bold")
).pack(pady=5)


result_text = tk.Text(
    root,
    width=65,
    height=10
)

result_text.pack(pady=5)


# ---------------------------------------------------------
# CLEAR / RESET BUTTON
# ---------------------------------------------------------

tk.Button(
    root,
    text="Clear / Reset",
    command=clear_all
).pack(pady=8)


# ---------------------------------------------------------
# START APPLICATION
# ---------------------------------------------------------

root.mainloop()