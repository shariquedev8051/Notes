## OOPs in python 

### Why OOPs In Python?

- Like many other programming languages, Python also supports object-oriented paradigm.
- OOPs helps the developers to write reusable code.
- With the help of OOPs, we can easily maintain and modify the existing code.

#### Let’s first discuss what Python is?

 Python is an interpreted (code is executed line  by line) high-level programming language with dynamic semantics, which  means, like other languages, we don’t have to specify the data type of  variable we are declaring.

#### What Is Object-Oriented Programming(OOP)?

- It is evident from the name that Object-Oriented programming  is something related to objects. Yes, the entire concept of OPP is based on **objects**. One of the popular methods to solve any query is by creating an object.
- OOP helps us to model real-world objects as software objects.
- With the help of OOP, we can model the relationships between real-world entities in programming.
- This is mostly used for code reusability.

#### What is Class?

 Classes are like **templates** that are used to create **objects**. It is like a *Blueprint* where the actual designing of an object takes place. The “Class” keyword is  used to create the class. We can have multiple objects in a class. The  class contains all the attributes of Object. For example, dairy milk is a subproduct of Cadbury here, dairy milk is like an object  of class Cadbury. Cadbury company has all the ingredients, materials,  etc., require to make dairy milk irrespective of the quantity.

### How to create a class in Python :

##### Syntax: 

```python
class ClassName :
        //code inside the class
```

##### Example :

```python
class Cadbury:
    pass
```

#### What are Objects?

 Objects are the instance of the class. Whatever  we want to do, we do it with the help of objects. Objects have  attributes and behavior. Let's take an example of a boy; here, height  and weight are the attributes. Behavior means the way of talking,  walking, etc., which are methods in the class. Objects contain methods  which are function in simple words. Methods mean creating a function in  class. Now, let's see how objects are created in Python :

```python
class Cadbury:
     //instance attribute
    def __init__(self,name,price):
        self.price = price
        self.name = name

    def display(self):
        print(self.price,self.name)

obj1 = Cadbury("DairyMilk",100) //obj1 is the object of the Cadbury class
obj1.display();
```

###  

---



### Classes, Objects and Constructors

In the previous article, I gave you a rough idea about the concept of  objects and classes in object-oriented programming. In this article, we  will be discussing Classes, Objects, and Constructors in detail.

**First, let’s discuss what are classes and objects?**

 Classes are just like the templates or blueprints, which hold all the functions of objects and objects are the actual product or instance of the class. Objects and  classes helps us to simplify our work by increasing the resuability of  the code.

Basically, before creating an object, we need to create a  class. Talking with an example, before creating anything, we gather all  the information on how to start, what all things are required, and from  where to start to get the possible results. Similarly, before creating  any object we design a blueprint of the object i.e., class. Let's see  how we can create a class in Python : 

#### Creating a class : 

Classes in python are created using the keyword class. The class is followed by the class name.

##### Syntax :

```python
 class Employee:
    pass
```

In the above code, we've created a class named Employee.

**Note**: 'pass' means in the current scenario we  are performing nothing, later we will proceed with something. 'pass' is  used as a placeholder for future code.

#### Creating objects of the class : 

Suppose, **harry** and **rohan** are the workers, means the object of the class Employee. Here, all the  properties of rohan and harry will be the same as they both are from the same company or from the same **template (class)**. Properties like working timings, office location, etc., will be the same. Both harry and rohan (object) will be placed in different locations in memory.

```python
harry = Employee()
rohan = Employee()
```

#### Adding methods and attributes : 

- **Attributes** mean data of the Employees such as their names, email, passwords, salary.
- **Methods** are functions written inside a class. Suppose we want to increase the salary of the Employees so we will  create a method or function to carry on this process.

There are two ways to add methods and attributes to a class.

##### Method 1 : 

1. Here we are initializing the object of class Employee with the variables fname, lname, salary **outside the** **class.** rohan and harry are the object of the class.

```python
harry.fname ="harry"
harry.lname = 'jackson'
harry.salary = 4400

rohan.fname = "rohan"
rohan.lname = "das"
rohan.salary = 4400
```

Printing the values:

```python
#Retrieve the first name of both employees.
print(harry.fname)
print(rohan.fname)

#Retrieve the last name of both employees.
print(harry.lname)
print(rohan.lname)

#Retrieve the salary of both employees.
print(harry.salary)
print(rohan.salary)
```

#####  Output : 

```python
harry
rohan 
jackson
das
4400
4400
```

 These steps can also be followed to practice class and object, but this nullifies the meaning of **class.**

##### Method 2 :

