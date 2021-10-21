# First 

- Create project with name First

```powershell
django-admin startproject first
```

- Create an app

```powershell
cd first
python manage.py startapp app1
```

- Register that app in   `first/setting.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
]
```

- Change Engine to MySQL

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'first_db',# Change db_name with desired database name
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

- Create database in MySQL with name **first_db**

`app1/models.py`

```python
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.FloatField()
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return f"self.__dict__"

    def __repr__(self):
        return str(self)
```

- Makemigrations and migrate
- create file named db_shell in first main directory

```
from app1.models import Employee
# exec(open("file_path").read()) 
```

- Download terminal app from Microsoft store

```
>>> exec(open("D:\\Python_playground\\Practice\\Django_1\\first\\db_shell.py").read())
```

- we will only get Django queries not dictionary of python
- Adding data to you tables

```python
import random
 city = ['Pune','Banglore',"Hydarabad",'Nagpur']
 for i in range(26):
     emp = Employee.objects.create(name = 
                                   chr(65+i),
                                   salary = random.randint(35000, 65000), 
                                   address = random.choice(city)
                                  )
```

- To fetch data from database

```python
format1 = """
------------ ID:- {} ---------------
Name of Employee:- {}
Salary of Employee:- {}
Address of Employee:- {}
"""
for i in Employee.objects.all():
    print(format1.format(i.id, i.name, i.salary, i.address))
```

| Function                           | Operation                                                    |
| ---------------------------------- | ------------------------------------------------------------ |
| emp.objects.**all()**              | return QuerySet contain all emp objects in the database.     |
| emp.objects.**get(id = 4)**        | return QuerySet contain only one emp objects in the database.<br><span style = "color:red">**If it returns more than a object it will give  MultipleObjectReturn error.**</span> |
| emp.objects.**filter(name = "A")** | return QuerySet contain all emp objects in the database having same value of name e.g **"A"** |
| emp.objects.**exclued(id = 6)**    | returns QuerySet not containing the object having id = 6.    |



 

