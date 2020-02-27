from app import db
from app.models import Employee, Department, links

# clear the database
Employee.query.delete()
Department.query.delete()

# create employees
employee1 = Employee(first_name="Reena", last_name="Jones")
employee2 = Employee(first_name="Lava", last_name="Zgrovnever")


# create departments
department1 = Department(name="HR")
department2 = Department(name="Operations")
department3 = Department(name="Sales")


# add the employees and departments to the session
db.session.add(employee1)
db.session.add(employee2)
db.session.add(department1)
db.session.add(department2)
db.session.add(department3)
# db.session.add(link1)

# save (commit) the session
db.session.commit()




# print(employee1)
# print(employee1.first_name)
# print(employee1.last_name)
# print(employee1.departments[0])
# print(employee1.departments[1])

# print(department1)
# print(department2)
# print(employee2)
employee2.departments.append(department2)
db.session.commit()
# for department in employee2.departments:
#     print(department)
for department in employee1.departments:
    print(department)
# print(employee2.departments[1])
# add an employee to a department
# employee1.departments.append(department1)
# department1.employees.append(employee1)
# db.session.commit()
# print(employee1.departments)
# link1 = Link(employee_id=employee1.id, department_id=department1.id)

# print(department1)



# user = User.query.first()
# user.products  # List all products, eg [<productA>, <productB> ]
# user.orders    # List all orders, eg [<order1>, <order2>]
# user.orders[0].products  # List products from the first order

# p1 = Product.query.first()
# p1.users  # List all users who have bought this product, eg [<user1>, <user2>]