from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.animals import Animals
from app.utils.api_response import api_response
from app.service.animal_service import Animals_service

animal_blueprint = Blueprint("animal_endpoint", __name__)

@animal_blueprint.route("/", methods=["POST"])
def post_animal():
    try :
        data = request.json
        animal = Animals()
        animal.species = data["species"]
        animal.age = data["age"]
        animal.gender = data["gender"]
        animal.special_requirements = data["special_requirements"]
        db.session.add(animal)
        db.session.commit()
        return 'success', 200
    except Exception as e:
        return e, 500

@animal_blueprint.route("/", methods=["GET"])
def get_animal():
    animal_service = Animals_service()
    animals = animal_service.get_animals()
    return api_response(animals, 200, "success")
    
@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal_by_id(animal_id):
    try:
        animal = Animals.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        return animal.as_dict(), 200
    except Exception as e:
        return str(e), 500
    
@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def put_animal(animal_id):
    try:
        animal_service = Animals_service()
        animal = Animals()
        
        data = request.json

        animal.species = data.get("species", animal.species)
        animal.age = data.get("phone", animal.age)
        animal.gender = data.get("gender", animal.gender)

        updatedAnimal = animal_service.update_animals(animal_id, data)

        return api_response(updatedAnimal, 200, "success")
    except Exception as e:
        return str(e), 500


@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def animal_customer(animal_id):
    try:
        animal = Animals.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        db.session.delete(animal)
        db.session.commit()

        return 'Delete successful', 200
    except Exception as e:
        return str(e), 500
