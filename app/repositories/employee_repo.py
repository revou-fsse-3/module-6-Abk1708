# from app.models.employees import Employees
# from app.utils.database import db


# class Employees_repo:
#     def get_employee_list(self):
#         employees = Employees.query.all()
#         return employees

#     def update_employee(self, employee_id, data):
#         employee_obj = Employees.query.get(employee_id)
#         if not employee_obj:
#             FileNotFoundError("Employee not found")
#         employee_obj.name = data["name"]
#         employee_obj.email = data["email"]
#         employee_obj.phone = data["phone"]
#         db.session.commit()
#         return employee_obj
from app.models.employees import Employees
from app.utils.database import db

class Employees_repo:
    def add_employee_list(self, employee):
        db.session.add(employee)
        db.session.commit()
        return employee
    
    def get_employee_list(self):
        employees = Employees.query.all()
        return employees
    
    def get_employee_list_by_id(self, employee_id):
        employee = Employees.query.get(employee_id)

        if not employee:
            raise FileNotFoundError("Employee not found")
        return employee.as_dict(), 200
    
    def update_employee_list(self, employee_id, employee):
        employee_obj = Employees.query.get(employee_id)
        employee_obj.name = employee.name
        employee_obj.email = employee.email
        employee_obj.phone = employee.phone

        db.session.commit()
        return employee_obj
    
    def delete_employee_list(self, employee_id):
        employee_obj = Employees.query.get(employee_id)

        if not employee_obj:
            raise FileNotFoundError("Employee not found")

        db.session.delete(employee_obj)
        db.session.commit()

        return employee_obj
