## 0x00. AirBnB clone - The console
# Learning Objectives
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function
# Description
# Writing a command interpreter to manage AirBnB objects.
This is the first step towards building a first full web application: the AirBnB clone. This first step is very important because what is built during this project will be used with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:
* put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine
