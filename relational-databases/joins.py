import sqlite3

connection = sqlite3.connect("joins.db")
cursor = connection.cursor()

def create_table(table_name, *columns):
    col = ""
    for column in columns:
        col += column
        col += ', '
    col = col[:-2]
    query = f"CREATE TABLE {table_name}({col})"
    print(query)
    cursor.execute(query)

def delete_table(table_name):
    cursor.execute(f"DROP TABLE {table_name}")

def delete_database(database_name):
    cursor.execute(f"DROP DATABASE {database_name}")

def insert(table_name, columns, values):
    val = 
    query = f"""INSERT INTO ({columns}) VALUES ()"""
    print(query)
    cursor.execute(query, values)
    connection.commit()

create_table('student', 'enroll_nb', 'student_name', 'address')
create_table('student_course', 'course_id', 'enroll_nb')

insert('student', (), ('1001', 'John', 'California'))

delete_table('student')
delete_table('student_course')

connection.close()