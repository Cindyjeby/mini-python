#!/usr/bin/env python3

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'my.password',
    'database': 'employee_db',
}

con = mysql.connector.connect(**db_config)


def check_employee(employee_id):
    sql = 'select * from empd where id=%s'
    c = con.cursor(buffered=True)
    data = (employee_id,)
    c.execute(sql, data)
    r = c.rowcount
    return r == 1


def add_employee(data):
    sql = 'insert into empd values(%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    return "Employee Added Successfully"

@app.route('/add_employee', methods=['POST'])
def api_add_employee():
    data = request.get_json()
    if not check_employee(data['Id']):
        return add_employee((data['Id'], data['Name'], data['Post'], data['Salary']))
    else:
        return "Employee already exists"

def remove_employee(employee_id):
    sql = 'delete from empd where id=%s'
    data = (employee_id,)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    return "Employee Removed"

@app.route('/remove_employee/<int:employee_id>', methods=['DELETE'])
def api_remove_employee(employee_id):
    if check_employee(employee_id):
        return remove_employee(employee_id)
    else:
        return "Employee does not exist"

def promote_employee(employee_id, amount):
    sql_select = 'select salary from empd where id=%s'
    data_select = (employee_id,)
    c = con.cursor()
    c.execute(sql_select, data_select)
    r = c.fetchone()
    if r:
        new_salary = r[0] + amount
        sql_update = 'update empd set salary=%s where id=%s'
        data_update = (new_salary, employee_id)
        c.execute(sql_update, data_update)
        con.commit()
        return "Employee Promoted"
    else:
        return "Employee does not exist"

@app.route('/promote_employee/<int:employee_id>', methods=['PUT'])
def api_promote_employee(employee_id):
    data = request.get_json()
    amount = data.get('amount', 0)
    if check_employee(employee_id):
        return promote_employee(employee_id, amount)
    else:
        return "Employee does not exist"

def display_employees():
    sql = 'select * from empd'
    c = con.cursor()
    c.execute(sql)
    employees = []
    for i in c.fetchall():
        employee = {
            "id": i[0],
            "name": i[1],
            "post": i[2],
            "salary": i[3]
        }
        employees.append(employee)
    return jsonify(employees)

@app.route('/display_employees', methods=['GET'])
def api_display_employees():
    return display_employees()


if __name__ == '__main__':
    app.run(debug=True)