import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import random

# Function to create the database and tables
def create_database():
    try:
        conn = sqlite3.connect('timetable.db')
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Teachers (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Subjects (
            subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_name TEXT NOT NULL,
            teacher_id INTEGER,
            FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classrooms (
            classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_name TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS TimeSlots (
            slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_of_week TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL
        );
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Timetable (
            timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            teacher_id INTEGER,
            slot_id INTEGER,
            classroom_id INTEGER,
            FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id),
            FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id),
            FOREIGN KEY (slot_id) REFERENCES TimeSlots(slot_id),
            FOREIGN KEY (classroom_id) REFERENCES Classrooms(classroom_id)
        );
        ''')

        conn.commit()
    except Exception as e:
        print(f"Error creating database: {e}")
    finally:
        conn.close()

# Function to get DB connection
def get_db_connection():
    try:
        conn = sqlite3.connect('timetable.db')
        conn.row_factory = sqlite3.Row
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")

# Function to add teacher to the database
def add_teacher(teacher_name_entry):
    try:
        teacher_name = teacher_name_entry.get()
        if teacher_name:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Teachers (teacher_name) VALUES (?)', (teacher_name,))
            conn.commit()
            messagebox.showinfo("Success", "Teacher added successfully!")
            teacher_name_entry.delete(0, tk.END)
            populate_teachers()
        else:
            messagebox.showwarning("Input Error", "Please enter a teacher name.")
    except Exception as e:
        print(f"Error adding teacher: {e}")

# Function to delete a teacher from the database
def delete_teacher():
    try:
        teacher_id = delete_teacher_combobox.get().split()[0]
        if teacher_id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM Timetable WHERE teacher_id = ?', (teacher_id,))
            cursor.execute('DELETE FROM Subjects WHERE teacher_id = ?', (teacher_id,))
            cursor.execute('DELETE FROM Teachers WHERE teacher_id = ?', (teacher_id,))
            conn.commit()
            messagebox.showinfo("Success", "Teacher and associated data deleted!")
            populate_teachers()
    except Exception as e:
        print(f"Error deleting teacher: {e}")

# Function to add subject to the database
def add_subject(subject_name_entry, teacher_combobox):
    try:
        subject_name = subject_name_entry.get()
        teacher_id = teacher_combobox.get().split()[0]
        if subject_name and teacher_id:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Subjects (subject_name, teacher_id) VALUES (?, ?)', (subject_name, teacher_id))
            conn.commit()
            messagebox.showinfo("Success", "Subject added successfully!")
            subject_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter subject and select a teacher.")
    except Exception as e:
        print(f"Error adding subject: {e}")

# Function to add classroom to the database
def add_classroom(classroom_name_entry):
    try:
        classroom_name = classroom_name_entry.get()
        if classroom_name:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO Classrooms (room_name) VALUES (?)', (classroom_name,))
            conn.commit()
            messagebox.showinfo("Success", "Classroom added successfully!")
            classroom_name_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a classroom name.")
    except Exception as e:
        print(f"Error adding classroom: {e}")

# Function to generate time slots
def generate_time_slots(day_combobox, start_time_entry, end_time_entry):
    day = day_combobox.get()
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()

    if day and start_time and end_time:
        conn = get_db_connection()
        cursor = conn.cursor()

        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))

        current_hour = start_hour

        while current_hour < end_hour:
            slot_start = f"{current_hour:02d}:{start_minute:02d}"
            current_hour += 1
            slot_end = f"{current_hour:02d}:{start_minute:02d}"

            cursor.execute('INSERT INTO TimeSlots (day_of_week, start_time, end_time) VALUES (?, ?, ?)',
                           (day, slot_start, slot_end))

        conn.commit()
        messagebox.showinfo("Success", "Time Slots generated successfully!")
    else:
        messagebox.showwarning("Input Error", "Please enter day, start time, and end time.")

# Function to generate timetable for a specific day
def generate_timetable_for_day(delete_day_combobox):
    day = delete_day_combobox.get()
    if not day:
        messagebox.showwarning("Input Error", "Please select a day.")
        return

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('DELETE FROM Timetable WHERE slot_id IN (SELECT slot_id FROM TimeSlots WHERE day_of_week = ?)', (day,))
        
        cursor.execute('SELECT teacher_id, teacher_name FROM Teachers')
        teachers = cursor.fetchall()

        cursor.execute('SELECT subject_id, subject_name, teacher_id FROM Subjects')
        subjects = cursor.fetchall()

        cursor.execute('SELECT slot_id FROM TimeSlots WHERE day_of_week = ?', (day,))
        slots = cursor.fetchall()

        cursor.execute('SELECT classroom_id, room_name FROM Classrooms')
        classrooms = cursor.fetchall()

        if not slots or not classrooms or not subjects or not teachers:
            messagebox.showwarning("No Data", "Please ensure you have available teachers, subjects, slots, and classrooms.")
            return

        assigned_slots = set()

        for teacher in teachers:
            teacher_id = teacher['teacher_id']
            available_subjects = [s for s in subjects if s['teacher_id'] == teacher_id]

            for subject in available_subjects:
                available_slots = [s for s in slots if s['slot_id'] not in assigned_slots]

                if not available_slots:
                    break

                assigned_slot = random.choice(available_slots)
                assigned_classroom = random.choice(classrooms)

                cursor.execute('''INSERT INTO Timetable (subject_id, teacher_id, slot_id, classroom_id)
                                  VALUES (?, ?, ?, ?)''',
                               (subject['subject_id'], teacher_id, assigned_slot['slot_id'], assigned_classroom['classroom_id']))
                assigned_slots.add(assigned_slot['slot_id'])

        conn.commit()
        messagebox.showinfo("Success", f"Timetable for {day} generated successfully!")
        generate_timetable()  # Refresh the displayed timetable
    except Exception as e:
        print(f"Error generating timetable: {e}")
    finally:
        conn.close()

# Function to generate timetable and display it in the Treeview widget
def generate_timetable():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT s.subject_name, t.teacher_name, ts.day_of_week, ts.start_time, ts.end_time, c.room_name
    FROM Timetable tt
    JOIN Subjects s ON tt.subject_id = s.subject_id
    JOIN Teachers t ON tt.teacher_id = t.teacher_id
    JOIN TimeSlots ts ON tt.slot_id = ts.slot_id
    JOIN Classrooms c ON tt.classroom_id = c.classroom_id
    ORDER BY ts.day_of_week, ts.start_time;
    ''')

    timetable = cursor.fetchall()
    conn.close()

    for item in timetable_tree.get_children():
        timetable_tree.delete(item)

    for row in timetable:
        timetable_tree.insert('', 'end', values=(row['subject_name'], row['teacher_name'], row['day_of_week'], row['start_time'], row['end_time'], row['room_name']))

