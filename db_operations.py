# import sqlite3
# from datetime import datetime, timedelta

# DB_FILE = "cases.db"

# def create_table():
#     with sqlite3.connect(DB_FILE) as connection:
#         cursor = connection.cursor()

#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS cases (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 case_number INTEGER,
#                 case_type TEXT,
#                 last_hearing_date TEXT,
#                 waiting_time INTEGER,
#                 priority INTEGER,
#                 next_hearing_date TEXT
#             )
#         ''')

# def insert_case(case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date):
#     with sqlite3.connect(DB_FILE) as connection:
#         cursor = connection.cursor()

#         cursor.execute('''
#             INSERT INTO cases (case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date))

#         case_id = cursor.lastrowid

#     return case_id

# def schedule_next_hearing_date(waiting_time, priority, last_hearing_date):
#     last_hearing_datetime = datetime.strptime(last_hearing_date, "%d-%m-%Y")
#     days_to_add = {
#         1: 30,
#         2: 20,
#         3: 10
#     }[priority]
#     next_hearing_date = last_hearing_datetime + timedelta(days=days_to_add)

#     while count_cases_on_date(next_hearing_date.strftime("%d-%m-%Y")) >= 5:
#         next_hearing_date += timedelta(days=1)

#     return next_hearing_date.strftime("%d-%m-%Y")

# def count_cases_on_date(date):
#     with sqlite3.connect(DB_FILE) as connection:
#         cursor = connection.cursor()

#         cursor.execute('''
#             SELECT COUNT(*) FROM cases
#             WHERE next_hearing_date = ?
#         ''', (date,))

#         return cursor.fetchone()[0]

# def update_next_hearing_date(case_id, next_hearing_date):
#     with sqlite3.connect(DB_FILE) as connection:
#         cursor = connection.cursor()

#         cursor.execute('''
#             UPDATE cases
#             SET next_hearing_date = ?
#             WHERE id = ?
#         ''', (next_hearing_date, case_id))

# def print_table():
#     with sqlite3.connect(DB_FILE) as connection:
#         cursor = connection.cursor()

#         cursor.execute('SELECT * FROM cases')
#         rows = cursor.fetchall()
#         for row in rows:
#             print(row)

# if __name__ == "__main__":
#     create_table()
#     case_number = insert_case("M", "12-03-2024", 10, 2, 3, None)
#     print(f"Inserted case with case_number: {case_number}")
#     next_hearing_date = schedule_next_hearing_date(20, 3, "12-03-2024")
#     print(f"Next hearing date: {next_hearing_date}")
#     update_next_hearing_date(case_number, next_hearing_date)
#     print_table()


import sqlite3
from datetime import datetime, timedelta

DB_FILE = "cases.db"

def create_table():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_type TEXT,
                last_hearing_date TEXT,
                waiting_time INTEGER,
                priority INTEGER,
                next_hearing_date TEXT
            )
        ''')

def insert_case(case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            INSERT INTO cases (case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (case_number, case_type, last_hearing_date, waiting_time, priority, next_hearing_date))

        case_id = cursor.lastrowid

    return case_id


def schedule_next_hearing_date(waiting_time, priority, last_hearing_date):
    last_hearing_datetime = datetime.strptime(last_hearing_date, "%m/%d/%y")
    days_to_add = {
        1: 30,
        2: 20,
        3: 10
    }[priority]
    next_hearing_date = last_hearing_datetime + timedelta(days=days_to_add)

    while count_cases_on_date(next_hearing_date.strftime("%m/%d/%y")) >= 5:
        next_hearing_date += timedelta(days=1)

    return next_hearing_date.strftime("%m/%d/%y")

def count_cases_on_date(date):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            SELECT COUNT(*) FROM cases
            WHERE next_hearing_date = ?
        ''', (date,))

        return cursor.fetchone()[0]

def update_next_hearing_date(case_id, next_hearing_date):
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('''
            UPDATE cases
            SET next_hearing_date = ?
            WHERE id = ?
        ''', (next_hearing_date, case_id))

def print_table():
    with sqlite3.connect(DB_FILE) as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM cases')
        rows = cursor.fetchall()
        for row in rows:
            print(row)

if __name__ == "__main__":
    create_table()
    case_number = insert_case("M", "12/03/24", 10, 2, None)
    print(f"Inserted case with case_number: {case_number}")
    next_hearing_date = schedule_next_hearing_date(20, 3, "12/03/24")
    print(f"Next hearing date: {next_hearing_date}")
    update_next_hearing_date(case_number, next_hearing_date)
    print_table()