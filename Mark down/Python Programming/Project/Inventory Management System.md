# Inventory Management System

1. Start project named inventory
2. Create app named dashboard
3. Initialize database with MySQL
4. Create Following apps
5. Main app is dashboard
   1. **User:-** Anything related to user goes here.
   2. **Shops**:- 
   3. **Courier:-**
   4. **Payment**:-

6. We are going to extend the user in Django so add following line in settings.py

   ```
   'dashboard.apps.DashboardConfig',
   ```


7. In views.py type this

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   # Create your views here.
   
   def index(request):
       return HttpResponse("You are in index page.")
   
   
   def staff(request):
       return HttpResponse("You are in staff page.")
   ```

8. Create urls.py in dashboard app

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index, name='index'),
       path('staff/', views.staff, name='staff')
   ]
   ```

9. Include dashboard.urls into inventory.urls

   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('dashboard.urls')),
   ]
   ```

10. Create Template folder in BASE_DIR

11. Add templates path in settings.py

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

12. Create index.html and staff.html in templates folder

