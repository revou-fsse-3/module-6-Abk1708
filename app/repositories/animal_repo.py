from app.models.animals import Animals
from app.utils.database import db

class Animals_repo:
    def add_animal_list(self, animal):
        db.session.add(animal)
        db.session.commit()
        return animal
    
    def get_animal_list(self):
        animals = Animals.query.all()
        return animals
    
    def get_animal_list_by_id(self, animal_id):
        animal = Animals.query.get(animal_id)

        if not animal:
            raise FileNotFoundError("Animal not found")
        return animal.as_dict(), 200
    
    # def update_animal_list(self, animal_id, data):
    #     animal_obj = Animals.query.get(animal_id)
    #     if not animal_obj:
    #         raise FileNotFoundError("Animal not found")
    #     animal_obj.species = data["species"]
    #     animal_obj.age = data["age"]
    #     animal_obj.gender = data["gender"]

    #     db.session.commit()

    #     return animal_obj
    
    def update_animal_list(self, animal_id, animal):
        animal_obj = Animals.query.get(animal_id)
        animal_obj.species = animal.species
        animal_obj.age = animal.age
        animal_obj.gender = animal.gender

        db.session.commit()
        return animal_obj
    
    def delete_animal_list(self, animal_id):
        animal_obj = Animals.query.get(animal_id)

        if not animal_obj:
            raise FileNotFoundError("Animal not found")

        db.session.delete(animal_obj)
        db.session.commit()

        return animal_obj