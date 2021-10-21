###  List Comprehension, Dictionary Comprehension And Generator Comprehension

Hey! I promise after reading this blog you will leave as a much more cooler python programmer than earlier.

**Introduction:** In this blog we will learn about:

- [List comprehension](https://www.codewithharry.com/#liscom)
- [Dictionary comprehension](https://www.codewithharry.com/#diccom)
- [Set Comprehension](https://www.codewithharry.com/#setcom)
- [Generator Comprehension](https://www.codewithharry.com/#gencom)

There are 4 types of comprehensions. Their purpose is same i.e. to  make your code look cleaner, readable and also it makes it easy to code, decreases number of lines used big time. Now here are all 4 types of  comprehensions with example as follows:

#### List comprehension:

This is how we usually code:

```python
list_1 = [1,32,4,5,45,4,4,3,3,3,5,6,3,5,6,343,343,5,4]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print('Without using list comprehensions', divide_by_3)
```

But this can also be written like:

```python
list_1 = [1,32,4,5,45,4,4,3,3,3,5,6,3,5,6,343,343,5,4]
print("Using List comprehensions", [item for item in list_1 if item%3==0])
```



This is cleaner, readable and easy. This is comprehension.

This is what everything means:

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/intermediate-python-6/listcomprehension.jpg)

Similarly there are other comprehensions.

#### Dictionary comprehension:

```python
dict1 = {'a':45, 'b':65, 'A':5}
print({k.lower():dict1.get(k.lower(), 0)+dict1.get(k.upper(), 0) for k in dict1.keys()})
```

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/intermediate-python-6/dictionarycomprehension.jpg)

This is what it means, you can put condition too.

#### Set comprehension:

```python
squared = {x**2 for x in [1,2,3,4, 4,4,4,5,5,5,5]}
print(squared)
```

Similarly,

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/intermediate-python-6/setcomprehension.jpg)

In sets if value is repeating then it shows only one time so output is:

```python
{1, 4, 9, 16, 25}
```



#### Generator comprehension:

```python
gen = (i for i in range(56) if i%3==0)
for item in gen:
    print(item)
```

![img](https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/intermediate-python-6/generatorcomprehension.jpg)

gen is an object and with for loop we are iterating it.

#### #tut5.py file as described in the video

```python
'''
List comprehensions
Dictionary comprehensions
Set Comprehensions
Generator Comprehensions
'''

list_1 = [1,32,4,5,45,4,4,3,3,3,5,6,3,5,6,343,343,5,4]
divide_by_3 = []
for item in list_1:
    if item%3 == 0:
        divide_by_3.append(item)
print('Without using list comprehensions', divide_by_3)
print("Using List comprehensions", [item for item in list_1 if item%3==0])

dict1 = {'a':45, 'b':65, 'A':5}
print({k.lower():dict1.get(k.lower(), 0)+dict1.get(k.upper(), 0) for k in dict1.keys()})


squared = {x**2 for x in [1,2,3,4, 4,4,4,5,5,5,5]}
print(squared)


gen = (i for i in range(56) if i%3==0)
for item in gen:
    print(item)
```