## Chapter- 4 Working with Models And Databases

Working with Models and Databases:

☕ As the part of web application development, compulsory we required to interact with
 database to store our data and to retrieve our stored data.
 ☕ Django provides a big in-built support for database operations. Django provides one
 inbuilt database sqlite3.
 ☕ For small to medium applications this database is more enough. Django can provide
 support for other databases also like oracle, mysql,postgresql etc

Database Configuration:

☕ Django by default provides sqlite3 database. If we want to use this database,we are
 not required to do any configurations.
 ☕ The default sqllite3 configurations in settings.py file are declared as follows.

<span style = "color:blue">settings.py</span>

```python
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}
}
```

☕ If we don't want sqlite3 database then we have to configure our own database with
 the following parameters.

```python
ENGINE: Name of Database engine
NAME: Database Name
USER: Database Login user name
PASSWORD: Database Login password
HOST: The Machine on which database server is running
PORT: The port number on which database server is running
```

Note: Most of the times HOST and PORT are optional.

How to Check Django Database Connection:

☕ We can check whether django database configurations are properly configured or not
 by using the following commands from the shell
 ☕ D:\djangoprojects\modelProject>py manage.py shell

from django.db import connection
c = connection.cursor()
☕ If we are not getting any error means our database configurations are proper.

Configuration of MySQL Database:

☕ First we have to create our own logical database in the mysql.
 mysql> create database employeedb;
 ☕ We have to install mysqlclient by using pip as follows
 pip install --only-binary :all: mysqlclient

<span style = "color:blue">settings.py</span>

```python
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'employeedb',
'USER':'root',
'PASSWORD':'root'
}
}
```

Checking Configurations:

D:\djangoprojects\modelProject>py manage.py shell

from django.db import connection
c = connection.cursor()

Configuration of Oracle Database:

```python
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.oracle',
'NAME': 'XE',
'USER':'scott',
'PASSWORD':'tiger'
}
}
```

Note: We can find oracle database name by using the following command.
 SQL> select * from global_name;

Model Class:

☕ A Model is a Python class which contains database information.
 ☕ A Model is a single, definitive source of information about our data. It contains fields
 and behavior of the data what we are storing.

☕ Each model maps to one database table.
 ☕ Every model is a Python class which is the child class of (django.db.models.Model)
 ☕ Each attribute of the model represents a database field.
 ☕ **We have to write all model classes inside ‘models.py’ file.**

1. Create a project and application and link them.

django-admin startproject modelProject
 cd modelProject/
 python manage.py startapp testApp

After creating a project and application, in the models.py file, write the following code:

models.py

```python
from django.db import models

# Create your models here.
class Employee(models.Model):
eno=models.IntegerField()
ename=models.CharField(max_length= 30 )
esal=models.FloatField()
eaddr=models.CharField(max_length= 30 )
```

Note: This model class will be converted into Database table. Django is responsible for
 this.

table_name: appName_Employee
 fields: eno, ename, esal and eaddr. And one extra field: id
 behaviors: eno is of type Integer, ename is of type Char and max_length is 30 characters.

Hence, Model Class = Database Table Name + Field Names + Field Behaviors

Converting Model Class into Database specific SQL Code:
 Once we write Model class, we have to generate the corresponding SQL Code. For this, we
 **have to use “makemigrations” command.**
 Python manage.py make migrations

It results the following:
 Migrations for 'testApp':
 testApp/migrations/0001_initial.py

- Create model Employee

How to see corresponding SQL Code of Migrations:

**To see the generated SQL Code, we have to use the following command “sqlmigrate”**
 python manage.py sqlmigrate testApp 0001

```sql
BEGIN;
--
-- Create model Employee
--
CREATE TABLE "testApp_employee" ("id" integer NOT NULL PRIMARY KEY AUTOIN
CREMENT, "eno" integer NOT NULL, "ename" varchar(30) NOT NULL, "esal" real N
OT NULL, "eaddr" varchar(30) NOT NULL);
COMMIT;
```

Note: Here 0001 is the file passed as an argument

**“id” field:**
 1 ) **For every table(model), Django will generate a special column named with “id”.**
 2 ) ID is a Primary Key. (Unique Identifier for every row inside table is considered as a
 primary key).
 3 ) This field(id) is auto increment field and hence while inserting data, we are not
 required to provide data for this field.
 4 ) **This id field is of type “AutoField”**
 5 ) **We can override the behavior of “id” field and we can make our own field as “id”.**
 6 ) Every Field is **by default “NOT NULL”.**

How to execute generated SQL Code (migrate Command):
 After generating sql code, we have to execute that sql code to create table in database.
 **For this, we have to use ‘migrate’ command.**

python manage.py migrate

