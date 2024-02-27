from app import db
from app.service.animal_service import Animals_service

def test_get_animal(test_app, mocker):
    # Arrange
    mock_animal_data = [
        {
            "id": 22,
            "species": "Rhino",
            "age": 7,
            "gender": "Male"
        },
    ]
    mocker.patch.object(Animals_service, 'get_animals',
                        return_value=mock_animal_data)

    # Act
    with test_app.test_client() as client:
        response = client.get("/animals/")

    # Assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_animal_data)
    assert response.json['data'] == mock_animal_data
    

def test_post_animals(test_app, mocker):
    # Arrange
    data = {
        "id" : 1,
        "species": "Snake",
        "age": 6,
        "gender": "Male",
        "special_requirements": "Alive Food"
    }
    mocker.patch.object(Animals_service, 'post_animals', return_value=data)

    # Act
    with test_app.test_client() as client:
        response = client.post("/animals/", json=data)

    # Assert
    expected_response = {
        "species": "Snake",
        "age": 6,
        "gender": "Male",
        "special_requirements": "Alive Food"
    }
    assert response.json['data']["species"] == "Snake"
    assert response.status_code == 201
    
    
def test_post_animals_invalid_data(test_app, mocker):
    # Arrange
    data = {
        "id" : 1,
        "species": 1337,
        "age": "six",
        "gender": "IDK",
        "special_requirements": "Either this"
    }
    mocker.patch.object(Animals_service, 'post_animals', return_value=data)
    
    # Act
    with test_app.test_client() as client:
        response = client.post("/animals/", json=data)
    
    # Assert
    assert response.status_code == 400
    
    
def test_put_animal_update(test_app, mocker):
    # Arrange
    data = {
        "species": "Bear",
        "age": 6,
        "gender": "Male",
    }

    mocker.patch.object(Animals_service, 'update_animals', return_value=data)

    # Act
    with test_app.test_client() as client:
            response = client.put("/animals/22", json=data)

    # Assert
    assert response.status_code == 200
    
def test_put_animal_update_invalid_data(test_app, mocker):
    
    # Arrange
    data = {
        "species": 30081,
        "age": "six",
        "gender": "Unknown",
    }
    
    mocker.patch.object(Animals_service, 'update_animals', return_value=data)
    
    # Act
    with test_app.test_client() as client:
            response = client.put("/animals/22", json=data)
            
    # Assert
    assert response.status_code == 400
    
    
def test_delete_animal(test_app, mocker):
    # Arrange
    expected_response = {
        "species": "Bear",
        "age": 6,
        "gender": "Male"
    }

    mocker.patch.object(Animals_service, 'delete_animals', return_value=expected_response)
    with test_app.test_client() as client:
        # Act
        response = client.delete("/animals/23")

    # Assert
    assert response.status_code == 200

def test_delete_animal_not_found(test_app, mocker):
    # Arrange
    expected_response = "Animal not found"

    mocker.patch.object(Animals_service, 'delete_animals', return_value=expected_response)
    
    with test_app.test_client() as client:
        # Act
        response = client.delete("/animals/123")

    # Assert
    assert response.status_code == 404
    assert response.json['data'] == "Unavailable animal"