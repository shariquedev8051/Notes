# str and repr

- The `__repr__` aims at a complete string representation of the object;
- The `__str__` is to return a nice string for printing.

```python
In [38]: str('s')
Out[38]: 's'

In [39]: repr('s')
Out[39]: "'s'"

In [40]: eval(str('s'))
Traceback (most recent call last):

  File "<ipython-input-40-abd46c0c43e7>", line 1, in <module>
    eval(str('s'))

  File "<string>", line 1, in <module>

NameError: name 's' is not defined


In [41]: eval(repr('s'))
Out[41]: 's'
```

reference:- 

devjournal	[click me](https://www.journaldev.com/22460/python-str-repr-functions)

