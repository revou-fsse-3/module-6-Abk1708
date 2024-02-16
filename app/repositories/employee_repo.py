from app.models.employees import Employees
from app.utils.database import db


class Employees_repo:
    def get_employee_list(self):
        employees = Employees.query.all()
        return employees

    def update_employee(self, employee_id, employee):
        employee = Employees.query.get(employee_id)
        if not employee:
            return {"message": "User does not exist"}, 404
        employee.name = employee.name
        employee.email = employee.email
        employee.phone = employee.phone
        db.session.add(employee)
        db.session.commit()
        return {"message": "Success update user"}, 201
