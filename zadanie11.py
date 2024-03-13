#Napisz zapytanie SQL, które wyświetli wszystkie kursy użytkownika o id=5, które jeszcze się nie rozpoczęły

import datetime
import mysql.connector
from mysql.connector import connect, errorcode
from datetime import datetime

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

stmt = """SELECT uc.course_id AS Course_id, c.title AS Title, c.start_date FROM user_course as uc JOIN
course c ON uc.course_id = c.id 
WHERE uc.user_id = 5 AND c.start_date > now();"""

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

