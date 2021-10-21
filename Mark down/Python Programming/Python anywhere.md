# Python related terms

- **Transition Atomic** in python. Roll happens in python if something bad happens but entry goes MYSQL.

- **Updating Site content in python anywhere** if you're talking about a bash console on PythonAnywhere, then all  you need to do to update your website with code that you've pushed from  your local machine to GitHub is run `git pull` inside the checkout directory.  That is, for the Django Girls tutorial site, start a new bash console, then

```
cd my-first-blog
git pull
```

That will pull all of your code changes into PythonAnywhere.   Then  you need to reload the site, which you can either do by clicking the  button on the the "Web" tab, or from Bash by running a command like  this:

```
touch /var/www/cochewen_pythonanywhere_com_wsgi.py
```

...where the filename is the hostname for your site, with dots replaced by underscores and `_wsgi.py` added to the end.

