## Template folder 

### Registering your templates in setting.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], <--- here
        'APP_DIRS': True,
        'OPTIONS': {
            ....
            ],
```

Be always careful what you type in that place

### Project level

following folder structure should be followed

**project_folder\templates\home.html**

### App level 

following folder structure should be followed

**template\app_name\home.html**

---

### Templates seeking mechanism when written in templates folder

Suppose you created the template in the following manner in the 

project level :- **templates/home.html**

app level :- **templates/home.html**

and your view function look like this

```python
def home(request):
	return render(request, "home.html")
```

 Then the highest priority would be **Project_level**

So to get the desired level of result always store your html file in **templates/app_name/home.html**



