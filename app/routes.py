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

# add an employee
@app.route('/employees', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    # department = request.form.get('department')
    # department_id = request.form.get('department_id')
    # department_id = request.form['department_id']
    new_department = request.form.get('department')
    newEmployee = Employee(first_name=first_name, last_name=last_name)
    # new_department = Department.query.filter_by(id=department_id).first() 
    db.session.add(newEmployee)
    db.session.commit()
    newEmployee.departments.append(new_department)
    db.session.commit()
    return redirect('/employees')

# edit employee. I've decided to focus on the names here. I will use a different method for editing the departments.
@app.route('/employees/<int:employee_id>/update', methods=['POST'])
def update_employee(employee_id):
    new_first_name = request.form.get("new_first_name")
    new_last_name = request.form.get("new_last_name")
    employee_id = request.form.get("employee_id")
    employee = Employee.query.filter_by(id=employee_id).first()
    employee.first_name = new_first_name
    employee.last_name = new_last_name
    db.session.commit()
    return redirect('/employees')

# add a department to an employee - on hold
# @app.route('/employees/<int:employee_id>/add_department', methods=['GET', 'POST'])
# def add_department_to_employee(employee_id, department_id):
# def add_department_to_employee(employee_id, department):
# def add_department_to_employee():
    # departments = Department.query.all()
    # employee_id = request.form.get("employee_id")
    # employee_id = request.form['employee_id']
    # department_id = request.form.get("department_id")
    # department = request.form.get("department")
    # department = request.form["department"]
    # employee = Employee.query.filter_by(id=employee_id).first()
    # department = Department.query.filter_by(id=department_id).first()
    # employee.departments.append(department) 
    # db.session.commit()
    # return redirect('/employees')


# function to remove a department from an employee.
# @app.route('/employees/<int:employee_id>/remove_department', methods=['POST'])
# def remove_department(employee_id):
#     department = request.form.get("department") # should this be id? does it need to be an argument?
#     employee_id = request.form.get("employee_id")
#     employee = Employee.query.filter_by(id=employee_id).first()
#     employee.remove(department)
#     db.session.commit()
#     return redirect('/employees')


# function to delete an employee
@app.route('/employees/<int:employee_id>/delete', methods=['POST'])
def delete_employee(employee_id):
    employee_to_delete = Employee.query.get(employee_id)
    db.session.delete(employee_to_delete)
    db.session.commit()
    return redirect('/employees')



# departments routes
@app.route('/departments')
def show_departments():
    employees = Employee.query.all()
    departments = Department.query.all()
    return render_template('departments.html', title="Departments", employees=employees, departments=departments)

# add a department
@app.route('/departments', methods=['POST'])
def add_department():
    name = request.form['name']
    newDepartment = Department(name=name)
    db.session.add(newDepartment)
    db.session.commit()
    return redirect('/departments')

@app.route('/departments/<int:department_id>/update', methods=['POST'])
def update_department(department_id):
    new_name = request.form.get("new_name")
    department_id = request.form.get("department_id")
    department = Department.query.filter_by(id=department_id).first()
    department.name = new_name
    db.session.commit()
    return redirect('/departments')


# function to delete a department
@app.route('/departments/<int:department_id>/delete', methods=['POST'])
def delete_department(department_id):
    department_to_delete = Department.query.get(department_id)
    db.session.delete(department_to_delete)
    db.session.commit()
    return redirect('/departments')

