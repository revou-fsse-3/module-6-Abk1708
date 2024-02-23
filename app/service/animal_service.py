from app.repositories.animal_repo import Animals_repo
from app.models.animals import Animals

class Animals_service:
    def __init__(self):
        self.animals_repo = Animals_repo()
        
    def post_animals(self, data):
        animal = Animals()
        
        animal.species = data.species
        animal.age = data.age
        animal.gender = data.gender
        animal.special_requirements = data.special_requirements
        
        created_animal = self.animals_repo.add_animal_list(animal)
        return created_animal.as_dict()
    
    def get_animals(self):
        animals = self.animals_repo.get_animal_list()
        return [animal.as_dict() for animal in animals]
    
    def update_animals(self, animal_id, data):
        updated_animal = self.animals_repo.update_animal_list(animal_id, data)
        return updated_animal.as_dict()
    
    def delete_animals(self, animal_id):
        animal = Animals.query.get(animal_id)
        if not animal:
            return "Animal not found"

        deleted_animal = self.animals_repo.delete_animal_list(animal_id)
        return deleted_animal.as_dict()