#!/usr/bin/env python3

import mysql.connector

db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'my.password',
        'database': 'employee_db',
}

con = mysql.connector.connect(**db_config)


cursor = con.cursor()

employee_data = [
    (1, 'Sumit', 'Manager', 70000),
    (2, 'Rahul', 'Assistant Manager', 40000),
    (3, 'Neha', 'Receptionist', 30000),
    (4, 'Manish', 'Electrician', 20000),
    (5, 'Parul', 'Accountant', 50000),
]

insert_query = 'INSERT INTO empd (id, name, post, salary) VALUES (%s, %s, %s, %s)'

cursor.executemany(insert_query, employee_data)
con.commit()
cursor.close()
con.close()
