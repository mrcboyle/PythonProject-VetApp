from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
import repositories.vet_repository as vet_repository

# CREATE

def save(vet):
    sql = "INSERT INTO vets (name) VALUES ( ?) RETURNING *"
    values = [vet.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    # what does this part do????????    
    vet.id = id
    return vet

# READ

def select_all():
    vets = [] # create an empty list
    sql = "SELECT * FROM vets"
    results = run_sql(sql) # returns rows in sql format

    for row in results:
        # convert returned SQL from above query to python list-format below
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets

def select(id):
    owner = None
    sql = "SELECT * FROM vets WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['name'], result['id'])
    return vet

# UPDATE

def update(vet):
    sql = "UPDATE vets SET (name) = ( ?) WHERE id = ?"
    values = [vet.name]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM vets WHERE id = ?"
    values = [id]
    # if values = id (above) why don't we just return id in the run_sql below?
    run_sql(sql, values)