Operations to perform:
 Apply all migrations: admin, auth, contenttypes, sessions, testApp
 Running migrations:
 ⚽ Applying contenttypes.0001_initial... OK
 ⚽ Applying auth.0001_initial... OK
 ⚽ Applying admin.0001_initial... OK
 ⚽ Applying admin.0002_logentry_remove_auto_add... OK
 ⚽ Applying contenttypes.0002_remove_content_type_name... OK
 ⚽ Applying auth.0002_alter_permission_name_max_length... OK
 ⚽ Applying auth.0003_alter_user_email_max_length... OK
 ⚽ Applying auth.0004_alter_user_username_opts... OK
 ⚽ Applying auth.0005_alter_user_last_login_null... OK

⚽ Applying auth.0006_require_contenttypes_0002... OK
⚽ Applying auth.0007_alter_validators_add_error_messages... OK
⚽ Applying auth.0008_alter_user_username_max_length... OK
⚽ Applying sessions.0001_initial... OK
⚽ Applying testApp.0001_initial... OK

Note: Now tables will be created in the database.

What is the Advantage of creating T **ables with ‘migrate’ Command
 If we use ‘migrate’ command, then all Django required tables will be created in addition to**
 our application specific tables. If we create table manually with sql code, then only our
 application specific table will be created and django my not work properly. Hence it is
 **highly recommended to create tables with ‘migrate’ command.**

How to Check created Table in Django admin Interface:
 We have **to register model class in ‘admin.py’ file.**

admin.py

```python
from django.contrib import admin
from testApp.models import Employee

# Register your models here.

admin.site.register(Employee)
```

Creation of Super User to login to admin Interface:

☕ We can create super user with the following command by providing username, mailid,
 password.
 python manage.py createsuperuser

☕ **We can login to admin interface → Start the server and login to admin interface using**
 the created credentials.
 ☕ python manage.py runserver

☕ Open the following in browser: http://127.0.0.1:8000/admin/

Difference between makemigrations and migrate:

**“makemigrations” is responsible to generate SQL code for Python model class whereas
 “migrate” is responsible to execute that SQL code so that tables will be created in the**
 database.

To Display Data in admin Interface in Browser:

models.py

```python
from django.db import models

# Create your models here.

class Employee(models.Model):
eno=models.IntegerField()
ename=models.CharField(max_length= 30 )
esal=models.FloatField()
eaddr=models.CharField(max_length= 30 )
def __str__(self):
	return 'Employee Object with eno: +str(self.no)'
```

admin.py

```python
from django.contrib import admin
from testApp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)
```

Note:
 We should do this registration in a single line otherwise we are getting error.
 admin.site.register(Employee)
 admin.site.register(EmployeeAdmin)

### Practice Activity:

Create the following tables and populate with some sample data

```html
1. Job(posting date,location,offeredsalary,qualification)
2. Book(number,title,author,publisheddate)
3. Customer(name,ano,mailid,phonenumber,age)
```

Now we can write views to get data from the database and send to template.
 Before writing views.py file, create “templates” and “static” folder with respective
 application folders and HTML and CSS files and link them in settings.py file.

Views.py

```python
from django.shortcuts import render
from testApp.models import Employee

# Create your views here.
def empdata(request):
emp_list=Employee.objects.all()
my_dict={'emp_list':emp_list}
return render(request, 'testApp/emp.html', context=my_dict)
```

emp.html

```html
<!DOCTYPE html>
{% load staticfiles %}
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title></title>
<link rel="stylesheet" href="{% static '/css/demo.css'%}">
</head>

 <body>
 <h1> The employees list is : </h1>
 
 {% if emp_list %}
 <table>
 <thead>
 <th> eno </th>
 <th> ename </th>
 <th> esal </th>
 <th> eaddr </th>
 </thead>
 
 {% for emp in emp_list %}
 <tr>
 <td> {{emp.eno}}</td>
 <td>{{emp.ename}}</td>
 <td>{{emp.esal}}</td>
 <td> {{emp.eaddr}}</td>
 </tr>
 {% endfor %}
 
 </table>
 {%else%}
 <p> No records found </p>
 {% endif %}
 
 </body>
 </html>
```

Important FAQs Related to Model and database

configurations:

1 ) How to configure database inside settings.py?
 2 ) How to check connections?
 3 ) How to define Model class inside models.py
 4 ) How we can perform makemigrations?
 5 ) How we can perform migrate?
 6 ) How to add our model to admin interface inside admin.py
 7 ) To display total data how to write ModelAdmin class inside admin.py
 8 ) How to createsuperuser?
 9 ) How to login to admin interface and add data to our tables?
 10 ) How to see generated sqlcode b'z of makemigrations

### Faker Module:

We can use Faker Module to generate fake data for our database models.

```python
from faker import Faker
from random import *
fakegen=Faker()
name=fakegen.name()
print(name)
first_name=fakegen.first_name()
last_name=fakegen.last_name()
print(first_name)
print(last_name)
date=fakegen.date()
print(date)
number=fakegen.random_number( 5 )
print(number)
email=fakegen.email()
print(email)
print(fakegen.city())
print(fakegen.random_int(min= 0 , max= 9999 ))
print(fakegen.random_element(elements=('Project Manager', 'TeamLead', 'Software Engineer')))
```

