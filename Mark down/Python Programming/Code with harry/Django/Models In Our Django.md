### Models In Our Django 

While building modern web applications, we need to store the user's data somewhere so that it can be used for a better user experience. We are building an E-commerce website, so we also need to store the data somewhere. So, my question is, where do we store the data? A  straightforward answer to this question is the database. There are  various types of database management systems, such as MySQL, Oracle  Database, SQLite, etc. So we can conclude that we need to get our hands  dirty with DBMS to store the data. But, wait a minute. I have some good  news for you! In Django, you can use the models to access the database  instead of directly interacting with messy SQL. So, let's start our  discussion on Django models:

#### Django models:

- Models in Django are the single and definitive source of information.
- With the help of Django models, we can manipulate and retrieve the data instead of writing complex SQL to perform the same task.
- Whenever we create a model, Django automatically executes SQL and creates a corresponding table in the database.

