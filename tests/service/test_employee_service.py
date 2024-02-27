from app.controller.employee.schema.create_employee_request import Create_employee_request
from app.models.employees import Employees
from app.service.employee_service import Employees_service
from app.repositories.employee_repo import Employees_repo

def test_get_employee_list_success(test_app, mocker):
    """service get customer success"""

    # Arrange
    mock_employee_data = [
        Employees(id=1, name='Steve', email='steve@mail.com', phone=555069, role='Telemarketer', schedule='9-5'),
        Employees(id=2, name='Brad', email='brad@mail.com', phone=555420, role='Telemarketer', schedule='9-5'),
    ]
    mocker.patch.object(Employees_repo, 'get_employee_list',
                        return_value=mock_employee_data)
    
    # Act
    with test_app.test_request_context():
        employee_service = Employees_service().get_employees()

    # Assert
    assert len(employee_service) == 2
    assert employee_service[0]['name'] == 'Steve'
    assert employee_service[1]['role'] == 'Telemarketer'
    
def test_post_employees_success(test_app, mocker):
    """service get customer success"""
    # Arrange
    mock_employee_data = Employees(id=2, name='Jeff', email='jeff@mail.com', phone=555268, role='Telemarketer', schedule='1-9')
    mocker.patch.object(Employees_repo, 'add_employee_list', return_value=mock_employee_data)
    
    create_data = Create_employee_request(name='Jeff', email='jeff@mail.com', phone=555268, role='Telemarketer', schedule='1-9')

    # Act
    with test_app.test_request_context():
        employee_service_create = Employees_service().post_employees(create_data)
        
    # Assert
    assert employee_service_create['id'] == 2
    assert employee_service_create['name'] == 'Jeff'
    assert employee_service_create['role'] == 'Telemarketer'