- [1. The Django ;)](#1-the-django-)
  - [1.1. CMD](#11-cmd)
    - [1.1.1. Folder directory](#111-folder-directory)
  - [1.2. working with your project](#12-working-with-your-project)
    - [1.2.1. Open terminal in vscode](#121-open-terminal-in-vscode)
    - [Creating app in Django](#creating-app-in-django)
  - [4.python manage.py sqlmigrate app1 0001 -- will give you querries](#4python-managepy-sqlmigrate-app1-0001----will-give-you-querries)
- [2. HTML](#2-html)
  - [Adding hyperlinks](#adding-hyperlinks)
- [Vscode usefull shortcuts](#vscode-usefull-shortcuts)
- [Built_in function example](#built_in-function-example)
  - [os.walk](#oswalk)








# 1. The Django ;)
```python
The secret of getting ahead is  
Getting started....
```
## 1.1. CMD
1. Activate python environment..
2. Do not exit the cmd and go to Django project folder
3. You can use  ***pip freezee***  to check installed packages
4. To check python version type  ***python --version*** 
5. Type followin code in cmd
6. use *cd* for selecting directory and *cd..*  coming out of current directory
```python
django-admin startproject project_name
```
### 1.1.1. Folder directory
<span style = "color:yellow">***Note: Always kill the powershell and open a new terminal***<span>

 Project/folder/directory structure:
 - project_name --folder --root directory  
   - __init__.py -- empty python file --  
   - asgi.py -- asynchronous -- 
   - wsgi.py -- web server gateway interface -- changes
   - urls.py -- registers urls
   - settings.py -- project settings -- databse settings --
 - manage.py -- python file -- command line utility file -- interact with your project

## 1.2. working with your project
- open folder containg your project
- open it in vscode
- select python interpreter of b5_env or whatever name your environment have
<!-- <span style = "color:yellow">Text</span> -->
note:You can use os.walk() shows tree directory
### 1.2.1. Open terminal in vscode 
Terminal - new terminal..
- choose directory where *pythone.py* reside
- type -- *python manage.py* -- so you can see commands and subcommands
- type -- *python manage.py help* -- so you can see commands and subcommands
- type -- *python manage.py check* -- to find if there is any issue
- type -- *python manage.py runserver* -- check the file first and then runs server
- ctrl + c -- to break the runserver
- *python manage.py runserver 3306* -- To change the port to 3306 always check free port befor changing the default port.
- *python manage.py migrate* it will genrate sql queries
- if your see <span style = "color:yellow">**name_id**</span> it is an foreign key just saying
>Q:What is python package?
>Ans: It is a collection of modules. Related modules are placed in same folder.
### Creating app in Django
1. <span style = "color:yellow">***python manage.py startapp app1***</span> to create app in django
2. <span style = "color:yellow">***python manage.py migrate***</span> to genrate querry for database
3. <span style = "color:yellow">***python manage.py makemigrations***</span> to genrate tables  
 <span style = "color:yellow">Note: To avoid opening shell as a default terminal press F1-> Terminal defualt profile-> Select cmd</span>
 4.python manage.py sqlmigrate app1 0001 -- will give you querries
---
# 2. HTML 

> HTML stand for Hyper Text MarkUP Language  
sample HTML code:
``` HTMl
 <!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html> 
```
## Adding hyperlinks
```HTML
 <a href="https://www.w3schools.com">This is a link</a> 
```
for more info <a href=https://www.w3schools.com/html>W3school </a>

# Vscode usefull shortcuts
1. shift + alt + r : to open current working directly in windows
2. shift + ctrl + p : open preference   


# Built_in function example
## os.walk
It can give all the file, folder in the directory
```python
import os
for (root,dirs,files) in os.walk("D:\\Soft Tech videos\\Python",topdown =True):
    print(root)
    print(dir)
    print(files)
    print('________________________________')
```