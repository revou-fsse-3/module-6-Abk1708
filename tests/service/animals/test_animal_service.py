from app.controller.animal.schema.create_animal_request import Create_animal_request
from app.models.animals import Animals
from app.service.animal_service import Animals_service
from app.repositories.animal_repo import Animals_repo

def test_get_animal_list_success(test_app, mocker):
    """service get customer success"""

    # Arrange
    mock_animal_data = [
        Animals(id=1, species='Capybara', age=4, gender='Male', special_requirements='Fur Combing'),
        Animals(id=2, species='Capybara', age=2, gender='Male', special_requirements='Fur Combing'),
    ]
    mocker.patch.object(Animals_repo, 'get_animal_list',
                        return_value=mock_animal_data)
    
    # Act
    with test_app.test_request_context():
        animal_service = Animals_service().get_animals()

    # Assert
    assert len(animal_service) == 2
    assert animal_service[0]['species'] == 'Capybara'
    assert animal_service[1]['gender'] == 'Male'
    
def test_post_animals_success(test_app, mocker):
    """service get customer success"""
    # Arrange
    mock_animal_data = Animals(id=2, species='Capybara', age=3, gender='Female', special_requirements='Coconut')
    mocker.patch.object(Animals_repo, 'add_animal_list', return_value=mock_animal_data)
    
    create_data = Create_animal_request(species='Capybara', age=3, gender='Female', special_requirements='Coconut')

    # Act
    with test_app.test_request_context():
        animal_service_create = Animals_service().create_customer(create_data)
        
    # Assert
    assert animal_service_create['id'] == 2
    assert animal_service_create['species'] == 'Capybara'
    assert animal_service_create['gender'] == 'Female'