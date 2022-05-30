PRAGMA FOREIGN_KEYS = ON;

DROP TABLE owners;
DROP TABLE animals;
DROP TABLE vets;

CREATE TABLE vets (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR
);

CREATE TABLE animals (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR,
  dob VARCHAR,
  animal_type VARCHAR,
  notes TEXT,
  owner VARCHAR,
    -- Can reintroduce this id I manage to get to extensions and the owner class.
    -- FOREIGN KEY  (owner_id)
    --   REFERENCES owners(id) ON DELETE CASCADE,
  vet_id INTEGER NOT NULL,
    FOREIGN KEY  (vet_id)
      REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE owners (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR,
  contact VARCHAR

);

INSERT INTO vets (name) VALUES ("Dr Jones");
INSERT INTO vets (name) VALUES ("Dr Herriot");
INSERT INTO vets (name) VALUES ("Dr Dolittle");
INSERT INTO vets (name) VALUES ("Dr Farnon");
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Buffy", "21-03-2022", "Rabbit", "Second vaccinaton due", "penny.smith@hotmail.com", 1);
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Jarvis", "12-07-2016", "Dog", "Medication prescribed for heart murmur", "jsmith69@gmail.com", 3);
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Fred", "02-01-2014", "Cat", "Operation for furballs was successfull", "bigdonny@altavista.co.uk", 2);
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Mia", "22-06-2010", "Dog", "Bloods taken. Awaiting results", "woodybabs@outlook.com", 4);
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Benji", "04-11-2019", "Dog", "Book in for follow-up visit", "jsmith69@gmail.com", 3);
INSERT INTO animals (name, dob, animal_type, notes, owner, vet_id) VALUES ("Pip", "02-04-2022", "Hamster", "Clean bill of health", "penny.smith@hotmail.com", 1);
INSERT INTO owners (name, contact) VALUES ("James Smith","jsmith69@gmail.com");
INSERT INTO owners (name, contact) VALUES ("Penny Lane","penny.smith@hotmail.com");
INSERT INTO owners (name, contact) VALUES ("Don Maclean","bigdonny@altavista.co.uk");
INSERT INTO owners (name, contact) VALUES ("Barbara Woodhouse","woodybabs@outlook.com");