- We will start with creating a constructor inside the Employee class.
- Don’t worry constructor is nothing but a default function which is invoked automatically everytime an object is created.
- In Python, __init__() method is called everytime an object is created.

```python
def __init__(self):
    pass
```

The __init__() method accepts self as the first argument which helps  us to access the methods or attributes of the class. We can pass  multiple arguments to __init__() as shown in the code given below :

```python
def __init__(self,fname,lname,salary):  
        pass      
```

Let's create a constructor inside the Employee class :

```python
class Employee:
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
```

##### Creating objects of the Employee class :

```python
harry = Employee("harry","jackson",4400)
rohan = Employee("rohan","das",4400)      
```

In the above code :

- “harry” will go in the position of fname.
- “Jackson” will go in the position of name.
- 4400 will go in the position of salary. 
- Self is our object means harry. The same applies to the second object (rohan) also.

##### Printing values :

```python
print(harry.fname)
print(rohan.fname)
print(harry.lname)
print(rohan.lname)
print(harry.salary)
print(rohan.salary)    
```

##### Output:

```python
harry 
rohan
jackson
das
4400
4400
```

 Both the outputs are the same but Type 2 is the actual implementation of the class.

This is just the basic implementation of class and objects. In the next article, we will be discussing instances of class and variables. 

----

###  Instance and Class Variables

In the previous article, we have discussed Classes, objects, and  constructors. In this article, we are going to study Instance and class  variables. Take a look at the code given below:

```python
class Employee:
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary

# Initializing the object
harry = Employee("harry","jackson",4400)
rohan = Employee("rohan","das",4400)


print(harry.fname,rohan.fname)
```

- Here rohan and harry are the object of class Employee with attributes such as fname,lname, and salary.
- These mentioned attributes are associated with the particular object and may differ in their properties.
- But, there are many attributes which are common for all the object of the class—Eg. salary increment, total holidays, total annual race, etc.

To deal with this situation, a **class variable** is taken into consideration.

#### Class variable :

Suppose we want to increase the salary of all the Employees of the class.

1.  We will create a method which will increase the salary of all the Employees.

2.  Let the method name be increase be *increase* ***()***.

   ```python
   def increase(self): 
       pass
   ```

3. Let *increment* be the name of the variable which is responsible for the change in salary.

```python
increment = 1.5 
```

4. Why Self?
   Here, You might be thinking about why the *self* is used, or the self is passed as a parameter to the function: Just  remember, the Self is the object. In class, everything is associated  with the instance variable, i.e., Object. Here, self represents the  instance of the Class. Take a look at the example given below to get a  better understanding:

```python
harry.increase()
```

In the above code, the increase() function is called on the harry  object. Note that we have not passed any arguments in the method call,  but by default, self is passed, and self means the object itself, i.e.,  harry. Now, let's what happens if we do not pass *self* as an argument to the function.

```python
def increase():
    pass

harry.increase()
```

The above code will prompt the following error:

```python
TypeError: increase() takes 0 positional arguments but 1 was given
```

 When we call any method inside a class, self is  passed as the default argument. But, in the increase() function, we have not accepted *self* as an argument. Function increase() takes 0 argument means we have not provided any arguments, but while  function call, self is passed by default. Now, let's get back to the  increase() function, which will help us to increase the salary of the  employees. There are 2 ways to work with the increase method and increment variable.

1. ##### With the help of instance:  

   ```python
   self.salary = self.salary * self.increment
   ```

   

2. ##### With class :

```python
def __init__(self,fname,lname,salary):  
    self.fname=fname
    self.lname=lname
    self.salary=salary
    self.incriment=1.4 #instance variable

self.salary = self.salary * Employee.increment
 
```

Variable Self.salary will not search for increment in the instance and will directly use the increment of Employee class.

Now, let's create one more class variable, which will increase  the total number of employees by 1 when a new employee is added to the  Employee class, or a new object is created.

```python
class Employee:
 
    increment = 1.5
    no_of_employe= 0 #Initilizing the varaible with 0
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employe +=1 #incrementing values
 
    def increase(self):
        self.salary = int(self.salary * Employee.increment)
```

#####  Object creation :  

```python
print(Employee.no_of_employee)  #Till now, no object is created, so 0 will be printed
harry = Employee("harry","jackson",4400) #one object created, value of no_of_employee will be incremented by 1.
print(Employee.no_of_employe)  #1 will be printed
rohan = Employee("rohan","das",4400) #second object created
print(Employee.no_of_employe)  #2 will be printed
```

Output :

```python
0
1
2
```

---

###  Class Methods As Alternative Constructor

