### Django Admin & Adding Data To The Database 

In our previous tutorial, we saw how we could make changes to the database with the help of Django models. In this tutorial, we will discuss the  Django admin. We will also add data to the database. So, without wasting any time, let's start our discussion on Django admin.

#### Django admin :

In the last tutorial, we successfully made changes to the database  using Django models, but how do we verify that the changes we made are  applied correctly? So, to do so, we need to create a superuser in  Django. 

- Django admin or superuser is like the root user of Linux OS. 
- Django admin is the most dominant user, which means it has all powers to read, view, update, create and delete the data.

#### Registering the model

But we can not see the product table that we created in the previous  tutorial. This is because Django requires us to register all the models  in the admin.py file. So, to register, open the admin.py file of the  shop and type the below command:

```python
from django.contrib import admin

from .models import Product
admin.site.register(Product)
```

for more info [click me](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
