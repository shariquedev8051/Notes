## test, unit test and pytest

### TDD(Test driven developement):-

reference:- [click me](https://test-driven-django-development.readthedocs.io/en/latest/)

info:- Test-driven development (TDD) is a **software development process relying on software requirements being converted to test cases before software is fully developed**, and tracking all software development by repeatedly testing the software against all test cases.

----

### Test



### Unittest



### Pytest

- install pytest
- test file should always start with **test_file_name** or should end with _test.
- function_name should always start with **test_methode_name** and they should be unique not same name.
- you can test by using following commands

```shell
pytest file_name # simple way
pytest file_name -v # detailed view

py.test # To run all the file having word test as tests cases
py.test -v # To see the detailed view

py.test -v -s # to see the console logs in the output

py.test file_name -v -s # To run specific file in folder

py.test -k test_methode_name -v -s # to run a specific methode

py.test -m smoke -v -s # to run a specific methode using mark methode

```



### Decorators

- Tagging or marking test_methode using decorator `@pytest.mark.smoke` 
- To skip a test_methode add decorator `@pytest.mark.skip`
- To run the test_methode but do not want to report it `@pytest.mark.xfail`
- fixture is like it will run before and after the test.

----



### Conftest file

define fixture in only one file and use it in wherever you need it.

---

```shell
pip install pytest-html
```

