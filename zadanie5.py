import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'


INSERT_COURSES = """
INSERT INTO course (title, description, start_date, end_date) VALUE 
(%s, %s, %s, %s);
"""

COURSES = [
    ('Matematyka podstawowa ','Kurs z podstaw matematyki dla początkujących.','2024-01-01','2024-03-01'),
    ('Historia sztuki','Wprowadzenie do historii sztuki i jej głównych nurtów.','2024-02-15','2024-05-15'),
    ('Programowanie w języku Python','Kurs programowania w języku Python dla początkujących.','2024-03-10','2024-06-10'),
    ('Angielski dla zaawansowanych ','Kurs angielskiego dla osób posługujących się językiem na poziomie zaawansowanym.','2024-04-01','2024-07-01'),
    ('Marketing internetowy', 'Omówienie podstawowych technik marketingu w internecie.','2024-05-15','2024-08-15')
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_COURSES, COURSES)
            cnx.commit()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists.")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n", err)
    else:
        print("An error occured\n", err)
else:
    print("Done.")








