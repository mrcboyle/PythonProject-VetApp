import pdb      
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet

import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.owner_repository as owner_repository

owner_repository.delete_all()
# animal_repository.delete_all()
# vet_repository.delete_all()

# CREATE Test

# vet1 = Vet("Dr Jones")
# vet_repository.save(vet1)
# vet2 = Vet("Dr Herriot")
# vet_repository.save(vet2)
# vet3 = Vet("Dr Dolittle")
# vet_repository.save(vet3)
# vet4 = Vet("Dr Farnon")
# vet_repository.save(vet4)

for vet in vet_repository.select_all():
    print(vet.__dict__)

# animal1 = Animal("Buffy", "21-03-2022", "Rabbit", "Second vaccinaton due")
# animal_repository.save(animal1)
# animal2 = Animal("Jarvis", "12-07-2016", "Dog", "Medication prescribed for heart murmur")
# animal_repository.save(animal2)
# animal3 = Animal("Fred", "02-01-2014", "Cat", "Operation for furballs was successfull")
# animal_repository.save(animal3)
# animal4 = Animal("Mia", "22-06-2010", "Dog", "Bloods taken. Awaiting results")
# animal_repository.save(animal4)
# animal5 = Animal("Benji", "04-11-2019", "Dog", "Book in for follow-up visit")
# animal_repository.save(animal5)
# animal6 = Animal("Pip", "02-04-2022", "Hamster", "Clean bill of health")
# animal_repository.save(animal6)

# for animal in animal_repository.select_all():
#     print(animal.__dict__)

owner1 = Owner("James Smith","jsmith69@gmail.com")
owner_repository.save(owner1)
owner2 = Owner("Penny Lane","penny.smith@hotmail.com")
owner_repository.save(owner2)
owner3 = Owner("Don Maclean","bigdonny@altavista.co.uk")
owner_repository.save(owner3)
owner4 = Owner("Barbara Woodhouse","woodybabs@outlook.com")
owner_repository.save(owner4)

for owner in owner_repository.select_all():
    print(owner.__dict__)

# READ Test

# owner_repository.select_all()
# animal_repository.select_all()
# vet_repository.select_all()

# UPDATE Test

# animal1 = Animal("Plant seeds", user1, 30)
# animal_repository.save(animal1)
# animal2 = Animal("Plant seeds", user1, 30)
# animal_repository.save(animal2)

# DELETE Test

# animal_repository.delete(animal2.id)

pdb.set_trace()