# Fetch teachers for the combobox
def populate_teachers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT teacher_id, teacher_name FROM Teachers')
    teachers = cursor.fetchall()
    conn.close()

    teacher_list = [f"{teacher['teacher_id']} - {teacher['teacher_name']}" for teacher in teachers]
    delete_teacher_combobox['values'] = teacher_list
    teacher_combobox['values'] = teacher_list

# Function to open the dashboard GUI
def open_dashboard():
    try:
        global delete_teacher_combobox, teacher_combobox, timetable_tree

        dashboard_root = tk.Tk()
        dashboard_root.title("School Timetable Generator")

        frame_top = tk.Frame(dashboard_root,bg="lightblue")
        frame_top.pack(pady=20)

        # Add teacher section
        tk.Label(frame_top, text="Add Teacher", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=5)
        teacher_name_entry = tk.Entry(frame_top)
        teacher_name_entry.grid(row=0, column=1, padx=5)
        tk.Button(frame_top, text="Add Teacher", command=lambda: add_teacher(teacher_name_entry), bg='lightgreen', fg='black').grid(row=0, column=2, padx=5)

        tk.Label(frame_top, text="Select Teacher to Delete:", font=("Helvetica", 12,"bold")).grid(row=1, column=0, padx=5)
        delete_teacher_combobox = ttk.Combobox(frame_top)
        delete_teacher_combobox.grid(row=1, column=1, padx=5)
        tk.Button(frame_top, text="Delete Teacher", command=delete_teacher, bg='red', fg='black').grid(row=1, column=2, padx=5)

        # Add subject section
        tk.Label(frame_top, text="Add Subject", font=("Helvetica", 12, "bold")).grid(row=2, column=0, padx=5)
        subject_name_entry = tk.Entry(frame_top)
        subject_name_entry.grid(row=2, column=1, padx=5)

        teacher_combobox = ttk.Combobox(frame_top)
        teacher_combobox.grid(row=2, column=2, padx=5)
        tk.Button(frame_top, text="Add Subject", command=lambda: add_subject(subject_name_entry, teacher_combobox), bg='lightgreen', fg='black').grid(row=2, column=3, padx=5)

        # Add classroom section
        tk.Label(frame_top, text="Add Classroom", font=("Helvetica", 12, "bold")).grid(row=3, column=0, padx=5)
        classroom_name_entry = tk.Entry(frame_top)
        classroom_name_entry.grid(row=3, column=1, padx=5)
        tk.Button(frame_top, text="Add Classroom", command=lambda: add_classroom(classroom_name_entry), bg='lightgreen', fg='black').grid(row=3, column=2, padx=5)

        # Generate time slots section
        tk.Label(frame_top, text="Generate Time Slots", font=("Helvetica", 12, "bold")).grid(row=4, column=0, padx=5)
        day_combobox = ttk.Combobox(frame_top, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        day_combobox.grid(row=4, column=1, padx=5)
        start_time_entry = tk.Entry(frame_top)
        start_time_entry.grid(row=4, column=2, padx=5)
        start_time_entry.insert(0, "HH:MM")  # Placeholder text
        end_time_entry = tk.Entry(frame_top)
        end_time_entry.grid(row=4, column=3, padx=5)
        end_time_entry.insert(0, "HH:MM")  # Placeholder text
        tk.Button(frame_top, text="Generate Time Slots", command=lambda: generate_time_slots(day_combobox, start_time_entry, end_time_entry), bg='lightgreen', fg='black').grid(row=4, column=4, padx=5)

        # Generate timetable section
        tk.Label(frame_top, text="Generate Timetable for Day", font=("Helvetica", 12, "bold")).grid(row=5, column=0, padx=5)
        delete_day_combobox = ttk.Combobox(frame_top, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        delete_day_combobox.grid(row=5, column=1, padx=5)
        tk.Button(frame_top, text="Generate Timetable", command=lambda: generate_timetable_for_day(delete_day_combobox), bg='lightgreen', fg='black').grid(row=5, column=2, padx=5)

        # Timetable display section
        timetable_tree = ttk.Treeview(dashboard_root, columns=("Subject", "Teacher", "Day", "Start Time", "End Time", "Classroom"), show="headings")
        timetable_tree.heading("Subject", text="Subject")
        timetable_tree.heading("Teacher", text="Teacher")
        timetable_tree.heading("Day", text="Day")
        timetable_tree.heading("Start Time", text="Start Time")
        timetable_tree.heading("End Time", text="End Time")
        timetable_tree.heading("Classroom", text="Classroom")
        timetable_tree.pack(pady=20)

        create_database()  # Initialize the database
        populate_teachers()  # Load teachers into comboboxes
        dashboard_root.mainloop()
    except Exception as e:
        print(f"Error opening dashboard: {e}")

if __name__ == "__main__":
    open_dashboard()