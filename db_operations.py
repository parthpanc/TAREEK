import sqlite3

def create_table():
    connection = sqlite3.connect("cases.db")
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            last_hearing_date TEXT,
            waiting_time INTEGER
        )
    ''')

    connection.commit()
    connection.close()

def insert_case(case_number, case_type, last_hearing_date, waiting_time):
    connection = sqlite3.connect("cases.db")
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO cases (case_type, last_hearing_date, waiting_time)
        VALUES (?, ?, ?)
    ''', (case_type, last_hearing_date, waiting_time))

    case_number = cursor.lastrowid

    connection.commit()
    connection.close()

    return case_number

def print_table():
    connection = sqlite3.connect("cases.db")
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM cases')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    connection.close()

# Uncomment the line below if you want to create the table
# create_table()
# Uncomment the line below if you want to insert a sample case
# case_number = insert_case("Murder", "2023-01-01", 30)
# print(f"Case inserted with case number: {case_number}")
# Uncomment the line below if you want to print the contents of the table
# print_table()
