#!/usr/bin/env python3

import mysql-connector

db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'my.password',
        'database': 'employee_db',
}

con = mysql.connector.connect(**db_config)
