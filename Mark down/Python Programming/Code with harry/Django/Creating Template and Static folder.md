### Creating Template and Static folder

#### Creating template folder

- Add folder within **app_name**
- name it template
- create a folder name it same ass **app_name**
- Add templates related to app_name there

#### Creating static folder

- Add folder within **app_name**
- name it static
- create a folder name it same ass **app_name**
- Add static files related to app_name there

##### Accessing static file on the blog:

To access the static file, first of all, we need to load the  static file in index.html. So, open the blog/index.html file and type  the following code in <body>:

```html
  {% load static %}
<a href="{%static 'blog/mystatic.txt' %}" >Click me </a>
```

The above code is the syntax to load static files in Django templates.

``