In the previous article, we discussed how to work with class methods. In  this article, we are going to discuss the class method as an alternative constructor. 

```python
class Employee:
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary

# Initializing the object
harry = Employee("harry","jackson",4400)
rohan = Employee("rohan","das",4400)


print(harry.fname,rohan.fname)
```

From the above code, it is clear that when we want to add a new object to the class Employee, we simply initialize the new object variable with the conditions such as  fname,lname, and salary. Using the object name, we can call any  function. Example :

```python
harry.increase()
```

In this above example, we have called the **increase** function using the object **harry.** This function, by default, takes the argument “self” which is our object.  But in certain conditions, we do not require any object in the function. Thus, we started using the *class method* to avoid code inefficiency. Now the question is how we can use the class method as an alternative constructor.

#### Starting with the solution:

Creating an object that holds a string. Initializing the object. Let the object name be **lovish.**

```python
lovish = Employee.from_str("lovish-jackson-76000")
```

  

The **employee** is the class, and **from_str** is the method. Now, we will create a class method that will be treated as an alternative class method. The alternative class method will take a string as input and sets all the variables. Here, **from_str** is a new method in the Class.

```python
@classmethod
    def from_str(cls,emp_string):
        fname,lname,salary= emp_string.split("-")
        return cls(fname,lname,salary)
```

Let's understand the above code line by line :

1. Here, the method from_str takes the argument *cls,* which is our class *Employee,* and *emp_strin*g is the string provided.`

2. We are using a split function that returns a list and will be  separated followed by the condition “-” and will be stored in the  respective variables, i.e., fname, name, and salary. This is parsing the string.

3. After the split, the variables will be populated in the respective variables,i.e.,

   ```python
   fname=lovish
   lname=jackson
   salary=76000k
   ```

4. At last, we are calling the class constructor or returning cls (cls is our class Employee) with fname, name, and salary.

5. **from_str** function will return an object that will be allocated in **“lovish”**

#### Getting the output :

```python
print(lovish.fname)
print(lovish.lname)
print(lovish.salary)
```

#### Output :

```python
Lovish
Jackson
7600
```

---

###  Static Methods In Python oops

In the previous article, we have discussed how to work with class methods. In this article, we are going to discuss the static method. Take a look at the code given below to remember the work that we've done in the  previous tutorial:

```python
class Employee:
    increment = 1.5
    no_of_employe= 0
 
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employe +=1
 
    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary= emp_string.split("-")
        return cls(fname,lname,salary)
 
harry = Employee("harry","jackson",4400)
lovish = Employee.from_str("lovish-jackson-7600")
rohan = Employee("rohan","das",4400)
```

In the above code, we have created class Methods to deal with class variables. The class variable is used when we don’t have any requirements for the instance variable. Now a question must have popped in your mind: Which method should be used if we don’t want to work with both the class method and the instance method? To deal with this scenario, the *static method* is taken into consideration.

#### What is static method?

- It is one type of decorator used when you don’t want any class and instance variable parameters. This is just a simple function.

- Static methods deal with the parameters, and they know nothing about the class.

  ##### Syntax: 

  ```python
  @staticmethod
  def method_name(argument):
      pass
  ```

#### Working with our Program: 

1. We are creating a static method with the name *isopen* with the argument that will be a string in datatype.

2. The approach of the program will be, if we pass the string “sunday” the function should return False else should return True.

   ##### Method: 

   ```python
   @staticmethod
   def isopne(day):
          if day=="sunday":
               return False
           else:
               return True
   ```

3. Assume, this function will return false when the company is closed and will return True in the working days.

4. Remember that, this method is neither taking class variable nor instance variable this is just a simple python function.

#### Getting the output:

1. With class:

   ```python
   print(Employee.isopen("Monday"))
   print(Employee.isopen("sunday"))
   print(Employee.isopen("tuesday"))
   ```

##### Output:

```python
True
False
```

With Instance variable:

```python
print(harry.isopen("sunday"))
print(harry.isopen("Monday"))
print(harry.isopen("tuesday"))
```

##### Output:

```python
False
True
True
```

---

###  Inheritance In Python oops

In the previous article, we have discussed classes, instance variables,  and methods. In this article, we are going to study Inheritance.  Inheritance is considered one of the four pillars of object-oriented  programming. So, let us, deep-dive into this concept.

#### What is Inheritance?

- Inheritance allows us to define a class that **inherits** all the methods and properties from another class. The parent class is the class being **inherited** from, also called the base class. The child class is the class that **inherits** from another class, also called the **derived class**.
- The question is, why we want to inherit a class? Why can't we  simply copy and paste the same code for a different class? The  straightforward answer to this question is that we do not want to copy  and paste the code because it violates the first rule of programming,  i.e., Do Not Repeat Yourself.
- The concept of inheritance was introduced to deal with the  scenarios where we want to use the methods and variables of a class in  some other class.
- Inheritance increases the **reusability** of a code so that we don’t have to write the same code again and again.

In the previous tutorial, we created a class Employee with class methods, static methods, and instance variables. Below is the code for the same:

```python
class Employee:
    increment = 1.5
    no_of_employe= 0
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employe +=1
 
    def increase(self):
        self.salary = int(self.salary * Employee.increment)
 
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
 
