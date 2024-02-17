from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employees import Employees
from app.utils.api_response import api_response
from app.service.employee_service import Employees_service

employee_blueprint = Blueprint("employee_endpoint", __name__)

@employee_blueprint.route("/", methods=["POST"])
def post_employee():
    try :
        data = request.json
        employee = Employees()
        employee.name = data["name"]
        employee.email = data["email"]
        employee.phone = data["phone"]
        employee.role = data["role"]
        employee.schedule = data["schedule"]
        db.session.add(employee)
        db.session.commit()
        return 'success', 200
    except Exception as e:
        return e, 500

@employee_blueprint.route("/", methods=["GET"])
def get_employee():
    employee_service = Employees_service()
    employees = employee_service.get_employees()
    return api_response(employees, 200, "success")
    
@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    try:
        employee = Employees.query.get(employee_id)

        if not employee:
            return "Employee not found", 404

        return employee.as_dict(), 200
    except Exception as e:
        return str(e), 500
    
@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def put_employee(employee_id):
    try:
        employee_service = Employees_service()
        employee = Employees()
        
        data = request.json

        employee.name = data.get("name", employee.name)
        employee.email = data.get("email", employee.email)
        employee.phone = data.get("phone", employee.phone)

        updatedEmployee = employee_service.update_employee(employee_id, data)
        return api_response(updatedEmployee, 200, "success")
    except Exception as e:
        return str(e), 500


@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def employee_customer(employee_id):
    try:
        employee = Employees.query.get(employee_id)

        if not employee:
            return "Animal not found", 404

        db.session.delete(employee)
        db.session.commit()

        return 'Delete successful', 200
    except Exception as e:
        return str(e), 500
