from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.animal import Animal
from models.vet import Vet
import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route("/animals")
def animals():
    animals = animal_repository.select_all() # NEW
    return render_template("animals/index.html", animals = animals)

@animals_blueprint.route("/animals",  methods=['POST'])
def create_animal():
    animal_name = request.form['animal_name']
    animal_type = request.form['animal_type']
    date_of_birth = request.form['date_of_birth']
    owner = request.form['owner']
    vet_id = request.form['vet_id']
    notes = request.form['notes']
    vet = vet_repository.select(vet_id)
    a = animal_repository.select(animal_name)
    b = animal_repository.select(date_of_birth)
    c = animal_repository.select(animal_type)
    d = animal_repository.select(notes)
    e = animal_repository.select(owner)
    new_animal = Animal(a, b, c, d, e, vet)
    animal_repository.save(new_animal)
    return redirect('/animals')    

@animals_blueprint.route("/animals/<id>")
def show(id):
    animal = animal_repository.select(id)
    vets = animal_repository.vets(animal)
    return render_template("animals/show.html", animal=animal, vets=vets)