#shubham =Employee("shubham", "jackson", "88000")
#rohan = Employee("rohan","das",4400)
```

To understand the concept of inheritance, we will create a new class  named Programmer that will inherit the Employee class. So, let's get  started.

#### Creating a new class:

```python
class Programmer(Employee):
    pass
```

1. Here, the class Programmer will *inherit* all the methods and functions of class Employee as we have passed Employee as the **parameter** in **Programmer class.**

2. **Let us create an object of class Programmer:**

   ```python
   harry = Programmer("harry","jackson",99000)
   ```

##### Printing the output:

```python
print(harry.fname)
print(harry.lname)
print(harry.salary)
```

##### Output:

```python
harry
jackson
99000
```

Here, the **Programmer** class has inherited/copied all the methods, functions, and working of a class **Employee.** Like any other class, we can also create constructors, methods, and attributes for the **Programmer** class. So, let's do it.

#### Creating a constructor: 

```python
def __init__(self,lname,fname,salary,proglang,exp):
        super.__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp
```

- In the above code, we've used super.`__init__` to call the `__init__` of the super class.
- We've also created two instance variables named **prolang** and **exp** for the **Programmer** class.

##### Creating an object of the programmer class:

```python
abhishek = Programmer("abhishek","Pathak",10000,"python","1 yrs")
```

In the above code:

-  fname = “abhishek”
-  lname = “Pathak”
-  Salary = 10000
-  proglang = “python”
-  exp = “1 yrs”

##### Getting the output:

```python
print(abhishek.fname)
print(abhishek.lname)
print(abhishek.salary)
print(abhishek.proglang)
print(abhishek.exp)
```

##### Output:

```python
abhishek
Pathak
10000
python
1 yrs
```

Try this help function on an function to get help

```python
help(programmmer)
```

---

### What is a Dunder Method?

Dunder method also called a magic method is the method having two  prefixes and suffix underscores in the method name. Dunder here means  “Double Under (Underscores)”.

Simplifying the statement. This simply means **__methodName__**

-    To learn the Dunder Method in depth. Let us consider the following code snippet...

```python
class Employee:
    increment = 1.5
 
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
 
harry = Employee("harry", "jackson", 99000)
rohan = Employee("rohan", "das", 9)
```

In this snippet, **harry** and **rohan** are the objects of class **Employee**.

__init__ is the special method, which tends to auto-execute when the class is called.

As there are different types of Dunder Methods. Let's consider some of these...

#### 1. Dunder __add__ method:

Take a look at the below code:

```python
print(3+2)
print('rohan'+’2’)
```

**Output:**

```python
5
rohan2
```

In the above block, an addition operation is performed. The addition  of two string variables may also be referred to as a concatenation  operation.

Since we work with Dunder Method, both above addition operations can be performed with this method as follows: 

```python
a=3
#Addition
print(a.__add__(2)) 
#Multiplicaton
C= ‘rohan’
print(a.__add__(‘2’)) 
```

**Output:**

```python
5
Rohan2
```

### General Syntax of Dunder Method:

The general syntax of the Dunder method may be memorized as,

**“variable1. __methodName__(variable2)"**

Based on the above scenarios, we learned that the addition (add) has the same features as the Dunder method (__add__)

Now you're probably thinking about, if the "add" method works correctly then why should we use the "__add__" Dunder method.

Suppose we wanted to add the salaries of the two items. Assuming the answer is straightforward.

We may conduct:

```python
print(harry+rohan)
```

In this operation, to get our result, we simply add the two items of  the Employee class. This will usually provide us with an error because  we did not specify anything.

But, we want the above program to return us the addition of salaries. To obtain the desired outcome of this condition, the Dunder method can  be considered.

Dunder Method substitutes for the "add" inbuild method. The process is also called overriding. The addition operation does not differ from the __add__ method. Add  method calls the inbuilt __add__ method, which is our Dunder method.

A method called __add__ may be created within our class. Reason for  creating the method within the class as both variables are objects of  the same class.

Creating Method:

```python
def __add__(self,other):
    return self.salary + other.salary