### Working with MYSQL Database (studentinfo project):

<span style = "color:blue">settings.py</span>

```python
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
INSTALLED_APPS = [
....,
'testapp'
]
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [TEMPLATE_DIR],
....
}
]
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'studentdb',
'USER':'root',
'PASSWORD':'root'
}
}
```

models.py

```python
from django.db import models

# Create your models here.
class Student(models.Model):
name=models.CharField(max_length= 30 )
marks=models.IntegerField()
```

admin.py

```python
from django.contrib import admin

# Register your models here.
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
list_display=['name','marks']

admin.site.register(Student,StudentAdmin)
```

views.py

```python
from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def studentview(request):
student_list=Student.objects.order_by('marks')
my_dict={'student_list':student_list}
return render(request,'testapp/students.html',context=my_dict)
```

students.html

```html
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title></title>
</head>
<body>
{%if student_list %}
<table border="1" margin='auto'>
 <thead>
 <th>Name</th>
 <th>Marks</th>
 </thead>
 {% for student in student_list %}
 <tr>
 <td>{{student.name}}</td>
 <td>{{student.marks}}</td>
 </tr>
 {% endfor %}
 </table>
 {% else %}
 <p>No Studetns found</p>
 {% endif %}
 </body>
 </html>
```

urls.py

```python
from django.conf.urls import url
from django.contrib import admin
from testapp import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.studentview),
]
```

### Working with MYSQL Database and Faker Module

#### (studentinfo Project):

settings.py

```python
TEMPLATE_DIR=os.path.join(BASE_DIR,'templates')
STATIC_DIR=os.path.join(BASE_DIR,'static')
INSTALLED_APPS = [
....,
'testapp'
]
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [TEMPLATE_DIR],
....
}
]
DATABASES = {
'default': {
'ENGINE': 'django.db.backends.mysql',
'NAME': 'studentdb',
'USER':'root',
'PASSWORD':'root'
}
}
STATIC_URL = '/static/'
STATICFILES_DIRS=[
STATIC_DIR,
]
```

models.py

```python
from django.db import models

# Create your models here.
class Student(models.Model):
rollno=models.IntegerField()
name=models.CharField(max_length= 30 )
dob=models.DateField()
marks=models.IntegerField()
email=models.EmailField()
phonenumber=models.IntegerField( 15 )
address=models.TextField()
```

admin.py

```python
from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
list_display=['rollno','name','dob','marks','email','phonenumber','address']
admin.site.register(Student,StudentAdmin)
```

populate_student_info.py

```python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studentinfoproject.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
d1=randint( 6 , 9 )
num=''+str(d1)
for i in range( 9 ):
num=num+str(randint( 0 , 9 ))
return int(num)
def populate(n):
for i in range(n):
frollno=fake.random_int(min= 1 ,max= 999 )
fname=fake.name()
fdob=fake.date()
fmarks=fake.random_int(min= 1 ,max= 100 )
femail=fake.email()
fphonenumber=phonenumbergen()
faddress=fake.address()
student_record=Student.objects.get_or_create(rollno=frollno,name=fname,do
b=fdob,marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddre
ss)
populate( 30 )
```

views.py

```python
from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def home_page_view(request):
students=Student.objects.all()
#students=Student.objects.filter(marks__lt=35)
#students=Student.objects.filter(name__startswith='A')
#students=Student.objects.all().order_by('marks')
#students=Student.objects.all().order_by('-marks')
return render(request,'testapp/index.html',{'students':students})
```

index.html

```html
<!DOCTYPE html>
{%load staticfiles%}
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title></title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7
/css/bootstrap.min.css" integrity="sha384-
BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" 
crossorigin="anonymous">
<link rel="stylesheet" href="{%static "css/sinfo.css"%}">
</head>
1<body>
<div class="container" >
<h1>Student Information</h1><hr>
{% if students%}
{%for student in students%}
<h2>{{student.name}} Information</h2><hr>
<ul>
<li>Student Rollno:{{student.rollno}}</li>
<li>Student DOB:{{student.dob}}</li>
<li>Student Marks:{{student.marks}}</li>
<li>Student Email:{{student.email}}</li>
<li>Student Phone Number:{{student.phonenumber}}</li>
<li>Student Address:{{student.address}}</li>
</ul>
<br>
{%endfor%}
{%else%}
<p>Student Records Are Not Available</p>
{%endif%}
</div>
</body>
</html>
```

sinfo.css

```css
body .container{
background: red;
color:white;
}
h 1 {
text-align: center;
}
h 2 {
color:yellow;
}
```

urls.py

```python
from django.conf.urls import url
from django.contrib import admin
from testapp import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.home_page_view),
]
```

## 