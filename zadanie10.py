#Napisz zapytanie SQL, które znajdzie wszystkich użytkowników , którzy są zapisani na kurs o id=5

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

stmt = """SELECT c.id AS Course_id, up.first_name AS Name, up.last_name AS Surname, c.title FROM user_course as uc JOIN
user_profile up ON uc.user_id = up.id JOIN
course as c ON uc.course_id=c.id
WHERE c.id = 5;"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor(dictionary = True) as cursor:
            cursor.execute(stmt)

            for row in cursor:
                print(row)

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

