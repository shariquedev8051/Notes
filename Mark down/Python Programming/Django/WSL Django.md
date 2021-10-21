# WSL Django

## Copying the lists

```python
l = [1, 2, 3, 4]
l1 = l
print(id(l), id(l1))
```

output :-

```powershell
1924301183360 1924301183360
```

As we can say they are pointing to same reference if change the value of l or l1 it will be reflected to into other one

-----

### Method 1

```python
l = [1,2,3,4]
l1 = [1,2,3,4]
print(id(l), id(l1))
```

Output :-

```powershell
1924301183360 1924301182848
```

Here the content of list l and l1 are same but the way there were created they will have their own references to store data.

---

### Method 2 

copy method

```python
import copy 
l = [1,2,3,4]
l3 = copy.copy(l)
print(id(l), id(l3))
```

Output :-

```powershell
1924301183360 1924301484928
```

---

#### Shallow Copy

As we are using copy method to isolate two lists to avoid modification in both of the list when one is changed.

But there is a catch

```python
import copy
l = [1,2,3,[4,5]]
l3 = copy.copy(l)
print("l:- ", l)
print("l3:- ", l3)

l[3][1] = 25
print("l:- ", l)
print("l3:- ", l3)
```

Output :-

```python
l:-  [1, 2, 3, [4, 5]]
l3:-  [1, 2, 3, [4, 5]]
l:-  [1, 2, 3, [4, 25]] # we chaged the list l
l3:-  [1, 2, 3, [4, 25]]# modification can be observed
```

It provides different reference for 1,2,3 as they are integers but for list [4, 5] both l and l3 are point the same reference so we modify one we will see the change in other one too.

Try to avoid this for nested list.

```python
print(id(l[3]),id(l3[3]))
```

output:-

```
1671088109696 1671088109696
```

So as they are using same reference for listed list.

#### Deep Copy

```python
import copy
l = [1,2,3,[4,5]]
l3 = copy.deepcopy(l)
print("l:- ", l)
print("l3:- ", l3)

l[3][1] = 25
print("l:- ", l)
print("l3:- ", l3)
```

output:- 

```powershell
l:-  [1, 2, 3, [4, 5]]
l3:-  [1, 2, 3, [4, 5]]
l:-  [1, 2, 3, [4, 25]]
l3:-  [1, 2, 3, [4, 5]]
```

As we are deep copy lets check the what is happing to our nested list

```python
print(id(l[3]),id(l3[3]))
```

output:- 

```
1489549785216 1489549610688
```

## call by value and call by reference

```python
def func(x):
    print(x, id(x))
    x = 35
    print(x, id(x))
    
x = 10
func(x)
print(x, id(x))
```

Output:-

```powershell
10 2236621220432 # inside the func
35 2236621221232 # as int is immutable assigning new reference
10 2236621220432 # value of x could not be modified inside the funcion
```

------

```python
def func(x):
    print(x, id(x))
    x = 35
    print(x, id(x))
    return x
x = 10
x = func(x)
print(x, id(x))
```

Output:-

```powershell
10 2118088288848
35 2118088289648
35 2118088289648
```

----

**For list**

```python
def func2(lst):
    print(lst, id(lst))
    lst.append(50)
    print(lst, id(lst))

lst = [1,2,3,4]
print(lst, id(lst))
func2(lst)
```

output:-

```powershell
[1, 2, 3, 4] 2092639875968
[1, 2, 3, 4] 2092639875968
[1, 2, 3, 4, 50] 2092639875968 # Lists are mutable
```

There no change in reference as list are mutable.

Whether you extend or append reference wont change.

-----

```python
def func2(lst):
    print(lst, id(lst))
    lst = [10,20,45]
    print(lst, id(lst))

lst = [1,2,3,4]
print(lst, id(lst))
func2(lst)
print(lst, id(lst))
```

Output:-

```powershell
[1, 2, 3, 4] 2725783958464
[1, 2, 3, 4] 2725783958464
[10, 20, 45] 2725783958784  # list modified inside the list
[1, 2, 3, 4] 2725783958464  # won't be affected outside there is no record of list modification
```

bonus

```powershell
>>> lst = [1,2,3]
>>> id(lst)
2415132757120
>>> lst = [1,2,3]
>>> id(lst)
2415132465024
```

As you can see even though the contents are same but python is thinking that you are declaring new list with name lst.

```python
>>> s = "Hello"
>>> id(s)
2415132766896
>>> s += "World"
>>> id(s)
2415132766960
```

---

- Working with strings.

```python
def str_func(s):
    print(s, id(s))
    s += "World"
    print(s, id(s))

s = "Hello "
print(s, id(s))
str_func(s)
print(s, id(s))
```

output:-

```powershell
Hello  1937913509040
Hello  1937913509040
Hello World 1937913835568
Hello  1937913509040	
```

- With return function

```python
def str_func(s):
    print(s, id(s))
    s += "World"
    print(s, id(s))
    return s

s = "Hello "
print(s, id(s))
s = str_func(s)
print(s, id(s))
```

output:- 

```powershell
Hello  2828257686768
Hello  2828257686768
Hello World 2828258013232
Hello World 2828258013232
```

---

## Linux OS

### WSL -- windows subsystem for Linux

1. Go to settings
2. Go to apps
3. Go to program and features
4. Turn windows features on and off
5. Windows subsystem for Linux
6. restart pc

7. Go to Microsoft store
8. Search Ubuntu
9. Install Ubuntu
