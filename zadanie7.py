import mysql.connector
from mysql.connector import connect, errorcode

USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'


INSERT_USER_PROFILE = """
INSERT INTO user_profile (id, user_id, first_name, last_name, address, phone_number, registration_date) VALUE 
(%s, %s, %s, %s, %s, %s, %s);
"""

USER_PROFILE = [
    (1, 1,'John','Doe','123 Main St, Anytown','555-1234','2023-01-15'),
    (2, 2,'Jane','Smith','456 Oak St, Anycity','555-5678','2023-02-20'),
    (3, 3,'Mike','Jones','789 Elm St, Anycity','555-9012','2023-03-10'),
    (4, 4,'Emily','White','101 Pine St, Anytown','555-3456','2023-04-05'),
    (5, 5,'Alex','Brown','202 Maple St, Anycity','555-7890','2023-05-12')
]

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.executemany(INSERT_USER_PROFILE, USER_PROFILE)
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








