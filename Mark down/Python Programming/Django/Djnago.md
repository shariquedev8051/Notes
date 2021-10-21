## Djnago

1. Activate environment

   ```shell
   Workon django_env
   ```

2. Create new project

   ```
   djnago-admin startproject project_name
   ```

3. Create new app

   ```
   python manage.py startapp app_name
   ```

4. Register app

5. Initialize database for your project

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'db_name',# Change db_name with desired database name
           'USER': 'root',
           'PASSWORD': 'root',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

6. db_shell command

   ```
   >>> exec(open("file_path").read())
   ```

7. 





