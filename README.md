# HR Database with Flask and Sqlalchemy
I've created this web app to learn how to use many-to-many relationships with Sqlalchemy and Flask. The use case for the app is for someone in an organisation's Human Resources department. The app would be used to help them view, edit and delete employee records.

## Methodological Thoughts
It is perhaps a bit strange to create a many-to-many relationship between employees and departments: in organisations large enough to have separate departments, I imagine that each employee is only attached to one department. However, for the sake of practising many-to-many relationships, let's imagine this is a small organisation in which employees have to switch between departments. What's important here is learning the pattern of many-to-many relationships: the pattern could be transferred to other relationships, for example skills/experience (an employee has many skills and a skill can be linked to many employees.  

## Use Case for this App
The imagined user would be someone working in an HR department who needs to manage a database of employees. The user should be able to:
* View all employees :white_check_mark:
* View all departments :white_check_mark:
* For each department, view all the employees :white_check_mark:
* For each employee, view all the departments they work for :white_check_mark:
* Delete employees :heavy_exclamation_mark:
* Delete departments :heavy_exclamation_mark:
* Edit employee details ::heavy_exclamation_mark:
* Edit department details :heavy_exclamation_mark:
* Add an employee to a department :heavy_exclamation_mark:
* Add a department to an employee :heavy_exclamation_mark:
* Delete an employee from a department :heavy_exclamation_mark:
* Delete a department from an employee :heavy_exclamation_mark:

### Key
* :white_check_mark: success! I have achieved this feature.
* :heavy_exclamation_mark: I have been able to achieve this feature to some extent, but not completely. 

## Areas I Would Like to Work on in Future
In the web app the user can edit an employee's/department's name details, but not their connection to the other class. So, you can't edit an employee's departments, and you can't edit a department's employees. However, you can do this if you are directly saving data to the seeds file.

In the web app the user can delete an employee or department that is not linked to the other class. So, you can delete an employee who is not in a department. 

In the web app the user can add an employee or department, but only their names. You can't add the connection to the other class through the web app.
 

