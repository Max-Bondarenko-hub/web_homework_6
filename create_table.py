from connection import create_connection


def create_table(connection, create_table_sql):
    # try:
    cursor = connection.cursor()
    cursor.execute(create_table_sql)
    connection.commit()
    # except:
    # print('some error')


if __name__ == "__main__":
    sql_create_groups_table = """CREATE TABLE IF NOT EXISTS group_names (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name CHAR(4)
        );"""
    sql_create_students_table = """CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30),
        age INT,
        group_id INT,
        FOREIGN KEY (group_id) REFERENCES group_names (id) 
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );"""
    sql_create_professors_table = """CREATE TABLE IF NOT EXISTS professors (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(30),
        disc_id INT,
        FOREIGN KEY (disc_id) REFERENCES disceplines (id) 
            ON UPDATE CASCADE
            ON DELETE CASCADE        
        );"""
    sql_create_disceplines_table = """CREATE TABLE IF NOT EXISTS disceplines (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(15),
        group_id INT,
        FOREIGN KEY (group_id) REFERENCES group_names (id) 
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );"""
    sql_create_grades_table = """CREATE TABLE IF NOT EXISTS grades (
        id INT PRIMARY KEY AUTO_INCREMENT,
        student_name VARCHAR(30),
        discipline_name VARCHAR(15),
        grade INT,
        student_id INT,
        FOREIGN KEY (student_id) REFERENCES students (id) 
            ON UPDATE CASCADE
            ON DELETE CASCADE
        );"""

    with create_connection() as connection:
        if connection is not None:
            create_table(connection, sql_create_groups_table)
            create_table(connection, sql_create_disceplines_table)
            create_table(connection, sql_create_students_table)
            create_table(connection, sql_create_professors_table)
            create_table(connection, sql_create_grades_table)
        else:
            print("Error! cannot create the database connection.")

