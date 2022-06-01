Assignment

Vet Management App
A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

MVP
The practice wants to be able to register / track animals. Important information for the vets to know is -
Name
Date Of Birth (use a VARCHAR initially)
Type of animal
Contact details for the owner
Treatment notes
Be able to assign animals to vets
CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?


How to Run

1: In VS Code, CD to python_project_vet
2: Create the database by using the following command sqlite3 db/vet_surgery.db < db/vet_surgery.sql
    Some data has been included in the .sql file to seed the database
3: Enter flask run to start the web server
4: In Google Chrome, browse to http://127.0.0.1:5000/ and the webpage should load.
