# HR Database with Flask and Sqlalchemy

I've created this app to learn how to use many-to-many relationships with Sqlalchemy and Flask. 

## Use Case for this App
The imagined user would be someone working in an HR department who needs to manage a database of employees. The user should be able to:
* View all employees 
* View all departments
* For each department, view all the employees
* For each employee, view all the departments they work for. 
* Delete employees
* Delete departments
* Edit employee details
* Edit department details
* Add an employee to a department
* Add a department to an employee
* Delete an employee from a department
* Delete a department from an employee

## Methodological Thoughts

It is perhaps a bit strange to create a many-to-many relationship between employees and departments: in organisations large enough to have separate departments, I imagine that each employee is only attached to one department. However, for the sake of practising many-to-many relationships, let's imagine this is a small organisation in which employees have to switch between departments. What's important here is learning the pattern of many-to-many relationships: the pattern could be transferred to other relationships, for example skills/experience (an employee has many skills and a skill can be linked to many employees.  