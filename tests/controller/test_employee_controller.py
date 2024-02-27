from app import db
from app.service.employee_service import Employees_service

def test_get_employee(test_app, mocker):
    # Arrange
    mock_employee_data = [
        {
            "id": 22,
            "name": "Milton",
            "email": "miller@mail.com",
            "phone": 555789,
            "role": "Telemarketer",
        },
    ]
    mocker.patch.object(Employees_service, 'get_employees',
                        return_value=mock_employee_data)

    # Act
    with test_app.test_client() as client:
        response = client.get("/employees/")

    # Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_employee_data)
    assert response.json['data'] == mock_employee_data
    

def test_post_employees(test_app, mocker):
    # Arrange
    data = {
        "id": 1,
        "name": "Mike",
        "email": "mocca@mail.com",
        "phone": 555123,
        "role": "Telemarketer",
        "schedule": "8-6"
    }
    mocker.patch.object(Employees_service, 'post_employees', return_value=data)

    # Act
    with test_app.test_client() as client:
        response = client.post("/employees/", json=data)

    # Assert
    expected_response = {
        "name": "Mike",
        "email": "mocca@mail.com",
        "phone": 555123,
        "role": "Telemarketer",
        "schedule": "8-6"
    }
    assert response.json['data']["name"] == "Mike"
    assert response.status_code == 201
    
    
def test_post_employees_invalid_data(test_app, mocker):
    # Arrange
    data = {
        "id": 1,
        "name": 1337,
        "email": False,
        "phone": "fiveofive",
        "role": "none",
        "schedule": ""
    }
    mocker.patch.object(Employees_service, 'post_employees', return_value=data)
    
    # Act
    with test_app.test_client() as client:
        response = client.post("/employees/", json=data)
    
    # Assert
    assert response.status_code == 400
    
    
def test_put_employee_update(test_app, mocker):
    # Arrange
    data = {
        "name": "Barry",
        "email": "bigby@mail.com",
        "phone": 555456,
        "role": "Telemarketer"
    }

    mocker.patch.object(Employees_service, 'update_employees', return_value=data)

    # Act
    with test_app.test_client() as client:
            response = client.put("/employees/22", json=data)

    # Assert
    assert response.status_code == 200
    
def test_put_employee_update_invalid_data(test_app, mocker):
    
    # Arrange
    data = {
        "name": 344770,
        "email": "scuffed@mail.com",
        "phone": "fivefivefivesixsixsix",
        "role": "Some Guy"
    }
    
    mocker.patch.object(Employees_service, 'update_employees', return_value=data)
    
    # Act
    with test_app.test_client() as client:
            response = client.put("/employees/22", json=data)
            
    # Assert
    assert response.status_code == 400
    
    
def test_delete_employee(test_app, mocker):
    # Arrange
    expected_response = {
        "name": "Barry",
        "email": "bigby@mail.com",
        "phone": 555456,
        "role": "Telemarketer"
    }

    mocker.patch.object(Employees_service, 'delete_employees', return_value=expected_response)
    with test_app.test_client() as client:
        # Act
        response = client.delete("/employees/23")

    # Assert
    assert response.status_code == 200
    
def test_delete_employee_not_found(test_app, mocker):
    # Arrange
    expected_response = "Employee not found"

    mocker.patch.object(Employees_service, 'delete_employees', return_value=expected_response)
    
    with test_app.test_client() as client:
        # Act
        response = client.delete("/employees/123")

    # Assert
    assert response.status_code == 404
    assert response.json['data'] == "Unavailable employee"
