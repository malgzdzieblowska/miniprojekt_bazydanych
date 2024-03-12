import mysql.connector
from mysql.connector import connect, errorcode


USER = 'root'
PASSWORD = 'admin'
DB = 'course_management'

CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS user(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
);
"""

CREATE_COURSE_TABLE = """
CREATE TABLE IF NOT EXISTS course(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT NOT NULL,
    start_date DATE,
    end_date DATE
);
"""

CREATE_USER_COURSE_TABLE = """
CREATE TABLE IF NOT EXISTS user_course(
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (course_id) REFERENCES course(id)
);
"""

CREATE_USER_PROFILE_TABLE = """
CREATE TABLE IF NOT EXISTS user_profile(
    id INT PRIMARY KEY,
    user_id INT NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(20),
    registration_date DATE,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
"""

try:
    with connect(user=USER, password=PASSWORD, database=DB) as cnx:
        with cnx.cursor() as cursor:
            cursor.execute(CREATE_USER_TABLE)
            cursor.execute(CREATE_COURSE_TABLE)
            cursor.execute(CREATE_USER_COURSE_TABLE)
            cursor.execute(CREATE_USER_PROFILE_TABLE)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")
    elif err.errno == errorcode.ER_PARSE_ERROR:
        print("SQL syntax error\n",err)
    else:
        print("An Error occured\n", err)

else:
    print("Done")