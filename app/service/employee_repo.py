from app.repositories.employee_repo import Employees_repo

class Employees_service:
    def __init__(self):
        self.employee_repo = Employees_repo()
        
    def get_employees(self):
        employee = self.employee_repo.get_employee_list()
        return employee
    
    def update_employee(self, employee_id, data):
        updated_employee = self.employee_repo.update_animal_list(employee_id, data)
        return updated_employee