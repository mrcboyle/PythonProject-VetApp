from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all()
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>", methods=['GET'])
def show(id):
    vet = vet_repository.select(id)
    return render_template("vets/show.html", vet=vet)


@vets_blueprint.route("/vets/new", methods=['GET'])
def new_vet():
    vets = vet_repository.select_all()
    return render_template("vets/new.html", vets = vets)

@vets_blueprint.route("/vets",  methods=['POST'])
def create_vet():
    name    = request.form['name']
    vet     = Vet(name)
    vet_repository.save(vet)
    return redirect('/vets')

# DELETE
# DELETE '/animals/<id>'
@vets_blueprint.route("/vets/delete/<id>", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')    