#Printing the values
print(harry+rohan) 
```

Here:

-    self = harry,
-    other = rohan

**Output:**

```python
99009
```

This will simply return the addition of salaries of harry and rohan.

#### 2. Dunder method **__repr__**

**__repr__** is a special method used to represent a  class's objects as a string. It returns us the official string or syntax representation of the object from which it is made up.

**__repr__** can be examined with the help of the following method.

Method:

```python
def __repr__(self):
    return "Employee({},{},{})".format(self.fname,self.lname,self.salary)
print(harry)
```

**Note: “. format” is used to handle complex strings.**

**Output:**

```python
Employee(harry,jackson,99000)
```

#### 3. Dunder method __str__:

Another Dunder method similar to __repr__ is**__str__**

Both __repr__ and __str__ have the same features and both may be used in different ways.

To understand __str__ , we create a method that will return the object fname or first name. Like simple string output.

This can be achieved by:

```python
def __str__(self):
    return f"The name of the employee is {self.fname}"
print(str(harry)
```

**Output:**

```python
The name of the employee is harry
```

---

### What are Decorators?

A decorator is the design pattern that adds additional  responsibilities to an object dynamically. It's used to add additional  features to the function without modifying it.

To continue learning about what decorators are, consider the following snippet of code.

```python
class Employee:
 
    def __init__(self,fname,lname,salary):  
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
 
    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount
 
if __name__ == '__main__':
    harry = Employee("harry", "jackson", 9400)    
    rohan = Employee("rohan", "aagarwal", 9)
```

In this code snippet, **harry** and **rohan** are the objects of class **Employee.**

There are different types of decorators such as Property, setter, deletor, and many more...

Let’s elaborate on some of these decorators using our code snippet.

#### 1. Property Decorator

Property Decorator just means that by initializing **@property** before our method, we force the method to *behave like an **attribute**.*

**Let’s work with the property Decorator:**

In the above code block, suppose we want an email from the object.

This can be achieved by creating some other instance variable or method within the class. As follows:

```python
self.email = self.fname +“.”+ self.lname + "@gmail.com"
```

**Note: Email is in the format: fname.lname@gmail.com**

But, as the email is dynamically created using fname and lname.

It will be mind-tempting to customize the email field according to our desired need with all its dependencies.

To perform this very well **property decorator** can be taken into consideration.

You only need to code **@property** prior to the class function.

```python
@property()
        def email(self):
        return self.fname + "." + self.lname + "@gmail.com"
```

As in this case, our method has become an attribute. 

Let’s try to change the **lname** of the object dynamically.

```python
print(rohan.email)
    rohan.lname ="khanna" # dynamically changing the lname
    print( rohan.email)
```

Output:

```python
rohan.aagarwal@gmail.com
rohan.aagarwal@gmail.com
```

It seems that here our email declaration did not function properly. We thought it was going to be "**rohan.khanna@gmail.com**", but the email hasn't changed.

#### 2. To achieve this, we will use a **setter**.

Setter means setting the value.

In the following method, setter is performed for the Employee class.

```python
# setting the email
    @email.setter
    def email(self,given_email):
        self.email = given_email
```

**Note: given_email is our provided argument.**

Here, as setter directly defines or changes the email, this will  prompt us with an error, as the email is derived from fname and lname.

To pursue the solution. Since the email provided is in the specified  format, we can retrieve fname and lname separately in our setter method  and can be used for dynamical allocation. The **split** functionality of Python can be considered.

Creating setter:

```python
@email.setter
    def email(self,given_email):
        # self.email = given_email
        change_email = given_email.split("@")[0].split(".")[0]
        self.fname= change_email[0]  # as split return a list
        self.lname =change_email[1]
```

This function simply takes email as its argument. After the split function is implemented, it declares fname and lname as shown.

Getting the output:

```python
    rohan.email= "khanna.rohan@gmail.com"
    print(rohan.email)
```

Output:

```python
khanna.rohan@gmail.com
```

Here we get our desired output.

#### 3. **Deletor** Decorator

We also have a delete decorator that is used to **remove** the value assigned by the **setter**.

Here, the value assigned by the setter is **email**.

Let's try and remove the email field.

To pursue this, we will create a **deletor decorator**

```python
@email.deleter
    def email(self):
        self.fname=None
        self.lname =None
```

**Note: None is used here because in OOP we generally initialize the object with none rather than deleting it.**

```python
del rohan.email
        	print(rohan.email)
```

No email field will be printed.