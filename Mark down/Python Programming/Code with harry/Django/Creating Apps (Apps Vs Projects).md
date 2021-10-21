### Creating Apps (Apps Vs Projects) 

#### Django Apps :

- Apps in Django are pluggable web applications.
- Django apps are the self-sufficient submodule of a project. A  project can contain more than one apps, and an app can be used in more  than more one project.

#### How to create apps :

Django apps can be created within a project by using the syntax given below :

```python
python manage.py startapp name_of_the_app
```

We will create two apps on the MAC website, first is the **blog,** and the other is **shop**. Open the existing terminal of Pycharm and type the below code:

```python
python manage.py startapp blog
```

Similarly, for shop app:

```python
python manage.py startapp shop
```

In the image given below, you can see that both the apps are created successfully. 

Now, we will create views and URLs of the shop app. So, open the views.py file of the shop and type the following code:

```python
from django.http import HttpResponse
def index(request):
return HttpResponse("Index Shop")
```

In the above code, we have created an index function that  returns an Http response. Now, let's create the urls.py file of the shop app. Follow the steps given below :

**Step 1:** Double click on the shop folder and then click on New.

**Step 2:** After clicking on New select python file.

**Step 3:** Name the file as urls.py and press enter.

Now, let's map views and URLs of the shop app. Open the urls.py file and type the below code :

```python
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
]
```

Django requires us to declare the URLs of apps in the urls.py  file of the main project. So, open the urls.py file of mac and type the  below code :

```python
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
path('admin/', admin.site.urls),
path('shop/', include('shop.urls'))
]
```

By following the same procedure, we will create the URLs and  views of the blog app. Open the views.py of blog app and type the below  code :

```python
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Blog Index")
```

After doing that, create and open urls.py file of blog app and type the below code:

```python
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index,name="blogHome"),
]
```

With this, we have successfully mapped the URLs and views of  the blog app. Now, we need to add this URL in the urls.py file of mac.  Open urls.py file of mac and type the below code :

```python
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='Home'),
    path('blog/', include("blog.urls")),
    path('shop/', include("shop.urls")),
]
```

Now, let's check everything is working correctly or not. So,  open the existing terminal of Pycharm and start the development server  by typing the below command :

```python
python manage.py runserver
```

#### mac/urls.py code as described/written in the video

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls'))
]
```

#### shop/views.py code as described/written in the video

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("We are at about")

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productView(request):
    return HttpResponse("We are at product view")

def checkout(request):
    return HttpResponse("We are at checkout")
```

#### shop/urls.py code as described/written in the video

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("productview/", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
```

#### blog/views.py code as described/written in the video

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')
```

#### blog/urls.py code as described/written in the video

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome")
]
```