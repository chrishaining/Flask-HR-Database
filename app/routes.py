from app import app, db
from app.models import Employee, Department, links 
from flask import render_template, redirect, request
from sqlalchemy import update

@app.route('/')
def index():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('index.html', title="Home", employees=employees, departments=departments)

# employees routes
@app.route('/employees')
def show_employees():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('employees.html', title="Employees", employees=employees, departments=departments)


@app.route('/employees', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    newEmployee = Employee(first_name=first_name, last_name=last_name)
    db.session.add(newEmployee)
    db.session.commit()
    return redirect('/employees')


# departments routes
@app.route('/departments')
def show_departments():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('departments.html', title="Departments", employees=employees, departments=departments)