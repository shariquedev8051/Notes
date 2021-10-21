### Adding Media Directory In Django | Python Django Tutorials In Hindi #28

In this tutorial, we will see how to serve media files with the help of the media directory.

To deal with the media files, Django requires us to tell it the name of the directory in which we wish we upload and keep the media  files. Another thing that Django wants from us is the URL under which we want to access the media files while serving the website. Now, follow  the below steps to serve the media files:

**Step 1:** Open the settings.py file of the mac.

**Step 2:** Type the below code at the end of the settings.py file: 

```python
STATIC_URL= "/static/"
MEDIA_ROOT= os.path.join(BASE_DIR, "media")
MEDIA_URL="/media/"
```

Now, let's understand the above code, line by line:

\1. STATIC_URL: It is simply the prefix of the URL that will be visible to the user while accessing the static files.

Example: Suppose a user tries to access a static file named  "mystatic.txt" of the shop app. Then, he or she will access the file at [http://127.0.0.1:8000/static/shop/mystatic.txt](http://127.0.0.1:8000/static/blog/mystatic.txt). 

\2. MEDIA_ROOT: It is the path to the directory in which all the media files will be saved. Here, we have written(BASE_DIR, "media")  which means that Django will create a folder named "media" under the  base directory and all the media files will be saved in the "media"  folder.

3.MEDIA_URL: Similar to the STATIC_URL, it is also the prefix  of the URL that will be visible to the user while accessing the media  files.

After doing this, we need to make some changes in the urls.py file of the mac. So, open the urls.py file and type the below code :

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='Home'),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
```

Now, restart the development server and head over to the admin  panel and then add a new product by clicking on the "ADD PRODUCT". In  the below image, you can see that I have added a mobile phone. After  filling all the details, save the product.

Now, click on the product that you just added and then click on the "shop/images/name_of_file.jpg" and you will be able to see the  image added by you. Below you can see that I am able to see the image at the following URL: http://127.0.0.1:8000/media/shop/images/samsung.jpg. 

Now, get back to the Pycharm and you will see a folder named  "media" under which you can find the image uploaded by you. In the below image you can see that media folder is created under the base  directory.

This tutorial ends here and I will see you in the next tutorial.

#### Code shop/models.py as described/written in the video

```python
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
```

#### Code mac/settings.py as described/written in the video

```python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9h_#wy*6)%#ug3-uv@7xlryan5a36rqe^j5a$-i0@fo9szu=%n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mac.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mac.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# Managing media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
```





#### Code mac/urls.py as described/written in the video

```python
"""mac URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```