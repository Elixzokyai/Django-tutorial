DJANGO
THis is a python web framework (a software framework that simplifies the development of web apps by providing a structure and common components (tools and libs to handle common web dev tasks) )
routing : mapping url routes to various pages or functionalities
Authentication : authorization , identity
Database integration and interaction
Session Management
Form Handling
Examples Backend Frameworks

NodeJS
Python (Flask and Django)
PHP (Laravel)
Ruby on Rails
GO (GIN, ECHO)
Frontend Framework

React JS
Next JS
Angular
Vue
A DJANGO WEBSITE
This typically consists of a single Project , that is then spilt into separates apps Instagram (case study)

user management : Logging in and out , registering , forgot password
media features : upload, edit and display media
messaging : send messages
django apps are structured to separate the logic pieces

django supports the architecural pattern of MVC.

Models : define the data. This is usually the database description and often the base layer to an app.
Views : display some or all data and also enable client interaction. HTML AND CSS things
Controllers : handles how the database and the views interact
django recognizes above as an MVT pattern

Models : define the data. This is usually the database description and often the base layer to an app.
Views : url mapping logic
Templates : HTML and CSS ,
Conclusion:
A django site starts off as a project , and its built up with a number of apps that handle separate functionalities. Each app follows the MVT pattern.

Tools to work with django
Python - python --version python3 --version

pip - pip install django

python -m django --version

How to create to django projects
python -m django-admin startproject PROJECTNAME

How to run the django server
cd projectname
python manage.py runserver
How to add an app
python manage.py startapp todo
next register the app to the project , in settings.py on project folder add it to the installed apps list
How to map models to database tables (applying migrations)
Define the model
make the migrations ( python manage.py makemigrations )
apply the migrations ( python manage.py migrate )


## object relationships
defining how different object can interact with one another
common types relationshios amongst objects
1. Association
description : A general relationship where one object uses another, often described as a 'has' relationship
one object can old reference to another


scenario
- libraries :


## SQL : structured Query language
The standard language for interacting with realations database
1. manage and manupulates data stored in tables
2. 2. SQL supports the CRUD operations


