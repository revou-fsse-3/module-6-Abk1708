from app.repositories.animal_repo import Animals_repo

class Animals_service:
    def __init__(self):
        self.animals_repo = Animals_repo()
        
    def post_animals(self):
        animals = self.animals_repo.add_animal_list()
        return animals
    
    def get_animals(self):
        animals = self.animals_repo.get_animal_list()
        return [animal.as_dict() for animal in animals]
    
    def update_animals(self, animal_id, data):
        updated_animal = self.animals_repo.update_animal_list(animal_id, data)
        return updated_animal