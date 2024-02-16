from app.models.animals import Animals
from app.utils.database import db

class Animals_repo:
    def add_animal_list(self, animal, data):
        animal.species = data["species"]
        animal.age = data["age"]
        animal.gender = data["gender"]
        animal.special_requirements = data["special_requirements"]
        db.session.add(animal)
        db.session.commit()
        return {"message": "Success posting animal"}, 200
    
    def get_animal_list(self):
        animals = Animals.query.all()
        return animals
    
    def get_animal_list_by_id(self, animal_id):
        animal = Animals.query.get(animal_id)

        if not animal:
            return {"message": "Animal not found"}, 404
        return animal.as_dict(), 200
    
    def update_animal_list(self, animal_id, animal):
        animal = Animals.query.get(animal_id)
        if not animal:
            return {"message": "Animal not found"}, 404
        animal.species = animal.species
        animal.age = animal.age
        animal.gender = animal.gender

        db.session.add(animal)
        db.session.commit()

        return {"message": "Update successful"}, 200
    
    def delete_animal_list(self, animal_id):
        animal = Animals.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        db.session.delete(animal)
        db.session.commit()

        return {"message": "Delete successful"}, 200