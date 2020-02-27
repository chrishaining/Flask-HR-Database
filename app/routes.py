from app import app
from app.models import Employee, Department, links 
from flask import render_template, redirect, request
from sqlalchemy import update

@app.route('/')
def index():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('index.html', title="Home", employees=employees, departments=departments)

@app.route('/employees')
def show_employees():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('employees.html', title="Home", employees=employees, departments=departments)

@app.route('/departments')
def show_departments():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('departments.html', title="Home", employees=employees, departments=departments)