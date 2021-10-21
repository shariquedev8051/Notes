## VirtualenvWrapper-win 

```powershell
pip install virtualenvwrapper-win
```

**Imp command**

```
lsvirtualenv
```

List all of the environments stored in WORKON_HOME.

```
rmvirtualenv <name>
```

Remove the environment *<name>*.

```
workon [<name>]
```

If *<name>* is specified, activate the environment named *<name>* (change the working virtualenv to *<name>*). If a project directory has been defined, we will change into it. If no argument is specified, list the available environments. One can pass additional option -c after virtualenv name to cd to virtualenv directory if no projectdir is set.

```
deactivate
```

Deactivate the working virtualenv and switch back to the default system Python.

