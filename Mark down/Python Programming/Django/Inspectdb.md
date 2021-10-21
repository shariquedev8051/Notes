# Inspectdb

## Creating Django models of an existing DB            

​          Django is well known for its ORM efficiency. More often,  we come across a point where we want to integrate our existing database  to a new backend framework. And first step towards it is generally (ORM  supporting frameworks) creating database models. In this article we will learn creating Django models of an existing database.

## Database set up

It is quite possible to integrate Django into legacy databases. First step towards it is to set up database connection for Django to connect  to existing database in `settings.py` file.

## Django inspectdb command

Once you have set up the database connection in Django, you can  auto-generate the models. Yes you heard it correctly! Django provides a  utility to auto-generate models from an existing database via `inspectdb` command.

You can create models by introspecting an existing database by executing following command:

```
$ python manage.py inspectdb
```

The above command will output all the models Django can create from  the existing database to stdout. You can save this as a file by using  standard Unix output redirection:

```
$ python manage.py inspectdb > models.py
```

The output file will be saved to your current directory. Move that  file to the correct app and you have a good starting point for further  customization.

Remember: You need to run the Django project before running inspect db

## More options for inspectdb

`inspectdb` command by default without any argument,  outputs all the tables from the database. If you want to introspect  particular table(s), you can pass table names as an argument separated  by space after the command:

```
$ python manage.py inspectdb table1 table2
```

You can refer to Django [documentation](https://docs.djangoproject.com/en/2.2/ref/django-admin/#django-admin-inspectdb) for more information.

## Points to remember

- If `inspectdb` cannot map a column's type to a model field type, it'll use *TextField* and will insert the Python comment `'This field type is a guess.'` next to the field in the generated model. Keep an eye out for that, and change the field type accordingly if needed.

- If a database column name is a Python reserved word (such as `pass`, `class`, or `for`), `inspectdb` will append `'_field'` to the attribute name and set the `db_column` attribute to the real field name (e.g., `pass`, `class`, or `for`).
   For example, if a table has an `INT` column called `for`, the generated model will have a field like this:

  `for_field = models.IntegerField(db_column='for')`

  `inspectdb` will insert the Python comment `'Field renamed because it was a Python reserved word.'` next to the field.

- If your database contains tables that refer to other tables (as  most databases do), you might need to rearrange the order of the  generated models so that models that refer to other models are ordered  properly.

- Django doesn’t create database `defaults` when a  default is specified on a model field. Similarly, database defaults  aren't translated to model field defaults or detected in any fashion by `inspectdb`.

- By default, `inspectdb` creates `unmanaged models`. That is, `managed = False` in the model's `Meta` class tells Django not to manage each table's creation, modification,  and deletion. If you do want to allow Django to manage the table's  life-cycle, you'll need to change the `managed` option to `True` (or simply remove it because True is its default value).

- Each database table is converted to a model class (i.e., there is a one-to-one mapping between database tables and model classes). This  means that you'll need to refactor the models for any many-to-many join  tables into `ManyToManyField` objects.

- Foreign-key detection only works with PostgreSQL and with certain  types of MySQL tables. In other cases, foreign-key fields will be  generated as:

  `IntegerField's, assuming the foreign-key column was an``INT` column.

This feature is meant as a shortcut, not as definitive model  generation. After you run it, you'll want to look over the generated  models yourself to make customization.