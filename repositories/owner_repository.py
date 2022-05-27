from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
import repositories.owner_repository as owner_repository

# CREATE

def save(owner):
    sql = "INSERT INTO owners (name, contact) VALUES ( ?, ?) RETURNING *"
    values = [owner.name, owner.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    # what does this part do????????    
    owner.id = id
    return owner

# READ

def select_all():
    owners = [] # create an empty list
    sql = "SELECT * FROM owners"
    results = run_sql(sql) # returns rows in sql format

    for row in results:
        # convert returned SQL from above query to python list-format below
        owner = Owner(row['name'], row['contact']), row['id']
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = ?"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        owner = Owner(result['name'], result['contact'], result['id'])
    return owner

# UPDATE

def update(owner):
    sql = "UPDATE owners SET (name, contact) = ( ?, ?) WHERE id = ?"
    values = [owner.name, owner.contact]
    run_sql(sql, values)

# DELETE

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM owners WHERE id = ?"
    values = [id]
    # if values = id (above) why don't we just return id in the run_sql below?
    run_sql(sql, values)