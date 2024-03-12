import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'


INSERT_USER_COURSE = """
INSERT INTO user_course (user_id, course_id, enrollment_date) VALUE 
(%s, %s, %s);
"""

USER_COURSE = [
    (1,1,'2024-01-20'),
    (1,3,'2024-03-15'),
    (2,2,'2024-02-25'),
    (3,4,'2024-04-10'),
    (4,5,'2024-05-20'),
    (5,3,'2024-03-20'),
    (5,5,'2024-06-01')
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_USER_COURSE, USER_COURSE)
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








