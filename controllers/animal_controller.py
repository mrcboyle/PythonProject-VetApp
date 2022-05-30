from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all()
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals",  methods=['POST'])
def create_animal():
    name            = request.form['name']
    # vet_id        = request.form['vet_id']
    date_of_birth   = request.form['date_of_birth']
    animal_type     = request.form['animal_type']
    owner           = request.form['owner']      
    notes           = request.form['notes']
    vet             = vet_repository.select(request.form['vet_id'])
    animal          = Animal(name, vet, date_of_birth, animal_type, owner, notes)
    animal_repository.save(animal)
    return redirect('/animals/index.html')

@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animal=animal, vets=vets)
