from app import db
from flask_sqlalchemy import SQLAlchemy 


links = db.Table('links',
    db.Column('employee.id', db.Integer, db.ForeignKey('employee.id')),
    db.Column('department.id', db.Integer, db.ForeignKey('department.id'))

)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64), index=True)
    departments = db.relationship('Department', secondary=links, backref='employee', lazy='dynamic')

    # departments = db.relationship('Department', backref='employee', lazy='dynamic')

    def __repr__(self):
        return '<Employee {} {}>'.format(self.first_name, self.last_name)

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    # employees = db.relationship('Employee', secondary = 'link')
    employees = db.relationship('Employee', secondary=links, backref='department', lazy='dynamic')

    def __repr__(self):
        return '<{} Department>'.format(self.name)


        # create a class to link an employee to a department
# class Link(db.Model):

    # id = db.Column(db.Integer, primary_key=True)
    # employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    # department_id = db.Column(db.Integer, db.ForeignKey('department.id'))


    # employee = db.relationship(Employee, backref='link') 
    # department = db.relationship(Department, backref='link')