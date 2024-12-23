import sqlite3

# Function to create the database and tables
def create_database():
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()

    # Create Teachers table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        teacher_name TEXT NOT NULL
    );
    ''')

    # Create Subjects table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Subjects (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
    );
    ''')

    # Create Classrooms table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Classrooms (
        classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
        room_name TEXT NOT NULL
    );
    ''')

    # Create TimeSlots table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TimeSlots (
        slot_id INTEGER PRIMARY KEY AUTOINCREMENT,
        day_of_week TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL
    );
    ''')

    # Create Timetable table
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
    conn.close()

create_database()
