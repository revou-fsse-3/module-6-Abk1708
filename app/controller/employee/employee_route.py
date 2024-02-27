# from flask import Blueprint, jsonify, request
# from app.utils.database import db
# from app.models.employees import Employees
# from app.utils.api_response import api_response
# from app.service.employee_service import Employees_service

# employee_blueprint = Blueprint("employee_endpoint", __name__)

# @employee_blueprint.route("/", methods=["POST"])
# def post_employee():
#     try :
#         data = request.json
#         employee = Employees()
#         employee.name = data["name"]
#         employee.email = data["email"]
#         employee.phone = data["phone"]
#         employee.role = data["role"]
#         employee.schedule = data["schedule"]
#         db.session.add(employee)
#         db.session.commit()
#         return 'success', 200
#     except Exception as e:
#         return e, 500

# @employee_blueprint.route("/", methods=["GET"])
# def get_employee():
#     employee_service = Employees_service()
#     employees = employee_service.get_employees()
#     return api_response(employees, 200, "success")
    
# @employee_blueprint.route("/<int:employee_id>", methods=["GET"])
# def get_employee_by_id(employee_id):
#     try:
#         employee = Employees.query.get(employee_id)

#         if not employee:
#             return "Employee not found", 404

#         return employee.as_dict(), 200
#     except Exception as e:
#         return str(e), 500
    
# @employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
# def put_employee(employee_id):
#     try:
#         employee_service = Employees_service()
        
#         data = request.json

#         updatedEmployee = employee_service.update_employee(employee_id, data)
#         return api_response(updatedEmployee, 200, "success")
#     except Exception as e:
#         return str(e), 500


# @employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
# def employee_customer(employee_id):
#     try:
#         employee = Employees.query.get(employee_id)

#         if not employee:
#             return "Employee not found", 404

#         db.session.delete(employee)
#         db.session.commit()

#         return 'Delete successful', 200
#     except Exception as e:
#         return str(e), 500

from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employees import Employees
from app.utils.api_response import api_response
from app.service.employee_service import Employees_service
from app.controller.employee.schema.update_employee_request import Update_employee_request
from app.controller.employee.schema.create_employee_request import Create_employee_request
from pydantic import ValidationError

employee_blueprint = Blueprint("employee_endpoint", __name__)

@employee_blueprint.route("/", methods=["POST"])
def post_employee():
    try:

        data = request.json
        update_employee_request = Create_employee_request(**data)

        employee_service = Employees_service()

        employees = employee_service.post_employees(update_employee_request)

        return api_response(
            status_code=201,
            message="updated",
            data=employees
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )


@employee_blueprint.route("/", methods=["GET"])
def get_employee():
    try:
        employee_service = Employees_service()

        employees = employee_service.get_employees()

        return api_response(
            status_code=200,
            message="",
            data=employees
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
        
@employee_blueprint.route("/<int:employee_id>", methods=["GET"])
def get_employee_by_id(employee_id):
    try:
        employee = Employees.query.get(employee_id)

        if not employee:
            return "Employee not found", 404

        return employee.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=employee
        )
    
@employee_blueprint.route("/<int:employee_id>", methods=["PUT"])
def put_employee(employee_id):
    try:

        data = request.json
        update_employee_request = Update_employee_request(**data)

        employee_service = Employees_service()

        employees = employee_service.update_employees(
            employee_id, update_employee_request)

        return api_response(
            status_code=200,
            message="updated",
            data=employees
        )
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )


@employee_blueprint.route("/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        employee_service = Employees_service()

        employee = employee_service.delete_employees(employee_id)
        if employee == "Employee not found":
            return api_response(
                status_code=404,
                message=employee,
                data="Unavailable employee"
            )
        return api_response(
            status_code=200,
            message="deleted",
            data=employee
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
