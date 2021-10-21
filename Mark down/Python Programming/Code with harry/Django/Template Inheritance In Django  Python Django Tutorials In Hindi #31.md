###  Template Inheritance In Django | Python Django Tutorials In Hindi #31

Do you remember the DRY principle of programming? DRY stands for DO NOT  REPEAT YOURSELF. Now, suppose are designing a website in which you want  to serve the same navigation bar on every page of the website. What will you do? You can copy and paste the code of the navigation bar again and again. But is it an efficient approach? A big NO! Why? Because you are  repeating yourself and violating the concept of DRY. Here comes the  concept of Template inheritance in Django. The Django template language  is very powerful and the concept of Django template inheritance is  similar to the concept of inheritance in programming languages. So,  let's see how can we use template inheritance on our E-commerce website.





First of all, open the template folder of the shop app and create two HTML files:

1. about.html: This file will contain HTML for the about page of the shop app.
2. basic.html: We will inherit the code from this file.

After doing this open the index.html and copy the navigation bar and additional javascript code from and paste in the basic.html file. You can also copy the below code :

```markup
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
        integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <title>Title</title>
    <style>
    </style>

</head>

<body>
<!--{% load static %}-->

    <!--  navigation bar code starts here-->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">My Awesome Cart</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                        data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Dropdown
                    </a>
                    <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                    </div>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                </li>
            </ul>
            <form class="form-inline my-2 my-lg-0">
                <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form>
        </div>
    </nav>

<!-- Optional JavaScript -->
      <!-- jQuery first, then Popper.js, then Bootstrap JS -->
      <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
        integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
        crossorigin="anonymous"></script>
      <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
        integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
        crossorigin="anonymous"></script>
</body>
    <!--nav bar code ends here-->
```

Now, replace the <title> tag of the above code from the code given below :

```markup
<title>{% block title %} {% endblock %}</title>
```

After doing this, open the about.html file and type the below code :

```markup
{% extends 'shop/basic.html' %}
{% block title %} Title of about{% endblock %}
```

In the above code, we have used the extend tag to inherit the basic.html in the about.html file. Extend simple tells the Django that we want to inherit or use the code from the basic.html file. Restart the development server and head over to the about page of the shop app. If you have followed all the steps correctly then you  will see a screen like this:

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-django-tutorials-hindi-31/base64.png)





In the above image, you can see that we have successfully  inherited the navigation bar without writing the same code again. So,  that' how you can easily inherit code from one to another template. Now, let's create a block for the body of the about page. So, open the  basic.html file and type the below code :

```markup
{% block body %} {% endblock %}
```

Paste the above code after the navigation bar code in the basic.html file. After doing this, open the about.html file and type the below code:

```markup
{% block body %} {% endblock %}
```

Restart the development server and go to the about page. You will see a screen like this :

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-django-tutorials-hindi-31/base64_k9TUcMK.png)

So in the above image, you can see that we have created the  navigation bar and body of the about page by just writing three lines of code. This is the power of the Django template language! I hope the  concept of template inheritance is clear to you and I will see you in  the next tutorial.





#### Code views.py as described/written in the video

```python
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

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

#### Code models.py as described/written in the video

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

#### Code about.html as described/written in the video

```html
{% extends 'shop/basic.html' %}

{% block title%} Title of About{% endblock %}
{% block body %} This is body {% endblock %}
```

#### Code basic.html as described/written in the video

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">

    <title>{% block title%} {% endblock %}</title>
     <style>
       {% block css %} {% endblock %}
  </style>
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">My Awesome Cart</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item dropdown">
        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          Dropdown
        </a>
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="#">Action</a>
          <a class="dropdown-item" href="#">Another action</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
      </li>
      <li class="nav-item">
        <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form>
  </div>
</nav>
  {% block body %} {% endblock %}

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
  </body>
</html>
```





#### Code as described/written in the video

```html
{% extends 'shop/basic.html' %}
{% block css %}
          .col-md-3
          {
          display: inline-block;
          margin-left:-4px;
          }

          .carousel-indicators .active {
          background-color: blue;
            }

          .col-md-3 img{

          width:100%;
          height:auto;
          }

          body .carousel-indicator li{
          background-color: blue;
          }

          body .carousel-indicators{
          bottom: 0;
          }

          body .carousel-control-prev-icon,
          body .carousel-control-next-icon{
          background-color: blue;
          }
           body .no-padding{
           padding-left: 0,
           padding-right: 0;
           }
 {% endblock %}

{% block body %}
{% load static %}
<div class="container">
<div id="demo" class="carousel slide my-3" data-ride="carousel">
    <ul class="carousel-indicators">
      <li data-target="#demo" data-slide-to="0" class="active"></li>
      <li data-target="#demo" data-slide-to="1" ></li>
      <li data-target="#demo" data-slide-to="2" ></li>
    </ul>

    <!--Slideshow starts here -->
    <div class="container carousel-inner no-padding">

      <div class="carousel-item active">
        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
       </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>



      <div class="carousel-item">
        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>

      <div class="carousel-item">
        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
       </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>

        <div class="col-xs-3 col-sm-3 col-md-3">
          <div class="card" style="width: 18rem;">
            <img src='{% static "shop/test.jpg" %}' class="card-img-top" alt="...">
            <div class="card-body">
              <h5 class="card-title">Card title</h5>
              <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
          </div>
        </div>
      </div>
    </div>

</div>

    <!-- left and right controls for the slide -->
    <a class="carousel-control-prev" href="#demo" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
    </a>
    <a class="carousel-control-next" href="#demo" data-slide="next">
        <span class="carousel-control-next-icon"></span>
    </a>


 {% endblock %}
```