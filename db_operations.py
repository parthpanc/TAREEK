import sqlite3

DB_FILE = "cases.db"

def create_table():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_number INTEGER,                
                case_type TEXT,
                last_hearing_date TEXT,
                waiting_time INTEGER
            )
        ''')

def insert_case(case_number, case_type, last_hearing_date, waiting_time):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO cases (case_number, case_type, last_hearing_date, waiting_time)
            VALUES (?, ?, ?, ?)
        ''', (case_number, case_type, last_hearing_date, waiting_time))

        case_number = cursor.lastrowid

    return case_number

def print_table():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM cases')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

if __name__ == "__main__":
    create_table()
    case_number = insert_case("M", "2024-03-12", 10)
    print(f"Inserted case with case_number: {case_number}")
    print("Current cases in the database:")
    print_table()
