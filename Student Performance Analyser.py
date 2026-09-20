import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("500x600")
mark_entries = []

def enter_marks():
    global mark_entries

    for widget in marks_frame.winfo_children():
        widget.destroy()

    mark_entries = []

    try:
        n = int(subject_entry.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid positive number of subjects.")
        return

    for i in range(n):
        tk.Label(marks_frame, text=f"Subject {i + 1} Mark:").pack()
        entry = tk.Entry(marks_frame)
        entry.pack()
        mark_entries.append(entry)

def calculate_result():
    if not mark_entries:
        messagebox.showerror("Error", "Click 'Enter Marks' first.")
        return

    try:
        marks = []
        for entry in mark_entries:
            mark = float(entry.get())
            if mark < 0 or mark > 100:
                raise ValueError
            marks.append(mark)
    except ValueError:
        messagebox.showerror("Error", "Enter marks between 0 and 100.")
        return

    total = sum(marks)
    average = total / len(marks)

    if any(mark < 35 for mark in marks):
        status = "Fail"
    else:
        status = "Pass"

    if status == "Fail":
        grade = "F"
    elif average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "E"

    name = name_entry.get().strip()

    result_text.set(
        f"Student: {name}\n"
        f"Total: {total:.2f}\n"
        f"Average: {average:.2f}\n"
        f"Result: {status}\n"
        f"Grade: {grade}"
    )

def clear_all():
    name_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    result_text.set("")

    for widget in marks_frame.winfo_children():
        widget.destroy()

    mark_entries.clear()

tk.Label(root, text="Student Performance Analyzer",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Number of Subjects").pack()
subject_entry = tk.Entry(root)
subject_entry.pack()

tk.Button(root, text="Enter Marks", command=enter_marks).pack(pady=8)

marks_frame = tk.Frame(root)
marks_frame.pack()

tk.Button(root, text="Calculate Result",
          command=calculate_result).pack(pady=8)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text,
         justify="left", font=("Arial", 11)).pack(pady=10)

tk.Button(root, text="Clear / Reset", command=clear_all).pack(pady=8)

root.mainloop()
