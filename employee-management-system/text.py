#!/usr/bin/env python3
import mysql.connector

# Update these values with your actual MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'my.password',
    'database': 'employee_db',
}

try:
    # Establish a connection to the MySQL server
    con = mysql.connector.connect(**db_config)

    # Create a cursor object to execute SQL queries
    cursor = con.cursor()

    # Your SQL queries and operations here...

    # Commit changes and close the cursor and connection
    con.commit()
    cursor.close()
    con.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")
