### Boostrap Css static folder

Okay so I know there are a lot of SO questions on this and I have  combed through all of them trying to find an answer but nothing was  exactly what I was looking for.

My issue is that whenever I try to load the static files into a Django template it just won't work. Here is my file structure:

```lua
MainProjectDir
|
+-- DjangoProject
|  |
|  +-- MainDjangoSub
|  |  |
|  |  +-- __init__.py
|  |  +-- settings.py (all the other usual folders below)
|  |
|  +-- StaticPages (this is my App directory)
|  |  |
|  |  +-- templates (will contain all templates for StaticPages app)
|  |  |  |
|  |  |  +-- StaticPages (directory containing html templates for the Static Pages App)
|  |  |  |  |
|  |  |  |  +-- main.html
|  |  |  |  +-- navbar.html
|  |  |
|  |  +-- __init__.py
|  |  +-- views.py (all other usual app files below)
|  |
|  +-- static (contains all static files for the project)
|  |  |
|  |  +-- Bootstrap (subdirectory containing the Bootstrap static files)
|  |  |  |
|  |  |  +-- css (directory containing all css files from Bootstrap precompiled files)
|  |  |  +-- js (directory containing all js files from Bootstrap precompiled files)
|  +-- manage.py
```

My the settings in my settings file pertaining to static files:

```ini
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'StaticPages',
]

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
```

In my views.py file under the StaticPages app I have this view to render my templates:

```python
def home(request):
    return render(request, 'StaticPages/main.html')
```

So here we get to my issue. In the main.html file I use `{% load static %}` to load the static files and then inside any calls to css or js files I do something similar but pycharm highlights the text and says "cannot  resolve directory ..." Here is a sample of my html file:

```xml
<!DOCTYPE html>
<html lang="en">

{% load static %}

<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <link rel="stylesheet" href='{% static "/Bootstrap/css/bootstrap.min.css" %}'
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

    <style>
        .navbar-custom{
            background-color: #e86813;
        }
    </style>

    <h3>Hello World</h3>

</head>
<body>
    {% include 'StaticPages/navbar.html' %}
</body>
</html>
```