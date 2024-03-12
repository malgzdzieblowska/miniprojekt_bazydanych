import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'


INSERT_USERS = """
INSERT INTO user (username, email ) VALUE 
(%s, %s);
"""

USERS = [
    ('john_doe','john@example.com'),
    ('jane_smith','jane@example.com'),
    ('mike_jones','mike@example.com'),
    ('emily_white','emily@example.com'),
    ('alex_brown','alex@example.com')
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_USERS, USERS)
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



