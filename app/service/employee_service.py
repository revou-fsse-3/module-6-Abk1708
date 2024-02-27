# from app.repositories.employee_repo import Employees_repo

# class Employees_service:
#     def __init__(self):
#         self.employee_repo = Employees_repo()
        
#     def get_employees(self):
#         employees = self.employee_repo.get_employee_list()
#         return [employee.as_dict() for employee in employees]
    
#     def update_employee(self, employee_id, data):
#         updated_employee = self.employee_repo.update_employee(employee_id, data)
#         return updated_employee.as_dict()
from app.repositories.employee_repo import Employees_repo
from app.models.employees import Employees

class Employees_service:
    def __init__(self):
        self.employees_repo = Employees_repo()
        
    def post_employees(self, data):
        employee = Employees()
        
        employee.name = data.name
        employee.email = data.email
        employee.phone = data.phone
        employee.role = data.role
        employee.schedule = data.schedule
        
        created_employee = self.employees_repo.add_employee_list(employee)
        return created_employee.as_dict()
    
    def get_employees(self):
        employees = self.employees_repo.get_employee_list()
        return [employee.as_dict() for employee in employees]
    
    def update_employees(self, employee_id, data):
        updated_employee = self.employees_repo.update_employee_list(employee_id, data)
        return updated_employee.as_dict()
    
    def delete_employees(self, employee_id):
        employee = Employees.query.get(employee_id)
        if not employee:
            return "Employee not found"

        deleted_employee = self.employees_repo.delete_employee_list(employee_id)
        return deleted_employee.as_dict()