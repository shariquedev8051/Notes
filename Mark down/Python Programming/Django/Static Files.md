### Static files

Add this code in **settings.py**

```python
#DataFlair #Django #Static files
STATIC_URL = '/static/'
#--------------------------------------------------
STATIC_ROOT = os.path.join(BASE_DIR, 'root')
#-----------------------------------------------------
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
]
```

[click me](https://data-flair.training/blogs/django-static-files-handling/)

for django 3+

```python
STATIC_ROOT = str(BASE_DIR.joinpath('root'))

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    str(BASE_DIR.joinpath('static'))
]

```

