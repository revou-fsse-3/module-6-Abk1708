from app.models.employees import Employees
from app.utils.database import db


class Employees_repo:
    def get_employee_list(self):
        employees = Employees.query.all()
        return employees

    def update_employee(self, employee_id, data):
        employee_obj = Employees.query.get(employee_id)
        if not employee_obj:
            FileNotFoundError("Employee not found")
        employee_obj.name = data["name"]
        employee_obj.email = data["email"]
        employee_obj.phone = data["phone"]
        db.session.commit()
        return employee_obj
