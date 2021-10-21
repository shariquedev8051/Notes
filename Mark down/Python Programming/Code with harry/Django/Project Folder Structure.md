#### What Is __init__.py?

- Django generates this file for us. It is mandatory to have an  __inti__.py file in a directory to denote that the project is a python  package and can be imported into other files. This file usually remains  empty.
- If this file gets missing, you will see a “package not found error” in the absence of this file.

#### What Is settings.py?

- This is the core file of our Django projects.
- It contains the configuration values which are needed by web apps to work properly, such as database settings, static files location,  template location, etc. We will keep coming to this file to edit the  project configuration throughout this course.

#### What is urls.py?

- Url declaration and mapping are made under this file.

#### What is wsgi.py?

- WSGI stands for web-server gateway interface.
- WSGI is a specification that describes the communication between a web server and a web application.

#### What is manage.py?

- Command-line utility for performing administrative tasks.
- We will be using manage.py frequently while developing a Django project.