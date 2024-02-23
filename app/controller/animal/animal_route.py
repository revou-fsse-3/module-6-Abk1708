from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.animals import Animals
from app.utils.api_response import api_response
from app.service.animal_service import Animals_service
from app.controller.animal.schema.update_animal_request import Update_animal_request
from app.controller.animal.schema.create_animal_request import Create_animal_request
from pydantic import ValidationError

animal_blueprint = Blueprint("animal_endpoint", __name__)

@animal_blueprint.route("/", methods=["POST"])
def post_animal():
    # try :
    #     data = request.json
    #     animal = Animals()
    #     animal.species = data["species"]
    #     animal.age = data["age"]
    #     animal.gender = data["gender"]
    #     animal.special_requirements = data["special_requirements"]
    #     db.session.add(animal)
    #     db.session.commit()
    #     return 'success', 200
    # except Exception as e:
    #     return e, 500
    try:

        data = request.json
        update_animal_request = Create_animal_request(**data)

        animal_service = Animals_service()

        animals = animal_service.post_animals(update_animal_request)

        return api_response(
            status_code=201,
            message="updated",
            data=animals
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


@animal_blueprint.route("/", methods=["GET"])
def get_animal():
    # animal_service = Animals_service()
    # animals = animal_service.get_animals()
    # return api_response(animals, 200, "success")

    try:
        animal_service = Animals_service()

        animals = animal_service.get_animals()

        return api_response(
            status_code=200,
            message="",
            data=animals
        )

    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )
        
@animal_blueprint.route("/<int:animal_id>", methods=["GET"])
def get_animal_by_id(animal_id):
    try:
        animal = Animals.query.get(animal_id)

        if not animal:
            return "Animal not found", 404

        return animal.as_dict(), 200
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data=animal
        )
    
@animal_blueprint.route("/<int:animal_id>", methods=["PUT"])
def put_animal(animal_id):
    # try:
    #     animal_service = Animals_service()
        
    #     data = request.json

    #     updatedAnimal = animal_service.update_animals(animal_id, data)

    #     return api_response(updatedAnimal, 200, "success")
    # except Exception as e:
    #     return str(e), 500
    try:

        data = request.json
        update_animal_request = Update_animal_request(**data)

        animal_service = Animals_service()

        animals = animal_service.update_animals(
            animal_id, update_animal_request)

        return api_response(
            status_code=200,
            message="updated",
            data=animals
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


@animal_blueprint.route("/<int:animal_id>", methods=["DELETE"])
def animal_customer(animal_id):
    # try:
    #     animal = Animals.query.get(animal_id)

    #     if not animal:
    #         return "Animal not found", 404

    #     db.session.delete(animal)
    #     db.session.commit()

    #     return 'Delete successful', 200
    # except Exception as e:
    #     return str(e), 500
    try:
        animal_service = Animals_service()

        animal = animal_service.delete_animals(animal_id)
        if animal == "Animal not found":
            return api_response(
                status_code=404,
                message=animal,
                data="Unavailable animal"
            )
        return api_response(
            status_code=200,
            message="deleted",
            data=animal
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )

