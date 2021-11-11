## Flask

### Starter minimal code template

```python
from flask import Flask
app=Flask(__name__)
@app.route('/')
def sayhello():
       return 'Hello'
if __name__=='__main__':
       app.debug=True
       app.run()
```

### How Websites Work - Web Development Using Flask and Python #1

In this video, I have explained how a basic structure of a website works  and how a beginner can get an answer of his "How I can start developing  websites" question. This video is a starter for this web development  using flask playlist wherein I have explained different operations one  can achieve using python flask module. Python flask module comes with a  decent documentation but the same can be very difficult and tricky to  understand if you are a beginner.

This video breaks down the syntax, concept as well as the best  practices of developing web applications using python flask module.  Later in this series, we will work with Flask-SQLAlchemy module which  will help us to leverage sqlalchemy using flask.

Flask module can also be used as a rest service using jsonify  function but in this series we will use flask to create a blog in  python. The blog will have all the different parameters configurable  which means that anyone can open the config.json file, edit it and make  the fork of this blog his own.

In a nut shell, this video is a practical demonstration of how flask  works and how any website utilizes its backend to serve http requests.

### Server:

To do web development, to establish a website, first thing which is  needed is server. Server is like space in the internet. Like if we want  to make a house we first need land. Everything is stored in server. It  is from where clients can fetch the website. Server is connected to  internet and client is also connected to the internet. Internet is the  medium through which server connects to client. All data and every  authentication is done by server, internet just transfers it. You know  how we say everything is on the internet, it’s a wrong statement,  everything is on servers, internet just takes it and transfers it to  you.

Let’s understand how all this works with help of an example:

You are a client(user), you go on a website, say Facebook. You  requested Facebook to internet so internet went to Facebook, fetched a  login page, showed you the login page and asked you to login. You gave  your credentials, internet sent them to Facebook, Facebook checked if  they are correct. If they are correct, Facebook handed over a logged in  page to internet where you can see all your posts and profile. This is  the process but there are a lot of other things too like **server side coding**, **client side coding**. What things to keep on server and what to keep on client side. We don’t want to give all our code to client that’s why there is a server side.  Client can’t access/see server side code. In client side we usually send files like HTML, JS, CSS, images, videos, etc . In server side we keep  data of our clients, website algorithm, etc.

There are other server side scripting languages too like php, aspnet, java. In python there is Django and flask.

