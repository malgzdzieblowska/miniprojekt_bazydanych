#Napisz zapytanie SQL, którym wyświetlisz mail użytkownika o id 5

import datetime
import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

stmt = """SELECT email FROM user WHERE id = 5;"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor(dictionary=True) as cursor:
            cursor.execute(stmt)
            result = cursor.fetchone()
            if result:
                print("Adres email użytkownika o id 5:", result['email'])
            else:
                print("Użytkownik o podanym id nie został znaleziony.")

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

