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

## steps on creation
1. create and register the second app to our project
python manage.py startapp todo_api
2. install DRF (djangorestframework)
pip install djangorestframework
3. models
user : one to many relationship
tag  : many to many relationship with todos
tasks: data to define our todos

5. set up of serializers

Key features of REST
Stateless : Each request from a client contains all the info. needed to process it and the server does not store any CLIENT state
HTTP methods : Common methods
GET : Retrieve Data
POST : Create the new data
PUT/PATCH : Update data
Delete : Delete Data
Resources : Everything is treated as a resource (e.g. users , products ) and each has a unique URL
Format : Typically uses JSON or XML for data exchange
JSON (Javascript Object Notation)
JSON is a lightweight data-interchange format. Widely used in API for data exchange

JSON OBJECT -> { "key" : "value" }

JSON ARRAY [ { "key" : "value" }, { "key" : "value" }, { "key" : "value" } ]

Approach to Developing APIS
Understand Requirements
identify what the API needs to do.
Designing the API
REST way , GraphQL
design the route and specify input/output
API versioning and documentation (SWAGGER ? POSTMAN)
Build the API
select the framework to use (DJANGO , EXPRESS IN JS ,FLASK )
Implement the endpoints '/tasks' '/task/int:id' usingt the HTTP methods
validations and if necessary implement authentication.
Test the API
test the api for performance , security, and proper data handling tools (POSTMAN)
Deploy and maintain for live use.
DJANGO APPROACH TO BUILDING THE APIS
Django REST Framework
DRF is a powerful and flexible toolkit for building web apps in DJANGO Steps
Install DRF : pip install djangorestframework
Define models for data
Create serializers to convert btw JSON and model instances
Define API Views and use DRF generic views for common patterns
use routers to handle URL Routing
Using core DJANGO
popular for simpler project
DJANGO built in JSONRESPONSE and your simple views for routing functionality
Steps for creation
Create and register the second app to our project python manage.py startapp todo_api
Install DRF (djangorestframework) pip install djangorestframework
Models :
user : one to many relationship todos
tag : many to many relationship with todos
tasks : data to define todos.
task : buy groceries tag : urgent, personal

A task can have multiple tags
A tag can be associated to multiple tasks
tag : urgent Buy Groceries , Pay bills

Make the migrations python manage.py makemigrations python manage.py migrate

Set up of serializers a. create a serializers.py file

Create the viewsets in view.py

Create the urls.py file for our app

Create the urls paths for the app

Register the apps urls to the project urls

Test : using a tool like POSTMAN then run the project and test the endpoints.

open settings, get to the marketplace , search and install postman~~~~
Serializers
-Serializers are used to convert model instances to simple python data types e.g. list , dictionary , which enables them to be easily rendered into JSON

Conversely, serializers also handle converting incoming data back into django model instances for saving into database Summary a. Serialization : Converting python object i.e. model instance into JSON for API responses b. deserialization : converting incoming python objects into model instances for creating or updating records
Types of serializers in DRF (DJANGO REST FRAMEWORK)
ModelSerializer
Class that acts a shortcut i.e. it auto. generates and validates fields based on the model
Standard Serializer
Used when we need more control over the serialization process
Does not depend on the model for validation and generation , i.e. needs explicit definations.
