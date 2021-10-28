**1**

```

```

# **Language Fundamentals**

## **Introduction**

 **Python is a general purpose high level programming language.**

 **Python was developed by Guido Van Rossam in 1989 while working at National
 Research Institute at Netherlands.**

 **But officially Python was made available to public in 1991. The official Date of Birth for**

```
Python is : Feb 20th 1991.
```

 **Python is recommended as first programming language for beginners.**

**Eg1: To print Helloworld:**

**Java:**

```
 public class HelloWorld
{
p s v main(String[] args)
{
SOP("Hello world");
}
}
```

**C:**

```
#include<stdio.h>
void main()
{
print("Hello world");
}
```

**Python:**

**print("Hello World")**

**2**

```

```

**Eg2: To print the sum of 2 numbers**

**Java:**

```
public class Add
{
public static void main(String[] args)
{
int a,b;
a = 10 ;
b= 20 ;
System.out.println("The Sum:"+(a+b));
}
}
```

**C:**

```
 #include <stdio.h>

void main()
{
int a,b;
a =10;
b=20;
printf("The Sum:%d",(a+b));
}
```

**Python:**

```
 a= 10
b= 20
print("The Sum:",(a+b))
```

**The name Python was selected from the TV Show**

**"The Complete
 Monty**

**Python's**

**Circus", which was broadcasted in BBC from 1969 to 1974.**

**Guido developed Python language by taking almost all programming features from**

**different languages**

**1. Functional Programming Features from C

1. Object Oriented Programming Features from C++
2. Scripting Language Features from Perl and Shell Script**

**3**

```

```

**4. Modular Programming Features from Modula- 3**

**Most of syntax in Python Derived from C and ABC languages.**

**Where we can use Python:**

**We can use everywhere. The most common important application areas are**

**1. For developing Desktop Applications

1. For developing web Applications
2. For developing database Applications
3. For Network Programming
4. For developing games
5. For Data Analysis Applications
6. For Machine Learning
7. For developing Artificial Intelligence Applications
8. For IOT**

**...**

**Note:**

**Internally Google and Youtube use Python coding**

**NASA and Nework Stock Exchange Applications developed by Python.**

**Top Software companies like Google, Microsoft, IBM, Yahoo using Python.**

**Features of Python:**

**1. Simple and easy to learn:**

**Python is a simple programming language. When we read Python program,we can feel like**

**reading english statements.**

**The syntaxes are very simple and only 30+ kerywords are available.
 When compared with other languages, we can write programs with very less number of**

**lines. Hence more readability and simplicity.
 We can reduce development and cost of the project.**

**2. Freeware and Open Source:**

**We can use Python software without any licence and it is freeware.**

**Its source code is open,so that we can we can customize based on our requirement.**

**Eg: Jython is customized version of Python to work with Java Applications.**

**4**

```

```

**3. High Level Programming language:**

**Python is high level programming language and hence it is programmer friendly language.**

**Being a programmer we are not required to concentrate low level activities like memory**

**management and security etc..**

**4. Platform Independent:**

**Once we write a Python program,it can run on any platform without rewriting once again.
 Internally PVM is responsible to convert into machine understandable form.**

**5. Portability:**

**Python programs are portable. ie we can migrate from one platform to another platform**

**very easily. Python programs will provide same results on any paltform.**

**6. Dynamically Typed:**

**In Python we are not required to declare type for variables. Whenever we are assigning**

**the value, based on value, type will be allocated automatically.Hence Python is considered
 as dynamically typed language.**

**But Java, C etc are Statically Typed Languages b'z we have to provide type at the beginning
 only.**

**This dynamic typing nature will provide more flexibility to the programmer.**

**7. Both Procedure Oriented and Object Oriented:**

**Python language supports both Procedure oriented (like C, pascal etc) and object oriented
 (like C++,Java) features. Hence we can get benefits of both like security and reusability etc**

**8. Interpreted:**

**We are not required to compile Python programs explcitly. Internally Python interpreter**

**will take care that compilation.**

**If compilation fails interpreter raised syntax errors. Once compilation success then PVM**

**(Python Virtual Machine) is responsible to execute.**

**9. Extensible:**

**We can use other language programs in Python.**

**The main advantages of this approach are:**

**5**

```

```

**1. We can use already existing legacy non-Python code

1. We can improve performance of the application
2. Embedded:**

**We can use Python programs in any other language programs.**

**i.e we can embedd Python programs anywhere.**

**11. Extensive Library:**

**Python has a rich inbuilt library.**

**Being a programmer we can use this library directly and we are not responsible to
 implement the functionality.**

**etc...**

**Limitations of Python:**

**1. Performance wise not up to the mark b'z it is interpreted language.

1. Not using for mobile Applications**

**Flavors of Python:**

**1.CPython:**

**It is the standard flavor of Python. It can be used to work with C lanugage Applications**

**2. Jython or JPython:**

**It is for Java Applications. It can run on JVM**

**3. IronPython:**

**It is for C#.Net platform**

**4.PyPy:**

**The main advantage of PyPy is performance will be improved because JIT compiler is
 available inside PVM.**

**5.RubyPython
 For Ruby Platforms**

**6. AnacondaPython
 It is specially designed for handling large volume of data processing.**

**...**

**6**

```

```

**Python Versions:**

**Python 1.0V introduced in Jan 1994
 Python 2.0V introduced in October 2000**

**Python 3.0V introduced in December 2008**

**Note: Python 3 won't provide backward compatibility to Python 2**

**i.e there is no guarantee that Python2 programs will run in Python3.**

**Current versions**

**Python 3.6.1 Python 2.7.**

**7**

```

```

# Identifiers

**A name in Python program is called identifier.**

**It can be class name or function name or module name or variable name.**

**a = 10**

**Rules to define identifiers in Python:**

**1. The only allowed characters in Python are**

```
 alphabet symbols(either lower case or upper case)
 digits(0 to 9)
 underscore symbol(_)
```

**By mistake if we are using any other symbol like $ then we will get syntax error.**

```
 cash = 10 √
 ca$h =20 
```

**2. Identifier should not starts with digit**

```
 123total 
 total123 √
```

**3. Identifiers are case sensitive. Of course Python language is case sensitive language.**

```
 total=
 TOTAL=
 print(total) #
 print(TOTAL) #
```

**8**

```

```

**Identifier:**

**1. Alphabet Symbols (Either Upper case OR Lower case)**

**2. If Identifier is start with Underscore (_) then it indicates it is private.

1. Identifier should not start with Digits.
2. Identifiers are case sensitive.**

**5. We cannot use reserved words as identifiers**

**Eg: def=10** 

**6. There is no length limit for Python identifiers. But not recommended to use too lengthy**

**identifiers.**

**7. Dollor ($) Symbol is not allowed in Python.**

**Q. Which of the following are valid Python identifiers?**

```
 123total 
total123 √
java2share √
ca$h 
_abc_abc_ √
def 
if 
```

**Note:**

**1. If identifier starts with _ symbol then it indicates that it is private

1. If identifier starts with __(two under score symbols) indicating that strongly private**

**identifier.
 3.If the identifier starts and ends with two underscore symbols then the identifier is**

**language defined special name,which is also known as magic methods.**

**Eg: \**add\****

**9**

```

```

## **Reserved Words**

**In Python some words are reserved to represent some meaning or functionality. Such type**

**of words are called Reserved words.**

**There are 33 reserved words available in Python.**

```
 True,False,None
 and, or ,not,is
 if,elif,else
 while,for,break,continue,return,in,yield
 try,except,finally,raise,assert
 import,from,as,class,def,pass,global,nonlocal,lambda,del,with
```

**Note:**

**1. All Reserved words in Python contain only alphabet symbols.

1. Except the following 3 reserved words, all contain only lower case alphabet symbols.**

```
 True
 False
 None
```

**Eg: a= true** 

**a=True** √

**>>> import keyword**

**>>> keyword.kwlist**

**['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',**

**'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']**

**10**

```

```

# **Data Types**

**Data Type represent the type of data present inside a variable.**

**In Python we are not required to specify the type explicitly. Based on value provided,the
 type will be assigned automatically.Hence Python is Dynamically Typed Language.**

**Python contains the following inbuilt data types**

**1. int

1. float**

**3.complex
 4.bool**

**5.str**

**6.bytes
 7.bytearray**

**8.range**

**9.list
 10.tuple**

**11.set**

**12.frozenset
 13.dict**

**14.None**

**Note: Python contains several inbuilt functions**

**1.type()**

**to check the type of variable**

**2. id()
 to get address of object**

```
10
10
20
a
a
b
a = 10
a = 20
a = 10
b = 10
```

**11**

```

```

**3. print()
 to print the value**

**In Python everything is object**

**int data type:**

**We can use int data type to represent whole numbers (integral values)
 Eg:**

**a=**

**type(a) #int**

**Note:**

**In Python2 we have long data type to represent very large integral values.
 But in Python3 there is no long type explicitly and we can represent long values also by**

**using int type only.**

**We can represent int values in the following ways**

**1. Decimal form

1. Binary form
2. Octal form
3. Hexa decimal form
4. Decimal form(base-10):**

**It is the default number system in Python**

**The allowed digits are: 0 to 9**

**Eg: a =**

**2. Binary form(Base-2):**

**The allowed digits are : 0 & 1
 Literal value should be prefixed with 0b or 0B**

**Eg: a = 0B
 a =0B**

**a=b**

**3. Octal Form(Base-8):**

**The allowed digits are : 0 to 7**

**Literal value should be prefixed with 0o or 0O.**

**12**

```

```

**Eg: a=0o
 a=0o**

**4. Hexa Decimal Form(Base-16):**

**The allowed digits are : 0 to 9, a-f (both lower and upper cases are allowed)**

**Literal value should be prefixed with 0x or 0X**

**Eg:**

**a =0XFACE**

**a=0XBeef
 a =0XBeer**

**Note: Being a programmer we can specify literal values in decimal, binary, octal and hexa
 decimal forms. But PVM will always provide values only in decimal form.**

**a=**

**b=0o**

**c=0X
 d=0B**

**print(a)**

**print(b)
 print(c)**

**print(d)**

**Base Conversions**

**Python provide the following in-built functions for base conversions**

**1.bin():**

**We can use bin() to convert from any base to binary**

**Eg:**

```
 >>> bin( 15 )
'0b1111'
>>> bin(0o11)
'0b1001'
>>> bin(0X10)
'0b10000'
```

**2. oct():**

**We can use oct() to convert from any base to octal**

**13**

```

```

**Eg:**

```
 >>> oct( 10 )
'0o12'
>>> oct(0B1111)
'0o17'
>>> oct(0X123)
'0o443'
```

**3. hex():**

**We can use hex() to convert from any base to hexa decimal**

**Eg:**

```
 >>> hex( 100 )
'0x64'
>>> hex(0B111111)
'0x3f'
>>> hex(0o12345)
'0x14e5'
```

**float data type:**

**We can use float data type to represent floating point values (decimal values)**

**Eg: f=1.
 type(f) float**

**We can also represent floating point values by using exponential form (scientific notation)**

**Eg: f=1.2e**

**print(f) 1200.
 instead of 'e' we can use 'E'**

**The main advantage of exponential form is we can represent big values in less memory.**

*****Note:
 We can represent int values in decimal, binary, octal and hexa decimal forms. But we can**

**represent float values only by using decimal form.**

**Eg:**

```
 >>> f=0B11. 01
File "<stdin>", line 1
f=0B11. 01
```

**14**

```

^
SyntaxError: invalid syntax
6 )
>>> f=0o123. 456
SyntaxError: invalid syntax
9 )
>>> f=0X123. 456
1 SyntaxError: invalid syntax
```

**Complex Data Type:**

**A complex number is of the form**

**a and b contain intergers or floating point values**

**Eg:
 3+5j**

**10+5.5j**

**0.5+0.1j**

**In the real part if we use int value then we can specify that either by decimal,octal,binary**

**or hexa decimal form.
 But imaginary part should be specified only by using decimal form.**

```
 >>> a=0B11+5j
>>> a
( 3 +5j)
>>> a= 3 +0B11j
SyntaxError: invalid syntax
```

**Even we can perform operations on complex type values.**

```
 >>> a= 10 +1.5j
>>> b= 20 +2.5j
>>> c=a+b
>>> print(c)
( 30 +4j)
>>> type(c)
<class 'complex'>
```

**a + bj**

```
Real Part Imaginary Part
j2 = - 1
j =
```

**15**

```

```

**Note: Complex data type has some inbuilt attributes to retrieve the real part and
 imaginary part**

**c=10.5+3.6j**

**c.real==>10.**

**c.imag==>3.**

**We can use complex type generally in scientific Applications and electrical engineering
 Applications.**

**4.bool data type:**

**We can use this data type to represent boolean values.**

**The only allowed values for this data type are:
 True and False**

**Internally Python represents True as 1 and False as 0**

**b=True
 type(b) =>bool**

**Eg:**

**a=
 b=**

**c=a<b
 print(c)==>True**

**True+True==>**

**True-False==>**

**str type:**

**str represents String data type.**

**A String is a sequence of characters enclosed within single quotes or double quotes.**

**s1='durga'**

**s1="durga"**

**By using single quotes or double quotes we cannot represent multi line string literals.**

**s1="durga**

**16**

```

```

**soft"**

**For this requirement we should go for triple single quotes(''') or triple double quotes(""")**

**s1='''durga**

**soft'''**

**s1="""durga**

**soft"""**

**We can also use triple quotes to use single quote or double quote in our String.**

**''' This is " character'''**

**' This i " Character '**

**We can embed one string in another string**

**'''This "Python class very helpful" for java students'''**

**Slicing of Strings:**

**slice means a piece**

**[ ] operator is called slice operator,which can be used to retrieve parts of String.**

**In Python Strings follows zero based index.**

**The index can be either +ve or -ve.
 +ve index means forward direction from Left to Right**

**- ve index means backward direction from Right to Left**

```
 >>> s="durga"
>>> s[ 0 ]
'd'
>>> s[ 1 ]
'u'
>>> s[- 1 ]
'a'
>>> s[ 40 ]
```

**IndexError: string index out of range**

```
d u r g a
0 1 2 3 4
```

**- 5 - 4 - 3 - 2 - 1**

**17**

```

 >>> s[ 1 : 40 ]
'urga'
>>> s[ 1 :]
'urga'
>>> s[: 4 ]
'durg'
>>> s[:]
'durga'
>>>
10 )
1
1>>> s* 3
1'durgadurgadurga'
14 )
1>>> len(s)
15
```

**Note:**

**1. In Python the following data types are considered as Fundamental Data types**

```
 int
 float
 complex
 bool
 str
```

**2. In Python,we can represent char values also by using str type and explicitly char type is
 not available.**

**Eg:**

```
 >>> c='a'
>>> type(c)
<class 'str'>
```

**3. long Data Type is available in Python2 but not in Python3. In Python3 long values also**

**we can represent by using int type only.**

**4. In Python we can present char Value also by using str Type and explicitly char Type is**

**not available.**

**18**

```

```

# **Type Casting**

**We can convert one type value to another type. This conversion is called Typecasting or**

**Type coersion.
 The following are various inbuilt functions for type casting.**

**1. int()

1. float()
2. complex()
3. bool()
4. str()**

**1.int():**

**We can use this function to convert values from other types to int**

**Eg:**

```
 >>> int(123.987)
123
>>> int( 10 +5j)
TypeError: can't convert complex to int
>>> int(True)
1
>>> int(False)
0
>>> int("10")
10
1 >>> int("10.5")
1ValueError: invalid literal for int() with base 10 : '10.5'
1>>> int("ten")
1ValueError: invalid literal for int() with base 10 : 'ten'
1>>> int("0B1111")
1ValueError: invalid literal for int() with base 10 : '0B1111'
```

**Note:**

**1. We can convert from any type to int except complex type.

1. If we want to convert str type to int type, compulsary str should contain only integral**

**value and should be specified in base- 10**

**19**

```

```

**2. float():**

**We can use float() function to convert other type values to float type.**

```
 >>> float( 10 )
10.
>>> float( 10 +5j)
TypeError: can't convert complex to float
>>> float(True)
1.
>>> float(False)
0.
>>> float("10")
10.
1 >>> float("10.5")
110.
1>>> float("ten")
1ValueError: could not convert string to float: 'ten'
1>>> float("0B1111")
1ValueError: could not convert string to float: '0B1111'
```

**Note:**

**1. We can convert any type value to float type except complex type.

1. Whenever we are trying to convert str type to float type compulsary str should be**

**either integral or floating point literal and should be specified only in base-10.**

**3.complex():**

**We can use complex() function to convert other types to complex type.**

**Form-1: complex(x)**

**We can use this function to convert x into complex number with real part x and imaginary**

**part 0.**

**Eg:**

```
 complex( 10 )==> 10 +0j
complex(10.5)===>10.5+0j
complex(True)==> 1 +0j
complex(False)==>0j
complex("10")==> 10 +0j
complex("10.5")==>10.5+0j
complex("ten")
ValueError: complex() arg is a malformed string
```

**20**

```

```

**Form-2: complex(x,y)**

**We can use this method to convert x and y into complex number such that x will be real**

**part and y will be imaginary part.**

**Eg: complex(10,-2)==>10-2j**

**complex(True,False)==>1+0j**

**4. bool():**

**We can use this function to convert other type values to bool type.**

**Eg:**

```
 bool( 0 )==>False
bool( ==>True
bool( 10 )===>True
bool(10.5)===>True
bool(0.178)==>True
bool(0.0)==>False
bool( 10 - 2j)==>True
bool( 0 +1.5j)==>True
bool( 0 +0j)==>False
bool("True")==>True
1 bool("False")==>True
1bool("")==>False
```

**21**

```

```

**5. str():**

**We can use this method to convert other type values to str type**

**Eg:**

```
 >>> str( 10 )
'10'
>>> str(10.5)
'10.5'
>>> str( 10 +5j)
'(10+5j)'
>>> str(True)
'True'
```

**Fundamental Data Types vs Immutability:**

**All Fundamental Data types are immutable. i.e once we creates an object,we cannot
 perform any changes in that object. If we are trying to change then with those changes a**

**new object will be created. This non-chageable behaviour is called immutability.**

**22**

```

```

**In Python if a new object is required, then PVM wont create object immediately. First it
 will check is any object available with the required content or not. If available then**

**existing object will be reused. If it is not available then only a new object will be created.**

**The advantage of this approach is memory utilization and performance will be improved.**

**But the problem in this approach is,several references pointing to the same object,by**

**using one reference if we are allowed to change the content in the existing object then the
 remaining references will be effected. To prevent this immutability concept is required.**

**According to this once creates an object we are not allowed to change content. If we are
 trying to change with those changes a new object will be created.**

**Eg:**

```
 >>> a= 10
>>> b= 10
>>> a is b
True
>>> id(a)
1572353952
>>> id(b)
1572353952
>>>
>>> a=10
>>> b=10
>>> id(a)
1572353952
>>> id(b)
1572353952
>>> a is b
True
>>> a=10+5j
>>> b=10+5j
>>> a is b
False
>>> id(a)
15980256
>>> id(b)
15979944
>>> a=True
>>> b=True
>>> a is b
True
>>> id(a)
1572172624
>>> id(b)
1572172624
>>> a='durga'
>>> b='durga'
>>> a is b
True
>>> id(a)
16378848
>>> id(b)
16378848
```

**23**

```

```

**bytes Data Type:**

**bytes data type represens a group of byte numbers just like an array.**

**Eg:**

```
 x = [ 10 , 20 , 30 , 40 ]
b = bytes(x)
type(b)==>bytes
print(b[ 0 ])==> 10
print(b[- 1 ])==> 40
>>> for i in b : print(i)
7 )
10
20
30
1 40
```

**Conclusion 1:**

**The only allowed values for byte data type are 0 to 256. By mistake if we are trying to
 provide any other values then we will get value error.**

**Conclusion 2:**

**Once we creates bytes data type value, we cannot change its values,otherwise we will get
 TypeError.**

**Eg:**

```
 >>> x=[ 10 , 20 , 30 , 40 ]
>>> b=bytes(x)
>>> b[ 0 ]= 100
TypeError: 'bytes' object does not support item assignment
```

**bytearray Data type:**

**bytearray is exactly same as bytes data type except that its elements can be modified.**

**Eg 1:**

```
 x=[ 10 , 20 , 30 , 40 ]
b = bytearray(x)
for i in b : print(i)
10
```

**24**

```

20
30
40
b[ 0 ]= 100
for i in b: print(i)
100
1 20
130
140
```

**Eg 2 :**

```
 >>> x =[ 10 , 256 ]
>>> b = bytearray(x)
ValueError: byte must be in range( 0 , 256 )
```

**list data type:**

**If we want to represent a group of values as a single entity where insertion order required
 to preserve and duplicates are allowed then we should go for list data type.**

**1. insertion order is preserved

1. heterogeneous objects are allowed
2. duplicates are allowed
3. Growable in nature
4. values should be enclosed within square brackets.**

**Eg:**

```
 list=[ 10 ,10.5,'durga',True, 10 ]
print(list) # [10,10.5,'durga',True,10]
```

**Eg:**

```
 list=[ 10 , 20 , 30 , 40 ]
>>> list[ 0 ]
10
>>> list[- 1 ]
40
>>> list[ 1 : 3 ]
[ 20 , 30 ]
>>> list[ 0 ]= 100
>>> for i in list:print(i)
...
1 100
120
130
```

**25**

```

140
```

**list is growable in nature. i.e based on our requirement we can increase or decrease the**

**size.**

```
 >>> list=[ 10 , 20 , 30 ]
>>> list.append("durga")
>>> list
[ 10 , 20 , 30 , 'durga']
>>> list.remove( 20 )
>>> list
[ 10 , 30 , 'durga']
>>> list2=list* 2
>>> list2
[ 10 , 30 , 'durga', 10 , 30 , 'durga']
```

**Note: An ordered, mutable, heterogenous collection of eleemnts is nothing but list, where
 duplicates also allowed.**

**tuple data type:**

**tuple data type is exactly same as list data type except that it is immutable.i.e we cannot
 chage values.**

**Tuple elements can be represented within parenthesis.**

**Eg:**

```
 t=( 10 , 20 , 30 , 40 )
type(t)
<class 'tuple'>
t[ 0 ]= 100
TypeError: 'tuple' object does not support item assignment
>>> t.append("durga")
AttributeError: 'tuple' object has no attribute 'append'
>>> t.remove( 10 )
AttributeError: 'tuple' object has no attribute 'remove'
```

**Note: tuple is the read only version of list**

**range Data Type:**

**range Data Type represents a sequence of numbers.**

**The elements present in range Data type are not modifiable. i.e range Data type is
 immutable.**

**26**

```

```

**Form-1: range(10)**

**generate numbers from 0 to 9**

**Eg:**

**r=range(10)
 for i in r : print(i) 0 to 9**

**Form-2: range(10,20)**

**generate numbers from 10 to 19**

**r = range(10,20)
 for i in r : print(i) 10 to 19**

**Form-3: range(10,20,2)**

**2 means increment value**

**r = range(10,20,2)
 for i in r : print(i) 10,12,14,16,18**

**We can access elements present in the range Data Type by using index.
 r=range(10,20)**

**r[0]==>10**

**r[15]==>IndexError: range object index out of range**

**We cannot modify the values of range data type**

**Eg:**

**r[0]=100
 TypeError: 'range' object does not support item assignment**

**We can create a list of values with range data type**

**Eg:**

```
 >>> l = list(range( 10 ))
>>> l
[ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
```

**set Data Type:**

**If we want to represent a group of values without duplicates where order is not important**

**then we should go for set Data Type.**

**27**

```

```

**1. insertion order is not preserved

1. duplicates are not allowed
2. heterogeneous objects are allowed
3. index concept is not applicable
4. It is mutable collection
5. Growable in nature**

**Eg:**

```
 s={ 100 , 0 , 10 , 200 , 10 ,'durga'}
s # {0, 100, 'durga', 200, 10}
s[ 0 ] ==>TypeError: 'set' object does not support indexing
4 )
set is growable in nature, based on our requirement we can increase or decrease the size.
6 )
>>> s.add( 60 )
>>> s
{ 0 , 100 , 'durga', 200 , 10 , 60 }
>>> s.remove( 100 )
1 >>> s
1{ 0 , 'durga', 200 , 10 , 60 }
```

**frozenset Data Type:**

**It is exactly same as set except that it is immutable.**

**Hence we cannot use add or remove functions.**

```
 >>> s={ 10 , 20 , 30 , 40 }
>>> fs=frozenset(s)
>>> type(fs)
<class 'frozenset'>
>>> fs
frozenset({ 40 , 10 , 20 , 30 })
>>> for i in fs:print(i)
...
40
10
1 20
130
13 )
1>>> fs.add( 70 )
1AttributeError: 'frozenset' object has no attribute 'add'
1>>> fs.remove( 10 )
1AttributeError: 'frozenset' object has no attribute 'remove'
```

**28**

```

```

**dict Data Type:**

**If we want to represent a group of values as key-value pairs then we should go for dict
 data type.**

**Eg:
 d={101:'durga',102:'ravi',103:'shiva'}**

**Duplicate keys are not allowed but values can be duplicated. If we are trying to insert an
 entry with duplicate key then old value will be replaced with new value.**

**Eg:**

```
1. >>> d={ 101 :'durga', 102 :'ravi', 103 :'shiva'}
2. >>> d[ 101 ]='sunny'
3. >>> d
4. { 101 : 'sunny', 102 : 'ravi', 103 : 'shiva'}
5.
6. We can create empty dictionary as follows
7. d={ }
8. We can add key-value pairs as follows
9. d['a']='apple'
10. d['b']='banana'
11. print(d)
```

**Note: dict is mutable and the order wont be preserved.**

**Note:**

**1. In general we can use bytes and bytearray data types to represent binary information
 like images,video files etc

1. In Python2 long data type is available. But in Python3 it is not available and we can
    represent long values also by using int type only.
2. In Python there is no char data type. Hence we can represent char values also by using**

**str type.**

**29**

```

```

**Summary of Datatypes in Python 3**

**Datatype Description Is Immutable Example
 Int We can use to represent the
 whole/integral numbers**

**Immutable >>> a=10

> > > type(a)
> > >  <class 'int'>
> > >  Float We can use to represent the
> > >  decimal/floating point
> > >  numbers**

**Immutable >>> b=10.5

> > > type(b)
> > >  <class 'float'>
> > >  Complex We can use to represent the
> > >  complex numbers**

**Immutable >>> c=10+5j

> > > type(c)
> > >  <class 'complex'>
> > >  c.real
> > >  10.0
> > >  c.imag
> > >  5.0
> > >  Bool We can use to represent the
> > >  logical values(Only allowed
> > >  values are True and False)**

**Immutable >>> flag=True

> > > flag=False
> > >  type(flag)
> > >  <class 'bool'>
> > >  Str To represent sequence of
> > >  Characters**

**Immutable >>> s='durga'

> > > type(s)
> > >  <class 'str'>
> > >  s="durga"
> > >  s='''Durga Software Solutions
> > >  ... Ameerpet'''
> > >  type(s)
> > >  <class 'str'>
> > >  bytes To represent a sequence of
> > >  byte values from 0- 255**

**Immutable >>> list=[1,2,3,4]

> > > b=bytes(list)
> > >  type(b)
> > >  <class 'bytes'>
> > >  bytearray To represent a sequence of
> > >  byte values from 0- 255**

**Mutable >>> list=[10,20,30]

> > > ba=bytearray(list)
> > >  type(ba)
> > >  <class 'bytearray'>
> > >  range To represent a range of
> > >  values**

**Immutable >>> r=range(10)

> > > r1=range(0,10)
> > >  r2=range(0,10,2)
> > >  list To represent an ordered
> > >  collection of objects**

**Mutable >>> l=[10,11,12,13,14,15]

> > > type(l)
> > >  <class 'list'>
> > >  tuple To represent an ordered
> > >  collections of objects**

**Immutable >>> t=(1,2,3,4,5)

> > > type(t)
> > >  <class 'tuple'>
> > >  set To represent an unordered
> > >  collection of unique objects**

```
Mutable >>> s={1,2,3,4,5,6}
>>> type(s)
```

**30**

```

```

**<class 'set'>
 frozenset To represent an unordered
 collection of unique objects**

**Immutable >>> s={11,2,3,'Durga',100,'Ramu'}

> > > fs=frozenset(s)
> > >  type(fs)
> > >  <class 'frozenset'>
> > >  dict To represent a group of key
> > >  value pairs**

```
Mutable >>>
d={101:'durga',102:'ramu',103:'hari'}
>>> type(d)
<class 'dict'>
```

**None Data Type:**

**None means Nothing or No value associated.**

**If the value is not available,then to handle such type of cases None introduced.
 It is something like null value in Java.**

**Eg:**

**def m1():
 a=10**

**print(m1())
 None**

**Escape Characters:**

**In String literals we can use esacpe characters to associate a special meaning.**

```
 >>> s="durga\nsoftware"
>>> print(s)
durga
software
>>> s="durga\tsoftware"
>>> print(s)
durga software
>>> s="This is " symbol"
File "<stdin>", line 1
s="This is " symbol"
1 ^
1SyntaxError: invalid syntax
1>>> s="This is \" symbol"
1>>> print(s)
1This is " symbol
```

**31**

```

```

**The following are various important escape characters in Python**

```
 \n==>New Line
\t===>Horizontal tab
\r ==>Carriage Return
\b===>Back space
\f===>Form Feed
\v==>Vertical tab
\'===>Single quote
\"===>Double quote
\\===>back slash symbol
....
```

**Constants:**

**Constants concept is not applicable in Python.**

**But it is convention to use only uppercase characters if we don’t want to change value.**

**MAX_VALUE=10**

**It is just convention but we can change the value.**

**1**

```

```

###### Operators

**Operator is a symbol that performs certain operations.**

**Python provides the following set of operators**

**1. Arithmetic Operators

1. Relational Operators or Comparison Operators
2. Logical operators
3. Bitwise oeprators
4. Assignment operators
5. Special operators
6. Arithmetic Operators:**

**+ ==>Addition**

**- ==>Subtraction**

*** ==>Multiplication**

**/ ==>Division operator
 % ===>Modulo operator**

**// ==>Floor Division operator**

**** ==>Exponent operator or power operator**

**Eg: test.py:**

```
 a= 10
b= 2
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a//b=',a//b)
print('a%b=',a%b)
print('a**b=',a**b)
```

**2**

```

```

**Output:**

```
 Python test.py or py test.py
a+b= 12
a-b= 8
a*b= 20
a/b= 5.0
a//b= 5
a%b= 0
a**b= 100
```

**Eg:**

```
 a = 10.5
b= 2
3 )
a+b= 12.5
a-b= 8.5
a*b= 21.0
a/b= 5.25
a//b= 5.0
a%b= 0.5
a**b= 110.25
```

**Eg:
 10/2==>5.0**

**10//2==>5**

**10.0/2===>5.0
 10.0//2===>5.0**

**Note: / operator always performs floating point arithmetic. Hence it will always returns**

**float value.**

**But Floor division (//) can perform both floating point and integral arithmetic. If**

**arguments are int type then result is int type. If atleast one argument is float type then
 result is float type.**

**Note:**

**We can use +,\* operators for str type also.**

**If we want to use + operator for str type then compulsory both arguments should be str**

**type only otherwise we will get error.**

```
 >>> "durga"+ 10
TypeError: must be str, not int
>>> "durga"+"10"
'durga10'
```

**3**

```

```

**If we use \* operator for str type then compulsory one argument should be int and other
 argument should be str type.**

**2\*"durga"
 "durga"*2**

**2.5\*"durga" ==>TypeError: can't multiply sequence by non-int of type 'float'**

**"durga"\*"durga"==>TypeError: can't multiply sequence by non-int of type 'str'**

**+====>String concatenation operator

- ===>String multiplication operator**

**Note: For any number x,**

**x/0 and x%0 always raises "ZeroDivisionError"**

**10/0
 10.0/0**

**.....**

**Relational Operators:**

**>,>=,<,<=**

**Eg 1:**

```
 a= 10
b= 20
print("a > b is ",a>b)
print("a >= b is ",a>=b)
print("a < b is ",a<b)
print("a <= b is ",a<=b)
7 )
a > b is False
a >= b is False
a < b is True
1 a <= b is True
```

**We can apply relational operators for str types also**

**Eg 2:**

```
 a="durga"
b="durga"
print("a > b is ",a>b)
print("a >= b is ",a>=b)
print("a < b is ",a<b)
```

**4**

```

print("a <= b is ",a<=b)
7 )
a > b is False
a >= b is True
a < b is False
1 a <= b is True
```

**Eg:**

```
 print(True>True) False
print(True>=True) True
print( 10 >True) True
print(False > True) False
5 )
print( 10 >'durga')
TypeError: '>' not supported between instances of 'int' and 'str'
```

**Eg:**

```
 a= 10
b= 20
if(a>b):
print("a is greater than b")
else:
print("a is not greater than b")
```

**Outputa is not greater than b**

**Note: Chaining of relational operators is possible. In the chaining, if all comparisons**

**returns True then only result is True. If atleast one comparison returns False then the**

**result is False**

**Eg:**

```
 10 < 20 ==>True
10 < 20 < 30 ==>True
10 < 20 < 30 < 40 ==>True
10 < 20 < 30 < 40 > 50 ==>False
```

**equality operators:**

**== , !=**

**We can apply these operators for any type even for incompatible types also**

```
 >>> 10 == 20
False
>>> 10 != 20
```

**5**

```

True
>>> 10 ==True
False
>>> False==False
True
>>> "durga"=="durga"
True
1 >>> 10 =="durga"
1False
```

**Note: Chaining concept is applicable for equality operators. If atleast one comparison**

**returns False then the result is False. otherwise the result is True.**

**Eg:**

```
 >>> 10 == 20 == 30 == 40
False
>>> 10 == 10 == 10 == 10
True
```

**Logical Operators:**

**and, or ,not**

**We can apply for all types.**

**For boolean types behaviour:**

**and ==>If both arguments are True then only result is True**

**or ====>If atleast one arugemnt is True then result is True**

**not ==>complement**

**True and False ==>False
 True or False ===>True**

**not False ==>True**

**For non-boolean types behaviour:**

**0 means False**

**non-zero means True
 empty string is always treated as False**

**x and y:**

**==>if x is evaluates to false return x otherwise return y**

**6**

```

```

**Eg:
 10 and 20**

**0 and 20**

**If first argument is zero then result is zero otherwise result is y**

**x or y:**

**If x evaluates to True then result is x otherwise result is y**

**10 or 20 ==> 10
 0 or 20 ==> 20**

**not x:**

**If x is evalutates to False then result is True otherwise False**

**not 10 ==>False**

**not 0 ==>True**

**Eg:**

```
 "durga" and "durgasoft" ==>durgasoft
"" and "durga" ==>""
"durga" and "" ==>""
"" or "durga" ==>"durga"
"durga" or ""==>"durga"
not ""==>True
not "durga" ==>False
```

**Bitwise Operators:**

**We can apply these operators bitwise.**

**These operators are applicable only for int and boolean types.**

**By mistake if we are trying to apply for any other type then we will get Error.**

**&,|,^,~,<<,>>**

**print(4&5) ==>valid**

**print(10.5 & 5.6) ==>**

**TypeError: unsupported operand type(s) for &: 'float' and 'float'**

**print(True & True) ==>valid**

**7**

```

```

**& ==> If both bits are 1 then only result is 1 otherwise result is 0
 | ==> If atleast one bit is 1 then result is 1 otherwise result is 0**

**^ ==>If bits are different then only result is 1 otherwise result is 0**

**~ ==>bitwise complement operator
 1==>0 & 0==>1**

**<< ==>Bitwise Left shift**

**>> ==>Bitwise Right Shift**

**print(4&5) ==>4
 print(4|5) ==>5**

**print(4^5) ==>1**

**Operator Description**

**& If both bits are 1 then only result is 1 otherwise result is 0**

**| If atleast one bit is 1 then result is 1 otherwise result is 0**

**^ If bits are different then only result is 1 otherwise result is 0**

**~ bitwise complement operator i.e 1 means 0 and 0 means 1**

**>> Bitwise Left shift Operator**

**<< Bitwise Right shift Operator**

**bitwise complement operator(~):**

**We have to apply complement for total bits.**

**Eg: print(~5) ==>- 6**

**Note:**

**The most significant bit acts as sign bit. 0 value represents +ve number where as 1**

**represents -ve value.**

**positive numbers will be repesented directly in the memory where as -ve numbers will be
 represented indirectly in 2's complement form.**

**Shift Operators:**

**<< Left shift operator**

**After shifting the empty cells we have to fill with zero**

**print(10<<2)==>40**

**0 0 0 0 1 0 1 0**

**0 0 1 0 1 0 0 0**

**8**

```

```

**>> Right Shift operator**

**After shifting the empty cells we have to fill with sign bit.( 0 for +ve and 1 for -ve)**

**print(10>>2) ==>2**

**We can apply bitwise operators for boolean types also**

**print(True & False) ==>False**

**print(True | False) ===>True**

**print(True ^ False) ==>True
 print(~True) ==>- 2**

**print(True<<2) ==>4**

**print(True>>2) ==>0**

**Assignment Operators:**

**We can use assignment operator to assign value to the variable.**

**Eg:
 x=10**

**We can combine asignment operator with some other operator to form compound
 assignment operator.**

**Eg: x+=10 ====> x = x+10**

**The following is the list of all possible compound assignment operators in Python**

**+=**

**- =
 \*=**

**/=**

**%=
 //=**

****=
 &=**

**|=**

**^=**

**0 0 0 0 1 0 1 0**

**0 0 0 0 0 0 1 0**

**9**

```

```

**>>=
 <<=**

**Eg:**

```
 x= 10
x+= 20
print(x) ==> 30
```

**Eg:**

```
 x= 10
x&= 5
print(x) ==> 0
```

**Ternary Operator:**

**Syntax:
 x = firstValue if condition else secondValue**

**If condition is True then firstValue will be considered else secondValue will be considered.**

**Eg 1:**

```
 a,b= 10 , 20
x= 30 if a<b else 40
print(x) #30
```

**Eg 2: Read two numbers from the keyboard and print minimum value**

```
 a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
min=a if a<b else b
print("Minimum Value:",min)
```

**Output:
 Enter First Number:10
 Enter Second Number:30
 Minimum Value: 10**

**Note: Nesting of ternary operator is possible.**

**10**

```

```

**Q. Program for minimum of 3 numbers**

```
 a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
min=a if a<b and a<c else b if b<c else c
print("Minimum Value:",min)
```

**Q. Program for maximum of 3 numbers**

```
 a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
max=a if a>b and a>c else b if b>c else c
print("Maximum Value:",max)
```

**Eg:**

```
 a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("Both numbers are equal" if a==b else "First Number is Less than Second Number" if
a<b else "First Number Greater than Second Number")
```

**Output:
 D:\python_classes>py test.py
 Enter First Number:10
 Enter Second Number:10
 Both numbers are equal**

**D:\python_classes>py test.py
 Enter First Number:10
 Enter Second Number:20
 First Number is Less than Second Number**

**D:\python_classes>py test.py
 Enter First Number:20
 Enter Second Number:10
 First Number Greater than Second Number**

**11**

```

```

**Special operators:**

**Python defines the following 2 special operators**

**1. Identity Operators

1. Membership operators
2. Identity Operators**

**We can use identity operators for address comparison.
 2 identity operators are available**

**1. is

1. is not**

**r1 is r2 returns True if both r1 and r2 are pointing to the same object
 r1 is not r2 returns True if both r1 and r2 are not pointing to the same object**

**Eg:**

```
 a= 10
b= 10
print(a is b) True
x=True
y=True
print( x is y) True
```

**Eg:**

```
 a="durga"
b="durga"
print(id(a))
print(id(b))
print(a is b)
```

**Eg:**

```
 list1=["one","two","three"]
list2=["one","two","three"]
print(id(list1))
print(id(list2))
print(list1 is list2) False
print(list1 is not list2) True
print(list1 == list2) True
```

**12**

```

```

**Note:**

**We can use is operator for address comparison where as == operator for content
 comparison.**

**2. Membership operators:**

**We can use Membership operators to check whether the given object present in the**

**given collection.(It may be String,List,Set,Tuple or Dict)**

**in**  **Returns True if the given object present in the specified Collection**

**not in**  **Retruns True if the given object not present in the specified Collection**

**Eg:**

```
 x="hello learning Python is very easy!!!"
print('h' in x) True
print('d' in x) False
print('d' not in x) True
print('Python' in x) True
```

**Eg:**

```
 list1=["sunny","bunny","chinny","pinny"]
print("sunny" in list1) True
print("tunny" in list1) False
print("tunny" not in list1) True
```

**Operator Precedence:**

**If multiple operators present then which operator will be evaluated first is decided by**

**operator precedence.**

**Eg:**

**print(3+10\*2)**  **23**

**print((3+10)\*2)**  **26**

**The following list describes operator precedence in Python**

**()**  **Parenthesis**

******  **exponential operator**

**~,-**  **Bitwise complement operator,unary minus operator
 \*,/,%,//**  **multiplication,division,modulo,floor division**

**+,-**  **addition,subtraction**

**<<,>>**  **Left and Right Shift
 &**  **bitwise And**

**13**

```

```

**^**  **Bitwise X-OR
 |**  **Bitwise OR**

**>,>=,<,<=, ==, != ==>Relational or Comparison operators**

**=,+=,-=,\*=... ==>Assignment operators
 is , is not**  **Identity Operators**

**in , not in**  **Membership operators**

**not**  **Logical not
 and**  **Logical and**

**or**  **Logical or**

**Eg:**

```
 a= 30
b= 20
c= 10
d= 5
print((a+b)*c/d) 100.0
print((a+b)*(c/d)) 100.0
print(a+(b*c)/d) 70.0
8 )
9 )
3 / 2 * 4 + 3 +( 10 / 5 )** 3 - 2
1 3 / 2 * 4 + 3 +2.0** 3 - 2
13 / 2 * 4 + 3 +8.0- 2
11.5* 4 + 3 +8.0- 2
16.0+ 3 +8.0- 2
115.0
```

**14**

```

```

**Mathematical Functions (math Module)**

**A Module is collection of functions, variables and classes etc.**

**math is a module that contains several functions to perform mathematical operations**

**If we want to use any module in Python, first we have to import that module.**

**import math**

**Once we import a module then we can call any function of that module.**

**import math
 print(math.sqrt(16))**

**print(math.pi)**

**4.0**

**3.141592653589793**

**We can create alias name by using as keyword.**

**import math as m**

**Once we create alias name, by using that we can access functions and variables of that
 module**

**import math as m
 print(m.sqrt(16))**

**print(m.pi)**

**We can import a particular member of a module explicitly as follows**

**from math import sqrt
 from math import sqrt,pi**

**If we import a member explicitly then it is not required to use module name while**

**accessing.**

**from math import sqrt,pi**

**print(sqrt(16))**

**print(pi)
 print(math.pi)**  **NameError: name 'math' is not defined**

**15**

```

```

**important functions of math module:**

**ceil(x)
 floor(x)**

**pow(x,y)**

**factorial(x)
 trunc(x)**

**gcd(x,y)**

**sin(x)
 cos(x)**

**tan(x)**

**....**

**important variables of math module:**

**pi3.14**

**e===>2.71**

**inf ==>infinity
 nan ==>not a number**

**Q. Write a Python program to find area of circle**

**pi\*r**2**

**from math import pi**

**r=16
 print("Area of Circle is :",pi\*r**2)**

**OutputArea of Circle is : 804.247719318987**

**1**

```

```

**Input And Output Statements**

**Reading dynamic input from the keyboard:**

**In Python 2 the following 2 functions are available to read dynamic input from the**

**keyboard.**

**1. raw_input()

1. input()
2. raw_input():**

**This function always reads the data from the keyboard in the form of String Format. We**

**have to convert that string type to our required type by using the corresponding type
 casting methods.**

**Eg:
 x=raw_input("Enter First Number:")**

**print(type(x)) It will always print str type only for any input type**

**2. input():**

**input() function can be used to read data directly in our required format.We are not**

**required to perform type casting.**

**x=input("Enter Value)**

**type(x)**

**10 ===> int**

**"durga"===>str
 10.5===>float**

**True==>bool**

*****Note: But in Python 3 we have only input() method and raw_input() method is not**

**available.**

**Python3 input() function behaviour exactly same as raw_input() method of Python2. i.e**

**every input value is treated as str type only.**

**raw_input() function of Python 2 is renamed as input() function in Python 3**

**2**

```

```

**Eg:**

```
 >>> type(input("Enter value:"))
Enter value: 10
<class 'str'>
4 )
Enter value:10.5
<class 'str'>
7 )
Enter value:True
<class 'str'>
```

**Q. Write a program to read 2 numbers from the keyboard and print sum.**

```
 x=input("Enter First Number:")
y=input("Enter Second Number:")
i = int(x)
j = int(y)
print("The Sum:",i+j)
6 )
Enter First Number: 100
Enter Second Number: 200
The Sum: 300
```

**-----------------------------------------------------**

```
 x=int(input("Enter First Number:"))
y=int(input("Enter Second Number:"))
print("The Sum:",x+y)
```

**-----------------------------------------------------------**

```
 print("The Sum:",int(input("Enter First Number:"))+int(input("Enter Second Number:")))
```

**Q. Write a program to read Employee data from the keyboard and print that data.**

```
 eno=int(input("Enter Employee No:"))
ename=input("Enter Employee Name:")
esal=float(input("Enter Employee Salary:"))
eaddr=input("Enter Employee Address:")
married=bool(input("Employee Married ?[True|False]:"))
print("Please Confirm Information")
print("Employee No :",eno)
print("Employee Name :",ename)
print("Employee Salary :",esal)
print("Employee Address :",eaddr)
1 print("Employee Married? :",married)
12 )
```

**3**

```

1D:\Python_classes>py test.py
1Enter Employee No: 100
1Enter Employee Name:Sunny
1Enter Employee Salary: 1000
1Enter Employee Address:Mumbai
1Employee Married ?[True|False]:True
1Please Confirm Information
20 ) Employee No : 100
2 Employee Name : Sunny
2Employee Salary : 1000.0
2Employee Address : Mumbai
2Employee Married? : True
```

**How to read multiple values from the keyboard in a single line:**

```
 a,b= [int(x) for x in input("Enter 2 numbers :").split()]
print("Product is :", a*b)
3 )
D:\Python_classes>py test.py
Enter 2 numbers : 10 20
Product is : 200
```

**Note: split() function can take space as seperator by default .But we can pass**

**anything as seperator.**

**Q. Write a program to read 3 float numbers from the keyboard with , seperator and print**

**their sum.**

```
 a,b,c= [float(x) for x in input("Enter 3 float numbers :").split(',')]
print("The Sum is :", a+b+c)
3 )
D:\Python_classes>py test.py
Enter 3 float numbers :10.5,20.6,20.1
The Sum is : 51.2
```

**eval():**

**eval Function take a String and evaluate the Result.**

**Eg: x = eval(“10+20+30”)**

**print(x)**

**Output: 60**

**Eg: x = eval(input(“Enter Expression”))**

**Enter Expression: 10+2\*3/4**

**Output11.5**

**4**

```

```

**eval() can evaluate the Input to list, tuple, set, etc based the provided Input.**

**Eg: Write a Program to accept list from the keynboard on the display**

```
 l = eval(input(“Enter List”))
print (type(l))
print(l)
```

**Command Line Arguments**

 **argv is not Array it is a List. It is available sys Module.**

 **The Argument which are passing at the time of execution are called Command Line**

```
Arguments.
```

**Eg: D:\Python_classes py test.py 10 20 30**

**Command Line Arguments**

**Within the Python Program this Command Line Arguments are available in argv. Which is**

**present in SYS Module.**

**Note: argv[0] represents Name of Program. But not first Command Line Argument.**

**argv[1] represent First Command Line Argument.**

**Program: To check type of argv from sys**

**import argv**

**print(type(argv))**

**D:\Python_classes\py test.py**

**Write a Program to display Command Line Arguments**

```
 from sys import argv
print(“The Number of Command Line Arguments:”, len(argv))
print(“The List of Command Line Arguments:”, argv)
print(“Command Line Arguments one by one:”)
for x in argv:
print(x)
7 )
D:\Python_classes>py test.py 10 20 30
The Number of Command Line Arguments: 4
test.py 10 20 30
```

**5**

```

The List of Command Line Arguments: [‘test.py’, ‘ 10 ’,’ 20 ’,’ 30 ’]
1 Command Line Arguments one by one:
1test.py
110
120
130
 from sys import argv
sum= 0
args=argv[ 1 :]
for x in args :
n=int(x)
sum=sum+n
print("The Sum:",sum)
8 )
D:\Python_classes>py test.py 10 20 30 40
The Sum: 100
```

**Note1: usually space is seperator between command line arguments. If our command line**

**argument itself contains space then we should enclose within double quotes(but not
 single quotes)**

**Eg:**

```
 from sys import argv
print(argv[ 1 ])
3 )
D:\Python_classes>py test.py Sunny Leone
Sunny
6 )
D:\Python_classes>py test.py 'Sunny Leone'
'Sunny
9 )
D:\Python_classes>py test.py "Sunny Leone"
1 Sunny Leone
```

**Note2: Within the Python program command line arguments are available in the String**

**form. Based on our requirement,we can convert into corresponding type by using type**

**casting methods.**

**Eg:**

```
 from sys import argv
print(argv[ 1 ]+argv[ 2 ])
print(int(argv[ 1 ])+int(argv[ 2 ]))
```

**6**

```

4 )
D:\Python_classes>py test.py 10 20
1020
30
```

**Note3: If we are trying to access command line arguments with out of range index then**

**we will get Error.**

**Eg:**

```
 from sys import argv
print(argv[ 100 ])
3 )
D:\Python_classes>py test.py 10 20
IndexError: list index out of range
```

**Note:**

**In Python there is argparse module to parse command line arguments and display some
 help messages whenever end user enters wrong input.**

**input()
 raw_input()**

**command line arguments**

**output statements:**

**We can use print() function to display output.**

**Form-1: print() without any argument**

**Just it prints new line character**

**Form-2:**

```
 print(String):
print("Hello World")
We can use escape characters also
print("Hello \n World")
print("Hello\tWorld")
We can use repetetion operator (*) in the string
print( 10 *"Hello")
print("Hello"* 10 )
We can use + operator also
print("Hello"+"World")
```

**7**

```

```

**Note:**

**If both arguments are String type then + operator acts as concatenation operator.**

**If one argument is string type and second is any other type like int then we will get Error**

**If both arguments are number type then + operator acts as arithmetic addition operator.**

**Note:**

```
 print("Hello"+"World")
print("Hello","World")
3 )
HelloWorld
Hello World
```

**Form-3: print() with variable number of arguments:**

```
1. a,b,c= 10 , 20 , 30
2. print("The Values are :",a,b,c)
3.
4. OutputThe Values are : 10 20 30
```

**By default output values are seperated by space.If we want we can specify seperator by
 using "sep" attribute**

```
1. a,b,c= 10 , 20 , 30
2. print(a,b,c,sep=',')
3. print(a,b,c,sep=':')
4.
5. D:\Python_classes>py test.py
6. 10 , 20 , 30
7. 10 : 20 : 30
```

**Form-4:print() with end attribute:**

```
1. print("Hello")
2. print("Durga")
3. print("Soft")
```

**Output:**

```
1. Hello
2. Durga
3. Soft
```

**If we want output in the same line with space**

**8**

```

1. print("Hello",end=' ')
2. print("Durga",end=' ')
3. print("Soft")
```

**Output: Hello Durga Soft**

**Note: The default value for end attribute is \n,which is nothing but new line character.**

**Form-5: print(object) statement:**

**We can pass any object (like list,tuple,set etc)as argument to the print() statement.**

**Eg:**

```
1. l=[ 10 , 20 , 30 , 40 ]
2. t=( 10 , 20 , 30 , 40 )
3. print(l)
4. print(t)
```

**Form-6: print(String,variable list):**

**We can use print() statement with String and any number of arguments.**

**Eg:**

```
1. s="Durga"
2. a= 48
3. s1="java"
4. s2="Python"
5. print("Hello",s,"Your Age is",a)
6. print("You are teaching",s1,"and",s2)
```

**Output:**

```
 Hello Durga Your Age is 48
You are teaching java and Python
```

**Form-7: print(formatted string):**

**%i====>int**

**%d====>int**

**%f=====>float
 %s======>String type**

**9**

```

```

**Syntax:**

**print("formatted string" %(variable list))**

**Eg 1 :**

```
 a= 10
b= 20
c= 30
print("a value is %i" %a)
print("b value is %d and c value is %d" %(b,c))
6 )
Output
a value is 10
b value is 20 and c value is 30
```

**Eg 2 :**

```
 s="Durga"
list=[ 10 , 20 , 30 , 40 ]
print("Hello %s ...The List of Items are %s" %(s,list))
4 )
Output Hello Durga ...The List of Items are [ 10 , 20 , 30 , 40 ]
```

**Form-8: print() with replacement operator {}**

**Eg:**

```
 name="Durga"
salary= 10000
gf="Sunny"
print("Hello {0} your salary is {1} and Your Friend {2} is waiting".format(name,salary,gf))
print("Hello {x} your salary is {y} and Your Friend {z} is waiting".format(x=name,y=salary,z=
gf))
6 )
Output
Hello Durga your salary is 10000 and Your Friend Sunny is waiting
Hello Durga your salary is 10000 and Your Friend Sunny is waiting
```

**1**

```

```

**Flow Control**

```
Flow control describes the order in which statements will be executed at runtime.
```

**I. Conditional Statements**

** if**

```
if condition : statement
or
if condition :
statement- 1
statement- 2
statement- 3
If condition is true then statements will be executed.
```

**Control Flow**

```
Conditional
Statements
Transfer
Statements
Iterative
Statements
 if
if-elif
if-elif-else
 break
continue
pass
 for
while
```

**2**

```

```

**Eg:**

```
 name=input("Enter Name:")
if name=="durga" :
print("Hello Durga Good Morning")
print("How are you!!!")
5 )
D:\Python_classes>py test.py
Enter Name:durga
Hello Durga Good Morning
How are you!!!
10 )
1 D:\Python_classes>py test.py
1Enter Name:Ravi
1How are you!!!
```

**if-else:**

**if condition :
 Action- 1**

**else :
 Action- 2**

**if condition is true then Action-1 will be executed otherwise Action-2 will be executed.**

**Eg:**

```
 name=input("Enter Name:")
if name=="durga" :
print("Hello Durga Good Morning")
else:
print("Hello Guest Good Moring")
print("How are you!!!")
7 )
D:\Python_classes>py test.py
Enter Name:durga
Hello Durga Good Morning
1 How are you!!!
12 )
1D:\Python_classes>py test.py
1Enter Name:Ravi
1Hello Guest Good Moring
1How are you!!!
```

**3**

```

```

**if-elif-else:**

**Syntax:**

**if condition1:**

**Action- 1
 elif condition2:**

**Action- 2**

**elif condition3:
 Action- 3**

**elif condition4:**

**Action- 4
 ...**

**else:**

**Default Action**

**Based condition the corresponding action will be executed.**

**Eg:**

```
 brand=input("Enter Your Favourite Brand:")
if brand=="RC" :
print("It is childrens brand")
elif brand=="KF":
print("It is not that much kick")
elif brand=="FO":
print("Buy one get Free One")
else :
print("Other Brands are not recommended")
10 )
1
1D:\Python_classes>py test.py
1Enter Your Favourite Brand:RC
1It is childrens brand
15 )
1D:\Python_classes>py test.py
1Enter Your Favourite Brand:KF
1It is not that much kick
19 )
20 ) D:\Python_classes>py test.py
2 Enter Your Favourite Brand:KALYANI
2Other Brands are not recommended
```

**4**

```

```

**Note:**

**1. else part is always optional
 Hence the following are various possible syntaxes.

1. if
2. if - else
3. if-elif-else**

**4.if-elif**

**2. There is no switch statement in Python**

**Q. Write a program to find biggest of given 2 numbers from the commad prompt?**

```
 n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
if n1>n2:
print("Biggest Number is:",n1)
else :
print("Biggest Number is:",n2)
7 )
D:\Python_classes>py test.py
Enter First Number: 10
Enter Second Number: 20
1 Biggest Number is: 20
```

**Q. Write a program to find biggest of given 3 numbers from the commad prompt?**

```
 n1=int(input("Enter First Number:"))
n2=int(input("Enter Second Number:"))
n3=int(input("Enter Third Number:"))
if n1>n2 and n1>n3:
print("Biggest Number is:",n1)
elif n2>n3:
print("Biggest Number is:",n2)
else :
print("Biggest Number is:",n3)
10 )
1 D:\Python_classes>py test.py
1Enter First Number: 10
1Enter Second Number: 20
1Enter Third Number: 30
1Biggest Number is: 30
16 )
1D:\Python_classes>py test.py
1Enter First Number: 10
```

**5**

```

1Enter Second Number: 30
20 ) Enter Third Number: 20
2 Biggest Number is: 30
```

**Q. Write a program to find smallest of given 2 numbers?
 Q. Write a program to find smallest of given 3 numbers?**

**Q. Write a program to check whether the given number is even or odd?
 Q. Write a program to check whether the given number is in between 1 and 100?**

```
 n=int(input("Enter Number:"))
if n>= 1 and n<= 10 :
print("The number",n,"is in between 1 to 10")
else:
print("The number",n,"is not in between 1 to 10")
```

**Q. Write a program to take a single digit number from the key board and print is value in**

**English word?**

```
 0 ==>ZERO
1 ==>ONE
3 )
n=int(input("Enter a digit from o to 9:"))
if n== 0 :
print("ZERO")
elif n== 1 :
print("ONE")
elif n== 2 :
print("TWO")
1 elif n== 3 :
1print("THREE")
1elif n== 4 :
1print("FOUR")
1elif n== 5 :
1print("FIVE")
1elif n== 6 :
1print("SIX")
1elif n== 7 :
20 ) print("SEVEN")
2 elif n== 8 :
2print("EIGHT")
2elif n== 9 :
2print("NINE")
2else:
2print("PLEASE ENTER A DIGIT FROM 0 TO 9")
```

**6**

```

```

**II. Iterative Statements**

```
If we want to execute a group of statements multiple times then we should go for
Iterative statements.
Python supports 2 types of iterative statements.
```

**1. for loop

1. while loop**

** for loop:**

```
If we want to execute some action for every element present in some sequence(it may be
string or collection)then we should go for for loop.
Syntax:
for x in sequence :
body
where sequence can be string or any collection.
Body will be executed for every element present in the sequence.
Eg 1 : To print characters present in the given string
 s="Sunny Leone"
for x in s :
print(x)
4 )
Output
S
u
n
n
y
1
1L
1e
1o
1n
1e
```

**7**

```

```

**Eg 2: To print characters present in string index wise:**

```
 s=input("Enter some String: ")
i= 0
for x in s :
print("The character present at ",i,"index is :",x)
i=i+ 1
6 )
7 )
D:\Python_classes>py test.py
Enter some String: Sunny Leone
The character present at 0 index is : S
1 The character present at 1 index is : u
1The character present at 2 index is : n
1The character present at 3 index is : n
1The character present at 4 index is : y
1The character present at 5 index is :
1The character present at 6 index is : L
1The character present at 7 index is : e
1The character present at 8 index is : o
1The character present at 9 index is : n
20 ) The character present at 10 index is : e
```

**Eg 3 : To print Hello 10 times**

```
 for x in range( :
print("Hello")
```

**Eg 4 : To display numbers from 0 to 10**

```
 for x in range( 1 :
print(x)
```

**Eg 5 : To display odd numbers from 0 to 20**

```
 for x in range( 2 :
if (x% 2 != 0 ):
print(x)
```

**Eg 6 : To display numbers from 10 to 1 in descending order**

```
 for x in range( 10 , 0 ,-  :
print(x)
```

**8**

```

```

**Eg 7 : To print sum of numbers presenst inside list**

```
 list=eval(input("Enter List:"))
sum= 0 ;
for x in list:
sum=sum+x;
print("The Sum=",sum)
6 )
D:\Python_classes>py test.py
Enter List:[ 10 , 20 , 30 , 40 ]
The Sum= 100
10 )
1 D:\Python_classes>py test.py
1Enter List:[ 45 , 67 ]
1The Sum= 112
```

**while loop:**

**If we want to execute a group of statements iteratively until some condition false,then we**

**should go for while loop.**

**Syntax:**

**while condition :**

**body**

**Eg: To print numbers from 1 to 10 by using while loop**

```
 x= 1
while x <= 10 :
print(x)
x=x+ 1
```

**Eg: To display the sum of first n numbers**

```
 n=int(input("Enter number:"))
sum= 0
i= 1
while i<=n:
sum=sum+i
i=i+ 1
print("The sum of first",n,"numbers is :",sum)
```

**9**

```

```

**Eg: write a program to prompt user to enter some name until entering Durga**

```
 name=""
while name!="durga":
name=input("Enter Name:")
print("Thanks for confirmation")
```

**Infinite Loops:**

```
 i= 0 ;
while True :
i=i+ 1 ;
print("Hello",i)
```

**Nested Loops:**

**Sometimes we can take a loop inside another loop,which are also known as nested loops.**

**Eg:**

```
 for i in range( 4 ):
for j in range( 4 ):
print("i=",i," j=",j)
4 )
Output
D:\Python_classes>py test.py
i= 0 j= 0
i= 0 j= 1
i= 0 j= 2
i= 0 j= 3
1 i= 1 j= 0
1i= 1 j= 1
1i= 1 j= 2
1i= 1 j= 3
1i= 2 j= 0
1i= 2 j= 1
1i= 2 j= 2
1i= 2 j= 3
1i= 3 j= 0
20 ) i= 3 j= 1
2 i= 3 j= 2
2i= 3 j= 3
```

**10**

```

```

**Q. Write a program to dispaly \*'s in Right angled triangled form**

```
 *
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
8 )
n = int(input("Enter number of rows:"))
for i in range( 1 ,n+ :
1 for j in range( 1 ,i+ :
1print("*",end=" ")
1print()
```

**Alternative way:**

```
 n = int(input("Enter number of rows:"))
for i in range( 1 ,n+ :
print("* " * i)
```

**Q. Write a program to display \*'s in pyramid style(also known as equivalent triangle)**

```
 *
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
8 )
n = int(input("Enter number of rows:"))
for i in range( 1 ,n+ :
1 print(" " * (n-i),end="")
1print("* "*i)
```

**11**

```

```

**III. Transfer Statements**

** break:**

```
We can use break statement inside loops to break loop execution based on some
condition.
Eg:
 for i in range( 10 ):
if i== 7 :
print("processing is enough..plz break")
break
print(i)
6 )
D:\Python_classes>py test.py
0
1
2
1 3
14
15
16
1processing is enough..plz break
Eg:
 cart=[ 10 , 20 , 600 , 60 , 70 ]
for item in cart:
if item> 500 :
print("To place this order insurence must be required")
break
print(item)
7 )
D:\Python_classes>py test.py
10
20
1 To place this order insurence must be required
```

**12**

```

```

**continue:**

**We can use continue statement to skip current iteration and continue next iteration.**

**Eg 1 : To print odd numbers in the range 0 to 9**

```
 for i in range( 10 ):
if i% 2 == 0 :
continue
print(i)
5 )
D:\Python_classes>py test.py
1
3
5
7
1 9
```

**Eg 2 :**

```
 cart=[ 10 , 20 , 500 , 700 , 50 , 60 ]
for item in cart:
if item>= 500 :
print("We cannot process this item :",item)
continue
print(item)
7 )
Output
D:\Python_classes>py test.py
10
1 20
1We cannot process this item : 500
1We cannot process this item : 700
150
160
```

**Eg 3 :**

```
 numbers=[ 10 , 20 , 0 , 5 , 0 , 30 ]
for n in numbers:
if n== 0 :
print("Hey how we can divide with zero..just skipping")
continue
print("100/{} = {}".format(n, 100 /n))
7 )
```

**13**

```

Output
9 )
100 / 10 = 10.0
1 100 / 20 = 5.0
1Hey how we can divide with zero..just skipping
1100 / 5 = 20.0
1Hey how we can divide with zero..just skipping
1100 / 30 = 3.3333333333333335
```

**loops with else block:**

**Inside loop execution,if break statement not executed ,then only else part will be
 executed.**

**else means loop without break**

**Eg:**

```
 cart=[ 10 , 20 , 30 , 40 , 50 ]
for item in cart:
if item>= 500 :
print("We cannot process this order")
break
print(item)
else:
print("Congrats ...all items processed successfully")
9 )
Output
1 10
120
130
140
150
1Congrats ...all items processed successfully
```

**Eg:**

```
 cart=[ 10 , 20 , 600 , 30 , 40 , 50 ]
for item in cart:
if item>= 500 :
print("We cannot process this order")
break
print(item)
else:
print("Congrats ...all items processed successfully")
```

**14**

```

9 )
Output
1 D:\Python_classes>py test.py
110
120
1We cannot process this order
```

**Q. What is the difference between for loop and while loop in Python?**

**We can use loops to repeat code execution
 Repeat code for every item in sequence ==>for loop**

**Repeat code as long as condition is true ==>while loop**

**Q. How to exit from the loop?**

**by using break statement**

**Q. How to skip some iterations inside loop?**

**by using continue statement.**

**Q. When else part will be executed wrt loops?**

**If loop executed without break**

**pass statement:**

**pass is a keyword in Python.**

**In our programming syntactically if block is required which won't do anything then we can**

**define that empty block with pass keyword.**

**pass**

**|- It is an empty statement
 |- It is null statement**

**|- It won't do anything**

**Eg:**

**if True:
 SyntaxError: unexpected EOF while parsing**

**if True: pass
 ==>valid**

**def m1():
 SyntaxError: unexpected EOF while parsing**

**15**

```

```

**def m1(): pass**

**use case of pass:**

**Sometimes in the parent class we have to declare a function with empty body and child
 class responsible to provide proper implementation. Such type of empty body we can**

**define by using pass keyword. (It is something like abstract method in java)**

**Eg:**

**def m1(): pass**

**Eg:**

```
 for i in range( 100 ):
if i% 9 == 0 :
print(i)
else:pass
5 )
D:\Python_classes>py test.py
0
9
18
27
1 36
145
154
163
172
181
190
199
```

**del statement:**

**del is a keyword in Python.**

**After using a variable, it is highly recommended to delete that variable if it is no longer
 required,so that the corresponding object is eligible for Garbage Collection.**

**We can delete variable by using del keyword.**

**Eg:**

```
 x= 10
print(x)
del x
```

**16**

```

```

**After deleting a variable we cannot access that variable otherwise we will get NameError.**

**Eg:**

```
 x= 10
del x
print(x)
```

**NameError: name 'x' is not defined.**

**Note:**

**We can delete variables which are pointing to immutable objects.But we cannot delete**

**the elements present inside immutable object.**

**Eg:**

```
 s="durga"
print(s)
del s==>valid
del s[ 0 ] ==>TypeError: 'str' object doesn't support item deletion
```

**Difference between del and None:**

**In the case del, the variable will be removed and we cannot access that variable(unbind**

**operation)**

```
 s="durga"
del s
print(s) ==>NameError: name 's' is not defined.
```

**But in the case of None assignment the variable won't be removed but the corresponding**

**object is eligible for Garbage Collection(re bind operation). Hence after assigning with
 None value,we can access that variable.**

```
 s="durga"
s=None
print(s) # None
```

**1**

```

```

**String Data Type**

**The most commonly used object in any project and in any programming language is String only.
 Hence we should aware complete information about String data type.**

**What is String?**

**Any sequence of characters within either single quotes or double quotes is considered as a String.**

**Syntax:
 s='durga'
 s="durga"**

**Note: In most of other languges like C, C++,Java, a single character with in single quotes is treated
 as char data type value. But in Python we are not having char data type.Hence it is treated as
 String only.**

**Eg:

> > > ch='a'
> > >  type(ch)
> > >  <class 'str'>**

**How to define multi-line String literals:**

**We can define multi-line String literals by using triple single or double quotes.**

**Eg:

> > > s='''durga
> > >  software
> > >  solutions'''**

**We can also use triple quotes to use single quotes or double quotes as symbol inside String literal.**

**Eg:
 s='This is ' single quote symbol' ==>invalid
 s='This is ' single quote symbol' ==>valid
 s="This is ' single quote symbol"====>valid
 s='This is " double quotes symbol' ==>valid
 s='The "Python Notes" by 'durga' is very helpful' ==>invalid
 s="The "Python Notes" by 'durga' is very helpful"==>invalid
 s='The "Python Notes" by 'durga' is very helpful' ==>valid
 s='''The "Python Notes" by 'durga' is very helpful''' ==>valid**

**2**

```

```

**How to access characters of a String:**

**We can access characters of a string by using the following ways.**

**1. By using index

1. By using slice operator
2. By using index:**

**Python supports both +ve and -ve index.
 +ve index means left to right(Forward direction)**

**- ve index means right to left(Backward direction)**

**Eg:
 s='durga'**

**diagram**

**Eg:

> > > s='durga'
> > >  s[0]
> > >  'd'
> > >  s[4]
> > >  'a'
> > >  s[-1]
> > >  'a'
> > >  s[10]
> > >  IndexError: string index out of range**

**Note: If we are trying to access characters of a string with out of range index then we will get
 error saying : IndexError**

**Q. Write a program to accept some string from the keyboard and display its characters by**

**index wise(both positive and nEgative index)**

**test.py:**

```
 s=input("Enter Some String:")
i= 0
for x in s:
print("The character present at positive index {} and at nEgative index {} is {}".format(i,i
```

**- len(s),x))
 i=i+ 1**

**Output:
 D:\python_classes>py test.py
 Enter Some String:durga**

**3**

```

```

**The character present at positive index 0 and at nEgative index -5 is d
 The character present at positive index 1 and at nEgative index -4 is u
 The character present at positive index 2 and at nEgative index -3 is r
 The character present at positive index 3 and at nEgative index -2 is g
 The character present at positive index 4 and at nEgative index -1 is a**

**2. Accessing characters by using slice operator:**

**Syntax: s[bEginindex:endindex:step]**

**bEginindex:From where we have to consider slice(substring)
 endindex: We have to terminate the slice(substring) at endindex- 1
 step: incremented value**

**Note: If we are not specifying bEgin index then it will consider from bEginning of the string.
 If we are not specifying end index then it will consider up to end of the string
 The default value for step is 1**

**Eg:**

```
 >>> s="Learning Python is very very easy!!!"
>>> s[ 1 : 7 : 1 ]
'earnin'
>>> s[ 1 : 7 ]
'earnin'
>>> s[ 1 : 7 : 2 ]
'eri'
>>> s[: 7 ]
'Learnin'
>>> s[ 7 :]
1 'g Python is very very easy!!!'
1>>> s[::]
1'Learning Python is very very easy!!!'
1>>> s[:]
1'Learning Python is very very easy!!!'
1>>> s[::- 1 ]
1'!!!ysae yrev yrev si nohtyP gninraeL'
```

**Behaviour of slice operator:**

**s[bEgin:end:step]**

**step value can be either +ve or –ve**

**if +ve then it should be forward direction(left to right) and we have to consider bEgin to end- 1**

**if -ve then it should be backward direction(right to left) and we have to consider bEgin to end+1**

**4**

```

```

*****Note:
 In the backward direction if end value is -1 then result is always empty.
 In the forward direction if end value is 0 then result is always empty.**

**In forward direction:**

**default value for bEgin: 0
 default value for end: length of string
 default value for step: +1**

**In backward direction:**

**default value for bEgin: - 1
 default value for end: -(length of string+1)**

**Note: Either forward or backward direction, we can take both +ve and -ve values for bEgin and
 end index.**

**Mathematical Operators for String:**

**We can apply the following mathematical operators for Strings.**

**1. + operator for concatenation

1. - operator for repetition**

**print("durga"+"soft") #durgasoft
 print("durga"\*2) #durgadurga**

**Note:**

**1. To use + operator for Strings, compulsory both arguments should be str type

1. To use * operator for Strings, compulsory one argument should be str and other argument
    should be int**

**len() in-built function:**

**We can use len() function to find the number of characters present in the string.**

**Eg:
 s='durga'
 print(len(s)) #5**

**5**

```

```

**Q. Write a program to access each character of string in forward and backward direction**

**by using while loop?**

```
 s="Learning Python is very easy !!!"
n=len(s)
i= 0
print("Forward direction")
while i<n:
print(s[i],end=' ')
i += 1
print("Backward direction")
i=- 1
while i>=-n:
1 print(s[i],end=' ')
1i=i- 1
```

**Alternative ways:**

```
 s="Learning Python is very easy !!!"
print("Forward direction")
for i in s:
print(i,end=' ')
5 )
print("Forward direction")
for i in s[::]:
print(i,end=' ')
9 )
print("Backward direction")
1 for i in s[::- 1 ]:
1print(i,end=' ')
```

**Checking Membership:**

**We can check whether the character or string is the member of another string or not by using in
 and not in operators**

**s='durga'
 print('d' in s) #True
 print('z' in s) #False**

**Program:**

```
 s=input("Enter main string:")
subs=input("Enter sub string:")
if subs in s:
print(subs,"is found in main string")
else:
```

**6**

```

print(subs,"is not found in main string")
```

**Output:
 D:\python_classes>py test.py
 Enter main string:durgasoftwaresolutions
 Enter sub string:durga
 durga is found in main string**

**D:\python_classes>py test.py
 Enter main string:durgasoftwaresolutions
 Enter sub string:python
 python is not found in main string**

**Comparison of Strings:**

**We can use comparison operators (<,<=,>,>=) and equality operators(==,!=) for strings.**

**Comparison will be performed based on alphabetical order.**

**Eg:**

```
 s1=input("Enter first string:")
s2=input("Enter Second string:")
if s1==s2:
print("Both strings are equal")
elif s1<s2:
print("First String is less than Second String")
else:
print("First String is greater than Second String")
```

**Output:
 D:\python_classes>py test.py
 Enter first string:durga
 Enter Second string:durga
 Both strings are equal**

**D:\python_classes>py test.py
 Enter first string:durga
 Enter Second string:ravi
 First String is less than Second String**

**D:\python_classes>py test.py
 Enter first string:durga
 Enter Second string:anil
 First String is greater than Second String**

**7**

```

```

**Removing spaces from the string:**

**We can use the following 3 methods**

**1. rstrip()===>To remove spaces at right hand side

1. lstrip()===>To remove spaces at left hand side
2. strip() ==>To remove spaces both sides**

**Eg:**

```
 city=input("Enter your city Name:")
scity=city.strip()
if scity=='Hyderabad':
print("Hello Hyderbadi..Adab")
elif scity=='Chennai':
print("Hello Madrasi...Vanakkam")
elif scity=="Bangalore":
print("Hello Kannadiga...Shubhodaya")
else:
print("your entered city is invalid")
```

**Finding Substrings:**

**We can use the following 4 methods**

**For forward direction:**

**find()
 index()**

**For backward direction:**

**rfind()
 rindex()**

**1. find():**

**s.find(substring)**

**Returns index of first occurrence of the given substring. If it is not available then we will get - 1**

**Eg:**

```
 s="Learning Python is very easy"
```

**8**

```

print(s.find("Python")) #9
print(s.find("Java")) # - 1
print(s.find("r"))#3
print(s.rfind("r"))#21
```

**Note: By default find() method can search total string. We can also specify the boundaries to
 search.**

**s.find(substring,bEgin,end)**

**It will always search from bEgin index to end-1 index**

**Eg:**

```
 s="durgaravipavanshiva"
print(s.find('a'))#4
print(s.find('a', 7 , 15 ))#10
print(s.find('z', 7 , 15 ))#- 1
```

**index() method:**

**index() method is exactly same as find() method except that if the specified substring is not
 available then we will get ValueError.**

**Eg:**

```
 s=input("Enter main string:")
subs=input("Enter sub string:")
try:
n=s.index(subs)
except ValueError:
print("substring not found")
else:
print("substring found")
```

**Output:
 D:\python_classes>py test.py
 Enter main string:learning python is very easy
 Enter sub string:python
 substring found**

**D:\python_classes>py test.py
 Enter main string:learning python is very easy
 Enter sub string:java
 substring not found**

**9**

```

```

**Q. Program to display all positions of substring in a given main string**

```
 s=input("Enter main string:")
subs=input("Enter sub string:")
flag=False
pos=- 1
n=len(s)
while True:
pos=s.find(subs,pos+ 1 ,n)
if pos==- 1 :
break
print("Found at position",pos)
1 flag=True
1if flag==False:
1print("Not Found")
```

**Output:**

**D:\python_classes>py test.py
 Enter main string:abbababababacdefg
 Enter sub string:a
 Found at position 0
 Found at position 3
 Found at position 5
 Found at position 7
 Found at position 9
 Found at position 11**

**D:\python_classes>py test.py
 Enter main string:abbababababacdefg
 Enter sub string:bb
 Found at position 1**

**Counting substring in the given String:**

**We can find the number of occurrences of substring present in the given string by using count()
 method.**

**1. s.count(substring) ==> It will search through out the string

1. s.count(substring, bEgin, end) ===> It will search from bEgin index to end-1 index**

**Eg:**

```
 s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a', 3 , 7 ))
```

**10**

```

```

**Output:
 6
 4
 2**

**Replacing a string with another string:**

**s.replace(oldstring,newstring)**

**inside s, every occurrence of oldstring will be replaced with newstring.**

**Eg1:
 s="Learning Python is very difficult"
 s1=s.replace("difficult","easy")
 print(s1)**

**Output:
 Learning Python is very easy**

**Eg2: All occurrences will be replaced**

**s="ababababababab"
 s1=s.replace("a","b")
 print(s1)**

**Output: bbbbbbbbbbbbbb**

**Q. String objects are immutable then how we can change the content by**

**using replace() method.**

**Once we creates string object, we cannot change the content.This non changeable behaviour is
 nothing but immutability. If we are trying to change the content by using any method, then with
 those changes a new object will be created and changes won't be happend in existing object.**

**Hence with replace() method also a new object got created but existing object won't be changed.**

**Eg:
 s="abab"
 s1=s.replace("a","b")
 print(s,"is available at :",id(s))
 print(s1,"is available at :",id(s1))**

**Output:
 abab is available at : 4568672
 bbbb is available at : 4568704**

**11**

```

```

**In the above example, original object is available and we can see new object which was created
 because of replace() method.**

**Splitting of Strings:**

**We can split the given string according to specified seperator by using split() method.**

**l=s.split(seperator)**

**The default seperator is space. The return type of split() method is List**

**Eg1:**

```
 s="durga software solutions"
l=s.split()
for x in l:
print(x)
```

**Output:
 durga
 software
 solutions**

**Eg2:**

```
 s="22- 02 - 2018"
l=s.split('-')
for x in l:
print(x)
```

**Output:
 22
 02
 2018**

**Joining of Strings:**

**We can join a group of strings(list or tuple) wrt the given seperator.**

**s=seperator.join(group of strings)**

**Eg:
 t=('sunny','bunny','chinny')
 s='-'.join(t)
 print(s)**

**Output: sunny-bunny-chinny**

**12**

```

```

**Eg2:
 l=['hyderabad','singapore','london','dubai']
 s=':'.join(l)
 print(s)**

**hyderabad:singapore:london:dubai**

**Changing case of a String:**

**We can change case of a string by using the following 4 methods.**

**1. upper()===>To convert all characters to upper case

1. lower() ===>To convert all characters to lower case
2. swapcase()===>converts all lower case characters to upper case and all upper case characters to
    lower case
3. title() ===>To convert all character to title case. i.e first character in every word should be upper
    case and all remaining characters should be in lower case.
4. capitalize() ==>Only first character will be converted to upper case and all remaining characters
    can be converted to lower case**

**Eg:
 s='learning Python is very Easy'
 print(s.upper())
 print(s.lower())
 print(s.swapcase())
 print(s.title())
 print(s.capitalize())**

**Output:
 LEARNING PYTHON IS VERY EASY
 learning python is very easy
 LEARNING pYTHON IS VERY eASY
 Learning Python Is Very Easy
 Learning python is very easy**

**Checking starting and ending part of the string:**

**Python contains the following methods for this purpose**

**1. s.startswith(substring)

1. s.endswith(substring)**

**Eg:
 s='learning Python is very easy'
 print(s.startswith('learning'))
 print(s.endswith('learning'))
 print(s.endswith('easy'))**

**13**

```

```

**Output:
 True
 False
 True**

**To check type of characters present in a string:**

**Python contains the following methods for this purpose.**

** isalnum(): Returns True if all characters are alphanumeric( a to z , A to Z ,0 to9 )
 isalpha(): Returns True if all characters are only alphabet symbols(a to z,A to Z)**

**isdigit(): Returns True if all characters are digits only( 0 to 9)**

**islower(): Returns True if all characters are lower case alphabet symbols
 isupper(): Returns True if all characters are upper case aplhabet symbols**

**istitle(): Returns True if string is in title case**

**isspace(): Returns True if string contains only spaces**

**Eg:
 print('Durga786'.isalnum()) #True
 print('durga786'.isalpha()) #False
 print('durga'.isalpha()) #True
 print('durga'.isdigit()) #False
 print('786786'.isdigit()) #True
 print('abc'.islower()) #True
 print('Abc'.islower()) #False
 print('abc123'.islower()) #True
 print('ABC'.isupper()) #True
 print('Learning python is Easy'.istitle()) #False
 print('Learning Python Is Easy'.istitle()) #True
 print(' '.isspace()) #True**

**Demo Program:**

```
 s=input("Enter any character:")
if s.isalnum():
print("Alpha Numeric Character")
if s.isalpha():
print("Alphabet character")
if s.islower():
print("Lower case alphabet character")
else:
print("Upper case alphabet character")
else:
1 print("it is a digit")
1elif s.isspace():
1print("It is space character")
1else:
```

**14**

```

1print("Non Space Special Character")
```

**D:\python_classes>py test.py
 Enter any character:7
 Alpha Numeric Character
 it is a digit**

**D:\python_classes>py test.py
 Enter any character:a
 Alpha Numeric Character
 Alphabet character
 Lower case alphabet character**

**D:\python_classes>py test.py
 Enter any character:$
 Non Space Special Character**

**D:\python_classes>py test.py
 Enter any character:A
 Alpha Numeric Character
 Alphabet character
 Upper case alphabet character**

**Formatting the Strings:**

**We can format the strings with variable values by using replacement operator {} and format()
 method.**

**Eg:
 name='durga'
 salary=10000
 age=48
 print("{} 's salary is {} and his age is {}".format(name,salary,age))
 print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
 print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))**

**Output:
 durga 's salary is 10000 and his age is 48
 durga 's salary is 10000 and his age is 48
 durga 's salary is 10000 and his age is 48**

**15**

```

```

**Important Programs rEgarding String Concept**

**Q1. Write a program to reverse the given String**

**input: durga
 output:agrud**

**1 st Way:**

**s=input("Enter Some String:")
 print(s[::-1])**

**2 nd Way:**

**s=input("Enter Some String:")
 print(''.join(reversed(s)))**

**3 rd Way:**

**s=input("Enter Some String:")
 i=len(s)- 1
 target=''
 while i>=0:
 target=target+s[i]
 i=i- 1
 print(target)**

**Q2. Program to reverse order of words.**

```
 input: Learning Python is very Easy
output: Easy Very is Python Learning
3 )
s=input("Enter Some String:")
l=s.split()
l1=[]
i=len(l)- 1
while i>= 0 :
l1.append(l[i])
i=i- 1
1 output=' '.join(l1)
1print(output)
```

**Output:
 Enter Some String:Learning Python is very easy!!
 easy!!! very is Python Learning**

**16**

```

```

**Q3. Program to reverse internal content of each word.**

**input: Durga Software Solutions
 output:agruD erawtfoS snoituloS**

```
 s=input("Enter Some String:")
l=s.split()
l1=[]
i= 0
while i<len(l):
l1.append(l[i][::- 1 ])
i=i+ 1
output=' '.join(l1)
print(output)
```

**Q4. Write a program to print characters at odd position and even position for the given**

**String?**

**1 st Way:**

**s=input("Enter Some String:")
 print("Characters at Even Position:",s[0::2])
 print("Characters at Odd Position:",s[1::2])**

**2 nd Way:**

```
 s=input("Enter Some String:")
i= 0
print("Characters at Even Position:")
while i< len(s):
print(s[i],end=',')
i=i+ 2
print()
print("Characters at Odd Position:")
i= 1
while i< len(s):
1 print(s[i],end=',')
1i=i+ 2
```

**Q5. Program to merge characters of 2 strings into a single string by taking characters**

**alternatively.**

**s1="ravi"
 s2="reja"**

**output: rtaevjia**

**17**

```

 s1=input("Enter First String:")
s2=input("Enter Second String:")
output=''
i,j= 0 , 0
while i<len(s1) or j<len(s2):
if i<len(s1):
output=output+s1[i]
i+= 1
if j<len(s2):
output=output+s2[j]
1 j+= 1
1print(output)
```

**Output:
 Enter First String:durga
 Enter Second String:ravisoft
 druarvgiasoft**

**Q6. Write a program to sort the characters of the string and first alphabet symbols**

**followed by numeric values**

**input: B4A1D3**

**Output: ABD134**

```
 s=input("Enter Some String:")
s1=s2=output=''
for x in s:
if x.isalpha():
s1=s1+x
else:
s2=s2+x
for x in sorted(s1):
output=output+x
for x in sorted(s2):
1 output=output+x
1print(output)
```

**Q7. Write a program for the following requirement**

**input: a4b3c2
 output: aaaabbbcc**

```
 s=input("Enter Some String:")
output=''
for x in s:
if x.isalpha():
output=output+x
previous=x
```

**18**

```

else:
output=output+previous*(int(x)- 
print(output)
```

**Note: chr(unicode)===>The corresponding character
 ord(character)===>The corresponding unicode value**

**Q8. Write a program to perform the following activity**

**input: a4k3b2
 output:aeknbd**

```
 s=input("Enter Some String:")
output=''
for x in s:
if x.isalpha():
output=output+x
previous=x
else:
output=output+chr(ord(previous)+int(x))
print(output)
```

**Q9. Write a program to remove duplicate characters from the given input string?**

**input: ABCDABBCDABBBCCCDDEEEF**

**output: ABCDEF**

```
 s=input("Enter Some String:")
l=[]
for x in s:
if x not in l:
l.append(x)
output=''.join(l)
print(output)
```

**Q10. Write a program to find the number of occurrences of each character present in the**

**given String?**

**input: ABCABCABBCDE**

**output: A-3,B-4,C-3,D-1,E- 1**

```
 s=input("Enter the Some String:")
d={}
for x in s:
if x in d.keys():
d[x]=d[x]+ 1
else:
d[x]= 1
```

**19**

```

for k,v in d.items():
print("{} = {} Times".format(k,v))
```

**Formatting the Strings:**

**We can format the strings with variable values by using replacement operator {} and format()
 method.**

**The main objective of format() method to format string into meaningful output form.**

**Case- 1: Basic Formatting for default, positional and keyword arguments**

**name='durga'
 salary=10000
 age=48
 print("{} 's salary is {} and his age is {}".format(name,salary,age))
 print("{0} 's salary is {1} and his age is {2}".format(name,salary,age))
 print("{x} 's salary is {y} and his age is {z}".format(z=age,y=salary,x=name))**

**Output:
 durga 's salary is 10000 and his age is 48
 durga 's salary is 10000 and his age is 48
 durga 's salary is 10000 and his age is 48**

**Case-2: Formatting Numbers**

**d--->Decimal IntEger
 f----->Fixed point number(float).The default precision is 6
 b-->Binary format
 o--->Octal Format
 x-->Hexa Decimal Format(Lower case)
 X-->Hexa Decimal Format(Upper case)**

**Eg-1:
 print("The intEger number is: {}".format(123))
 print("The intEger number is: {:d}".format(123))
 print("The intEger number is: {:5d}".format(123))
 print("The intEger number is: {:05d}".format(123))**

**Output:
 The intEger number is: 123
 The intEger number is: 123
 The intEger number is: 123
 The intEger number is: 00123**

**Eg-2:
 print("The float number is: {}".format(123.4567))
 print("The float number is: {:f}".format(123.4567))**

**20**

```

```

**print("The float number is: {:8.3f}".format(123.4567))
 print("The float number is: {:08.3f}".format(123.4567))
 print("The float number is: {:08.3f}".format(123.45))
 print("The float number is: {:08.3f}".format(786786123.45))**

**Output:
 The float number is: 123.4567
 The float number is: 123.456700
 The float number is: 123.457
 The float number is: 0123.457
 The float number is: 0123.450
 The float number is: 786786123.450**

**Note:
 {:08.3f}**

**Total positions should be minimum 8.
 After decimal point exactly 3 digits are allowed.If it is less then 0s will be placed in the last
 positions
 If total number is < 8 positions then 0 will be placed in MSBs
 If total number is >8 positions then all intEgral digits will be considered.
 The extra digits we can take only 0**

**Note: For numbers default alignment is Right Alignment(>)**

**Eg-3: Print Decimal value in binary, octal and hexadecimal form**

**print("Binary Form:{0:b}".format(153))
 print("Octal Form:{0:o}".format(153))
 print("Hexa decimal Form:{0:x}".format(154))
 print("Hexa decimal Form:{0:X}".format(154))**

**Output:
 Binary Form:10011001
 Octal Form:231
 Hexa decimal Form:9a
 Hexa decimal Form:9A**

**Note: We can represent only int values in binary, octal and hexadecimal and it is not possible for
 float values.**

**Note:
 {:5d} It takes an intEger argument and assigns a minimum width of 5.
 {:8.3f} It takes a float argument and assigns a minimum width of 8 including "." and after decimal
 point excatly 3 digits are allowed with round operation if required
 {:05d} The blank places can be filled with 0. In this place only 0 allowed.**

**21**

```

```

**Case-3: Number formatting for signed numbers**

**While displaying positive numbers,if we want to include + then we have to write**

**{:+d} and {:+f}**

**Using plus for -ve numbers there is no use and for -ve numbers - sign will come automatically.**

**print("int value with sign:{:+d}".format(123))
 print("int value with sign:{:+d}".format(-123))
 print("float value with sign:{:+f}".format(123.456))
 print("float value with sign:{:+f}".format(-123.456))**

**Output:
 int value with sign:+123
 int value with sign:- 123
 float value with sign:+123.456000
 float value with sign:-123.456000**

**Case-4: Number formatting with alignment**

**<,>,^ and = are used for alignment
 <==>Left Alignment to the remaining space
 ^===>Center alignment to the remaining space

> ===> Right alignment to the remaining space
>  = ===>Forces the signed(+) (-) to the left most position**

**Note: Default Alignment for numbers is Right Alignment.**

**Ex:**

```
 print("{:5d}".format( 12 ))
print("{:<5d}".format( 12 ))
print("{:<05d}".format( 12 ))
print("{:>5d}".format( 12 ))
print("{:>05d}".format( 12 ))
print("{:^5d}".format( 12 ))
print("{:=5d}".format(- 12 ))
print("{:^10.3f}".format(12.23456))
print("{:=8.3f}".format(-12.23456))
```

**Output:
 12
 12
 12000
 12
 00012
 12**

**- 12**

**22**

```

```

**12.235**

**- 12.235**

**Case-5: String formatting with format()**

**Similar to numbers, we can format String values also with format() method.**

**s.format(string)**

**Eg:**

```
 print("{:5d}".format( 12 ))
print("{:5}".format("rat"))
print("{:>5}".format("rat"))
print("{:<5}".format("rat"))
print("{:^5}".format("rat"))
print("{:*^5}".format("rat")) #Instead of * we can use any character(like +,$,a etc)
```

**Output:
 12
 rat
 rat
 rat
 rat
 \*rat\***

**Note: For numbers default alignment is right where as for strings default alignment is left**

**Case-6: Truncating Strings with format() method**

```
 print("{:.3}".format("durgasoftware"))
print("{:5.3}".format("durgasoftware"))
print("{:>5.3}".format("durgasoftware"))
print("{:^5.3}".format("durgasoftware"))
print("{:*^5.3}".format("durgasoftware"))
```

**Output:
 dur
 dur
 dur
 dur
 \*dur\***

**Case-7: Formatting dictionary members using format()**

```
 person={'age': 48 ,'name':'durga'}
print("{p[name]}'s age is: {p[age]}".format(p=person))
```

**23**

```

```

**Output:
 durga's age is: 48
 Note: p is alias name of dictionary
 person dictionary we are passing as keyword argument**

**More convinient way is to use **person**

**Eg:**

```
 person={'age': 48 ,'name':'durga'}
print("{name}'s age is: {age}".format(**person))
```

**Output:
 durga's age is: 48**

**Case-8: Formatting class members using format()**

**Eg:**

```
 class Person:
age= 48
name="durga"
print("{p.name}'s age is :{p.age}".format(p=Person()))
```

**Output:
 durga's age is :48**

**Eg:**

```
 class Person:
def __init__(self,name,age):
self.name=name
self.age=age
print("{p.name}'s age is :{p.age}".format(p=Person('durga', 48 )))
print("{p.name}'s age is :{p.age}".format(p=Person('Ravi', 50 )))
```

**Note: Here Person object is passed as keyword argument. We can access by using its reference
 variable in the template string**

**Case-9: Dynamic Formatting using format()**

```
 string="{:{fill}{align}{width}}"
print(string.format('cat',fill='*',align='^',width= 5 ))
print(string.format('cat',fill='*',align='^',width= 6 ))
print(string.format('cat',fill='*',align='<',width= 6 ))
print(string.format('cat',fill='*',align='>',width= 6 ))
```

**24**

```

```

**Output:
 \*cat\*
 \*cat**
 cat***
 ***cat**

**Case-10: Dynamic Float format template**

```
 num="{:{align}{width}.{precision}f}"
print(num.format(123.236,align='<',width= 8 ,precision= 2 ))
print(num.format(123.236,align='>',width= 8 ,precision= 2 ))
```

**Output:
 123.24
 123.24**

**Case-11: Formatting Date values**

```
 import datetime
#datetime formatting
date=datetime.datetime.now()
print("It's now:{:%d/%m/%Y %H:%M:%S}".format(date))
```

**Output: It's now:09/03/2018 12:36:26**

**Case-12: Formatting complex numbers**

```
 complexNumber= 1 +2j
print("Real Part:{0.real} and Imaginary Part:{0.imag}".format(complexNumber))
```

**Output: Real Part:1.0 and Imaginary Part:2.0**

**1**

```

```

**List Data Structure**

**If we want to represent a group of individual objects as a single entity where insertion**

**order preserved and duplicates are allowed, then we should go for List.**

**insertion order preserved.
 duplicate objects are allowed**

**heterogeneous objects are allowed.**

**List is dynamic because based on our requirement we can increase the size and decrease
 the size.**

**In List the elements will be placed within square brackets and with comma seperator.**

**We can differentiate duplicate elements by using index and we can preserve insertion**

**order by using index. Hence index will play very important role.**

**Python supports both positive and negative indexes. +ve index means from left to right
 where as negative index means right to left**

**[10,"A","B",20, 30, 10]**

**List objects are mutable.i.e we can change the content.**

**Creation of List Objects:**

**1. We can create empty list object as follows...**

```
 list=[]
print(list)
print(type(list))
4 )
[]
<class 'list'>
```

**2. If we know elements already then we can create list as follows**

**list=[10,20,30,40]**

**10 A B 20 30 10**

**- 6 - 5 - 4 - 3 - 2 - 1**

```
0 1 2 3 4 5
```

**2**

```

```

**3. With dynamic input:**

```
 list=eval(input("Enter List:"))
print(list)
print(type(list))
4 )
D:\Python_classes>py test.py
Enter List:[ 10 , 20 , 30 , 40 ]
[ 10 , 20 , 30 , 40 ]
<class 'list'>
```

**4. With list() function:**

```
 l=list(range( 0 , 10 , 2 ))
print(l)
print(type(l))
4 )
D:\Python_classes>py test.py
[ 0 , 2 , 4 , 6 , 8 ]
<class 'list'>
```

**Eg:**

```
 s="durga"
l=list(s)
print(l)
4 )
D:\Python_classes>py test.py
['d', 'u', 'r', 'g', 'a']
```

**5. with split() function:**

```
 s="Learning Python is very very easy !!!"
l=s.split()
print(l)
print(type(l))
5 )
D:\Python_classes>py test.py
['Learning', 'Python', 'is', 'very', 'very', 'easy', '!!!']
<class 'list'>
```

**Note:**

**Sometimes we can take list inside another list,such type of lists are called nested lists.**

**[10,20,[30,40]]**

**3**

```

```

**Accessing elements of List:**

**We can access elements of the list either by using index or by using slice operator(:)**

**1. By using index:**

**List follows zero based index. ie index of first element is zero.**

**List supports both +ve and -ve indexes.**

**+ve index meant for Left to Right**

**- ve index meant for Right to Left**

**list=[10,20,30,40]**

**print(list[0]) ==>10**

**print(list[-1]) ==>40**

**print(list[10]) ==>IndexError: list index out of range**

**2. By using slice operator:**

**Syntax:**

**list2= list1[start:stop:step]**

**start ==>it indicates the index where slice has to start**

**default value is 0**

**stop ===>It indicates the index where slice has to end**

**default value is max allowed index of list ie length of the list**

**step ==>increment value**

**default value is 1**

**Eg:**

```
 n=[ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
print(n[ 2 : 7 : 2 ])
print(n[ 4 :: 2 ])
print(n[ 3 : 7 ])
print(n[ 8 : 2 :- 2 ])
print(n[ 4 : 100 ])
```

**10 20 30 40**

**- 4 - 3 - 2 - 1**

```
0 1 2 3
list
```

**4**

```

7 )
Output
D:\Python_classes>py test.py
[ 3 , 5 , 7 ]
1 [ 5 , 7 , 9 ]
1[ 4 , 5 , 6 , 7 ]
1[ 9 , 7 , 5 ]
1[ 5 , 6 , 7 , 8 , 9 , 10 ]
```

**List vs mutability:**

**Once we creates a List object,we can modify its content. Hence List objects are mutable.**

**Eg:**

```
 n=[ 10 , 20 , 30 , 40 ]
print(n)
n[ 1 ]= 777
print(n)
5 )
D:\Python_classes>py test.py
[ 10 , 20 , 30 , 40 ]
[ 10 , 777 , 30 , 40 ]
```

**Traversing the elements of List:**

**The sequential access of each element in the list is called traversal.**

**1. By using while loop:**

```
 n=[ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
i= 0
while i<len(n):
print(n[i])
i=i+ 1
6 )
D:\Python_classes>py test.py
0
1
2
1 3
14
15
16
17
18
19
```

**5**

```

110
```

**2. By using for loop:**

```
 n=[ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
for n1 in n:
print(n1)
4 )
D:\Python_classes>py test.py
0
1
2
3
4
1 5
16
17
18
19
110
```

**3. To display only even numbers:**

```
 n=[ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
for n1 in n:
if n1% 2 == 0 :
print(n1)
5 )
D:\Python_classes>py test.py
0
2
4
6
1 8
110
```

**4. To display elements by index wise:**

```
 l=["A","B","C"]
x=len(l)
for i in range(x):
print(l[i],"is available at positive index: ",i,"and at negative index: ",i-x)
5 )
Output
D:\Python_classes>py test.py
A is available at positive index: 0 and at negative index: - 3
B is available at positive index: 1 and at negative index: - 2
C is available at positive index: 2 and at negative index: - 1
```

**6**

```

```

**Important functions of List:**

**I. To get information about list:**

**1. len():**

**returns the number of elements present in the list**

**Eg: n=[10,20,30,40]
 print(len(n))==>4**

**2. count():**

**It returns the number of occurrences of specified item in the list**

```
 n=[ 1 , 2 , 2 , 2 , 2 , 3 , 3 ]
print(n.count( )
print(n.count( 2 ))
print(n.count( 3 ))
print(n.count( 4 ))
6 )
Output
D:\Python_classes>py test.py
1
4
1 2
10
```

**3. index() function:**

**returns the index of first occurrence of the specified item.**

**Eg:**

```
 n=[ 1 , 2 , 2 , 2 , 2 , 3 , 3 ]
print(n.index( ) ==> 0
print(n.index( 2 )) ==> 1
print(n.index( 3 )) ==> 5
print(n.index( 4 )) ==>ValueError: 4 is not in list
```

**Note: If the specified element not present in the list then we will get ValueError.Hence**

**before index() method we have to check whether item present in the list or not by using in
 operator.**

**print( 4 in n)==>False**

**7**

```

```

**II. Manipulating elements of List:**

**1. append() function:**

**We can use append() function to add item at the end of the list.**

**Eg:**

```
 list=[]
list.append("A")
list.append("B")
list.append("C")
print(list)
6 )
D:\Python_classes>py test.py
['A', 'B', 'C']
```

**Eg: To add all elements to list upto 100 which are divisible by 10**

```
 list=[]
for i in range( 10:
if i% 10 == 0 :
list.append(i)
print(list)
6 )
7 )
D:\Python_classes>py test.py
[ 0 , 10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90 , 100 ]
```

**2. insert() function:**

**To insert item at specified index position**

```
 n=[ 1 , 2 , 3 , 4 , 5 ]
n.insert( 1 , 888 )
print(n)
4 )
D:\Python_classes>py test.py
[ 1 , 888 , 2 , 3 , 4 , 5 ]
```

**Eg:**

```
 n=[ 1 , 2 , 3 , 4 , 5 ]
n.insert( 10 , 777 )
n.insert(- 10 , 999 )
print(n)
5 )
```

**8**

```

D:\Python_classes>py test.py
[ 999 , 1 , 2 , 3 , 4 , 5 , 777 ]
```

**Note: If the specified index is greater than max index then element will be inserted at last**

**position. If the specified index is smaller than min index then element will be inserted at
 first position.**

**Differences between append() and insert()**

**3. extend() function:**

**To add all items of one list to another list**

**l1.extend(l2)
 all items present in l2 will be added to l1**

**Eg:**

```
 order1=["Chicken","Mutton","Fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)
5 )
D:\Python_classes>py test.py
['Chicken', 'Mutton', 'Fish', 'RC', 'KF', 'FO']
```

**Eg:**

```
 order=["Chicken","Mutton","Fish"]
order.extend("Mushroom")
print(order)
4 )
D:\Python_classes>py test.py
['Chicken', 'Mutton', 'Fish', 'M', 'u', 's', 'h', 'r', 'o', 'o', 'm']
```

**4. remove() function:**

**We can use this function to remove specified item from the list.If the item present**

**multiple times then only first occurrence will be removed.**

```
append() insert()
```

**In List when we add any element it will**

**come in last i.e. it will be last element.**

```
In List we can insert any element in
particular index number
```

**9**

```

 n=[ 10 , 20 , 10 , 30 ]
n.remove( 10 )
print(n)
4 )
D:\Python_classes>py test.py
[ 20 , 10 , 30 ]
```

**If the specified item not present in list then we will get ValueError**

```
 n=[ 10 , 20 , 10 , 30 ]
n.remove( 40 )
print(n)
4 )
ValueError: list.remove(x): x not in list
```

**Note: Hence before using remove() method first we have to check specified element**

**present in the list or not by using in operator.**

**5. pop() function:**

**It removes and returns the last element of the list.**

**This is only function which manipulates list and returns some element.**

**Eg:**

```
 n=[ 10 , 20 , 30 , 40 ]
print(n.pop())
print(n.pop())
print(n)
5 )
D:\Python_classes>py test.py
40
30
[ 10 , 20 ]
```

**If the list is empty then pop() function raises IndexError**

**Eg:**

```
 n=[]
print(n.pop()) ==> IndexError: pop from empty list
```

**10**

```

```

**Note:**

**1. pop() is the only function which manipulates the list and returns some value

1. In general we can use append() and pop() functions to implement stack datastructure**

**by using list,which follows LIFO(Last In First Out) order.**

**In general we can use pop() function to remove last element of the list. But we can use to**

**remove elements based on index.**

**n.pop(index)===>To remove and return element present at specified index.**

**n.pop()==>To remove and return last element of the list**

```
 n=[ 10 , 20 , 30 , 40 , 50 , 60 ]
print(n.pop()) #60
print(n.pop( ) #20
print(n.pop( 10 )) ==>IndexError: pop index out of range
```

**Differences between remove() and pop()**

**Note:**

**List objects are dynamic. i.e based on our requirement we can increase and decrease the
 size.**

**append(),insert() ,extend() ===>for increasing the size/growable nature
 remove(), pop() ======>for decreasing the size /shrinking nature**

```
remove() pop()
```

**1) We can use to remove special element
 from the List.**

```
1) We can use to remove last element
from the List.
```

**2) It can’t return any value. 2) It returned removed element.**

**3) If special element not available then we**

**get VALUE ERROR.**

```
3) If List is empty then we get Error.
```

**11**

```

```

**III. Ordering elements of List:**

**1. reverse():**

**We can use to reverse() order of elements of list.**

```
 n=[ 10 , 20 , 30 , 40 ]
n.reverse()
print(n)
4 )
D:\Python_classes>py test.py
[ 40 , 30 , 20 , 10 ]
```

**2. sort() function:**

**In list by default insertion order is preserved. If want to sort the elements of list according**

**to default natural sorting order then we should go for sort() method.**

**For numbers ==>default natural sorting order is Ascending Order**

**For Strings ==> default natural sorting order is Alphabetical Order**

```
 n=[ 20 , 5 , 15 , 10 , 0 ]
n.sort()
print(n) #[0,5,10,15,20]
4 )
s=["Dog","Banana","Cat","Apple"]
s.sort()
print(s) #['Apple','Banana','Cat','Dog']
```

**Note: To use sort() function, compulsory list should contain only homogeneous elements.**

**otherwise we will get TypeError**

**Eg:**

```
 n=[ 20 , 10 ,"A","B"]
n.sort()
print(n)
4 )
TypeError: '<' not supported between instances of 'str' and 'int'
```

**Note: In Python 2 if List contains both numbers and Strings then sort() function first sort**

**numbers followed by strings**

```
 n=[ 20 ,"B", 10 ,"A"]
n.sort()
```

**12**

```

print(n)# [10,20,'A','B']
```

**But in Python 3 it is invalid.**

**To sort in reverse of default natural sorting order:**

**We can sort according to reverse of default natural sorting order by using reverse=True
 argument.**

**Eg:**

```
1. n=[ 40 , 10 , 30 , 20 ]
2. n.sort()
3. print(n) ==>[ 10 , 20 , 30 , 40 ]
4. n.sort(reverse=True)
5. print(n) ===>[ 40 , 30 , 20 , 10 ]
6. n.sort(reverse=False)
7. print(n) ==>[ 10 , 20 , 30 , 40 ]
```

**Aliasing and Cloning of List objects:**

**The process of giving another reference variable to the existing list is called aliasing.**

**Eg:**

```
 x=[ 10 , 20 , 30 , 40 ]
y=x
print(id(x))
print(id(y))
```

**The problem in this approach is by using one reference variable if we are changing**

**content,then those changes will be reflected to the other reference variable.**

```
 x=[ 10 , 20 , 30 , 40 ]
y=x
y[ 1 ]= 777
print(x) ==>[ 10 , 777 , 30 , 40 ]
```

**To overcome this problem we should go for cloning.
 The process of creating exactly duplicate independent object is called cloning.**

**We can implement cloning by using slice operator or by using copy() function**

```
10 20 30 40
```

**x** (^)
 **y
 10 20
 777
 30 40
 x
 y**

**13**

```

```

**1. By using slice operator:**

```
 x=[ 10 , 20 , 30 , 40 ]
y=x[:]
y[ 1 ]= 777
print(x) ==>[ 10 , 20 , 30 , 40 ]
print(y) ==>[ 10 , 777 , 30 , 40 ]
```

**2. By using copy() function:**

```
 x=[ 10 , 20 , 30 , 40 ]
y=x.copy()
y[ 1 ]= 777
print(x) ==>[ 10 , 20 , 30 , 40 ]
print(y) ==>[ 10 , 777 , 30 , 40 ]
```

**Q. Difference between = operator and copy() function**

**= operator meant for aliasing
 copy() function meant for cloning**

```
10 20 30 40
```

**x** (^)
 **10 20
 777
 30 40
 y** (^)
 **10 20 30 40
 x** (^)
 **10 20
 777
 30 40
 y** (^)

**14**

```

```

**Using Mathematical operators for List Objects:**

**We can use + and \* operators for List objects.**

**1. Concatenation operator(+):**

**We can use + to concatenate 2 lists into a single list**

```
 a=[ 10 , 20 , 30 ]
b=[ 40 , 50 , 60 ]
c=a+b
print(c) ==>[ 10 , 20 , 30 , 40 , 50 , 60 ]
```

**Note: To use + operator compulsory both arguments should be list objects,otherwise we**

**will get TypeError.**

**Eg:**

**c=a+40 ==>TypeError: can only concatenate list (not "int") to list**

**c=a+[40] ==>valid**

**2. Repetition Operator(\*):**

**We can use repetition operator \* to repeat elements of list specified number of times**

**Eg:**

```
 x=[ 10 , 20 , 30 ]
y=x* 3
print(y)==>[ 10 , 20 , 30 , 10 , 20 , 30 , 10 , 20 , 30 ]
```

**Comparing List objects**

**We can use comparison operators for List objects.**

**Eg:**

```
1. x=["Dog","Cat","Rat"]
2. y=["Dog","Cat","Rat"]
3. z=["DOG","CAT","RAT"]
4. print(x==y) True
5. print(x==z) False
6. print(x != z) True
```

**15**

```

```

**Note:**

**Whenever we are using comparison operators(==,!=) for List objects then the following**

**should be considered**

**1. The number of elements

1. The order of elements
2. The content of elements (case sensitive)**

**Note: When ever we are using relatational operators(<,<=,>,>=) between List objects,only**

**first element comparison will be performed.**

**Eg:**

```
1. x=[ 50 , 20 , 30 ]
2. y=[ 40 , 50 , 60 , 100 , 200 ]
3. print(x>y) True
4. print(x>=y) True
5. print(x<y) False
6. print(x<=y) False
```

**Eg:**

```
1. x=["Dog","Cat","Rat"]
2. y=["Rat","Cat","Dog"]
3. print(x>y) False
4. print(x>=y) False
5. print(x<y) True
6. print(x<=y) True
```

**Membership operators:**

**We can check whether element is a member of the list or not by using memebership**

**operators.**

**in operator**

**not in operator**

**Eg:**

```
1. n=[ 10 , 20 , 30 , 40 ]
2. print ( 10 in n)
3. print ( 10 not in n)
4. print ( 50 in n)
5. print ( 50 not in n)
6.
7. Output
```

**16**

```

8. True
9. False
10. False
11. True
```

**clear() function:**

**We can use clear() function to remove all elements of List.**

**Eg:**

```
1. n=[ 10 , 20 , 30 , 40 ]
2. print(n)
3. n.clear()
4. print(n)
5.
6. Output
7. D:\Python_classes>py test.py
8. [ 10 , 20 , 30 , 40 ]
9. []
```

**Nested Lists:**

**Sometimes we can take one list inside another list. Such type of lists are called nested
 lists.**

**Eg:**

```
1. n=[ 10 , 20 ,[ 30 , 40 ]]
2. print(n)
3. print(n[ 0 ])
4. print(n[ 2 ])
5. print(n[ 2 ][ 0 ])
6. print(n[ 2 ][ 1 ])
7.
8. Output
9. D:\Python_classes>py test.py
10. [ 10 , 20 , [ 30 , 40 ]]
11. 10
12. [ 30 , 40 ]
13. 30
14. 40
```

**Note: We can access nested list elements by using index just like accessing multi**

**dimensional array elements.**

**17**

```

```

**Nested List as Matrix:**

**In Python we can represent matrix by using nested lists.**

```
 n=[[ 10 , 20 , 30 ],[ 40 , 50 , 60 ],[ 70 , 80 , 90 ]]
print(n)
print("Elements by Row wise:")
for r in n:
print(r)
print("Elements by Matrix style:")
for i in range(len(n)):
for j in range(len(n[i])):
print(n[i][j],end=' ')
print()
1
1Output
1D:\Python_classes>py test.py
1[[ 10 , 20 , 30 ], [ 40 , 50 , 60 ], [ 70 , 80 , 90 ]]
1Elements by Row wise:
1[ 10 , 20 , 30 ]
1[ 40 , 50 , 60 ]
1[ 70 , 80 , 90 ]
1Elements by Matrix style:
20 ) 10 20 30
2 40 50 60
270 80 90
```

**List Comprehensions:**

**It is very easy and compact way of creating list objects from any iterable objects(like**

**list,tuple,dictionary,range etc) based on some condition.**

**Syntax:**

**list=[expression for item in list if condition]**

**Eg:**

```
 s=[ x*x for x in range( 1 , 1]
print(s)
v=[ 2 **x for x in range( 1 , 6 )]
print(v)
m=[x for x in s if x% 2 == 0 ]
print(m)
7 )
Output
D:\Python_classes>py test.py
[ 1 , 4 , 9 , 16 , 25 , 36 , 49 , 64 , 81 , 100 ]
```

**18**

```

1 [ 2 , 4 , 8 , 16 , 32 ]
1[ 4 , 16 , 36 , 64 , 100 ]
```

**Eg:**

```
 words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[ 0 ] for w in words]
print(l)
4 )
Output['B', 'N', 'V', 'C']
```

**Eg:**

```
 num1=[ 10 , 20 , 30 , 40 ]
num2=[ 30 , 40 , 50 , 60 ]
num3=[ i for i in num1 if i not in num2]
print(num3) [ 10 , 20 ]
5 )
common elements present in num1 and num2
num4=[i for i in num1 if i in num2]
print(num4) [ 30 , 40 ]
```

**Eg:**

```
 words="the quick brown fox jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)
5 )
Output
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[['THE', 3 ], ['QUICK', 5 ], ['BROWN', 5 ], ['FOX', 3 ], ['JUMPS', 5 ], ['OVER', 4 ],
['THE', 3 ], ['LAZY', 4 ], ['DOG', 3 ]]
```

**Q. Write a program to display unique vowels present in the given word?**

```
 vowels=['a','e','i','o','u']
word=input("Enter the word to search for vowels: ")
found=[]
for letter in word:
if letter in vowels:
if letter not in found:
found.append(letter)
print(found)
print("The number of different vowels present in",word,"is",len(found))
10 )
1
1D:\Python_classes>py test.py
```

**19**

```

1Enter the word to search for vowels: durgasoftwaresolutions
1['u', 'a', 'o', 'e', 'i']
1The number of different vowels present in durgasoftwaresolutions is 5
```

**list out all functions of list and write a program to use these functions**

**1**

```

```

# Tuple Data Structure

**1. Tuple is exactly same as List except that it is immutable. i.e once we creates Tuple**

**object,we cannot perform any changes in that object.
 Hence Tuple is Read Only version of List.**

**2. If our data is fixed and never changes then we should go for Tuple.

1. Insertion Order is preserved
2. Duplicates are allowed
3. Heterogeneous objects are allowed.
4. We can preserve insertion order and we can differentiate duplicate objects by using**

**index. Hence index will play very important role in Tuple also.**

**Tuple support both +ve and -ve index. +ve index means forward direction(from left to**

**right) and -ve index means backward direction(from right to left)**

**7. We can represent Tuple elements within Parenthesis and with comma seperator.**

**Parenethesis are optional but recommended to use.**

**Eg:**

```
1. t= 10 , 20 , 30 , 40
2. print(t)
3. print(type(t))
4.
5. Output
6. ( 10 , 20 , 30 , 40 )
7. <class 'tuple'>
8.
9. t=()
10. print(type(t)) # tuple
```

**Note: We have to take special care about single valued tuple.compulsary the value**

**should ends with comma,otherwise it is not treated as tuple.**

**Eg:**

```
1. t=( 10 )
2. print(t)
3. print(type(t))
4.
5. Output
6. 10
7. <class 'int'>
```

**2**

```

```

**Eg:**

```
1. t=( 10 ,)
2. print(t)
3. print(type(t))
4.
5. Output
6. ( 10 ,)
7. <class 'tuple'>
```

**Q. Which of the following are valid tuples?**

**1. t=()

1. t=10,20,30,40
2. t=10
3. t=10,
4. t=(10)
5. t=(10,)
    7.t=(10,20,30,40)**

**Tuple creation:**

**1. t=()**

**creation of empty tuple**

**2. t=(10,)**

**t=10,**

**creation of single valued tuple ,parenthesis are optional,should ends with comma**

**3. t=10,20,30**

**t=(10,20,30)**

**creation of multi values tuples & parenthesis are optional**

**4. By using tuple() function:**

```
1. list=[ 10 , 20 , 30 ]
2. t=tuple(list)
3. print(t)
4.
5. t=tuple(range( 10 , 20 , 2 ))
6. print(t)
```

**3**

```

```

**Accessing elements of tuple:**

**We can access either by index or by slice operator**

**1. By using index:**

```
1. t=( 10 , 20 , 30 , 40 , 50 , 60 )
2. print(t[ 0 ]) #10
3. print(t[- 1 ]) #60
4. print(t[ 100 ]) IndexError: tuple index out of range
```

**2. By using slice operator:**

```
1. t=( 10 , 20 , 30 , 40 , 50 , 60 )
2. print(t[ 2 : 5 ])
3. print(t[ 2 : 100 ])
4. print(t[:: 2 ])
5.
6. Output
7. ( 30 , 40 , 50 )
8. ( 30 , 40 , 50 , 60 )
9. ( 10 , 30 , 50 )
```

**Tuple vs immutability:**

**Once we creates tuple,we cannot change its content.**

**Hence tuple objects are immutable.**

**Eg:**

**t=(10,20,30,40)
 t[1]=70 TypeError: 'tuple' object does not support item assignment**

**Mathematical operators for tuple:**

**We can apply + and \* operators for tuple**

**1. Concatenation Operator(+):**

```
1. t1=( 10 , 20 , 30 )
2. t2=( 40 , 50 , 60 )
3. t3=t1+t2
4. print(t3) # (10,20,30,40,50,60)
```

**4**

```

```

**2. Multiplication operator or repetition operator(\*)**

```
1. t1=( 10 , 20 , 30 )
2. t2=t1* 3
3. print(t2) #(10,20,30,10,20,30,10,20,30)
```

**Important functions of Tuple:**

**1. len()**

**To return number of elements present in the tuple**

**Eg:**

**t=(10,20,30,40)
 print(len(t)) #4**

**2. count()**

**To return number of occurrences of given element in the tuple**

**Eg:**

**t=(10,20,10,10,20)
 print(t.count(10)) #3**

**3. index()**

**returns index of first occurrence of the given element.
 If the specified element is not available then we will get ValueError.**

**Eg:
 t=(10,20,10,10,20)**

**print(t.index(10)) #0**

**print(t.index(30)) ValueError: tuple.index(x): x not in tuple**

**4. sorted()**

**To sort elements based on default natural sorting order**

```
1. t=( 40 , 10 , 30 , 20 )
2. t1=sorted(t)
3. print(t1)
4. print(t)
5.
6. Output
7. [ 10 , 20 , 30 , 40 ]
8. ( 40 , 10 , 30 , 20 )
```

**We can sort according to reverse of default natural sorting order as follows**

**5**

```

```

**t1=sorted(t,reverse=True)
 print(t1) [40, 30, 20, 10]**

**5. min() and max() functions:**

**These functions return min and max values according to default natural sorting order.**

**Eg:**

```
1. t=( 40 , 10 , 30 , 20 )
2. print(min(t)) #10
3. print(max(t)) #40
```

**6. cmp():**

**It compares the elements of both tuples.**

**If both tuples are equal then returns 0**

**If the first tuple is less than second tuple then it returns - 1
 If the first tuple is greater than second tuple then it returns +1**

**Eg:**

```
1. t1=( 10 , 20 , 30 )
2. t2=( 40 , 50 , 60 )
3. t3=( 10 , 20 , 30 )
4. print(cmp(t1,t2)) # - 1
5. print(cmp(t1,t3)) # 0
6. print(cmp(t2,t3)) # +1
```

**Note: cmp() function is available only in Python2 but not in Python 3**

**Tuple Packing and Unpacking:**

**We can create a tuple by packing a group of variables.**

**Eg:**

**a=10
 b=20**

**c=30**

**d=40
 t=a,b,c,d**

**print(t) #(10, 20, 30, 40)**

**Here a,b,c,d are packed into a tuple t. This is nothing but tuple packing.**

**6**

```

```

**Tuple unpacking is the reverse process of tuple packing
 We can unpack a tuple and assign its values to different variables**

**Eg:**

```
1. t=( 10 , 20 , 30 , 40 )
2. a,b,c,d=t
3. print("a=",a,"b=",b,"c=",c,"d=",d)
4.
5. Output
6. a= 10 b= 20 c= 30 d= 40
```

**Note: At the time of tuple unpacking the number of variables and number of values**

**should be same. ,otherwise we will get ValueError.**

**Eg:**

**t=(10,20,30,40)
 a,b,c=t #ValueError: too many values to unpack (expected 3)**

**Tuple Comprehension:**

**Tuple Comprehension is not supported by Python.**

**t= ( x**2 for x in range(1,6))**

**Here we are not getting tuple object and we are getting generator object.**

```
1. t= ( x** 2 for x in range( 1 , 6 ))
2. print(type(t))
3. for x in t:
4. print(x)
5.
6. Output
7. D:\Python_classes>py test.py
8. <class 'generator'>
9. 1
10. 4
11. 9
12. 16
13. 25
```

**7**

```

```

**Q. Write a program to take a tuple of numbers from the keyboard and print its sum and
 average?**

```
1. t=eval(input("Enter Tuple of Numbers:"))
2. l=len(t)
3. sum= 0
4. for x in t:
5. sum=sum+x
6. print("The Sum=",sum)
7. print("The Average=",sum/l)
8.
9. D:\Python_classes>py test.py
10. Enter Tuple of Numbers:( 10 , 20 , 30 , 40 )
11. The Sum= 100
12. The Average= 25.0
13.
14. D:\Python_classes>py test.py
15. Enter Tuple of Numbers:( 100 , 200 , 300 )
16. The Sum= 600
17. The Average= 200.0
```

**Differences between List and Tuple:**

**List and Tuple are exactly same except small difference: List objects are mutable where as
 Tuple objects are immutable.**

**In both cases insertion order is preserved, duplicate objects are allowed, heterogenous**

**objects are allowed, index and slicing are supported.**

**List Tuple**

**1) List is a Group of Comma separeated**

**Values within Square Brackets and Square
 Brackets are mandatory.**

**Eg: i = [10, 20, 30, 40]**

```
1) Tuple is a Group of Comma separeated
Values within Parenthesis and Parenthesis
are optional.
Eg: t = (10, 20, 30, 40)
t = 10, 20, 30, 40
```

**2) List Objects are Mutable i.e. once we
 creates List Object we can perform any**

**changes in that Object.**

**Eg: i[1] = 70**

```
2) Tuple Objeccts are Immutable i.e. once
we creates Tuple Object we cannot change
its content.
t[1] = 70  ValueError: tuple object does
not support item assignment.
```

**3) If the Content is not fixed and keep on**

**changing then we should go for List.**

```
3) If the content is fixed and never changes
then we should go for Tuple.
```

**4) List Objects can not used as Keys for
 Dictionries because Keys should be**

**Hashable and Immutable.**

```
4) Tuple Objects can be used as Keys for
Dictionries because Keys should be
Hashable and Immutable.
```

**8**

```

```

**1**

```

```

#### Set Data Structure

 **If we want to represent a group of unique values as a single entity then we should go**

**for set.**
  **Duplicates are not allowed.**

 **Insertion order is not preserved.But we can sort the elements.**

 **Indexing and slicing not allowed for the set.**
  **Heterogeneous elements are allowed.**

 **Set objects are mutable i.e once we creates set object we can perform any changes in
 that object based on our requirement.**

 **We can represent set elements within curly braces and with comma seperation**

 **We can apply mathematical operations like union,intersection,difference etc on set**

```
objects.
```

**Creation of Set objects:**

**Eg:**

```
1. s={ 10 , 20 , 30 , 40 }
2. print(s)
3. print(type(s))
4.
5. Output
6. { 40 , 10 , 20 , 30 }
7. <class 'set'>
```

**We can create set objects by using set() function**

**s=set(any sequence)**

**Eg 1 :**

```
1. l = [ 10 , 20 , 30 , 40 , 10 , 20 , 10 ]
2. s=set(l)
3. print(s) # {40, 10, 20, 30}
```

**Eg 2 :**

```
1. s=set(range( 5 ))
2. print(s) #{0, 1, 2, 3, 4}
```

**Note: While creating empty set we have to take special care.**

**Compulsory we should use set() function.**

**2**

```

```

**s={} ==>It is treated as dictionary but not empty set.**

**Eg:**

```
1. s={}
2. print(s)
3. print(type(s))
4.
5. Output
6. {}
7. <class 'dict'>
```

**Eg:**

```
1. s=set()
2. print(s)
3. print(type(s))
4.
5. Output
6. set()
7. <class 'set'>
```

**Important functions of set:**

**1. add(x):**

**Adds item x to the set**

**Eg:**

```
1. s={ 10 , 20 , 30 }
2. s.add( 40 );
3. print(s) #{40, 10, 20, 30}
```

**2. update(x,y,z):**

**To add multiple items to the set.
 Arguments are not individual elements and these are Iterable objects like List,range etc.**

**All elements present in the given Iterable objects will be added to the set.**

**Eg:**

```
1. s={ 10 , 20 , 30 }
2. l=[ 40 , 50 , 60 , 10 ]
3. s.update(l,range( 5 ))
4. print(s)
```

**3**

```

5.
6. Output
7. { 0 , 1 , 2 , 3 , 4 , 40 , 10 , 50 , 20 , 60 , 30 }
```

**Q. What is the difference between add() and update() functions in set?**

**We can use add() to add individual item to the Set,where as we can use update() function**

**to add multiple items to Set.
 add() function can take only one argument where as update() function can take any**

**number of arguments but all arguments should be iterable objects.**

**Q. Which of the following are valid for set s?**

**1. s.add(10)

1. s.add(10,20,30) TypeError: add() takes exactly one argument (3 given)
2. s.update(10) TypeError: 'int' object is not iterable
3. s.update(range(1,10,2),range(0,10,2))
4. copy():**

**Returns copy of the set.
 It is cloned object.**

**s={10,20,30}
 s1=s.copy()**

**print(s1)**

**4. pop():**

**It removes and returns some random element from the set.**

**Eg:**

```
1. s={ 40 , 10 , 30 , 20 }
2. print(s)
3. print(s.pop())
4. print(s)
5.
6. Output
7. { 40 , 10 , 20 , 30 }
8. 40
9. { 10 , 20 , 30 }
```

**4**

```

```

**5. remove(x):**

**It removes specified element from the set.**

**If the specified element not present in the Set then we will get KeyError**

**s={40,10,30,20}**

**s.remove(30)**

**print(s) # {40, 10, 20}
 s.remove(50) ==>KeyError: 50**

**6. discard(x):**

**It removes the specified element from the set.**

**If the specified element not present in the set then we won't get any error.**

**s={10,20,30}**

**s.discard(10)**

**print(s) ===>{20, 30}
 s.discard(50)**

**print(s) ==>{20, 30}**

**Q. What is the difference between remove() and discard() functions in Set?**

**Q. Explain differences between pop(),remove() and discard() functionsin Set?**

**7.clear():**

**To remove all elements from the Set.**

```
1. s={ 10 , 20 , 30 }
2. print(s)
3. s.clear()
4. print(s)
5.
6. Output
7. { 10 , 20 , 30 }
8. set()
```

**5**

```

```

**Mathematical operations on the Set:**

**1.union():**

**x.union(y) ==>We can use this function to return all elements present in both sets**

**x.union(y) or x|y**

**Eg:**

**x={10,20,30,40}
 y={30,40,50,60}**

**print(x.union(y)) #{10, 20, 30, 40, 50, 60}**

**print(x|y) #{10, 20, 30, 40, 50, 60}**

**2. intersection():**

**x.intersection(y) or x&y**

**Returns common elements present in both x and y**

**Eg:**

**x={10,20,30,40}
 y={30,40,50,60}**

**print(x.intersection(y)) #{40, 30}**

**print(x&y) #{40, 30}**

**3. difference():**

**x.difference(y) or x-y
 returns the elements present in x but not in y**

**Eg:**

**x={10,20,30,40}
 y={30,40,50,60}**

**print(x.difference(y)) #{10, 20}**

**print(x-y) #{10, 20}
 print(y-x) #{50, 60}**

**6**

```

```

**4.symmetric_difference():**

**x.symmetric_difference(y) or x^y**

**Returns elements present in either x or y but not in both**

**Eg:**

**x={10,20,30,40}**

**y={30,40,50,60}**

**print(x.symmetric_difference(y)) #{10, 50, 20, 60}
 print(x^y) #{10, 50, 20, 60}**

**Membership operators: (in , not in)**

**Eg:**

```
1. s=set("durga")
2. print(s)
3. print('d' in s)
4. print('z' in s)
5.
6. Output
7. {'u', 'g', 'r', 'd', 'a'}
8. True
9. False
```

**Set Comprehension:**

**Set comprehension is possible.**

**s={x\*x for x in range(5)}
 print(s) #{0, 1, 4, 9, 16}**

**s={2**x for x in range(2,10,2)}**

**print(s) #{16, 256, 64, 4}**

**set objects won't support indexing and slicing:**

**Eg:**

**s={10,20,30,40}**

**print(s[0]) ==>TypeError: 'set' object does not support indexing
 print(s[1:3]) ==>TypeError: 'set' object is not subscriptable**

**7**

```

```

**Q.Write a program to eliminate duplicates present in the list?**

**Approach-1:**

```
1. l=eval(input("Enter List of values: "))
2. s=set(l)
3. print(s)
4.
5. Output
6. D:\Python_classes>py test.py
7. Enter List of values: [ 10 , 20 , 30 , 10 , 20 , 40 ]
8. { 40 , 10 , 20 , 30 }
```

**Approach-2:**

```
1. l=eval(input("Enter List of values: "))
2. l1=[]
3. for x in l:
4. if x not in l1:
5. l1.append(x)
6. print(l1)
7.
8. Output
9. D:\Python_classes>py test.py
10. Enter List of values: [ 10 , 20 , 30 , 10 , 20 , 40 ]
11. [ 10 , 20 , 30 , 40 ]
```

**Q. Write a program to print different vowels present in the given word?**

```
1. w=input("Enter word to search for vowels: ")
2. s=set(w)
3. v={'a','e','i','o','u'}
4. d=s.intersection(v)
5. print("The different vowel present in",w,"are",d)
6.
7. Output
8. D:\Python_classes>py test.py
9. Enter word to search for vowels: durga
10. The different vowel present in durga are {'u', 'a'}
```

**1**

```

```

**Dictionary Data Structure**

**We can use List,Tuple and Set to represent a group of individual objects as a single entity.**

**If we want to represent a group of objects as key-value pairs then we should go for**

**Dictionary.**

**Eg:**

**rollno----name
 phone number--address**

**ipaddress---domain name**

**Duplicate keys are not allowed but values can be duplicated.**

**Hetrogeneous objects are allowed for both key and values.**

**insertion order is not preserved
 Dictionaries are mutable**

**Dictionaries are dynamic**

**indexing and slicing concepts are not applicable**

**Note: In C++ and Java Dictionaries are known as "Map" where as in Perl and Ruby it is**

**known as "Hash"**

**How to create Dictionary?**

**d={} or d=dict()**

**we are creating empty dictionary. We can add entries as follows**

**d[100]="durga"**

**d[200]="ravi"**

**d[300]="shiva"
 print(d) #{100: 'durga', 200: 'ravi', 300: 'shiva'}**

**If we know data in advance then we can create dictionary as follows**

**d={100:'durga' ,200:'ravi', 300:'shiva'}**

**d={key:value, key:value}**

**2**

```

```

**How to access data from the dictionary?**

**We can access data by using keys.**

**d={100:'durga' ,200:'ravi', 300:'shiva'}**

**print(d[100]) #durga
 print(d[300]) #shiva**

**If the specified key is not available then we will get KeyError**

**print(d[400]) # KeyError: 400**

**We can prevent this by checking whether key is already available or not by using**

**has_key() function or by using in operator.**

**d.has_key(400) ==> returns 1 if key is available otherwise returns 0**

**But has_key() function is available only in Python 2 but not in Python 3. Hence
 compulsory we have to use in operator.**

**if 400 in d:**

**print(d[400])**

**Q. Write a program to enter name and percentage marks in a dictionary and**

**display information on the screen**

```
 rec={}
n=int(input("Enter number of students: "))
i= 1
while i <=n:
name=input("Enter Student Name: ")
marks=input("Enter % of Marks of Student: ")
rec[name]=marks
i=i+ 1
print("Name of Student","\t","% of marks")
for x in rec:
1 print("\t",x,"\t\t",rec[x])
12 )
1Output
1D:\Python_classes>py test.py
1Enter number of students: 3
1Enter Student Name: durga
1Enter % of Marks of Student: 60 %
1Enter Student Name: ravi
1Enter % of Marks of Student: 70 %
20 ) Enter Student Name: shiva
```

**3**

```

2 Enter % of Marks of Student: 80 %
2Name of Student % of marks
2durga 60 %
2ravi 70 %
2shiva 80 %
```

**How to update dictionaries?**

**d[key]=value**

**If the key is not available then a new entry will be added to the dictionary with the
 specified key-value pair**

**If the key is already available then old value will be replaced with new value.**

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d)
3. d[ 400 ]="pavan"
4. print(d)
5. d[ 100 ]="sunny"
6. print(d)
7.
8. Output
9. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva'}
10. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva', 400 : 'pavan'}
11. { 100 : 'sunny', 200 : 'ravi', 300 : 'shiva', 400 : 'pavan'}
```

**How to delete elements from dictionary?**

**del d[key]**

**It deletes entry associated with the specified key.
 If the key is not available then we will get KeyError**

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d)
3. del d[ 100 ]
4. print(d)
5. del d[ 400 ]
6.
7. Output
8. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva'}
```

**4**

```

9. { 200 : 'ravi', 300 : 'shiva'}
10. KeyError: 400
```

**d.clear()**

**To remove all entries from the dictionary**

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d)
3. d.clear()
4. print(d)
5.
6. Output
7. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva'}
8. {}
```

**del d**

**To delete total dictionary.Now we cannot access d**

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d)
3. del d
4. print(d)
5.
6. Output
7. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva'}
8. NameError: name 'd' is not defined
```

**Important functions of dictionary:**

**1. dict():**

**To create a dictionary**

**d=dict() ===>It creates empty dictionary
 d=dict({100:"durga",200:"ravi"}) ==>It creates dictionary with specified elements**

**d=dict([(100,"durga"),(200,"shiva"),(300,"ravi")])==>It creates dictionary with the given**

**list of tuple elements**

**5**

```

```

**2. len()**

**Returns the number of items in the dictionary**

**3. clear():**

**To remove all elements from the dictionary**

**4. get():**

**To get the value associated with the key**

**d.get(key)
 If the key is available then returns the corresponding value otherwise returns None.It**

**wont raise any error.**

**d.get(key,defaultvalue)**

**If the key is available then returns the corresponding value otherwise returns default**

**value.**

**Eg:**

**d={100:"durga",200:"ravi",300:"shiva"}**

**print(d[100]) ==>durga**

**print(d[400]) ==>KeyError:400
 print(d.get(100)) ==durga**

**print(d.get(400)) ==>None
 print(d.get(100,"Guest")) ==durga**

**print(d.get(400,"Guest")) ==>Guest**

**3. pop():**

**d.pop(key)**

**It removes the entry associated with the specified key and returns the corresponding
 value**

**If the specified key is not available then we will get KeyError**

**Eg:**

```
 d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
print(d.pop( 100 ))
print(d)
print(d.pop( 400 ))
5 )
Output
```

**6**

```

durga
{ 200 : 'ravi', 300 : 'shiva'}
KeyError: 400
```

**4. popitem():**

**It removes an arbitrary item(key-value) from the dictionaty and returns it.**

**Eg:**

```
 d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
print(d)
print(d.popitem())
print(d)
5 )
Output
{ 100 : 'durga', 200 : 'ravi', 300 : 'shiva'}
( 300 , 'shiva')
{ 100 : 'durga', 200 : 'ravi'}
```

**If the dictionary is empty then we will get KeyError**

**d={}**

**print(d.popitem()) ==>KeyError: 'popitem(): dictionary is empty'**

**5. keys():**

**It returns all keys associated eith dictionary**

**Eg:**

```
 d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
print(d.keys())
for k in d.keys():
print(k)
5 )
Output
dict_keys([ 100 , 200 , 300 ])
100
200
300
```

**6. values():**

**It returns all values associated with the dictionary**

**7**

```

```

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d.values())
3. for v in d.values():
4. print(v)
5.
6. Output
7. dict_values(['durga', 'ravi', 'shiva'])
8. durga
9. ravi
10. shiva
```

**7. items():**

**It returns list of tuples representing key-value pairs.**

**[(k,v),(k,v),(k,v)]**

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. for k,v in d.items():
3. print(k,"--",v)
4.
5. Output
6. 100 -- durga
7. 200 -- ravi
8. 300 -- shiva
```

**8. copy():**

**To create exactly duplicate dictionary(cloned copy)**

**d1=d.copy();**

**9. setdefault():**

**d.setdefault(k,v)**

**If the key is already available then this function returns the corresponding value.
 If the key is not available then the specified key-value will be added as new item to the**

**dictionary.**

**8**

```

```

**Eg:**

```
1. d={ 100 :"durga", 200 :"ravi", 300 :"shiva"}
2. print(d.setdefault( 400 ,"pavan"))
3. print(d)
4. print(d.setdefault( 100 ,"sachin"))
5. print(d)
6.
7. Output
8. pavan
9. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva', 400 : 'pavan'}
10. durga
11. { 100 : 'durga', 200 : 'ravi', 300 : 'shiva', 400 : 'pavan'}
```

**10. update():**

**d.update(x)
 All items present in the dictionary x will be added to dictionary d**

**Q. Write a program to take dictionary from the keyboard and print the sum**

**of values?**

```
1. d=eval(input("Enter dictionary:"))
2. s=sum(d.values())
3. print("Sum= ",s)
4.
5. Output
6. D:\Python_classes>py test.py
7. Enter dictionary:{'A': 100 ,'B': 200 ,'C': 300 }
8. Sum= 600
```

**Q. Write a program to find number of occurrences of each letter present in**

**the given string?**

```
1. word=input("Enter any word: ")
2. d={}
3. for x in word:
4. d[x]=d.get(x, 0 )+ 1
5. for k,v in d.items():
6. print(k,"occurred ",v," times")
7.
8. Output
9. D:\Python_classes>py test.py
10. Enter any word: mississippi
11. m occurred 1 times
12. i occurred 4 times
13. s occurred 4 times
```

**9**

```

14. p occurred 2 times
```

**Q. Write a program to find number of occurrences of each vowel present in**

**the given string?**

```
1. word=input("Enter any word: ")
2. vowels={'a','e','i','o','u'}
3. d={}
4. for x in word:
5. if x in vowels:
6. d[x]=d.get(x, 0 )+ 1
7. for k,v in sorted(d.items()):
8. print(k,"occurred ",v," times")
9.
10. Output
11. D:\Python_classes>py test.py
12. Enter any word: doganimaldoganimal
13. a occurred 4 times
14. i occurred 2 times
15. o occurred 2 times
```

**Q. Write a program to accept student name and marks from the keyboard**

**and creates a dictionary. Also display student marks by taking student name**

**as input?**

```
 n=int(input("Enter the number of students: "))
d={}
for i in range(n):
name=input("Enter Student Name: ")
marks=input("Enter Student Marks: ")
d[name]=marks
while True:
name=input("Enter Student Name to get Marks: ")
marks=d.get(name,- 
if marks== - 1 :
1 print("Student Not Found")
1else:
1print("The Marks of",name,"are",marks)
1option=input("Do you want to find another student marks[Yes|No]")
1if option=="No":
1break
1print("Thanks for using our application")
18 )
1Output
20 ) D:\Python_classes>py test.py
2 Enter the number of students: 5
2Enter Student Name: sunny
2Enter Student Marks: 90
```

**10**

```

2Enter Student Name: banny
2Enter Student Marks: 80
2Enter Student Name: chinny
2Enter Student Marks: 70
2Enter Student Name: pinny
2Enter Student Marks: 60
30 ) Enter Student Name: vinny
3 Enter Student Marks: 50
3Enter Student Name to get Marks: sunny
3The Marks of sunny are 90
3Do you want to find another student marks[Yes|No]Yes
3Enter Student Name to get Marks: durga
3Student Not Found
3Do you want to find another student marks[Yes|No]No
3Thanks for using our application
```

**Dictionary Comprehension:**

**Comprehension concept applicable for dictionaries also.**

```
1. squares={x:x*x for x in range( 1 , 6 )}
2. print(squares)
3. doubles={x: 2 *x for x in range( 1 , 6 )}
4. print(doubles)
5.
6. Output
7. { 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16 , 5 : 25 }
8. { 1 : 2 , 2 : 4 , 3 : 6 , 4 : 8 , 5 : 10 }
```

**1**

```

```

##### FUNCTIONS

**If a group of statements is repeatedly required then it is not recommended to write these**

**statements everytime seperately.We have to define these statements as a single unit and**

**we can call that unit any number of times based on our requirement without rewriting.
 This unit is nothing but function.**

**The main advantage of functions is code Reusability.
 Note: In other languages functions are known as methods,procedures,subroutines etc**

**Python supports 2 types of functions**

**1. Built in Functions

1. User Defined Functions
2. Built in Functions:**

**The functions which are coming along with Python software automatically,are called built**

**in functions or pre defined functions**

**Eg:**

**id()
 type()**

**input()
 eval()**

**etc..**

**2. User Defined Functions:**

**The functions which are developed by programmer explicitly according to business
 requirements ,are called user defined functions.**

**Syntax to create user defined functions:**

**def function_name(parameters) :**

**""" doc string"""**

**----
 -----**

**return value**

**2**

```

```

**Note: While creating functions we can use 2 keywords**

**1. def (mandatory)

1. return (optional)**

**Eg 1 : Write a function to print Hello**

**test.py:**

```
 def wish():
print("Hello Good Morning")
wish()
wish()
wish()
```

**Parameters**

**Parameters are inputs to the function. If a function contains parameters,then at the time
 of calling,compulsory we should provide values otherwise,otherwise we will get error.**

**Eg: Write a function to take name of the student as input and print wish message by**

**name.**

```
1. def wish(name):
2. print("Hello",name," Good Morning")
3. wish("Durga")
4. wish("Ravi")
5.
6.
7. D:\Python_classes>py test.py
8. Hello Durga Good Morning
9. Hello Ravi Good Morning
```

**Eg: Write a function to take number as input and print its square value**

```
1. def squareIt(number):
2. print("The Square of",number,"is", number*number)
3. squareIt( 4 )
4. squareIt( 5 )
5.
6. D:\Python_classes>py test.py
7. The Square of 4 is 16
8. The Square of 5 is 25
```

**3**

```

```

**Return Statement:**

**Function can take input values as parameters and executes business logic, and returns**

**output to the caller with return statement.**

**Q. Write a function to accept 2 numbers as input and return sum.**

```
1. def add(x,y):
2. return x+y
3. result=add( 10 , 20 )
4. print("The sum is",result)
5. print("The sum is",add( 100 , 200 ))
6.
7.
8. D:\Python_classes>py test.py
9. The sum is 30
10. The sum is 300
```

**If we are not writing return statement then default return value is None**

**Eg:**

```
1. def f1():
2. print("Hello")
3. f1()
4. print(f1())
5.
6. Output
7. Hello
8. Hello
9. None
```

**Q. Write a function to check whether the given number is even or odd?**

```
1. def even_odd(num):
2. if num% 2 == 0 :
3. print(num,"is Even Number")
4. else:
5. print(num,"is Odd Number")
6. even_odd( 10 )
7. even_odd( 15 )
8.
9. Output
10. D:\Python_classes>py test.py
11. 10 is Even Number
12. 15 is Odd Number
```

**4**

```

```

**Q. Write a function to find factorial of given number?**

```
 def fact(num):
result= 1
while num>= 1 :
result=result*num
num=num- 1
return result
for i in range( 1 , 5 ):
print("The Factorial of",i,"is :",fact(i))
9 )
Output
1 D:\Python_classes>py test.py
1The Factorial of 1 is : 1
1The Factorial of 2 is : 2
1The Factorial of 3 is : 6
1The Factorial of 4 is : 24
```

**Returning multiple values from a function:**

**In other languages like C,C++ and Java, function can return atmost one value. But in
 Python, a function can return any number of values.**

**Eg 1 :**

```
 def sum_sub(a,b):
sum=a+b
sub=a-b
return sum,sub
x,y=sum_sub( 100 , 50 )
print("The Sum is :",x)
print("The Subtraction is :",y)
8 )
Output
The Sum is : 150
1 The Subtraction is : 50
```

**Eg 2 :**

```
 def calc(a,b):
sum=a+b
sub=a-b
mul=a*b
div=a/b
return sum,sub,mul,div
t=calc( 100 , 50 )
print("The Results are")
```

**5**

```

for i in t:
print(i)
1
1Output
1The Results are
1150
150
15000
12.0
```

**Types of arguments**

**def f1(a,b):
 ------**

**------**

**------
 f1(10,20)**

**a,b are formal arguments where as 10,20 are actual arguments**

**There are 4 types are actual arguments are allowed in Python.**

**1. positional arguments

1. keyword arguments
2. default arguments
3. Variable length arguments
4. positional arguments:**

**These are the arguments passed to function in correct positional order.**

**def sub(a,b):
 print(a-b)**

**sub(100,200)**

**sub(200,100)**

**The number of arguments and position of arguments must be matched. If we change the**

**order then result may be changed.**

**If we change the number of arguments then we will get error.**

**6**

```

```

**2. keyword arguments:**

**We can pass argument values by keyword i.e by parameter name.**

**Eg:**

```
1. def wish(name,msg):
2. print("Hello",name,msg)
3. wish(name="Durga",msg="Good Morning")
4. wish(msg="Good Morning",name="Durga")
5.
6. Output
7. Hello Durga Good Morning
8. Hello Durga Good Morning
```

**Here the order of arguments is not important but number of arguments must be matched.**

**Note:**

**We can use both positional and keyword arguments simultaneously. But first we have to**

**take positional arguments and then keyword arguments,otherwise we will get**

**syntaxerror.**

**def wish(name,msg):**

**print("Hello",name,msg)
 wish("Durga","GoodMorning") ==>valid**

**wish("Durga",msg="GoodMorning") ==>valid**

**wish(name="Durga","GoodMorning") ==>invalid
 SyntaxError: positional argument follows keyword argument**

**3. Default Arguments:**

**Sometimes we can provide default values for our positional arguments.**

**Eg:**

```
 def wish(name="Guest"):
print("Hello",name,"Good Morning")
3 )
wish("Durga")
wish()
6 )
Output
Hello Durga Good Morning
Hello Guest Good Morning
```

**7**

```

```

**If we are not passing any name then only default value will be considered.**

*****Note:**

**After default arguments we should not take non default arguments**

**def wish(name="Guest",msg="Good Morning"): ===>Valid**

**def wish(name,msg="Good Morning"): ===>Valid**

**def wish(name="Guest",msg): ==>Invalid**

**SyntaxError: non-default argument follows default argument**

**4. Variable length arguments:**

**Sometimes we can pass variable number of arguments to our function,such type of**

**arguments are called variable length arguments.**

**We can declare a variable length argument with \* symbol as follows**

**def f1(\*n):**

**We can call this function by passing any number of arguments including zero number.
 Internally all these values represented in the form of tuple.**

**Eg:**

```
 def sum(*n):
total= 0
for n1 in n:
total=total+n1
print("The Sum=",total)
6 )
sum()
sum( 10 )
sum( 10 , 20 )
sum( 10 , 20 , 30 , 40 )
1
1Output
1The Sum= 0
1The Sum= 10
1The Sum= 30
1The Sum= 100
```

**Note:**

**We can mix variable length arguments with positional arguments.**

**8**

```

```

**Eg:**

```
 def f1(n1,*s):
print(n1)
for s1 in s:
print(s1)
5 )
f1( 10 )
f1( 10 , 20 , 30 , 40 )
f1( 10 ,"A", 30 ,"B")
9 )
Output
1 10
110
120
130
140
110
1A
130
1B
```

**Note: After variable length argument,if we are taking any other arguments then we**

**should provide values as keyword arguments.**

**Eg:**

```
 def f1(*s,n1):
for s1 in s:
print(s1)
print(n1)
5 )
f1("A","B",n1= 10 )
Output
A
B
10
```

**f1("A","B",10) ==>Invalid
 TypeError: f1() missing 1 required keyword-only argument: 'n1'**

**Note: We can declare key word variable length arguments also.**

**For this we have to use **.**

**def f1(**n):**

**9**

```

```

**We can call this function by passing any number of keyword arguments. Internally these
 keyword arguments will be stored inside a dictionary.**

**Eg:**

```
 def display(**kwargs):
for k,v in kwargs.items():
print(k,"=",v)
display(n1= 10 ,n2= 20 ,n3= 30 )
display(rno= 100 ,name="Durga",marks= 70 ,subject="Java")
6 )
Output
n1 = 10
n2 = 20
n3 = 30
1 rno = 100
1name = Durga
1marks = 70
1subject = Java
```

**Case Study:**

**def f(arg1,arg2,arg3=4,arg4=8):**

**print(arg1,arg2,arg3,arg4)**

**1. f(3,2) ==> 3 2 4 8

1. f(10,20,30,40) ===>10 20 30 40
2. f(25,50,arg4=100) ==>25 50 4 100
3. f(arg4=2,arg1=3,arg2=4)===>3 4 4 2
4. f()===>Invalid
    TypeError: f() missing 2 required positional arguments: 'arg1' and 'arg2'
5. f(arg3=10,arg4=20,30,40) ==>Invalid**

**SyntaxError: positional argument follows keyword argument**

**[After keyword arguments we should not take positional arguments]**

**7. f(4,5,arg2=6)==>Invalid**

**TypeError: f() got multiple values for argument 'arg2'**

**8. f(4,5,arg3=5,arg5=6)==>Invalid**

**TypeError: f() got an unexpected keyword argument 'arg5'**

**10**

```

```

**Note: Function vs Module vs Library:**

**1. A group of lines with some name is called a function

1. A group of functions saved to a file , is called Module
2. A group of Modules is nothing but Library**

**Types of Variables**

**Python supports 2 types of variables.**

**1. Global Variables

1. Local Variables
2. Global Variables**

**The variables which are declared outside of function are called global variables.
 These variables can be accessed in all functions of that module.**

**Eg:**

```
 a= 10 # global variable
def f1():
print(a)
4 )
def f2():
print(a)
7 )
f1()
f2()
10 )
1 Output
110
110
Function 1
Function 2
Function 3
Module 1
Function 1
Function 2
Function 3
Module 2
Library
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
-----------------
```

**-**

```
Function
```

**11**

```

```

**2. Local Variables:**

**The variables which are declared inside a function are called local variables.**

**Local variables are available only for the function in which we declared it.i.e from outside**

**of function we cannot access.**

**Eg:**

```
 def f1():
a= 10
print(a) # valid
4 )
def f2():
print(a) #invalid
7 )
f1()
f2()
10 )
1 NameError: name 'a' is not defined
```

**global keyword:**

**We can use global keyword for the following 2 purposes:**

**1. To declare global variable inside function

1. To make global variable available to the function so that we can perform required**

**modifications**

**Eg 1 :**

```
 a= 10
def f1():
a= 777
print(a)
5 )
def f2():
print(a)
8 )
f1()
f2()
1
1Output
1777
110
```

**12**

```

```

**Eg 2 :**

```
 a= 10
def f1():
global a
a= 777
print(a)
6 )
def f2():
print(a)
9 )
f1()
1 f2()
12 )
1Output
1777
1777
```

**Eg 3 :**

```
 def f1():
a= 10
print(a)
4 )
def f2():
print(a)
7 )
f1()
f2()
10 )
1 NameError: name 'a' is not defined
```

**Eg 4 :**

```
 def f1():
global a
a= 10
print(a)
5 )
def f2():
print(a)
8 )
f1()
f2()
1
1Output
110
110
```

**13**

```

```

**Note: If global variable and local variable having the same name then we can access**

**global variable inside a function as follows**

```
 a= 10 #global variable
def f1():
a= 777 #local variable
print(a)
print(globals()['a'])
f1()
7 )
8 )
Output
777
1 10
```

**Recursive Functions**

**A function that calls itself is known as Recursive Function.**

**Eg:**

**factorial(3)=3\*factorial(2)**

**=3\*2*factorial(1)
 =3*2*1*factorial(0)**

**=3\*2*1*1**

**=6
 factorial(n)= n\*factorial(n-1)**

**The main advantages of recursive functions are:**

**1. We can reduce length of the code and improves readability

1. We can solve complex problems very easily.**

**Q. Write a Python Function to find factorial of given number with recursion.**

**Eg:**

```
 def factorial(n):
if n== 0 :
result= 1
else:
result=n*factorial(n- 
return result
print("Factorial of 4 is :",factorial( 4 ))
print("Factorial of 5 is :",factorial( 5 ))
9 )
Output
```

**14**

```

1 Factorial of 4 is : 24
1Factorial of 5 is : 120
```

**Anonymous Functions:**

**Sometimes we can declare a function without any name,such type of nameless functions
 are called anonymous functions or lambda functions.**

**The main purpose of anonymous function is just for instant use(i.e for one time usage)**

**Normal Function:**

**We can define by using def keyword.**

**def squareIt(n):
 return n\*n**

**lambda Function:**

**We can define by using lambda keyword**

**lambda n:n\*n**

**Syntax of lambda Function:**

**lambda argument_list : expression**

**Note: By using Lambda Functions we can write very concise code so that readability of**

**the program will be improved.**

**Q. Write a program to create a lambda function to find square of given**

**number?**

```
 s=lambda n:n*n
print("The Square of 4 is :",s( 4 ))
print("The Square of 5 is :",s( 5 ))
4 )
Output
The Square of 4 is : 16
The Square of 5 is : 25
```

**Q. Lambda function to find sum of 2 given numbers**

```
 s=lambda a,b:a+b
print("The Sum of 10,20 is:",s( 10 , 20 ))
```

**15**

```

print("The Sum of 100,200 is:",s( 100 , 200 ))
4 )
Output
The Sum of 10 , 20 is: 30
The Sum of 100 , 200 is: 300
```

**Q. Lambda Function to find biggest of given values.**

```
 s=lambda a,b:a if a>b else b
print("The Biggest of 10,20 is:",s( 10 , 20 ))
print("The Biggest of 100,200 is:",s( 100 , 200 ))
4 )
Output
The Biggest of 10 , 20 is: 20
The Biggest of 100 , 200 is: 200
```

**Note:**

**Lambda Function internally returns expression value and we are not required to write**

**return statement explicitly.**

**Note: Sometimes we can pass function as argument to another function. In such cases**

**lambda functions are best choice.**

**We can use lambda functions very commonly with filter(),map() and reduce() functions,b'z**

**these functions expect function as argument.**

**filter() function:**

**We can use filter() function to filter values from the given sequence based on some**

**condition.**

**filter(function,sequence)**

**where function argument is responsible to perform conditional check
 sequence can be list or tuple or string.**

**Q. Program to filter only even numbers from the list by using filter()**

**function?**

**without lambda Function:**

```
 def isEven(x):
if x% 2 == 0 :
return True
else:
```

**16**

```

return False
l=[ 0 , 5 , 10 , 15 , 20 , 25 , 30 ]
l1=list(filter(isEven,l))
print(l1) #[0,10,20,30]
```

**with lambda Function:**

```
 l=[ 0 , 5 , 10 , 15 , 20 , 25 , 30 ]
l1=list(filter(lambda x:x% 2 == 0 ,l))
print(l1) #[0,10,20,30]
l2=list(filter(lambda x:x% 2 != 0 ,l))
print(l2) #[5,15,25]
```

**map() function:**

**For every element present in the given sequence,apply some functionality and generate
 new element with the required modification. For this requirement we should go for**

**map() function.**

**Eg: For every element present in the list perform double and generate new list of doubles.**

**Syntax:**

**map(function,sequence)**

**The function can be applied on each element of sequence and generates new sequence.**

**Eg: Without lambda**

```
 l=[ 1 , 2 , 3 , 4 , 5 ]
def doubleIt(x):
return 2 *x
l1=list(map(doubleIt,l))
print(l1) #[2, 4, 6, 8, 10]
```

**with lambda**

```
 l=[ 1 , 2 , 3 , 4 , 5 ]
l1=list(map(lambda x: 2 *x,l))
print(l1) #[2, 4, 6, 8, 10]
```

**-------------------------------------------------------------**

**17**

```

```

**Eg 2 : To find square of given numbers**

```
1. l=[ 1 , 2 , 3 , 4 , 5 ]
2. l1=list(map(lambda x:x*x,l))
3. print(l1) #[1, 4, 9, 16, 25]
```

**We can apply map() function on multiple lists also.But make sure all list should have same**

**length.**

**Syntax: map(lambda x,y:x\*y,l1,l2))
 x is from l1 and y is from l2**

**Eg:**

```
1. l1=[ 1 , 2 , 3 , 4 ]
2. l2=[ 2 , 3 , 4 , 5 ]
3. l3=list(map(lambda x,y:x*y,l1,l2))
4. print(l3) #[2, 6, 12, 20]
```

**reduce() function:**

**reduce() function reduces sequence of elements into a single element by applying the
 specified function.**

**reduce(function,sequence)**

**reduce() function present in functools module and hence we should write import**

**statement.**

**Eg:**

```
 from functools import *
l=[ 10 , 20 , 30 , 40 , 50 ]
result=reduce(lambda x,y:x+y,l)
print(result) # 150
```

**Eg:**

```
 result=reduce(lambda x,y:x*y,l)
print(result) #12000000
```

**Eg:**

```
 from functools import *
result=reduce(lambda x,y:x+y,range( 1 , 10)
print(result) #5050
```

**18**

```

```

**Note:**
  **In Python every thing is treated as object.**
  **Even functions also internally treated as objects only.**

**Eg:**

```
 def f1():
print("Hello")
print(f1)
print(id(f1))
```

**Output
 <function f1 at 0x00419618>
 4298264**

**Function Aliasing:**

**For the existing function we can give another name, which is nothing but function aliasing.**

**Eg:**

```
 def wish(name):
print("Good Morning:",name)
3 )
greeting=wish
print(id(wish))
print(id(greeting))
7 )
greeting('Durga')
wish('Durga')
```

**Output
 4429336
 4429336
 Good Morning: Durga
 Good Morning: Durga**

**Note: In the above example only one function is available but we can call that function by using
 either wish name or greeting name.**

**If we delete one name still we can access that function by using alias name**

**Eg:**

```
 def wish(name):
print("Good Morning:",name)
```

**19**

```

3 )
greeting=wish
5 )
greeting('Durga')
wish('Durga')
8 )
del wish
#wish('Durga') ==>NameError: name 'wish' is not defined
1 greeting('Pavan')
```

**Output
 Good Morning: Durga
 Good Morning: Durga
 Good Morning: Pavan**

**Nested Functions:**

**We can declare a function inside another function, such type of functions are called Nested
 functions.**

**Eg:**

```
 def outer():
print("outer function started")
def inner():
print("inner function execution")
print("outer function calling inner function")
inner()
outer()
#inner() ==>NameError: name 'inner' is not defined
```

**Output
 outer function started
 outer function calling inner function
 inner function execution**

**In the above example inner() function is local to outer() function and hence it is not possible to call
 directly from outside of outer() function.**

**Note: A function can return another function.**

**Eg:**

```
 def outer():
print("outer function started")
def inner():
print("inner function execution")
```

**20**

```

print("outer function returning inner function")
return inner
f1=outer()
f1()
f1()
f1()
```

**Output
 outer function started
 outer function returning inner function
 inner function execution
 inner function execution
 inner function execution**

**Q. What is the differenece between the following lines?**

**f1 = outer**

**f1 = outer()**

 **In the first case for the outer() function we are providing another name f1(function aliasing).**
  **But in the second case we calling outer() function,which returns inner function.For that inner
 function() we are providing another name f1**

**Note: We can pass function as argument to another function**

**Eg: filter(function,sequence)
 map(function,sequence)
 reduce(function,sequence)**

**21**

```

```

**Function Decorators:**

**Decorator is a function which can take a function as argument and extend its functionality**

**and returns modified function with extended functionality.**

**The main objective of decorator functions is we can extend the functionality of existing**

**functions without modifies that function.**

```
 def wish(name):
print("Hello",name,"Good Morning")
```

**This function can always print same output for any name**

**Hello Durga Good Morning**

**Hello Ravi Good Morning
 Hello Sunny Good Morning**

**But we want to modify this function to provide different message if name is Sunny.**

**We can do this without touching wish() function by using decorator.**

**Eg:**

```
 def decor(func):
def inner(name):
if name=="Sunny":
print("Hello Sunny Bad Morning")
else:
func(name)
return inner
8 )
@decor
def wish(name):
1 print("Hello",name,"Good Morning")
12 )
1wish("Durga")
1wish("Ravi")
1wish("Sunny")
16 )
Decorator
Input Function
wish()
new(add some functionality)
inner()
Decorator
Function
Input Function
Output Function with
extended Functionality
```

**22**

```

1Output
1Hello Durga Good Morning
1Hello Ravi Good Morning
20 ) Hello Sunny Bad Morning
```

**In the above program whenever we call wish() function automatically decor function will**

**be executed.**

**How to call same function with decorator and without decorator:**

**We should not use @decor**

```
 def decor(func):
def inner(name):
if name=="Sunny":
print("Hello Sunny Bad Morning")
else:
func(name)
return inner
8 )
9 )
def wish(name):
1 print("Hello",name,"Good Morning")
12 )
1decorfunction=decor(wish)
14 )
1wish("Durga") #decorator wont be executed
1wish("Sunny") #decorator wont be executed
17 )
1decorfunction("Durga")#decorator will be executed
1decorfunction("Sunny")#decorator will be executed
20 )
2 Output
2Hello Durga Good Morning
2Hello Sunny Good Morning
2Hello Durga Good Morning
2Hello Sunny Bad Morning
```

**Eg 2 :**

```
 def smart_division(func):
def inner(a,b):
print("We are dividing",a,"with",b)
if b== 0 :
print("OOPS...cannot divide")
return
else:
return func(a,b)
```

**23**

```

return inner
10 )
1 @smart_division
1def division(a,b):
1return a/b
14 )
1print(division( 20 , 2 ))
1print(division( 20 , 0 ))
17 )
1without decorator we will get Error.In this case output is:
19 )
20 ) 10.0
2 Traceback (most recent call last):
2File "test.py", line 16 , in <module>
2print(division( 20 , 0 ))
2File "test.py", line 13 , in division
2return a/b
2ZeroDivisionError: division by zero
```

**with decorator we won't get any error. In this case output is:**

**We are dividing 20 with 2**

**10.0
 We are dividing 20 with 0**

**OOPS...cannot divide**

**None**

**Decorator Chaining**

**We can define multiple decorators for the same function and all these decorators will**

**form Decorator Chaining.**

**Eg:**

**@decor1
 @decor**

**def num():**

**For num() function we are applying 2 decorator functions. First inner decorator will work**

**and then outer decorator.**

**Eg:**

```
 def decor1(func):
def inner():
x=func()
return x*x
```

**24**

```

return inner
6 )
def decor(func):
def inner():
x=func()
return 2 *x
1 return inner
12 )
1@decor1
1@decor
1def num():
1return 10
17 )
1print(num())
```

**Demo Program for decorator Chaining:**

```
 def decor(func):
def inner(name):
print("First Decor(decor) Function Execution")
func(name)
return inner
6 )
def decor1(func):
def inner(name):
print("Second Decor(decor1) Execution")
func(name)
1 return inner
12 )
1@decor1
1@decor
1def wish(name):
1print("Hello",name,"Good Morning")
17 )
1wish("Durga")
```

**D:\durgaclasses>py decaratordemo1.py
 Second Decor(decor1) Execution**

**First Decor(decor) Function Execution**

**Hello Durga Good Morning**

**25**

```

```

**Generators**

**Generator is a function which is responsible to generate a sequence of values.
 We can write generator functions just like ordinary functions, but it uses yield keyword to**

**return values.**

**Eg 1 :**

```
 def mygen():
yield 'A'
yield 'B'
yield 'C'
5 )
g=mygen()
print(type(g))
8 )
print(next(g))
print(next(g))
1 print(next(g))
1print(next(g))
13 )
1Output
1<class 'generator'>
1A
1B
1C
1Traceback (most recent call last):
20 ) File "test.py", line 12 , in <module>
2 print(next(g))
2StopIteration
```

**Eg 2 :**

```
 def countdown(num):
print("Start Countdown")
while(num> 0 ):
yield num
num=num- 1
6 )
values=countdown( 5 )
for x in values:
Generator
Function
A Sequence of Values
yield
```

**26**

```

print(x)
10 )
1 Output
1Start Countdown
15
14
13
12
11
```

**Eg 3 : To generate first n numbers:**

```
 def firstn(num):
n= 1
while n<=num:
yield n
n=n+ 1
6 )
values=firstn( 5 )
for x in values:
print(x)
10 )
1 Output
11
12
13
14
15
```

**We can convert generator into list as follows:**

**values=firstn(10)
 l1=list(values)**

**print(l1) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

**Eg 4 : To generate Fibonacci Numbers...**

**The next is the sum of previous 2 numbers**

**Eg: 0,1,1,2,3,5,8,13,21,...**

```
 def fib():
a,b= 0 , 1
while True:
yield a
a,b=b,a+b
for f in fib():
if f> 100 :
break
print(f)
```

**27**

```

10 )
1 Output
10
11
11
12
13
15
18
113
20 ) 21
2 34
255
289
```

**Advantages of Generator Functions:**

**1. when compared with class level iterators, generators are very easy to use

1. Improves memory utilization and performance.
2. Generators are best suitable for reading data from large number of large files
3. Generators work great for web scraping and crawling.**

**Generators vs Normal Collections wrt performance:**

```
 import random
import time
3 )
names = ['Sunny','Bunny','Chinny','Vinny']
subjects = ['Python','Java','Blockchain']
6 )
def people_list(num_people):
results = []
for i in range(num_people):
person = {
1 'id':i,
1'name': random.choice(names),
1'subject':random.choice(subjects)
1}
1results.append(person)
1return results
17 )
1def people_generator(num_people):
1for i in range(num_people):
20 ) person = {
2 'id':i,
2'name': random.choice(names),
2'major':random.choice(subjects)
```

**28**

```

2}
2yield person
26 )
2'''''t1 = time.clock()
2people = people_list(10000000)
2t2 = time.clock()'''
30 )
3 t1 = time.clock()
3people = people_generator( 10000000 )
3t2 = time.clock()
34 )
3print('Took {}'.format(t2-t1))
```

**Note: In the above program observe the differnce wrt execution time by using list and generators**

**Generators vs Normal Collections wrt Memory Utilization:**

**Normal Collection:**

**l=[x\*x for x in range(10000000000000000)]
 print(l[0])**

**We will get MemoryError in this case because all these values are required to store in the memory.**

**Generators:**

**g=(x\*x for x in range(10000000000000000))
 print(next(g))**

**Output: 0
 We won't get any MemoryError because the values won't be stored at the beginning**

**1**

```

```

##### Modules

**A group of functions, variables and classes saved to a file, which is nothing but module.**

**Every Python file (.py) acts as a module.**

**Eg: durgamath.py**

```
 x= 888
2 )
def add(a,b):
print("The Sum:",a+b)
5 )
def product(a,b):
print("The Product:",a*b)
```

**durgamath module contains one variable and 2 functions.**

**If we want to use members of module in our program then we should import that module.**

**import modulename**

**We can access members by using module name.**

**modulename.variable**

**modulename.function()**

**test.py:**

```
 import durgamath
print(durgamath.x)
durgamath.add( 10 , 20 )
durgamath.product( 10 , 20 )
5 )
Output
888
The Sum: 30
The Product: 200
```

**2**

```

```

**Note:**

**whenever we are using a module in our program, for that module compiled file will be
 generated and stored in the hard disk permanently.**

**Renaming a module at the time of import (module aliasing):**

**Eg:
 import durgamath as m**

**here durgamath is original module name and m is alias name.
 We can access members by using alias name m**

**test.py:**

```
 import durgamath as m
print(m.x)
m.add( 10 , 20 )
m.product( 10 , 20 )
```

**from ... import:**

**We can import particular members of module by using from ... import.**

**The main advantage of this is we can access members directly without using module
 name.**

**Eg:**

**from durgamath import x,add**

**print(x)
 add(10,20)**

**product(10,20)==> NameError: name 'product' is not defined**

**We can import all members of a module as follows**

**from durgamath import ***

**test.py:**

```
 from durgamath import *
print(x)
add( 10 , 20 )
product( 10 , 20 )
```

**3**

```

```

**Various possibilties of import:**

**import modulename**

**import module1,module2,module3**

**import module1 as m
 import module1 as m1,module2 as m2,module3**

**from module import member
 from module import member1,member2,memebr3**

**from module import memeber1 as x**

**from module import ***

**member aliasing:**

**from durgamath import x as y,add as sum
 print(y)**

**sum(10,20)**

**Once we defined as alias name,we should use alias name only and we should not use**

**original name**

**Eg:**

**from durgamath import x as y**

**print(x)==>NameError: name 'x' is not defined**

**Reloading a Module:**

**By default module will be loaded only once eventhough we are importing multiple**

**multiple times.**

**Demo Program for module reloading:**

```
 import time
from imp import reload
import module1
time.sleep( 30 )
reload(module1)
time.sleep( 30 )
reload(module1)
print("This is test file")
```

**Note: In the above program, everytime updated version of module1 will be available to**

**our program**

**4**

```

```

**module1.py:**

**print("This is from module1")**

**test.py**

```
 import module1
import module1
import module1
import module1
print("This is test module")
6 )
Output
This is from module1
This is test module
```

**In the above program test module will be loaded only once eventhough we are importing
 multiple times.**

**The problem in this approach is after loading a module if it is updated outside then
 updated version of module1 is not available to our program.**

**We can solve this problem by reloading module explicitly based on our requirement.
 We can reload by using reload() function of imp module.**

**import imp
 imp.reload(module1)**

**test.py:**

```
 import module1
import module1
from imp import reload
reload(module1)
reload(module1)
reload(module1)
print("This is test module")
```

**In the above program module1 will be loaded 4 times in that 1 time by default and 3 times**

**explicitly. In this case output is**

```
 This is from module1
This is from module1
This is from module1
This is from module1
This is test module
```

**5**

```

```

**The main advantage of explicit module reloading is we can ensure that updated version is
 always available to our program.**

**Finding members of module by using dir() function:**

**Python provides inbuilt function dir() to list out all members of current module or a**

**specified module.**

**dir() ===>To list out all members of current module**

**dir(moduleName)==>To list out all members of specified module**

**Eg 1 : test.py**

```
 x= 10
y= 20
def f1():
print("Hello")
print(dir()) # To print all members of current module
6 )
Output
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__nam
e__', '__package__', '__spec__', 'f1', 'x', 'y']
```

**Eg 2: To display members of particular module:**

**durgamath.py:**

```
 x= 888
2 )
def add(a,b):
print("The Sum:",a+b)
5 )
def product(a,b):
print("The Product:",a*b)
```

**test.py:**

```
 import durgamath
print(dir(durgamath))
3 )
Output
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',
'__package__', '__spec__', 'add', 'product', 'x']
```

**Note: For every module at the time of execution Python interpreter will add some special**

**properties automatically for internal use.**

**6**

```

```

**Eg: \**builtins\**,\**cached\**,'\**doc\**,\**file\**, \**loader\**, \**name\**,\**package\**,
 \**spec\****

**Based on our requirement we can access these properties also in our program.**

**Eg: test.py:**

```
 print(__builtins__ )
print(__cached__ )
print(__doc__)
print(__file__)
print(__loader__)
print(__name__)
print(__package__)
print(__spec__)
9 )
Output
1 <module 'builtins' (built-in)>
1None
1None
```

**test.py**

```
 <_frozen_importlib_external.SourceFileLoader object at 0x00572170>
__main__
None
None
```

**The Special variable \**name\**:**

**For every Python program , a special variable \**name\** will be added internally.
 This variable stores information regarding whether the program is executed as an**

**individual program or as a module.**

**If the program executed as an individual program then the value of this variable is**

***\*main\****

**If the program executed as a module from some other program then the value of this
 variable is the name of module where it is defined.**

**Hence by using this \**name\** variable we can identify whether the program executed**

**directly or as a module.**

**7**

```

```

**Demo program:**

**module1.py:**

```
 def f1():
if __name__=='__main__':
print("The code executed as a program")
else:
print("The code executed as a module from some other program")
f1()
```

**test.py:**

```
 import module1
module1.f1()
3 )
D:\Python_classes>py module1.py
The code executed as a program
6 )
D:\Python_classes>py test.py
The code executed as a module from some other program
The code executed as a module from some other program
```

**Working with math module:**

**Python provides inbuilt module math.
 This module defines several functions which can be used for mathematical operations.**

**The main important functions are**

**1. sqrt(x)

1. ceil(x)
2. floor(x)
3. fabs(x)**

**5.log(x)**

**6. sin(x)

1. tan(x)**

**....**

**Eg:**

```
 from math import *
print(sqrt( 4 ))
print(ceil(10.1))
print(floor(10.1))
print(fabs(-10.6))
print(fabs(10.6))
```

**8**

```

7 )
Output
2.0
11
1 10
110.6
110.6
```

**Note:**

**We can find help for any module by using help() function**

**Eg:**

**import math**

**help(math)**

**Working with random module:**

**This module defines several functions to generate random numbers.**

**We can use these functions while developing games,in cryptography and to generate**

**random numbers on fly for authentication.**

**1. random() function:**

**This function always generate some float value between 0 and 1 ( not inclusive)
 0<x<1**

**Eg:**

```
 from random import *
for i in range( 10 ):
print(random())
4 )
Output
0.4572685609302056
0.6584325233197768
0.15444034016553587
0.18351427005232201
0.1330257265904884
1 0.9291139798071045
10.6586741197891783
10.8901649834019002
10.25540891083913053
10.7290504335962871
```

**9**

```

```

**2. randint() function:**

**To generate random integer beween two given numbers(inclusive)**

**Eg:**

```
 from random import *
for i in range( 10 ):
print(randint( 1 , 100 )) # generate random int value between 1 and 100(inclusive)
4 )
Output
51
44
39
70
49
1 74
152
110
140
18
```

**3. uniform():**

**It returns random float values between 2 given numbers(not inclusive)**

**Eg:**

```
 from random import *
for i in range( 10 ):
print(uniform( 1 , 10 ))
4 )
Output
9.787695398230332
6.81102218793548
8.068672144377329
8.567976357239834
6.363511674803802
1 2.176137584071641
14.822867939432386
16.0801725149678445
17.508457735544763
11.9982221862917555
```

**random() ===>in between 0 and 1 (not inclusive)
 randint(x,y) ==>in between x and y ( inclusive)**

**uniform(x,y) ==> in between x and y ( not inclusive)**

**10**

```

```

**4. randrange([start],stop,[step])**

**returns a random number from range
 start<= x < stop**

**start argument is optional and default value is 0**

**step argument is optional and default value is 1**

**randrange(10)-->generates a number from 0 to 9**

**randrange(1,11)-->generates a number from 1 to 10
 randrange(1,11,2)-->generates a number from 1,3,5,7,9**

**Eg 1 :**

```
 from random import *
for i in range( 10 ):
print(randrange( 10 ))
4 )
Output
9
4
0
2
9
1 4
18
19
15
19
```

**Eg 2 :**

```
 from random import *
for i in range( 10 ):
print(randrange( 1 , 1)
4 )
Output
2
2
8
10
3
1 5
19
11
16
13
```

**11**

```

```

**Eg 3 :**

```
 from random import *
for i in range( 10 ):
print(randrange( 1 , 11 , 2 ))
4 )
Output
1
3
9
5
7
1 1
11
11
17
13
```

**5. choice() function:**

**It wont return random number.**

**It will return a random object from the given list or tuple.**

**Eg:**

```
 from random import *
list=["Sunny","Bunny","Chinny","Vinny","pinny"]
for i in range( 10 ):
print(choice(list))
```

**Output
 Bunny
 pinny
 Bunny
 Sunny
 Bunny
 pinny
 pinny
 Vinny
 Bunny
 Sunny**

**1**

```

```

##### Packages

**It is an encapsulation mechanism to group related modules into a single unit.**

**package is nothing but folder or directory which represents collection of Python modules.**

**Any folder or directory contains \**init\**.py file,is considered as a Python package.This file**

**can be empty.**

**A package can contains sub packages also.**

```
File 1
x.py y.py
Home Loan
__init__.py
File 1
m.py n.py
Vehicle Loan
__init__.py
Loan
File 1
__init__.py
```

**2**

```

```

**The main advantages of package statement are**

**1. We can resolve naming conflicts

1. We can identify our components uniquely
2. It improves modularity of the application**

**Eg 1 :**

**D:\Python_classes>
 |-test.py**

**|-pack1
 |-module1.py**

**|-\**init\**.py**

***\*init\**.py:**

**empty file**

**module1.py:**

**def f1():
 print("Hello this is from module1 present in pack1")**

**test.py (version-1):
 import pack1.module1**

**pack1.module1.f1()**

```
Loan
File 1
__init__.py
File 1
Module 1
Home Loan
Module 1
__init__.py
Vehicle Loan
File 1
Module 1 Module 1
__init__.py
```

**3**

```

```

**test.py (version-2):**

**from pack1.module1 import f1**

**f1()**

**Eg 2 :**

**D:\Python_classes>**

**|-test.py
 |-com**

**|-module1.py**

**|-\**init\**.py
 |-durgasoft**

**|-module2.py**

**|-\**init\**.py**

***\*init\**.py:**

**empty file**

**module1.py:**

**def f1():
 print("Hello this is from module1 present in com")**

**module2.py:**

**def f2():
 print("Hello this is from module2 present in com.durgasoft")**

**test.py:**

```
1. from com.module1 import f1
2. from com.durgasoft.module2 import f2
3. f1()
4. f2()
5.
6. Output
7. D:\Python_classes>py test.py
8. Hello this is from module1 present in com
9. Hello this is from module2 present in com.durgasoft
```

**Note: Summary diagram of library,packages,modules which contains functions,classes**

**and variables.**

**4**

```

```

**module 1 module 2 module n**

```
Library
pack 1 pack 2 --------------- pack n
module 1 module 2 module n
function 1 function 2 function n variables classes
```

**1**

```

```

**File Handling**

**As the part of programming requirement, we have to store our data permanently for**

**future purpose. For this requirement we should go for files.**

**Files are very common permanent storage areas to store our data.**

**Types of Files:**

**There are 2 types of files**

**1. Text Files:**

**Usually we can use text files to store character data
 eg: abc.txt**

**2. Binary Files:**

**Usually we can use binary files to store binary data like images,video files, audio files etc...**

**Opening a File:**

**Before performing any operation (like read or write) on the file,first we have to open that**

**file.For this we should use Python's inbuilt function open()**

**But at the time of open, we have to specify mode,which represents the purpose of**

**opening file.**

**f = open(filename, mode)**

**The allowed modes in Python are**

**1. r**  **open an existing file for read operation. The file pointer is positioned at the**

**beginning of the file.If the specified file does not exist then we will get**

**FileNotFoundError.This is default mode.**

**2**

```

```

**2. w**  **open an existing file for write operation. If the file already contains some data
 then it will be overridden. If the specified file is not already avaialble then this mode will**

**create that file.**

**3. a**  **open an existing file for append operation. It won't override existing data.If the**

**specified file is not already avaialble then this mode will create a new file.**

**4. r+**  **To read and write data into the file. The previous data in the file will not be**

**deleted.The file pointer is placed at the beginning of the file.**

**5. w+**  **To write and read data. It will override existing data.

1. a+**  **To append and read data from the file.It wont override existing data.
2. x**  **To open a file in exclusive creation mode for write operation. If the file already
    exists then we will get FileExistsError.**

**Note: All the above modes are applicable for text files. If the above modes suffixed with
 'b' then these represents for binary files.**

**Eg: rb,wb,ab,r+b,w+b,a+b,xb**

**f = open("abc.txt","w")**

**We are opening abc.txt file for writing data.**

**Closing a File:**

**After completing our operations on the file,it is highly recommended to close the file.
 For this we have to use close() function.**

**f.close()**

**Various properties of File Object:**

**Once we opend a file and we got file object,we can get various details related to that file**

**by using its properties.**

**name**  **Name of opened file**

**mode**  **Mode in which the file is opened
 closed**  **Returns boolean value indicates that file is closed or not**

**readable()**  **Retruns boolean value indicates that whether file is readable or not
 writable()**  **Returns boolean value indicates that whether file is writable or not.**

**3**

```

```

**Eg:**

```
 f=open("abc.txt",'w')
print("File Name: ",f.name)
print("File Mode: ",f.mode)
print("Is File Readable: ",f.readable())
print("Is File Writable: ",f.writable())
print("Is File Closed : ",f.closed)
f.close()
print("Is File Closed : ",f.closed)
9 )
10 )
1 Output
1D:\Python_classes>py test.py
1File Name: abc.txt
1File Mode: w
1Is File Readable: False
1Is File Writable: True
1Is File Closed : False
1Is File Closed : True
```

**Writing data to text files:**

**We can write character data to the text files by using the following 2 methods.**

**write(str)
 writelines(list of lines)**

**Eg:**

```
 f=open("abcd.txt",'w')
f.write("Durga\n")
f.write("Software\n")
f.write("Solutions\n")
print("Data written to the file successfully")
f.close()
```

**abcd.txt:**

**Durga
 Software**

**Solutions**

**Note: In the above program, data present in the file will be overridden everytime if we**

**run the program. Instead of overriding if we want append operation then we should open**

**the file as follows.**

**f = open("abcd.txt","a")**

**4**

```

```

**Eg 2 :**

```
 f=open("abcd.txt",'w')
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()
```

**abcd.txt:**

**sunny
 bunny**

**vinny
 chinny**

**Note: while writing data by using write() methods, compulsory we have to provide line**

**seperator(\n),otherwise total data should be written to a single line.**

**Reading Character Data from text files:**

**We can read character data from text file by using the following read methods.**

**read()**  **To read total data from the file
 read(n)**  **To read 'n' characters from the file**

**readline()**  **To read only one line**

**readlines()**  **To read all lines into a list**

**Eg 1 : To read total data from the file**

```
 f=open("abc.txt",'r')
data=f.read()
print(data)
f.close()
5 )
Output
sunny
bunny
chinny
vinny
```

**Eg 2 : To read only first 10 characters:**

```
 f=open("abc.txt",'r')
data=f.read( 10 )
print(data)
f.close()
5 )
```

**5**

```

Output
sunny
bunn
```

**Eg 3: To read data line by line:**

```
 f=open("abc.txt",'r')
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close()
9 )
Output
1 sunny
1bunny
1chinny
```

**Eg 4: To read all lines into list:**

```
 f=open("abc.txt",'r')
lines=f.readlines()
for line in lines:
print(line,end='')
f.close()
6 )
Output
sunny
bunny
chinny
1 vinny
```

**Eg 5:**

```
 f=open("abc.txt","r")
print(f.read( 3 ))
print(f.readline())
print(f.read( 4 ))
print("Remaining data")
print(f.read())
7 )
Output
sun
ny
1
1bunn
1Remaining data
```

**6**

```

1y
1chinny
1vinny
```

**The with statement:**

**The with statement can be used while opening a file.We can use this to group file**

**operation statements within a block.
 The advantage of with statement is it will take care closing of file,after completing all**

**operations automatically even in the case of exceptions also, and we are not required to**

**close explicitly.
 Eg:**

```
 with open("abc.txt","w") as f:
f.write("Durga\n")
f.write("Software\n")
f.write("Solutions\n")
print("Is File Closed: ",f.closed)
print("Is File Closed: ",f.closed)
7 )
Output
Is File Closed: False
Is File Closed: True
```

**The seek() and tell() methods:**

**tell():**

**==>We can use tell() method to return current position of the cursor(file pointer) from
 beginning of the file. [ can you plese telll current cursor position]**

**The position(index) of first character in files is zero just like string index.**

**Eg:**

```
 f=open("abc.txt","r")
print(f.tell())
print(f.read( 2 ))
print(f.tell())
print(f.read( 3 ))
print(f.tell())
```

**abc.txt:**

**sunny
 bunny**

**chinny**

**vinny**

**7**

```

```

**Output:**

**0
 su**

**2**

**nny
 5**

**seek():**

**We can use seek() method to move cursor(file pointer) to specified location.
 [Can you please seek the cursor to a particular location]**

**f.seek(offset, fromwhere)**

**offset represents the number of positions**

**The allowed values for second attribute(from where) are**

**0 ---->From beginning of file(default value)**

**1 ---->From current position
 2 --->From end of the file**

**Note: Python 2 supports all 3 values but Python 3 supports only zero.**

**Eg:**

```
 data="All Students are STUPIDS"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+") as f:
text=f.read()
print(text)
print("The Current Cursor Position: ",f.tell())
f.seek( 17 )
print("The Current Cursor Position: ",f.tell())
f.write("GEMS!!!")
1 f.seek( 0 )
1text=f.read()
1print("Data After Modification:")
1print(text)
15 )
1Output
17 )
1All Students are STUPIDS
1The Current Cursor Position: 24
20 ) The Current Cursor Position: 17
2 Data After Modification:
```

**8**

```

2All Students are GEMS!!!
```

**How to check a particular file exists or not?**

**We can use os library to get information about files in our computer.
 os module has path sub module,which contains isFile() function to check whether a**

**particular file exists or not?**

**os.path.isfile(fname)**

**Q. Write a program to check whether the given file exists or not. If it is**

**available then print its content?**

```
 import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
print("File exists:",fname)
f=open(fname,"r")
else:
print("File does not exist:",fname)
sys.exit( 0 )
print("The content of file is:")
data=f.read()
1 print(data)
12 )
1Output
1D:\Python_classes>py test.py
1Enter File Name: durga.txt
1File does not exist: durga.txt
17 )
1D:\Python_classes>py test.py
1Enter File Name: abc.txt
20 ) File exists: abc.txt
2 The content of file is:
2All Students are GEMS!!!
2All Students are GEMS!!!
2All Students are GEMS!!!
2All Students are GEMS!!!
2All Students are GEMS!!!
2All Students are GEMS!!!
```

**Note:**

**sys.exit(0) ===>To exit system without executing rest of the program.**

**argument represents status code. 0 means normal termination and it is the default value.**

**9**

```

```

**Q. Program to print the number of lines,words and characters present in the**

**given file?**

```
 import os,sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
print("File exists:",fname)
f=open(fname,"r")
else:
print("File does not exist:",fname)
sys.exit( 0 )
lcount=wcount=ccount= 0
for line in f:
1 lcount=lcount+ 1
1ccount=ccount+len(line)
1words=line.split()
1wcount=wcount+len(words)
1print("The number of Lines:",lcount)
1print("The number of Words:",wcount)
1print("The number of Characters:",ccount)
18 )
1Output
20 ) D:\Python_classes>py test.py
2 Enter File Name: durga.txt
2File does not exist: durga.txt
23 )
2D:\Python_classes>py test.py
2Enter File Name: abc.txt
2File exists: abc.txt
2The number of Lines: 6
2The number of Words: 24
2The number of Characters: 149
```

**abc.txt:**

**All Students are GEMS!!!**

**All Students are GEMS!!!
 All Students are GEMS!!!**

**All Students are GEMS!!!**

**All Students are GEMS!!!
 All Students are GEMS!!!**

**10**

```

```

**Handling Binary Data:**

**It is very common requirement to read or write binary data like images,video files,audio**

**files etc.**

**Q. Program to read image file and write to a new image file?**

```
 f1=open("rossum.jpg","rb")
f2=open("newpic.jpg","wb")
bytes=f1.read()
f2.write(bytes)
print("New Image is available with the name: newpic.jpg")
```

**Handling csv files:**

**CSV==>Comma seperated values**

**As the part of programming,it is very common requirement to write and read data wrt csv
 files. Python provides csv module to handle csv files.**

**Writing data to csv file:**

```
 import csv
with open("emp.csv","w",newline='') as f:
w=csv.writer(f) # returns csv writer object
w.writerow(["ENO","ENAME","ESAL","EADDR"])
n=int(input("Enter Number of Employees:"))
for i in range(n):
eno=input("Enter Employee No:")
ename=input("Enter Employee Name:")
esal=input("Enter Employee Salary:")
eaddr=input("Enter Employee Address:")
1 w.writerow([eno,ename,esal,eaddr])
1print("Total Employees data written to csv file successfully")
```

**Note: Observe the difference with newline attribute and without**

**with open("emp.csv","w",newline='') as f:
 with open("emp.csv","w") as f:**

**Note: If we are not using newline attribute then in the csv file blank lines will be included**

**between data. To prevent these blank lines, newline attribute is required in Python-3,but
 in Python-2 just we can specify mode as 'wb' and we are not required to use newline**

**attribute.**

**11**

```

```

**Reading Data from csv file:**

```
 import csv
f=open("emp.csv",'r')
r=csv.reader(f) #returns csv reader object
data=list(r)
#print(data)
for line in data:
for word in line:
print(word,"\t",end='')
print()
10 )
1 Output
1D:\Python_classes>py test.py
1ENO ENAME ESAL EADDR
1100 Durga 1000 Hyd
1200 Sachin 2000 Mumbai
1300 Dhoni 3000 Ranchi
```

**Zipping and Unzipping Files:**

**It is very common requirement to zip and unzip files.**

**The main advantages are:**

**1. To improve memory utilization

1. We can reduce transport time
2. We can improve performance.**

**To perform zip and unzip operations, Python contains one in-bulit module zip file.**

**This module contains a class : ZipFile**

**To create Zip file:**

**We have to create ZipFile class object with name of the zip file,mode and constant
 ZIP_DEFLATED. This constant represents we are creating zip file.**

**f = ZipFile("files.zip","w","ZIP_DEFLATED")**

**Once we create ZipFile object,we can add files by using write() method.**

**f.write(filename)**

**12**

```

```

**Eg:**

```
 from zipfile import *
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("file1.txt")
f.write("file2.txt")
f.write("file3.txt")
f.close()
print("files.zip file created successfully")
```

**To perform unzip operation:**

**We have to create ZipFile object as follows**

**f = ZipFile("files.zip","r",ZIP_STORED)**

**ZIP_STORED represents unzip operation. This is default value and hence we are not**

**required to specify.
 Once we created ZipFile object for unzip operation,we can get all file names present in**

**that zip file by using namelist() method.**

**names = f.namelist()**

**Eg:**

```
 from zipfile import *
f=ZipFile("files.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
print( "File Name: ",name)
print("The Content of this file is:")
f1=open(name,'r')
print(f1.read())
print()
```

**Working with Directories:**

**It is very common requirement to perform operations for directories like**

**1. To know current working directory

1. To create a new directory
2. To remove an existing directory
3. To rename a directory
4. To list contents of the directory**

**etc...**

**13**

```

```

**To perform these operations,Python provides inbuilt module os,which contains several
 functions to perform directory related operations.**

**Q1. To Know Current Working Directory:**

**import os**

**cwd=os.getcwd()**

**print("Current Working Directory:",cwd)**

**Q2. To create a sub directory in the current working directory:**

**import os
 os.mkdir("mysub")**

**print("mysub directory created in cwd")**

**Q3. To create a sub directory in mysub directory:**

**cwd**

**|-mysub**

**|-mysub2**

**import os**

**os.mkdir("mysub/mysub2")
 print("mysub2 created inside mysub")**

**Note: Assume mysub already present in cwd.**

**Q4. To create multiple directories like sub1 in that sub2 in that sub3:**

**import os**

**os.makedirs("sub1/sub2/sub3")
 print("sub1 and in that sub2 and in that sub3 directories created")**

**Q5. To remove a directory:**

**import os**

**os.rmdir("mysub/mysub2")**

**print("mysub2 directory deleted")**

**Q6. To remove multiple directories in the path:**

**import os**

**os.removedirs("sub1/sub2/sub3")
 print("All 3 directories sub1,sub2 and sub3 removed")**

**14**

```

```

**Q7. To rename a directory:**

**import os**

**os.rename("mysub","newdir")**

**print("mysub directory renamed to newdir")**

**Q8. To know contents of directory:**

**os module provides listdir() to list out the contents of the specified directory. It won't
 display the contents of sub directory.**

**Eg:**

```
 import os
print(os.listdir("."))
3 )
Output
D:\Python_classes>py test.py
['abc.py', 'abc.txt', 'abcd.txt', 'com', 'demo.py', 'durgamath.py', 'emp.csv', '
file1.txt', 'file2.txt', 'file3.txt', 'files.zip', 'log.txt', 'module1.py', 'myl
og.txt', 'newdir', 'newpic.jpg', 'pack1', 'rossum.jpg', 'test.py', '__pycache__'
]
```

**The above program display contents of current working directory but not contents of sub**

**directories.**

**If we want the contents of a directory including sub directories then we should go for**

**walk() function.**

**Q9. To know contents of directory including sub directories:**

**We have to use walk() function
 [Can you please walk in the directory so that we can aware all contents of that directory]**

**os.walk(path,topdown=True,onerror=None,followlinks=False)**

**It returns an Iterator object whose contents can be displayed by using for loop**

**path-->Directory path. cwd means.**

**topdown=True --->Travel from top to bottom**

**onerror=None --->on error detected which function has to execute.
 followlinks=True -->To visit directories pointed by symbolic links**

**15**

```

```

**Eg: To display all contents of Current working directory including sub directories:**

```
 import os
for dirpath,dirnames,filenames in os.walk('.'):
print("Current Directory Path:",dirpath)
print("Directories:",dirnames)
print("Files:",filenames)
print()
7 )
8 )
Output
Current Directory Path:.
1 Directories: ['com', 'newdir', 'pack1', '__pycache__']
1Files: ['abc.txt', 'abcd.txt', 'demo.py', 'durgamath.py', 'emp.csv', 'file1.txt'
1, 'file2.txt', 'file3.txt', 'files.zip', 'log.txt', 'module1.py', 'mylog.txt', '
1newpic.jpg', 'rossum.jpg', 'test.py']
15 )
1Current Directory Path: .\com
1Directories: ['durgasoft', '__pycache__']
1Files: ['module1.py', '__init__.py']
19 )
20 ) ...
```

**Note: To display contents of particular directory,we have to provide that directory name**

**as argument to walk() function.**

**os.walk("directoryname")**

**Q. What is the difference between listdir() and walk() functions?**

**In the case of listdir(), we will get contents of specified directory but not sub directory**

**contents. But in the case of walk() function we will get contents of specified directory and**

**its sub directories also.**

**Running Other programs from Python program:**

**os module contains system() function to run programs and commands.**

**It is exactly same as system() function in C language.**

**os.system("commad string")
 The argument is any command which is executing from DOS.**

**Eg:**

**import os**

**os.system("dir \*.py")
 os.system("py abc.py")**

**16**

```

```

**How to get information about a File:**

**We can get statistics of a file like size, last accessed time,last modified time etc by using**

**stat() function of os module.**

**stats = os.stat("abc.txt")**

**The statistics of a file includes the following parameters:**

**st_mode==>Protection Bits**

**st_ino==>Inode number
 st_dev===>device**

**st_nlink===>no of hard links**

**st_uid===>userid of owner
 st_gid==>group id of owner**

**st_size===>size of file in bytes
 st_atime==>Time of most recent access**

**st_mtime==>Time of Most recent modification**

**st_ctime==> Time of Most recent meta data change**

**Note:**

**st_atime, st_mtime and st_ctime returns the time as number of milli seconds since Jan 1st**

**1970 ,12:00AM. By using datetime module fromtimestamp() function,we can get exact**

**date and time.**

**Q. To print all statistics of file abc.txt:**

```
 import os
stats=os.stat("abc.txt")
print(stats)
4 )
Output
os.stat_result(st_mode= 33206 , st_ino= 844424930132788 , st_dev= 2657980798 , st_nlin
k= 1 , st_uid= 0 , st_gid= 0 , st_size= 22410 , st_atime= 1505451446 , st_mtime= 1505538999
, st_ctime= 1505451446 )
```

**Q. To print specified properties:**

```
 import os
from datetime import *
stats=os.stat("abc.txt")
print("File Size in Bytes:",stats.st_size)
print("File Last Accessed Time:",datetime.fromtimestamp(stats.st_atime))
print("File Last Modified Time:",datetime.fromtimestamp(stats.st_mtime))
7 )
```

**17**

```

Output
File Size in Bytes: 22410
File Last Accessed Time: 2017 - 09 - 15 10 : 27 :26.599490
1 File Last Modified Time: 2017 - 09 - 16 10 : 46 :39.245394
```

**Pickling and Unpickling of Objects:**

**Sometimes we have to write total state of object to the file and we have to read total**

**object from the file.**

**The process of writing state of object to the file is called pickling and the process of**

**reading state of an object from the file is called unpickling.**

**We can implement pickling and unpickling by using pickle module of Python.**

**pickle module contains dump() function to perform pickling.**

```
pickle.dump(object,file)
```

**pickle module contains load() function to perform unpickling**

```
obj=pickle.load(file)
e2
eno: 100
ename: Durga
esal: 10000
eaddr: HYD
abc.txt
pickle.dump
(e1, f)
pickling
pickle load (f)
unpickling
eno: 100
ename: Durga
esal: 10000
eaddr: HYD
eno: 100
ename: Durga
esal: 10000
eaddr: HYD
e1
```

**18**

```

```

**Writing and Reading State of object by using pickle Module:**

```
 import pickle
class Employee:
def __init__(self,eno,ename,esal,eaddr):
self.eno=eno;
self.ename=ename;
self.esal=esal;
self.eaddr=eaddr;
def display(self):
print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
with open("emp.dat","wb") as f:
1 e=Employee( 100 ,"Durga", 1000 ,"Hyd")
1pickle.dump(e,f)
1print("Pickling of Employee Object completed...")
14 )
1with open("emp.dat","rb") as f:
1obj=pickle.load(f)
1print("Printing Employee Information after unpickling")
1obj.display()
```

**Writing Multiple Employee Objects to the file:**

**emp.py:**

```
 class Employee:
def __init__(self,eno,ename,esal,eaddr):
self.eno=eno;
self.ename=ename;
self.esal=esal;
self.eaddr=eaddr;
def display(self):
8 )
print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
```

**pick.py:**

```
 import emp,pickle
f=open("emp.dat","wb")
n=int(input("Enter The number of Employees:"))
for i in range(n):
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
esal=float(input("Enter Employee Salary:"))
eaddr=input("Enter Employee Address:")
e=emp.Employee(eno,ename,esal,eaddr)
pickle.dump(e,f)
1 print("Employee Objects pickled successfully")
```

**19**

```

```

**unpick.py:**

```
 import emp,pickle
f=open("emp.dat","rb")
print("Employee Details:")
while True:
try:
obj=pickle.load(f)
obj.display()
except EOFError:
print("All employees Completed")
break
1 f.close()
```

**1**

```

```

**Exception Handling**

**In any programming language there are 2 types of errors are possible.**

**1. Syntax Errors

1. Runtime Errors
2. Syntax Errors:**

**The errors which occurs because of invalid syntax are called syntax errors.**

**Eg 1 :**

**x=10
 if x==10**

**print("Hello")**

**SyntaxError: invalid syntax**

**Eg 2 :**

**print "Hello"**

**SyntaxError: Missing parentheses in call to 'print'**

**Note:**

**Programmer is responsible to correct these syntax errors. Once all syntax errors are
 corrected then only program execution will be started.**

**2. Runtime Errors:**

**Also known as exceptions.
 While executing the program if something goes wrong because of end user input or**

**programming logic or memory problems etc then we will get Runtime Errors.**

**Eg: print(10/0) ==>ZeroDivisionError: division by zero**

**print(10/"ten") ==>TypeError: unsupported operand type(s) for /: 'int' and 'str'**

**x=int(input("Enter Number:"))
 print(x)**

**D:\Python_classes>py test.py**

**2**

```

```

**Enter Number:ten
 ValueError: invalid literal for int() with base 10: 'ten'**

**Note: Exception Handling concept applicable for Runtime Errors but not for syntax errors**

**What is Exception:**

**An unwanted and unexpected event that disturbs normal flow of program is called**

**exception.**

**Eg:**

**ZeroDivisionError
 TypeError**

**ValueError**

**FileNotFoundError
 EOFError**

**SleepingError**

**TyrePuncturedError**

**It is highly recommended to handle exceptions. The main objective of exception handling**

**is Graceful Termination of the program(i.e we should not block our resources and we
 should not miss anything)**

**Exception handling does not mean repairing exception. We have to define alternative way
 to continue rest of the program normally.**

**Eg:**

**For example our programming requirement is reading data from remote file locating at
 London. At runtime if london file is not available then the program should not be**

**terminated abnormally. We have to provide local file to continue rest of the program**

**normally. This way of defining alternative is nothing but exception handling.**

**try:**

**read data from remote file locating at london**

**except FileNotFoundError:
 use local file and continue rest of the program normally**

**Q. What is an Exception?
 Q. What is the purpose of Exception Handling?**

**Q. What is the meaning of Exception Handling?**

**3**

```

```

**Default Exception Handing in Python:**

**Every exception in Python is an object. For every exception type the corresponding classes
 are available.**

**Whevever an exception occurs PVM will create the corresponding exception object and
 will check for handling code. If handling code is not available then Python interpreter**

**terminates the program abnormally and prints corresponding exception information to**

**the console.
 The rest of the program won't be executed.**

**Eg:**

```
 print("Hello")
print( 10 / 0 )
print("Hi")
4 )
D:\Python_classes>py test.py
Hello
Traceback (most recent call last):
File "test.py", line 2 , in <module>
print( 10 / 0 )
ZeroDivisionError: division by zero
```

**4**

```

```

**Python's Exception Hierarchy**

```
Every Exception in Python is a class.
All exception classes are child classes of BaseException.i.e every exception class extends
BaseException either directly or indirectly. Hence BaseException acts as root for Python
Exception Hierarchy.
Most of the times being a programmer we have to concentrate Exception and its child
classes.
```

**Customized Exception Handling by using try-except:**

```
It is highly recommended to handle exceptions.
The code which may raise exception is called risky code and we have to take risky code
inside try block. The corresponding handling code we have to take inside except block.
```

**Attribute**

**Error**

```
Arithmetic
Error
EOF
Error
Name
Error
Lookup
Error
OS
Error
Type
Error
Value
Error
BaseException
Exception SystemExit GeneratorExit^ KeyboardInterrupt
ZeroDivision
Error
FloatingPoint
Error
Overflow
Error
Index
Error
Key
Error
FileNotFound
Error
Interrupted
Error
Permission
Error
TimeOut
Error
```

**5**

```

```

**try:**

**Risky Code
 except XXX:**

**Handling code/Alternative Code**

**without try-except:**

```
1. print("stmt-1")
2. print( 10 / 0 )
3. print("stmt-3")
4.
5. Output
6. stmt- 1
7. ZeroDivisionError: division by zero
```

**Abnormal termination/Non-Graceful Termination**

**with try-except:**

```
1. print("stmt-1")
2. try:
3. print( 10 / 0 )
4. except ZeroDivisionError:
5. print( 10 / 2 )
6. print("stmt-3")
7.
8. Output
9. stmt- 1
10. 5.0
11. stmt- 3
```

**Normal termination/Graceful Termination**

**Control Flow in try-except:**

**try:**

**stmt- 1
 stmt- 2**

**stmt- 3**

**except XXX:
 stmt- 4**

**stmt- 5**

**case-1: If there is no exception**

**1,2,3,5 and Normal Termination**

**6**

```

```

**case-2: If an exception raised at stmt-2 and corresponding except block matched
 1,4,5 Normal Termination**

**case-3: If an exception raised at stmt-2 and corresponding except block not matched
 1, Abnormal Termination**

**case-4: If an exception raised at stmt-4 or at stmt-5 then it is always abnormal
 termination.**

**Conclusions:**

**1. within the try block if anywhere exception raised then rest of the try block wont be
 executed eventhough we handled that exception. Hence we have to take only risky code**

**inside try block and length of the try block should be as less as possible.**

**2. In addition to try block,there may be a chance of raising exceptions inside except and**

**finally blocks also.**

**3. If any statement which is not part of try block raises an exception then it is always**

**abnormal termination.**

**How to print exception information:**

**try:**

```
1. print( 10 / 0 )
2. except ZeroDivisionError as msg:
3. print("exception raised and its description is:",msg)
4.
5. Output exception raised and its description is: division by zero
```

**try with multiple except blocks:**

**The way of handling exception is varied from exception to exception.Hence for every**

**exception type a seperate except block we have to provide. i.e try with multiple except
 blocks is possible and recommended to use.**

**Eg:**

**try:**

**-------
 -------**

**-------**

**except ZeroDivisionError:
 perform alternative**

**arithmetic operations**

**7**

```

```

**except FileNotFoundError:
 use local file instead of remote file**

**If try with multiple except blocks available then based on raised exception the
 corresponding except block will be executed.**

**Eg:**

```
 try:
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(x/y)
except ZeroDivisionError :
print("Can't Divide with Zero")
except ValueError:
print("please provide int value only")
9 )
D:\Python_classes>py test.py
1 Enter First Number: 10
1Enter Second Number: 2
15.0
14 )
1D:\Python_classes>py test.py
1Enter First Number: 10
1Enter Second Number: 0
1Can't Divide with Zero
19 )
20 ) D:\Python_classes>py test.py
2 Enter First Number: 10
2Enter Second Number: ten
2please provide int value only
```

**If try with multiple except blocks available then the order of these except blocks is**

**important .Python interpreter will always consider from top to bottom until matched
 except block identified.**

**Eg:**

```
 try:
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(x/y)
except ArithmeticError :
print("ArithmeticError")
except ZeroDivisionError:
print("ZeroDivisionError")
9 )
D:\Python_classes>py test.py
```

**8**

```

1 Enter First Number: 10
1Enter Second Number: 0
1ArithmeticError
```

**Single except block that can handle multiple exceptions:**

**We can write a single except block that can handle multiple different types of exceptions.**

**except (Exception1,Exception2,exception3,..): or**

**except (Exception1,Exception2,exception3,..) as msg :**

**Parenthesis are mandatory and this group of exceptions internally considered as tuple.**

**Eg:**

```
 try:
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(x/y)
except (ZeroDivisionError,ValueError) as msg:
print("Plz Provide valid numbers only and problem is: ",msg)
7 )
D:\Python_classes>py test.py
Enter First Number: 10
Enter Second Number: 0
1 Plz Provide valid numbers only and problem is: division by zero
12 )
1D:\Python_classes>py test.py
1Enter First Number: 10
1Enter Second Number: ten
1Plz Provide valid numbers only and problem is: invalid literal for int() with b
1ase 10 : 'ten'
```

**Default except block:**

**We can use default except block to handle any type of exceptions.**

**In default except block generally we can print normal error messages.**

**Syntax:**

**except:**

**statements
 Eg:**

```
 try:
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(x/y)
```

**9**

```

except ZeroDivisionError:
print("ZeroDivisionError:Can't divide with zero")
except:
print("Default Except:Plz provide valid input only")
9 )
D:\Python_classes>py test.py
1 Enter First Number: 10
1Enter Second Number: 0
1ZeroDivisionError:Can't divide with zero
14 )
1D:\Python_classes>py test.py
1Enter First Number: 10
1Enter Second Number: ten
1Default Except:Plz provide valid input only
```

*****Note: If try with multiple except blocks available then default except block should be**

**last,otherwise we will get SyntaxError.**

**Eg:**

```
 try:
print( 10 / 0 )
except:
print("Default Except")
except ZeroDivisionError:
print("ZeroDivisionError")
7 )
SyntaxError: default 'except:' must be last
```

**Note:**

**The following are various possible combinations of except blocks**

**1. except ZeroDivisionError:

1. except ZeroDivisionError as msg:
2. except (ZeroDivisionError,ValueError) :
3. except (ZeroDivisionError,ValueError) as msg:
4. except :**

**finally block:**

**1. It is not recommended to maintain clean up code(Resource Deallocating Code or**

**Resource Releasing code) inside try block because there is no guarentee for the execution
 of every statement inside try block always.**

**2. It is not recommended to maintain clean up code inside except block, because if there
 is no exception then except block won't be executed.**

**10**

```

```

**Hence we required some place to maintain clean up code which should be executed
 always irrespective of whether exception raised or not raised and whether exception**

**handled or not handled. Such type of best place is nothing but finally block.**

**Hence the main purpose of finally block is to maintain clean up code.**

**try:
 Risky Code**

**except:
 Handling Code**

**finally:**

**Cleanup code**

**The speciality of finally block is it will be executed always whether exception raised or not**

**raised and whether exception handled or not handled.**

**Case-1: If there is no exception**

```
 try:
print("try")
except:
print("except")
finally:
print("finally")
7 )
Output
try
finally
```

**Case-2: If there is an exception raised but handled:**

```
 try:
print("try")
print( 10 / 0 )
except ZeroDivisionError:
print("except")
finally:
print("finally")
8 )
Output
try
1 except
1finally
```

**11**

```

```

**Case-3: If there is an exception raised but not handled:**

```
 try:
print("try")
print( 10 / 0 )
except NameError:
print("except")
finally:
print("finally")
8 )
Output
try
1 finally
1ZeroDivisionError: division by zero(Abnormal Termination)
```

***** Note: There is only one situation where finally block won't be executed ie whenever**

**we are using os._exit(0) function.**

**Whenever we are using os._exit(0) function then Python Virtual Machine itself will be**

**shutdown.In this particular case finally won't be executed.**

```
 imports
try:
print("try")
os._exit( 0 )
except NameError:
print("except")
finally:
print("finally")
9 )
Output
1 try
```

**Note:**

**os._exit(0)**

**where 0 represents status code and it indicates normal termination**

**There are multiple status codes are possible.**

**Control flow in try-except-finally:**

**try:**

**stmt- 1
 stmt- 2**

**stmt- 3**

**except:
 stmt- 4**

**12**

```

```

**finally:
 stmt- 5**

**stmt6**

**Case-1: If there is no exception**

**1,2,3,5,6 Normal Termination**

**Case-2: If an exception raised at stmt2 and the corresponding except block matched**

**1,4,5,6 Normal Termination**

**Case-3: If an exception raised at stmt2 but the corresponding except block not matched**

**1,5 Abnormal Termination**

**Case-4:If an exception raised at stmt4 then it is always abnormal termination but before**

**that finally block will be executed.**

**Case-5: If an exception raised at stmt-5 or at stmt-6 then it is always abnormal**

**termination**

**Nested try-except-finally blocks:**

**We can take try-except-finally blocks inside try or except or finally blocks.i.e nesting of try-**

**except-finally is possible.**

**try:**

**----------
 ----------**

**----------
 try:**

**-------------**

**--------------
 --------------**

**except:**

**--------------
 --------------**

**--------------**

**------------
 except:**

**-----------**

**-----------
 -----------**

**General Risky code we have to take inside outer try block and too much risky code we**

**have to take inside inner try block. Inside Inner try block if an exception raised then inner**

**13**

```

```

**except block is responsible to handle. If it is unable to handle then outer except block is
 responsible to handle.**

**Eg:**

```
 try:
print("outer try block")
try:
print("Inner try block")
print( 10 / 0 )
except ZeroDivisionError:
print("Inner except block")
finally:
print("Inner finally block")
except:
1 print("outer except block")
1finally:
1print("outer finally block")
14 )
1Output
1outer try block
1Inner try block
1Inner except block
1Inner finally block
20 ) outer finally block
```

**Control flow in nested try-except-finally:**

**try:**

**stmt- 1
 stmt- 2**

**stmt- 3**

**try:
 stmt- 4**

**stmt- 5**

**stmt- 6
 except X:**

**stmt- 7
 finally:**

**stmt- 8**

**stmt- 9
 except Y:**

**stmt- 10**

**finally:
 stmt- 11**

**stmt- 12**

**14**

```

```

**case-1: If there is no exception**

**1,2,3,4,5,6,8,9,11,12 Normal Termination**

**case-2: If an exception raised at stmt-2 and the corresponding except block matched**

**1,10,11,12 Normal Termination**

**case-3: If an exceptiion raised at stmt-2 and the corresponding except block not matched**

**1,11,Abnormal Termination**

**case-4: If an exception raised at stmt-5 and inner except block matched**

**1,2,3,4,7,8,9,11,12 Normal Termination**

**case-5: If an exception raised at stmt-5 and inner except block not matched but outer**

**except block matched**

**1,2,3,4,8,10,11,12,Normal Termination**

**case-6:If an exception raised at stmt-5 and both inner and outer except blocks are not**

**matched**

**1,2,3,4,8,11,Abnormal Termination**

**case-7: If an exception raised at stmt-7 and corresponding except block matched**

**1,2,3,.,.,.,8,10,11,12,Normal Termination**

**case-8: If an exception raised at stmt-7 and corresponding except block not matched**

**1,2,3,.,.,.,8,11,Abnormal Termination**

**case-9: If an exception raised at stmt-8 and corresponding except block matched**

**1,2,3,.,.,.,.,10,11,12 Normal Termination**

**case-10: If an exception raised at stmt-8 and corresponding except block not matched**

**1,2,3,.,.,.,.,11,Abnormal Termination**

**case-11: If an exception raised at stmt-9 and corresponding except block matched**

**1,2,3,.,.,.,.,8,10,11,12,Normal Termination**

**case-12: If an exception raised at stmt-9 and corresponding except block not matched**

**1,2,3,.,.,.,.,8,11,Abnormal Termination**

**case-13: If an exception raised at stmt-10 then it is always abonormal termination but**

**before abnormal termination finally block(stmt-11) will be executed.**

**15**

```

```

**case-14: If an exception raised at stmt-11 or stmt-12 then it is always abnormal**

**termination.**

**Note: If the control entered into try block then compulsary finally block will be executed.**

**If the control not entered into try block then finally block won't be executed.**

**else block with try-except-finally:**

**We can use else block with try-except-finally blocks.
 else block will be executed if and only if there are no exceptions inside try block.**

**try:
 Risky Code**

**except:**

**will be executed if exception inside try
 else:**

**will be executed if there is no exception inside try
 finally:**

**will be executed whether exception raised or not raised and handled or not**

**handled**

**Eg:**

**try:**

**print("try")**

**print(10/0)---> 1
 except:**

**print("except")**

**else:
 print("else")**

**finally:**

**print("finally")**

**If we comment line-1 then else block will be executed b'z there is no exception inside try.
 In this case the output is:**

**try
 else**

**finally**

**If we are not commenting line-1 then else block won't be executed b'z there is exception**

**inside try block. In this case output is:**

**16**

```

```

**try
 except**

**finally**

**Various possible combinations of try-except-else-finally:**

**1. Whenever we are writing try block, compulsory we should write except or finally**

**block.i.e without except or finally block we cannot write try block.**

**2. Wheneever we are writing except block, compulsory we should write try block. i.e**

**except without try is always invalid.**

**3. Whenever we are writing finally block, compulsory we should write try block. i.e finally**

**without try is always invalid.**

**4. We can write multiple except blocks for the same try,but we cannot write multiple**

**finally blocks for the same try**

**5. Whenever we are writing else block compulsory except block should be there. i.e**

**without except we cannot write else block.**

**6. In try-except-else-finally order is important.

1. We can define try-except-else-finally inside try,except,else and finally blocks. i.e nesting
    of try-except-else-finally is always possible.**

```
1
try:
print("try") ^
2
except:
print("Hello") ^
3
else:
print("Hello") ^
4
finally:
print("Hello") ^
5
try:
print("try")
except:
print("except")
```

√

```
6
try:
print("try")
finally:
print("finally")
```

√

```
7
try:
print("try") √^
```

**17**

```

except:
print("except")
else:
print("else")
8
try:
print("try")
else:
print("else")
```



```
9
try:
print("try")
else:
print("else")
finally:
print("finally")
```



```
10
try:
print("try")
except XXX:
print("except-1")
except YYY:
print("except-2")
```

√

```
11
try:
print("try")
except :
print("except-1")
else:
print("else")
else:
print("else")
```



```
12
try:
print("try")
except :
print("except-1")
finally:
print("finally")
finally:
print("finally")
```



```
13
try:
print("try")
print("Hello")
except:
print("except")
```



```
14
try:
print("try")
except:
```



**18**

```

print("except")
print("Hello")
except:
print("except")
15
try:
print("try")
except:
print("except")
print("Hello")
finally:
print("finally")
```



```
16
try:
print("try")
except:
print("except")
print("Hello")
else:
print("else")
```



```
17
try:
print("try")
except:
print("except")
try:
print("try")
except:
print("except")
```

√

```
18
try:
print("try")
except:
print("except")
try:
print("try")
finally:
print("finally")
```

√

```
19
try:
print("try")
except:
print("except")
if 10>20:
print("if")
else:
print("else")
```



```
20
try:
print("try") √^
```

**19**

```

try:
print("inner try")
except:
print("inner except block")
finally:
print("inner finally block")
except:
print("except")
21
try:
print("try")
except:
print("except")
try:
print("inner try")
except:
print("inner except block")
finally:
print("inner finally block")
```

√

```
22
try:
print("try")
except:
print("except")
finally:
try:
print("inner try")
except:
print("inner except block")
finally:
print("inner finally block")
```

√

```
23
try:
print("try")
except:
print("except")
try:
print("try")
else:
print("else")
```



```
24
try:
print("try")
try:
print("inner try")
except:
print("except")
```



**20**

```

```

**Types of Exceptions:**

**In Python there are 2 types of exceptions are possible.**

**1. Predefined Exceptions

1. User Definded Exceptions
2. Predefined Exceptions:**

**Also known as in-built exceptions**

**The exceptions which are raised automatically by Python virtual machine whenver a**

**particular event occurs, are called pre defined exceptions.**

**Eg 1: Whenever we are trying to perform Division by zero, automatically Python will raise**

**ZeroDivisionError.**

**print(10/0)**

**Eg 2: Whenever we are trying to convert input value to int type and if input value is not
 int value then Python will raise ValueError automatically**

**x=int("ten")===>ValueError**

**2. User Defined Exceptions:**

**Also known as Customized Exceptions or Programatic Exceptions**

**Some time we have to define and raise exceptions explicitly to indicate that something**

**goes wrong ,such type of exceptions are called User Defined Exceptions or Customized
 Exceptions**

**Programmer is responsible to define these exceptions and Python not having any idea
 about these. Hence we have to raise explicitly based on our requirement by using "raise"**

**keyword.**

```
25
try:
print("try")
else:
print("else")
except:
print("except")
finally:
print("finally")
```



**21**

```

```

**Eg:
 InSufficientFundsException**

**InvalidInputException**

**TooYoungException
 TooOldException**

**How to Define and Raise Customized Exceptions:**

**Every exception in Python is a class that extends Exception class either directly or**

**indirectly.**

**Syntax:**

**class classname(predefined exception class name):**

**def \**init\**(self,arg):
 self.msg=arg**

**Eg:**

```
 class TooYoungException(Exception):
def __init__(self,arg):
self.msg=arg
```

**TooYoungException is our class name which is the child class of Exception**

**We can raise exception by using raise keyword as follows
 raise TooYoungException("message")**

**Eg:**

```
 class TooYoungException(Exception):
def __init__(self,arg):
self.msg=arg
4 )
class TooOldException(Exception):
def __init__(self,arg):
self.msg=arg
8 )
age=int(input("Enter Age:"))
if age> 60 :
1 raise TooYoungException("Plz wait some more time you will get best match soon!!!")
1elif age< 18 :
1raise TooOldException("Your age already crossed marriage age...no chance of getting ma
rriage")
1else:
1print("You will get match details soon by email!!!")
16 )
1D:\Python_classes>py test.py
```

**22**

```

1Enter Age: 90
1__main__.TooYoungException: Plz wait some more time you will get best match soon!!!
20 )
2 D:\Python_classes>py test.py
2Enter Age: 12
2__main__.TooOldException: Your age already crossed marriage age...no chance of g
2etting marriage
25 )
2D:\Python_classes>py test.py
2Enter Age: 27
2You will get match details soon by email!!!
```

**Note:**

**raise keyword is best suitable for customized exceptions but not for pre defined**

**exceptions**

**23**

```

```

**PYTHON LOGGING**

**Logging the Exceptions:**

**It is highly recommended to store complete application flow and exceptions information**

**to a file. This process is called logging.**

**The main advantages of logging are:**

**1. We can use log files while performing debugging

1. We can provide statistics like number of requests per day etc**

**To implement logging, Python provides one inbuilt module logging.**

**logging levels:**

**Depending on type of information, logging data is divided according to the following 6**

**levels in Python.
 table**

**1. CRITICAL==>50==>Represents a very serious problem that needs high attention

1. ERROR===>40===>Represents a serious error
2. WARNING==>30==>Represents a warning message, some caution needed. It is alert to**

**the programmer**

**4. INFO===>20===>Represents a message with some important information

1. DEBUG===>10==>Represents a message with debugging information
2. NOTSET==>0==>Rrepresents that the level is not set.**

**By default while executing Python program only WARNING and higher level messages will
 be displayed.**

**How to implement logging:**

**To perform logging, first we required to create a file to store messages and we have to**

**specify which level messages we have to store.**

**We can do this by using basicConfig() function of logging module.**

**logging.basicConfig(filename='log.txt',level=logging.WARNING)**

**24**

```

```

**The above line will create a file log.txt and we can store either WARNING level or higher
 level messages to that file.**

**After creating log file, we can write messages to that file by using the following methods.**

**logging.debug(message)**

**logging.info(message)
 logging.warning(message)**

**logging.error(message)
 logging.critical(message)**

**Q.Write a Python program to create a log file and write WARNING and higher**

**level messages?**

```
 import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
```

**log.txt:**

```
 WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
```

**Note:**

**In the above program only WARNING and higher level messages will be written to log file.
 If we set level as DEBUG then all messages will be written to log file.**

```
 import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print("Logging Module Demo")
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
```

**log.txt:**

```
 DEBUG:root:This is debug message
INFO:root:This is info message
```

**25**

```

WARNING:root:This is warning message
ERROR:root:This is error message
CRITICAL:root:This is critical message
```

**Note: We can format log messages to include date and time, ip address of the client etc**

**at advanced level.**

**How to write Python program exceptions to the log file:**

**By using the following function we can write exceptions information to the log file.**

**logging.exception(msg)**

**Q. Python Program to write exception information to the log file**

```
 import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO)
logging.info("A New request Came:")
try:
x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))
print(x/y)
except ZeroDivisionError as msg:
print("cannot divide with zero")
logging.exception(msg)
1 except ValueError as msg:
1print("Enter only int values")
1logging.exception(msg)
1logging.info("Request Processing Completed")
15 )
16 )
1D:\Python_classes>py test.py
1Enter First Number: 10
1Enter Second Number: 2
20 ) 5.0
2
2D:\Python_classes>py test.py
2Enter First Number: 10
2Enter Second Number: 0
2cannot divide with zero
26 )
2D:\Python_classes>py test.py
2Enter First Number: 10
2Enter Second Number: ten
30 ) Enter only int values
```

**26**

```

```

**mylog.txt:**

```
 INFO:root:A New request Came:
INFO:root:Request Processing Completed
INFO:root:A New request Came:
ERROR:root:division by zero
Traceback (most recent call last):
File "test.py", line 7 , in <module>
print(x/y)
ZeroDivisionError: division by zero
INFO:root:Request Processing Completed
INFO:root:A New request Came:
1 ERROR:root:invalid literal for int() with base 10 : 'ten'
1Traceback (most recent call last):
1File "test.py", line 6 , in <module>
1y=int(input("Enter Second Number: "))
1ValueError: invalid literal for int() with base 10 : 'ten'
1INFO:root:Request Processing Completed
```

**27**

```

```

**PYTHON DEBUGGING BY USING ASSERTIONS**

**Debugging Python Program by using assert keyword:**

**The process of identifying and fixing the bug is called debugging.
 Very common way of debugging is to use print() statement. But the problem with the**

**print() statement is after fixing the bug,compulsory we have to delete the extra added**

**print() statments,otherwise these will be executed at runtime which creates performance
 problems and disturbs console output.**

**To overcome this problem we should go for assert statement. The main advantage of
 assert statement over print() statement is after fixing bug we are not required to delete**

**assert statements. Based on our requirement we can enable or disable assert statements.**

**Hence the main purpose of assertions is to perform debugging. Usully we can perform**

**debugging either in development or in test environments but not in production
 environment. Hence assertions concept is applicable only for dev and test environments**

**but not for production environment.**

**Types of assert statements:**

**There are 2 types of assert statements**

**1. Simple Version

1. Augmented Version
2. Simple Version:**

**assert conditional_expression**

**2. Augmented Version:**

**assert conditional_expression,message**

**conditional_expression will be evaluated and if it is true then the program will be
 continued.**

**If it is false then the program will be terminated by raising AssertionError.**

**By seeing AssertionError, programmer can analyze the code and can fix the problem.**

**Eg:**

```
 def squareIt(x):
return x**x
```

**28**

```

assert squareIt( 2 )== 4 ,"The square of 2 should be 4"
assert squareIt( 3 )== 9 ,"The square of 3 should be 9"
assert squareIt( 4 )== 16 ,"The square of 4 should be 16"
print(squareIt( 2 ))
print(squareIt( 3 ))
print(squareIt( 4 ))
9 )
D:\Python_classes>py test.py
1 Traceback (most recent call last):
1File "test.py", line 4 , in <module>
1assert squareIt( 3 )== 9 ,"The square of 3 should be 9"
1AssertionError: The square of 3 should be 9
15 )
1def squareIt(x):
1return x*x
1assert squareIt( 2 )== 4 ,"The square of 2 should be 4"
1assert squareIt( 3 )== 9 ,"The square of 3 should be 9"
20 ) assert squareIt( 4 )== 16 ,"The square of 4 should be 16"
2 print(squareIt( 2 ))
2print(squareIt( 3 ))
2print(squareIt( 4 ))
24 )
2Output
24
29
216
```

**Exception Handling vs Assertions:**

**Assertions concept can be used to alert programmer to resolve development time errors.**

**Exception Handling can be used to handle runtime errors.**

**1**

```

```

**Python's Object Oriented Programming (OOPs)**

**What is Class:**

⚽ **In Python every thing is an object. To create objects we required some Model or Plan or Blue
 print, which is nothing but class.**

⚽ **We can write a class to represent properties (attributes) and actions (behaviour) of object.**

⚽ **Properties can be represented by variables**

⚽ **Actions can be represented by Methods.**

⚽ **Hence class contains both variables and methods.**

**How to Define a class?**

**We can define a class by using class keyword.**

**Syntax:
 class className:
 ''' documenttation string '''
 variables:instance variables,static and local variables
 methods: instance methods,static methods,class methods**

**Documentation string represents description of the class. Within the class doc string is always
 optional. We can get doc string by using the following 2 ways.**

**1. print(classname.**doc**)

1. help(classname)**

**Example:**

```
 class Student:
''''' This is student class with required data'''
print(Student.__doc__)
help(Student)
```

**Within the Python class we can represent data by using variables.
 There are 3 types of variables are allowed.**

**1. Instance Variables (Object Level Variables)

1. Static Variables (Class Level Variables)
2. Local variables (Method Level Variables)**

**Within the Python class, we can represent operations by using methods. The following are various
 types of allowed methods**

**2**

```

```

**1. Instance Methods

1. Class Methods
2. Static Methods**

**Example for class:**

```
 class Student:
'''''Developed by durga for python demo'''
def __init__(self):
self.name='durga'
self.age= 40
self.marks= 80
7 )
def talk(self):
print("Hello I am :",self.name)
print("My Age is:",self.age)
1 print("My Marks are:",self.marks)
```

**What is Object:**

**Pysical existence of a class is nothing but object. We can create any number of objects for a class.**

**Syntax to create object: referencevariable = classname()**

**Example: s = Student()**

**What is Reference Variable:**

**The variable which can be used to refer object is called reference variable.
 By using reference variable, we can access properties and methods of object.**

**Program: Write a Python program to create a Student class and Creates an object to it. Call the
 method talk() to display student details**

```
 class Student:
2 )
def __init__(self,name,rollno,marks):
self.name=name
self.rollno=rollno
self.marks=marks
7 )
def talk(self):
print("Hello My Name is:",self.name)
print("My Rollno is:",self.rollno)
1 print("My Marks are:",self.marks)
12 )
```

**3**

```

1s1=Student("Durga", 101 , 80 )
1s1.talk()
```

**Output:
 D:\durgaclasses>py test.py
 Hello My Name is: Durga
 My Rollno is: 101
 My Marks are: 80**

**Self variable:**

**self is the default variable which is always pointing to current object (like this keyword in Java)**

**By using self we can access instance variables and instance methods of object.**

**Note:**

**1. self should be first parameter inside constructor
 def **init**(self):

1. self should be first parameter inside instance methods
    def talk(self):**

**Constructor Concept:**

☕ **Constructor is a special method in python.**

☕ **The name of the constructor should be \**init\**(self)**

☕ **Constructor will be executed automatically at the time of object creation.**
 ☕ **The main purpose of constructor is to declare and initialize instance variables.**

☕ **Per object constructor will be exeucted only once.**

☕ **Constructor can take atleast one argument(atleast self)**

☕ **Constructor is optional and if we are not providing any constructor then python will provide
 default constructor.**

**Example:**

```
 def __init__(self,name,rollno,marks):
self.name=name
self.rollno=rollno
self.marks=marks
```

**Program to demonistrate constructor will execute only once per object:**

```
 class Test:
2 )
def __init__(self):
print("Constructor exeuction...")
5 )
```

**4**

```

def m1(self):
print("Method execution...")
8 )
t1=Test()
t2=Test()
1 t3=Test()
1t1.m1()
```

**Output
 Constructor exeuction...
 Constructor exeuction...
 Constructor exeuction...
 Method execution...**

**Program:**

```
 class Student:
2 )
''''' This is student class with required data'''
def __init__(self,x,y,z):
self.name=x
self.rollno=y
self.marks=z
8 )
def display(self):
print("Student Name:{}\nRollno:{} \nMarks:{}".format(self.name,self.rollno,self.marks)
)
1
1s1=Student("Durga", 101 , 80 )
1s1.display()
1s2=Student("Sunny", 102 , 100 )
1s2.display()
```

**Output
 Student Name:Durga
 Rollno:101
 Marks:80
 Student Name:Sunny
 Rollno:102
 Marks:100**

**5**

```

```

**Differences between Methods and Constructors:**

**Method Constructor**

**1. Name of method can be any name 1. Constructor name should be always **init**

1. Method will be executed if we call that
    method**
    **2. Constructor will be executed automatically at**
    **the time of object creation.
2. Per object, method can be called any number
    of times.**
    **3. Per object, Constructor will be executed only**
    **once
3. Inside method we can write business logic**
    **4. Inside Constructor we have to declare and**
    **initialize instance variables**

**Types of Variables:**

**Inside Python class 3 types of variables are allowed.**

**1. Instance Variables (Object Level Variables)

1. Static Variables (Class Level Variables)
2. Local variables (Method Level Variables)
3. Instance Variables:**

**If the value of a variable is varied from object to object, then such type of variables are called
 instance variables.**

**For every object a separate copy of instance variables will be created.**

**Where we can declare Instance variables:**

**1. Inside Constructor by using self variable

1. Inside Instance Method by using self variable
2. Outside of the class by using object reference variable
3. Inside Constructor by using self variable:**

**We can declare instance variables inside a constructor by using self keyword. Once we creates
 object, automatically these variables will be added to the object.**

**Example:**

```
 class Employee:
2 )
def __init__(self):
self.eno= 100
self.ename='Durga'
self.esal= 10000
7 )
e=Employee()
```

**6**

```

print(e.__dict__)
```

**Output: {'eno': 100, 'ename': 'Durga', 'esal': 10000}**

**2. Inside Instance Method by using self variable:**

**We can also declare instance variables inside instance method by using self variable. If any
 instance variable declared inside instance method, that instance variable will be added once we
 call taht method.**

**Example:**

```
 class Test:
2 )
def __init__(self):
self.a= 10
self.b= 20
6 )
def m1(self):
self.c= 30
9 )
t=Test()
1 t.m1()
1print(t.__dict__)
```

**Output
 {'a': 10, 'b': 20, 'c': 30}**

**3. Outside of the class by using object reference variable:**

**We can also add instance variables outside of a class to a particular object.**

```
 class Test:
2 )
def __init__(self):
self.a= 10
self.b= 20
6 )
def m1(self):
self.c= 30
9 )
t=Test()
1 t.m1()
1t.d= 40
1print(t.__dict__)
```

**Output {'a': 10, 'b': 20, 'c': 30, 'd': 40}**

**7**

```

```

**How to access Instance variables:**

**We can access instance variables with in the class by using self variable and outside of the class by
 using object reference.**

```
 class Test:
2 )
def __init__(self):
self.a= 10
self.b= 20
6 )
def display(self):
print(self.a)
print(self.b)
10 )
1 t=Test()
1t.display()
1print(t.a,t.b)
```

**Output
 10
 20
 10 20**

**How to delete instance variable from the object:**

**1. Within a class we can delete instance variable as follows**

**del self.variableName**

**2. From outside of class we can delete instance variables as follows**

**del objectreference.variableName**

**Example:**

```
 class Test:
def __init__(self):
self.a= 10
self.b= 20
self.c= 30
self.d= 40
def m1(self):
del self.d
9 )
t=Test()
1 print(t.__dict__)
```

**8**

```

1t.m1()
1print(t.__dict__)
1del t.c
1print(t.__dict__)
```

**Output
 {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 {'a': 10, 'b': 20, 'c': 30}
 {'a': 10, 'b': 20}**

**Note: The instance variables which are deleted from one object,will not be deleted from other
 objects.**

**Example:**

```
 class Test:
def __init__(self):
self.a= 10
self.b= 20
self.c= 30
self.d= 40
7 )
8 )
t1=Test()
t2=Test()
1 del t1.a
1print(t1.__dict__)
1print(t2.__dict__)
```

**Output
 {'b': 20, 'c': 30, 'd': 40}
 {'a': 10, 'b': 20, 'c': 30, 'd': 40}**

**If we change the values of instance variables of one object then those changes won't be reflected
 to the remaining objects, because for every object we are separate copy of instance variables are
 available.**

**Example:**

```
 class Test:
def __init__(self):
self.a= 10
self.b= 20
5 )
t1=Test()
t1.a= 888
t1.b= 999
t2=Test()
print('t1:',t1.a,t1.b)
```

**9**

```

1 print('t2:',t2.a,t2.b)
```

**Output
 t1: 888 999
 t2: 10 20**

**1. Static variables:**

**If the value of a variable is not varied from object to object, such type of variables we have to
 declare with in the class directly but outside of methods. Such type of variables are called Static
 variables.**

**For total class only one copy of static variable will be created and shared by all objects of that
 class.**

**We can access static variables either by class name or by object reference. But recommended to
 use class name.**

**Instance Variable vs Static Variable:**

**Note: In the case of instance variables for every object a seperate copy will be created,but in the
 case of static variables for total class only one copy will be created and shared by every object of
 that class.**

```
 class Test:
x= 10
def __init__(self):
self.y= 20
5 )
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
Test.x= 888
1 t1.y= 999
1print('t1:',t1.x,t1.y)
1print('t2:',t2.x,t2.y)
```

**Output
 t1: 10 20
 t2: 10 20
 t1: 888 999
 t2: 888 20**

**10**

```

```

**Various places to declare static variables:**

**1. In general we can declare within the class directly but from out side of any method

1. Inside constructor by using class name
2. Inside instance method by using class name
3. Inside classmethod by using either class name or cls variable
4. Inside static method by using class name**

```
 class Test:
a= 10
def __init__(self):
Test.b= 20
def m1(self):
Test.c= 30
@classmethod
def m2(cls):
cls.d1= 40
Test.d2= 400
1 @staticmethod
1def m3():
1Test.e= 50
1print(Test.__dict__)
1t=Test()
1print(Test.__dict__)
1t.m1()
1print(Test.__dict__)
1Test.m2()
20 ) print(Test.__dict__)
2 Test.m3()
2print(Test.__dict__)
2Test.f= 60
2print(Test.__dict__)
```

**How to access static variables:**

**1. inside constructor: by using either self or classname

1. inside instance method: by using either self or classname
2. inside class method: by using either cls variable or classname
3. inside static method: by using classname
4. From outside of class: by using either object reference or classnmae**

```
 class Test:
a= 10
def __init__(self):
print(self.a)
print(Test.a)
def m1(self):
print(self.a)
```

**11**

```

print(Test.a)
@classmethod
def m2(cls):
1 print(cls.a)
1print(Test.a)
1@staticmethod
1def m3():
1print(Test.a)
1t=Test()
1print(Test.a)
1print(t.a)
1t.m1()
20 ) t.m2()
2 t.m3()
```

**Where we can modify the value of static variable:**

**Anywhere either with in the class or outside of class we can modify by using classname.
 But inside class method, by using cls variable.**

**Example:**

```
 class Test:
a= 777
@classmethod
def m1(cls):
cls.a= 888
@staticmethod
def m2():
Test.a= 999
print(Test.a)
Test.m1()
1 print(Test.a)
1Test.m2()
1print(Test.a)
```

**Output
 777
 888
 999**

**12**

```

```

------

**If we change the value of static variable by using either self**

**or object reference variable:**

**If we change the value of static variable by using either self or object reference variable, then the
 value of static variable won't be changed,just a new instance variable with that name will be
 added to that particular object.**

**Example 1:**

```
 class Test:
a= 10
def m1(self):
self.a= 888
t1=Test()
t1.m1()
print(Test.a)
print(t1.a)
```

**Output
 10
 888**

**Example:**

```
 class Test:
x= 10
def __init__(self):
self.y= 20
5 )
t1=Test()
t2=Test()
print('t1:',t1.x,t1.y)
print('t2:',t2.x,t2.y)
t1.x= 888
1 t1.y= 999
1print('t1:',t1.x,t1.y)
1print('t2:',t2.x,t2.y)
```

**Output
 t1: 10 20
 t2: 10 20
 t1: 888 999
 t2: 10 20**

**13**

```

```

**Example:**

```
 class Test:
a= 10
def __init__(self):
self.b= 20
t1=Test()
t2=Test()
Test.a= 888
t1.b= 999
print(t1.a,t1.b)
print(t2.a,t2.b)
```

**Output
 888 999
 888 20
 ------------------------------------**

```
 class Test:
a= 10
def __init__(self):
self.b= 20
def m1(self):
self.a= 888
self.b= 999
8 )
t1=Test()
t2=Test()
1 t1.m1()
1print(t1.a,t1.b)
1print(t2.a,t2.b)
```

**Output
 888 999
 10 20**

**Example:**

```
 class Test:
a= 10
def __init__(self):
self.b= 20
@classmethod
def m1(cls):
cls.a= 888
cls.b= 999
9 )
t1=Test()
1 t2=Test()
```

**14**

```

1t1.m1()
1print(t1.a,t1.b)
1print(t2.a,t2.b)
1print(Test.a,Test.b)
```

**Output
 888 20
 888 20
 888 999**

**How to delete static variables of a class:**

**We can delete static variables from anywhere by using the following syntax**

**del classname.variablename**

**But inside classmethod we can also use cls variable**

**del cls.variablename**

```
 class Test:
a= 10
@classmethod
def m1(cls):
del cls.a
Test.m1()
print(Test.__dict__)
```

**Example:**

```
 class Test:
a= 10
def __init__(self):
Test.b= 20
del Test.a
def m1(self):
Test.c= 30
del Test.b
@classmethod
def m2(cls):
1 cls.d= 40
1del Test.c
1@staticmethod
1def m3():
1Test.e= 50
1del Test.d
1print(Test.__dict__)
1t=Test()
```

**15**

```

1print(Test.__dict__)
20 ) t.m1()
2 print(Test.__dict__)
2Test.m2()
2print(Test.__dict__)
2Test.m3()
2print(Test.__dict__)
2Test.f= 60
2print(Test.__dict__)
2del Test.e
2print(Test.__dict__)
```

------

**Note: By using object reference variable/self we can read static variables, but we cannot modify
 or delete.**

**If we are trying to modify, then a new instance variable will be added to that particular object.
 t1.a = 70**

**If we are trying to delete then we will get error.**

**Example:**

```
 class Test:
a= 10
3 )
t1=Test()
del t1.a ===>AttributeError: a
```

**We can modify or delete static variables only by using classname or cls variable.**

```
 import sys
class Customer:
''''' Customer class with bank operations.. '''
bankname='DURGABANK'
def __init__(self,name,balance=0.0):
self.name=name
self.balance=balance
def deposit(self,amt):
self.balance=self.balance+amt
print('Balance after deposit:',self.balance)
1 def withdraw(self,amt):
1if amt>self.balance:
1print('Insufficient Funds..cannot perform this operation')
1sys.exit()
1self.balance=self.balance-amt
1print('Balance after withdraw:',self.balance)
17 )
1print('Welcome to',Customer.bankname)
```

**16**

```

1name=input('Enter Your Name:')
20 ) c=Customer(name)
2 while True:
2print('d-Deposit \nw-Withdraw \ne-exit')
2option=input('Choose your option:')
2if option=='d' or option=='D':
2amt=float(input('Enter amount:'))
2c.deposit(amt)
2elif option=='w' or option=='W':
2amt=float(input('Enter amount:'))
2c.withdraw(amt)
30 ) elif option=='e' or option=='E':
3 print('Thanks for Banking')
3sys.exit()
3else:
3print('Invalid option..Plz choose valid option')
```

**output:
 D:\durga_classes>py test.py
 Welcome to DURGABANK
 Enter Your Name:Durga
 d-Deposit
 w-Withdraw
 e-exit
 Choose your option:d
 Enter amount:10000
 Balance after deposit: 10000.0
 d-Deposit
 w-Withdraw
 e-exit
 Choose your option:d
 Enter amount:20000
 Balance after deposit: 30000.0
 d-Deposit
 w-Withdraw
 e-exit
 Choose your option:w
 Enter amount:2000
 Balance after withdraw: 28000.0
 d-Deposit
 w-Withdraw
 e-exit
 Choose your option:r
 Invalid option..Plz choose valid option
 d-Deposit
 w-Withdraw
 e-exit
 Choose your option:e
 Thanks for Banking**

**17**

```

```

**Local variables:**

**Sometimes to meet temporary requirements of programmer,we can declare variables inside a
 method directly,such type of variables are called local variable or temporary variables.**

**Local variables will be created at the time of method execution and destroyed once method
 completes.**

**Local variables of a method cannot be accessed from outside of method.**

**Example:**

```
 class Test:
def m1(self):
a= 1000
print(a)
def m2(self):
b= 2000
print(b)
t=Test()
t.m1()
t.m2()
```

**Output
 1000
 2000**

**Example 2:**

```
 class Test:
def m1(self):
a= 1000
print(a)
def m2(self):
b= 2000
print(a) #NameError: name 'a' is not defined
print(b)
t=Test()
t.m1()
1 t.m2()
```

**18**

```

```

**Types of Methods:**

**Inside Python class 3 types of methods are allowed**

**1. Instance Methods

1. Class Methods
2. Static Methods
3. Instance Methods:**

**Inside method implementation if we are using instance variables then such type of methods are
 called instance methods.
 Inside instance method declaration,we have to pass self variable.**

**def m1(self):**

**By using self variable inside method we can able to access instance variables.**

**Within the class we can call instance method by using self variable and from outside of the class
 we can call by using object reference.**

```
 class Student:
def __init__(self,name,marks):
self.name=name
self.marks=marks
def display(self):
print('Hi',self.name)
print('Your Marks are:',self.marks)
def grade(self):
if self.marks>= 60 :
print('You got First Grade')
1 elif self.marks>= 50 :
1print('Yout got Second Grade')
1elif self.marks>= 35 :
1print('You got Third Grade')
1else:
1print('You are Failed')
1n=int(input('Enter number of students:'))
1for i in range(n):
1name=input('Enter Name:')
20 ) marks=int(input('Enter Marks:'))
2 s= Student(name,marks)
2s.display()
2s.grade()
2print()
```

**19**

```

```

**ouput:
 D:\durga_classes>py test.py
 Enter number of students:2
 Enter Name:Durga
 Enter Marks:90
 Hi Durga
 Your Marks are: 90
 You got First Grade**

**Enter Name:Ravi
 Enter Marks:12
 Hi Ravi
 Your Marks are: 12
 You are Failed**

**Setter and Getter Methods:**

**We can set and get the values of instance variables by using getter and setter methods.**

**Setter Method:**

**setter methods can be used to set values to the instance variables. setter methods also known as
 mutator methods.**

**syntax:**

**def setVariable(self,variable):
 self.variable=variable**

**Example:
 def setName(self,name):
 self.name=name**

**Getter Method:**

**Getter methods can be used to get values of the instance variables. Getter methods also known as
 accessor methods.**

**syntax:**

**def getVariable(self):
 return self.variable**

**Example:
 def getName(self):
 return self.name**

**20**

```

```

**Demo Program:**

```
 class Student:
def setName(self,name):
self.name=name
4 )
def getName(self):
return self.name
7 )
def setMarks(self,marks):
self.marks=marks
10 )
1 def getMarks(self):
1return self.marks
13 )
1n=int(input('Enter number of students:'))
1for i in range(n):
1s=Student()
1name=input('Enter Name:')
1s.setName(name)
1marks=int(input('Enter Marks:'))
20 ) s.setMarks(marks)
2
2print('Hi',s.getName())
2print('Your Marks are:',s.getMarks())
2print()
```

**output:
 D:\python_classes>py test.py
 Enter number of students:2
 Enter Name:Durga
 Enter Marks:100
 Hi Durga
 Your Marks are: 100**

**Enter Name:Ravi
 Enter Marks:80
 Hi Ravi
 Your Marks are: 80**

**2. Class Methods:**

**Inside method implementation if we are using only class variables (static variables), then such type
 of methods we should declare as class method.**

**We can declare class method explicitly by using @classmethod decorator.
 For class method we should provide cls variable at the time of declaration**

**21**

```

```

**We can call classmethod by using classname or object reference variable.**

**Demo Program:**

```
 class Animal:
legs= 4
@classmethod
def walk(cls,name):
print('{} walks with {} legs...'.format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')
```

**Output
 D:\python_classes>py test.py
 Dog walks with 4 legs...
 Cat walks with 4 legs...**

**Program to track the number of objects created for a class:**

```
 class Test:
count= 0
def __init__(self):
Test.count =Test.count+ 1
@classmethod
def noOfObjects(cls):
print('The number of objects created for test class:',cls.count)
8 )
t1=Test()
t2=Test()
1 Test.noOfObjects()
1t3=Test()
1t4=Test()
1t5=Test()
1Test.noOfObjects()
```

**3. Static Methods:**

**In general these methods are general utility methods.
 Inside these methods we won't use any instance or class variables.
 Here we won't provide self or cls arguments at the time of declaration.**

**We can declare static method explicitly by using @staticmethod decorator
 We can access static methods by using classname or object reference**

```
 class DurgaMath:
2 )
@staticmethod
def add(x,y):
```

**22**

```

print('The Sum:',x+y)
6 )
@staticmethod
def product(x,y):
print('The Product:',x*y)
10 )
1 @staticmethod
1def average(x,y):
1print('The average:',(x+y)/ 2 )
14 )
1DurgaMath.add( 10 , 20 )
1DurgaMath.product( 10 , 20 )
1DurgaMath.average( 10 , 20 )
```

**Output
 The Sum: 30
 The Product: 200
 The average: 15.0**

**Note: In general we can use only instance and static methods.Inside static method we can access
 class level variables by using class name.**

**class methods are most rarely used methods in python.**

**Passing members of one class to another class:**

**We can access members of one class inside another class.**

```
 class Employee:
def __init__(self,eno,ename,esal):
self.eno=eno
self.ename=ename
self.esal=esal
def display(self):
print('Employee Number:',self.eno)
print('Employee Name:',self.ename)
print('Employee Salary:',self.esal)
class Test:
1 def modify(emp):
1emp.esal=emp.esal+ 10000
1emp.display()
1e=Employee( 100 ,'Durga', 10000 )
1Test.modify(e)
```

**Output
 D:\python_classes>py test.py
 Employee Number: 100
 Employee Name: Durga**

**23**

```

```

**Employee Salary: 2 0000**

**In the above application, Employee class members are available to Test class.**

**Inner classes:**

**Sometimes we can declare a class inside another class,such type of classes are called inner classes.**

**Without existing one type of object if there is no chance of existing another type of object,then we
 should go for inner classes.**

**Example: Without existing Car object there is no chance of existing Engine object. Hence Engine
 class should be part of Car class.**

**class Car:
 .....
 class Engine:
 ......**

**Example: Without existing university object there is no chance of existing Department object**

**class University:
 .....
 class Department:
 ......**

**eg3:
 Without existing Human there is no chance of existin Head. Hence Head should be part of Human.**

**class Human:
 class Head:**

**Note: Without existing outer class object there is no chance of existing inner class object. Hence
 inner class object is always associated with outer class object.**

**Demo Program-1:**

```
 class Outer:
def __init__(self):
print("outer class object creation")
class Inner:
def __init__(self):
print("inner class object creation")
def m1(self):
print("inner class method")
o=Outer()
i=o.Inner()
1 i.m1()
```

**24**

```

```

**Output
 outer class object creation
 inner class object creation
 inner class method**

**Note: The following are various possible syntaxes for calling inner class method**

**1.
 o=Outer()
 i=o.Inner()
 i.m1()**

**2.
 i=Outer().Inner()
 i.m1()**

**3. Outer().Inner().m1()**

**Demo Program-2:**

```
 class Person:
def __init__(self):
self.name='durga'
self.db=self.Dob()
def display(self):
print('Name:',self.name)
class Dob:
def __init__(self):
self.dd= 10
self.mm= 5
1 self.yy= 1947
1def display(self):
1print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
1p=Person()
1p.display()
1x=p.db
1x.display()
```

**Output
 Name: durga
 Dob=10/5/1947**

**Demo Program-3:**

**Inside a class we can declare any number of inner classes.**

```
 class Human:
2 )
def __init__(self):
```

**25**

```

self.name = 'Sunny'
self.head = self.Head()
self.brain = self.Brain()
def display(self):
print("Hello..",self.name)
9 )
class Head:
1 def talk(self):
1print('Talking...')
13 )
1class Brain:
1def think(self):
1print('Thinking...')
17 )
1h=Human()
1h.display()
20 ) h.head.talk()
2 h.brain.think()
```

**Output
 Hello.. Sunny
 Talking...
 Thinking...**

**Garbage Collection:**

**In old languages like C++, programmer is responsible for both creation and destruction of
 objects.Usually programmer taking very much care while creating object, but neglecting
 destruction of useless objects. Because of his neglectance, total memory can be filled with useless
 objects which creates memory problems and total application will be down with Out of memory
 error.**

**But in Python, We have some assistant which is always running in the background to destroy
 useless objects.Because this assistant the chance of failing Python program with memory
 problems is very less. This assistant is nothing but Garbage Collector.**

**Hence the main objective of Garbage Collector is to destroy useless objects.**

**If an object does not have any reference variable then that object eligible for Garbage Collection.**

**How to enable and disable Garbage Collector in our program:**

**By default Gargbage collector is enabled, but we can disable based on our requirement. In this
 context we can use the following functions of gc module.**

**1. gc.isenabled()
 Returns True if GC enabled**

**26**

```

```

**2. gc.disable()
 To disable GC explicitly

1. gc.enable()
    To enable GC explicitly**

**Example:**

```
 import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
```

**Output
 True
 False
 True**

**Destructors:**

**Destructor is a special method and the name should be \**del\**
 Just before destroying an object Garbage Collector always calls destructor to perform clean up
 activities (Resource deallocation activities like close database connection etc).
 Once destructor execution completed then Garbage Collector automatically destroys that object.**

**Note: The job of destructor is not to destroy object and it is just to perform clean up activities.**

**Example:**

```
 import time
class Test:
def __init__(self):
print("Object Initialization...")
def __del__(self):
print("Fulfilling Last Wish and performing clean up activities...")
7 )
t1=Test()
t1=None
time.sleep( 5 )
1 print("End of application")
```

**Output
 Object Initialization...
 Fulfilling Last Wish and performing clean up activities...
 End of application**

**27**

```

```

**Note:
 If the object does not contain any reference variable then only it is eligible fo GC. ie if the
 reference count is zero then only object eligible for GC**

**Example:**

```
 import time
class Test:
def __init__(self):
print("Constructor Execution...")
def __del__(self):
print("Destructor Execution...")
7 )
t1=Test()
t2=t1
t3=t2
1 del t1
1time.sleep( 5 )
1print("object not yet destroyed after deleting t1")
1del t2
1time.sleep( 5 )
1print("object not yet destroyed even after deleting t2")
1print("I am trying to delete last reference variable...")
1del t3
```

**Example:**

```
 import time
class Test:
def __init__(self):
print("Constructor Execution...")
def __del__(self):
print("Destructor Execution...")
7 )
list=[Test(),Test(),Test()]
del list
time.sleep( 5 )
1 print("End of application")
```

**Output
 Constructor Execution...
 Constructor Execution...
 Constructor Execution...
 Destructor Execution...
 Destructor Execution...
 Destructor Execution...
 End of application**

**28**

```

```

**How to find the number of references of an object:**

**sys module contains getrefcount() function for this purpose.**

**sys.getrefcount(objectreference)**

**Example:**

```
 import sys
class Test:
pass
t1=Test()
t2=t1
t3=t1
t4=t1
print(sys.getrefcount(t1))
```

**Output 5**

**Note: For every object, Python internally maintains one default reference variable self.**

**1**

```

```

**OOPs Part - 2**

**Agenda**

 **Inheritance**

```
 Has-A Relationship
 IS-A Relationship
 IS-A vs HAS-A Relationship
 Composition vs Aggregation
 Types of Inheritance
 Single Inheritance
 Multi Level Inheritance
 Hierarchical Inheritance
 Multiple Inheritance
 Hybrid Inheritance
 Cyclic Inheritance
```

 **Method Resolution Order (MRO)**

 **super() Method**

**2**

```

```

**Using members of one class inside another class:**

**We can use members of one class inside another class by using the following ways**

**1. By Composition (Has-A Relationship)

1. By Inheritance (IS-A Relationship)
2. By Composition (Has-A Relationship):**

**By using Class Name or by creating object we can access members of one class inside another class
 is nothing but composition (Has-A Relationship).**

**The main advantage of Has-A Relationship is Code Reusability.**

**Demo Program-1:**

```
 class Engine:
a= 10
def __init__(self):
self.b= 20
def m1(self):
print('Engine Specific Functionality')
class Car:
def __init__(self):
self.engine=Engine()
def m2(self):
1 print('Car using Engine Class Functionality')
1print(self.engine.a)
1print(self.engine.b)
1self.engine.m1()
1c=Car()
1c.m2()
```

**Output:
 Car using Engine Class Functionality
 10
 20
 Engine Specific Functionality**

**Demo Program-2:**

```
 class Car:
def __init__(self,name,model,color):
self.name=name
self.model=model
self.color=color
def getinfo(self):
```

**3**

```

print("Car Name:{} , Model:{} and Color:{}".format(self.name,self.model,self.color))
8 )
class Employee:
def __init__(self,ename,eno,car):
1 self.ename=ename
1self.eno=eno
1self.car=car
1def empinfo(self):
1print("Employee Name:",self.ename)
1print("Employee Number:",self.eno)
1print("Employee Car Info:")
1self.car.getinfo()
1c=Car("Innova","2.5V","Grey")
20 ) e=Employee('Durga', 10000 ,c)
2 e.empinfo()
```

**Output:
 Employee Name: Durga
 Employee Number: 10000
 Employee Car Info:
 Car Name: Innova, Model:2.5V and Color:Grey**

**In the above program Employee class Has-A Car reference and hence Employee class can access all
 members of Car class.**

**Demo Program-3:**

```
 class X:
a= 10
def __init__(self):
self.b= 20
def m1(self):
print("m1 method of X class")
class Y:
c= 30
def __init__(self):
self.d= 40
1 def m2(self):
1print("m2 method of Y class")
1def m3(self):
1x1=X()
1print(x1.a)
1print(x1.b)
1x1.m1()
1print(Y.c)
1print(self.d)
20 ) self.m2()
2 print("m3 method of Y class")
2y1=Y()
```

**4**

```

2y1.m3()
```

**Output:
 10
 20
 m1 method of X class
 30
 40
 m2 method of Y class
 m3 method of Y class**

**2. By Inheritance(IS-A Relationship):**

**What ever variables, methods and constructors available in the parent class by default available to
 the child classes and we are not required to rewrite. Hence the main advantage of inheritance is
 Code Reusability and we can extend existing functionality with some more extra functionality.**

**Syntax :
 class childclass(parentclass):**

**Demo Program for inheritance:**

```
 class P:
a= 10
def __init__(self):
self.b= 10
def m1(self):
print('Parent instance method')
@classmethod
def m2(cls):
print('Parent class method')
@staticmethod
1 def m3():
1print('Parent static method')
13 )
1class C(P):
1pass
16 )
1c=C()
1print(c.a)
1print(c.b)
20 ) c.m1()
2 c.m2()
2c.m3()
```

**Output:
 10
 10**

**5**

```

```

**Parent instance method
 Parent class method
 Parent static method**

**Eg:**

```
 class P:
10 methods
class C(P):
5 methods
```

**In the above example Parent class contains 10 methods and these methods automatically
 available to the child class and we are not required to rewrite those methods(Code Reusability)
 Hence child class contains 15 methods.**

**Note:
 What ever members present in Parent class are by default available to the child class through
 inheritance.**

**Demo Program:**

```
 class P:
def m1(self):
print("Parent class method")
class C(P):
def m2(self):
print("Child class method")
7 )
c=C();
c.m1()
c.m2()
```

**Output:
 Parent class method
 Child class method**

**What ever methods present in Parent class are automatically available to the child class and hence
 on the child class reference we can call both parent class methods and child class methods.**

**Similarly variables also**

```
 class P:
a= 10
def __init__(self):
self.b= 20
class C(P):
c= 30
def __init__(self):
super().__init__()===>Line- 1
```

**6**

```

self.d= 30
10 )
1 c1=C()
1print(c1.a,c1.b,c1.c,c1.d)
```

**If we comment Line-1 then variable b is not available to the child class.**

**Demo program for inheritance:**

```
 class Person:
def __init__(self,name,age):
self.name=name
self.age=age
def eatndrink(self):
print('Eat Biryani and Drink Beer')
7 )
class Employee(Person):
def __init__(self,name,age,eno,esal):
super().__init__(name,age)
1 self.eno=eno
1self.esal=esal
13 )
1def work(self):
1print("Coding Python is very easy just like drinking Chilled Beer")
1def empinfo(self):
1print("Employee Name:",self.name)
1print("Employee Age:",self.age)
1print("Employee Number:",self.eno)
20 ) print("Employee Salary:",self.esal)
2
2e=Employee('Durga', 48 , 100 , 10000 )
2e.eatndrink()
2e.work()
2e.empinfo()
```

**Output:
 Eat Biryani and Drink Beer
 Coding Python is very easy just like drinking Chilled Beer
 Employee Name: Durga
 Employee Age: 48
 Employee Number: 100
 Employee Salary: 10000**

**7**

```

```

**IS-A vs HAS-A Relationship:**

**If we want to extend existing functionality with some more extra functionality then we should go
 for IS-A Relationship**

**If we dont want to extend and just we have to use existing functionality then we should go for
 HAS-A Relationship**

**Eg: Employee class extends Person class Functionality
 But Employee class just uses Car functionality but not extending**

```
 class Car:
def __init__(self,name,model,color):
self.name=name
self.model=model
self.color=color
def getinfo(self):
print("\tCar Name:{} \n\t Model:{} \n\t Color:{}".format(self.name,self.model,self.col
or))
8 )
class Person:
def __init__(self,name,age):
1 self.name=name
1self.age=age
1def eatndrink(self):
1print('Eat Biryani and Drink Beer')
15 )
1class Employee(Person):
1def __init__(self,name,age,eno,esal,car):
1super().__init__(name,age)
1self.eno=eno
20 ) self.esal=esal
2 self.car=car
2def work(self):
2print("Coding Python is very easy just like drinking Chilled Beer")
2def empinfo(self):
Person
Employee Car
IS - A
HAS - A
```

**8**

```

2print("Employee Name:",self.name)
2print("Employee Age:",self.age)
2print("Employee Number:",self.eno)
2print("Employee Salary:",self.esal)
2print("Employee Car Info:")
30 ) self.car.getinfo()
3
3c=Car("Innova","2.5V","Grey")
3e=Employee('Durga', 48 , 100 , 10000 ,c)
3e.eatndrink()
3e.work()
3e.empinfo()
```

**Output:
 Eat Biryani and Drink Beer
 Coding Python is very easy just like drinking Chilled Beer
 Employee Name: Durga
 Employee Age: 48
 Employee Number: 100
 Employee Salary: 1000 0
 Employee Car Info:
 Car Name:Innova
 Model:2.5V
 Color:Grey**

**In the above example Employee class extends Person class functionality but just uses Car class
 functionality.**

**Composition vs Aggregation:**

**Composition:**

**Without existing container object if there is no chance of existing contained object then the
 container and contained objects are strongly associated and that strong association is nothing but
 Composition.**

**Eg: University contains several Departments and without existing university object there is no
 chance of existing Department object. Hence University and Department objects are strongly
 associated and this strong association is nothing but Composition.**

**9**

```

```

**Aggregation:**

**Without existing container object if there is a chance of existing contained object then the
 container and contained objects are weakly associated and that weak association is nothing but
 Aggregation.**

**Eg: Department contains several Professors. Without existing Department still there may be a
 chance of existing Professor. Hence Department and Professor objects are weakly associated,
 which is nothing but Aggregation.**

**Coding Example:**

```
 class Student:
collegeName='DURGASOFT'
def __init__(self,name):
self.name=name
print(Student.collegeName)
s=Student('Durga')
print(s.name)
Department Object
(Contained Object)
University Object
(Container Object)
:
:
:
```

**x x : : : x**

```
Department Object
(Container Object)
P
ro
fe
ssor
O
bject
(C
o
ntaine
d^
O
bject
)^
```

**10**

```

```

**Output:
 DURGASOFT
 Durga**

**In the above example without existing Student object there is no chance of existing his name.
 Hence Student Object and his name are strongly associated which is nothing but Composition.**

**But without existing Student object there may be a chance of existing collegeName. Hence
 Student object and collegeName are weakly associated which is nothing but Aggregation.**

**Conclusion:**

**The relation between object and its instance variables is always Composition where as the relation
 between object and static variables is Aggregation.**

**Note: Whenever we are creating child class object then child class constructor will be executed. If
 the child class does not contain constructor then parent class constructor will be executed, but
 parent object won't be created.**

**Eg:**

```
 class P:
def __init__(self):
print(id(self))
class C(P):
pass
c=C()
print(id(c))
```

**Output:
 6207088
 6207088**

**Eg:**

```
 class Person:
def __init__(self,name,age):
self.name=name
self.age=age
class Student(Person):
def __init__(self,name,age,rollno,marks):
super().__init__(name,age)
self.rollno=rollno
self.marks=marks
def __str__(self):
1 return 'Name={}\nAge={}\nRollno={}\nMarks={}'.format(self.name,self.age,self.rollno
,self.marks)
1s1=Student('durga', 48 , 101 , 90 )
1print(s1)
```

**11**

```

```

**Output:
 Name=durga
 Age=48
 Rollno=101
 Marks=90**

**Note: In the above example when ever we are creating child class object both parent and child
 class constructors got executed to perform initialization of child object**

**Types of Inheritance:**

**1. Single Inheritance:**

**The concept of inheriting the properties from one class to another class is known as single
 inheritance.**

**Eg:**

```
 class P:
def m1(self):
print("Parent Method")
class C(P):
def m2(self):
print("Child Method")
c=C()
c.m1()
c.m2()
```

**Output:
 Parent Method
 Child Method**

**P**

**C**

**Single Inheritance**

**12**

```

```

**2. Multi Level Inheritance:**

**The concept of inheriting the properties from multiple classes to single class with the concept of
 one after another is known as multilevel inheritance**

**Eg:**

```
 class P:
def m1(self):
print("Parent Method")
class C(P):
def m2(self):
print("Child Method")
class CC(C):
def m3(self):
print("Sub Child Method")
c=CC()
1 c.m1()
1c.m2()
1c.m3()
```

**Output:
 Parent Method
 Child Method
 Sub Child Method**

**P**

**C**

**CC**

**Multi – Level Inheritance**

**13**

```

```

**3. Hierarchical Inheritance:**

**The concept of inheriting properties from one class into multiple classes which are present at
 same level is known as Hierarchical Inheritance**

```
 class P:
def m1(self):
print("Parent Method")
class C1(P):
def m2(self):
print("Child1 Method")
class C2(P):
def m3(self):
print("Child2 Method")
c1=C1()
1 c1.m1()
1c1.m2()
1c2=C2()
1c2.m1()
1c2.m3()
```

**Output:
 Parent Method
 Child1 Method
 Parent Method
 Child2 Method**

```
Hierarchical
Inheritance
```

**P**

**C** (^1) **C 2**

**14**

```

```

**4. Multiple Inheritance:**

**The concept of inheriting the properties from multiple classes into a single class at a time, is
 known as multiple inheritance.**

```
 class P1:
def m1(self):
print("Parent1 Method")
class P2:
def m2(self):
print("Parent2 Method")
class C(P1,P2):
def m3(self):
print("Child2 Method")
c=C()
1 c.m1()
1c.m2()
1c.m3()
```

**Output:
 Parent1 Method
 Parent2 Method
 Child2 Method**

**If the same method is inherited from both parent classes,then Python will always consider the
 order of Parent classes in the declaration of the child class.**

**class C(P1,P2): ===>P1 method will be considered
 class C(P2,P1): ===>P2 method will be considered**

```
Multiple
Inheritance
```

**C**

**P 1 P 2**

**15**

```

```

**Eg:**

```
 class P1:
def m1(self):
print("Parent1 Method")
class P2:
def m1(self):
print("Parent2 Method")
class C(P1,P2):
def m2(self):
print("Child Method")
c=C()
1 c.m1()
1c.m2()
```

**Output:
 Parent1 Method
 Child Method**

**5. Hybrid Inheritance:**

**Combination of Single, Multi level, multiple and Hierarchical inheritance is known as Hybrid
 Inheritance.**

**D**

**A** (^) **B
 E
 F
 G** (^) **H
 C**

**16**

```

```

**6. Cyclic Inheritance:**

**The concept of inheriting properties from one class to another class in cyclic way, is called Cyclic
 inheritance.Python won't support for Cyclic Inheritance of course it is really not required.**

**Eg - 1 :**

**class A(A):pass**

**NameError: name 'A' is not defined**

**Eg - 2 :**

```
 class A(B):
pass
class B(A):
pass
```

**NameError: name 'B' is not defined**

**A**

**A**

**B**

**17**

```

```

**Method Resolution Order (MRO):**

**In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
 This algorithm is also known as C3 algorithm.
 Samuele Pedroni proposed this algorithm.
 It follows DLR (Depth First Left to Right)
 i.e Child will get more priority than Parent.
 Left Parent will get more priority than Right Parent**

**MRO(X)=X+Merge(MRO(P1),MRO(P2),...,ParentList)**

**Head Element vs Tail Terminology:**

**Assume C1,C2,C3,...are classes.
 In the list : C1C2C3C4C5....
 C1 is considered as Head Element and remaining is considered as Tail.**

**How to find Merge:**

**Take the head of first list
 If the head is not in the tail part of any other list,then add this head to the result and remove it
 from the lists in the merge.
 If the head is present in the tail part of any other list,then consider the head element of the next
 list and continue the same process.**

**Note: We can find MRO of any class by using mro() function.
 print(ClassName.mro())**

**Demo Program-1 for Method Resolution Order:**

**mro(A)=A,object
 mro(B)=B,A,object
 mro(C)=C,A,object
 mro(D)=D,B,C,A,object**

**A**

**D**

**B C**^

**18**

```

```

**test.py:**

```
 class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())
```

**Output:
 [<class '\**main\**.A'>, <class 'object'>]
 [<class '\**main\**.B'>, <class '\**main\**.A'>, <class 'object'>]
 [<class '\**main\**.C'>, <class '\**main\**.A'>, <class 'object'>]
 [<class '\**main\**.D'>, <class '\**main\**.B'>, <class '\**main\**.C'>, <class '\**main\**.A'>, <class
 'object'>]**

**Demo Program-2 for Method Resolution Order:**

**mro(A)=A,object
 mro(B)=B,object
 mro(C)=C,object
 mro(X)=X,A,B,object
 mro(Y)=Y,B,C,object
 mro(P)=P,X,A,Y,B,C,object**

```
Object
```

**X**

**A B C**^

**Y**

**P**

**19**

```

```

**Finding mro(P) by using C3 algorithm:**

**Formula: MRO(X)=X+Merge(MRO(P1),MRO(P2),...,ParentList)**

**mro(p)= P+Merge(mro(X),mro(Y),mro(C),XYC)
 = P+Merge(XABO,YBCO,CO,XYC)
 = P+X+Merge(ABO,YBCO,CO,YC)
 = P+X+A+Merge(BO,YBCO,CO,YC)
 = P+X+A+Y+Merge(BO,BCO,CO,C)
 = P+X+A+Y+B+Merge(O,CO,CO,C)
 = P+X+A+Y+B+C+Merge(O,O,O)
 = P+X+A+Y+B+C+O**

**test.py:**

```
 class A:pass
class B:pass
class C:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C):pass
print(A.mro())#AO
print(X.mro())#XABO
print(Y.mro())#YBCO
print(P.mro())#PXAYBCO
```

**Output:
 [<class '\**main\**.A'>, <class 'object'>]
 [<class '\**main\**.X'>, <class '\**main\**.A'>, <class '\**main\**.B'>, <class 'object'>]
 [<class '\**main\**.Y'>, <class '\**main\**.B'>, <class '\**main\**.C'>, <class 'object'>]
 [<class '\**main\**.P'>, <class '\**main\**.X'>, <class '\**main\**.A'>, <class '\**main\**.Y'>, <class
 '\**main\**.B'>,
 <class '\**main\**.C'>, <class 'object'>]**

**test.py:**

```
 class A:
def m1(self):
print('A class Method')
class B:
def m1(self):
print('B class Method')
class C:
def m1(self):
print('C class Method')
class X(A,B):
1 def m1(self):
1print('X class Method')
```

**20**

```

1class Y(B,C):
1def m1(self):
1print('Y class Method')
1class P(X,Y,C):
1def m1(self):
1print('P class Method')
1p=P()
20 ) p.m1()
```

**Output:
 P class Method**

**In the above example P class m1() method will be considered.If P class does not contain m1()
 method then as per MRO, X class method will be considered. If X class does not contain then A
 class method will be considered and this process will be continued.**

**The method resolution in the following order:PXAYBCO**

**Demo Program-3 for Method Resolution Order:**

**mro(o)=object
 mro(D)=D,object
 mro(E)=E,object
 mro(F)=F,object
 mro(B)=B,D,E,object
 mro(C)=C,D,F,object
 mro(A)=A+Merge(mro(B),mro(C),BC)
 =A+Merge(BDEO,CDFO,BC)
 =A+B+Merge(DEO,CDFO,C)
 =A+B+C+Merge(DEO,DFO)
 =A+B+C+D+Merge(EO,FO)
 =A+B+C+D+E+Merge(O,FO)
 =A+B+C+D+E+F+Merge(O,O)
 =A+B+C+D+E+F+O**

```
Object
```

**B**

**D**

```
F
E
```

**C**

**A**

**21**

```

```

**test.py:**

```
 class D:pass
class E:pass
class F:pass
class B(D,E):pass
class C(D,F):pass
class A(B,C):pass
print(D.mro())
print(B.mro())
print(C.mro())
print(A.mro())
```

**Output:
 [<class '\**main\**.D'>, <class 'object'>]
 [<class '\**main\**.B'>, <class '\**main\**.D'>, <class '\**main\**.E'>, <class 'object'>]
 [<class '\**main\**.C'>, <class '\**main\**.D'>, <class '\**main\**.F'>, <class 'object'>]
 [<class '\**main\**.A'>, <class '\**main\**.B'>, <class '\**main\**.C'>, <class '\**main\**.D'>, <class
 '\**main\**.E'>,
 <class '\**main\**.F'>, <class 'object'>]**

**super() Method:**

**super() is a built-in method which is useful to call the super class constructors,variables and
 methods from the child class.**

**Demo Program-1 for super():**

```
 class Person:
def __init__(self,name,age):
self.name=name
self.age=age
def display(self):
print('Name:',self.name)
print('Age:',self.age)
8 )
class Student(Person):
def __init__(self,name,age,rollno,marks):
1 super().__init__(name,age)
1self.rollno=rollno
1self.marks=marks
14 )
1def display(self):
1super().display()
1print('Roll No:',self.rollno)
1print('Marks:',self.marks)
19 )
20 ) s1=Student('Durga', 22 , 101 , 90 )
```

**22**

```

2 s1.display()
```

**Output:
 Name: Durga
 Age: 22
 Roll No: 101
 Marks: 90**

**In the above program we are using super() method to call parent class constructor and display()
 method**

**Demo Program-2 for super():**

```
 class P:
a= 10
def __init__(self):
self.b= 10
def m1(self):
print('Parent instance method')
@classmethod
def m2(cls):
print('Parent class method')
@staticmethod
1 def m3():
1print('Parent static method')
13 )
1class C(P):
1a= 888
1def __init__(self):
1self.b= 999
1super().__init__()
1print(super().a)
20 ) super().m1()
2 super().m2()
2super().m3()
23 )
2c=C()
```

**Output:
 10
 Parent instance method
 Parent class method
 Parent static method**

**In the above example we are using super() to call various members of Parent class.**

**23**

```

```

**How to call method of a particular Super class:**

**We can use the following approaches**

**1. super(D,self).m1()
 It will call m1() method of super class of D.

1. A.m1(self)
    It will call A class m1() method**

```
 class A:
def m1(self):
print('A class Method')
class B(A):
def m1(self):
print('B class Method')
class C(B):
def m1(self):
print('C class Method')
class D(C):
1 def m1(self):
1print('D class Method')
1class E(D):
1def m1(self):
1A.m1(self)
16 )
1e=E()
1e.m1()
```

**Output:
 A class Method**

**Various Important Points about super():**

**Case-1: From child class we are not allowed to access parent class instance variables by using
 super(),Compulsory we should use self only.
 But we can access parent class static variables by using super().**

**Eg:**

```
 class P:
a= 10
def __init__(self):
self.b= 20
5 )
class C(P):
def m1(self):
```

**24**

```

print(super().a)#valid
print(self.b)#valid
print(super().b)#invalid
1 c=C()
1c.m1()
```

**Output:
 10
 20
 AttributeError: 'super' object has no attribute 'b'**

**Case-2: From child class constructor and instance method, we can access parent class instance
 method,static method and class method by using super()**

```
 class P:
def __init__(self):
print('Parent Constructor')
def m1(self):
print('Parent instance method')
@classmethod
def m2(cls):
print('Parent class method')
@staticmethod
def m3():
1 print('Parent static method')
12 )
1class C(P):
1def __init__(self):
1super().__init__()
1super().m1()
1super().m2()
1super().m3()
19 )
20 ) def m1(self):
2 super().__init__()
2super().m1()
2super().m2()
2super().m3()
25 )
2c=C()
2c.m1()
```

**Output:
 Parent Constructor
 Parent instance method
 Parent class method
 Parent static method
 Parent Constructor
 Parent instance method**

**25**

```

```

**Parent class method
 Parent static method**

**Case-3: From child class, class method we cannot access parent class instance methods and
 constructors by using super() directly(but indirectly possible). But we can access parent class static
 and class methods.**

```
 class P:
def __init__(self):
print('Parent Constructor')
def m1(self):
print('Parent instance method')
@classmethod
def m2(cls):
print('Parent class method')
@staticmethod
def m3():
1 print('Parent static method')
12 )
1class C(P):
1@classmethod
1def m1(cls):
1#super().__init__()--->invalid
1#super().m1()--->invalid
1super().m2()
1super().m3()
20 )
2 C.m1()
```

**Output:
 Parent class method
 Parent static method**

**From Class Method of Child class,how to call parent class instance**

**methods and constructors:**

```
 class A:
def __init__(self):
print('Parent constructor')
4 )
def m1(self):
print('Parent instance method')
7 )
class B(A):
@classmethod
def m2(cls):
1 super(B,cls).__init__(cls)
1super(B,cls).m1(cls)
```

**26**

```

13 )
1B.m2()
```

**Output:
 Parent constructor
 Parent instance method**

**Case-4: In child class static method we are not allowed to use super() generally (But in special way
 we can use)**

```
 class P:
def __init__(self):
print('Parent Constructor')
def m1(self):
print('Parent instance method')
@classmethod
def m2(cls):
print('Parent class method')
@staticmethod
def m3():
1 print('Parent static method')
12 )
1class C(P):
1@staticmethod
1def m1():
1super().m1()-->invalid
1super().m2()--->invalid
1super().m3()--->invalid
19 )
20 ) C.m1()
```

**RuntimeError: super(): no arguments**

**How to call parent class static method from child class static method by using super():**

```
 class A:
2 )
@staticmethod
def m1():
print('Parent static method')
6 )
class B(A):
@staticmethod
def m2():
super(B,B).m1()
1
1B.m2()
```

**Output: Parent static method**

**1**

```

```

**Polymorphism**

**Poly means many. Morphs means forms.
 Polymorphism means 'Many Forms'.**

**Eg1: Yourself is best example of polymorphism.In front of Your parents You will have one type of
 behaviour and with friends another type of behaviour.Same person but different behaviours at
 different places,which is nothing but polymorphism.**

**Eg2: + operator acts as concatenation and arithmetic addition**

**Eg3: \* operator acts as multiplication and repetition operator**

**Eg4: The Same method with different implementations in Parent class and child
 classes.(overriding)**

**Related to polymorphism the following 4 topics are important**

**1. Duck Typing Philosophy of Python

1. Overloading
2. Operator Overloading
3. Method Overloading
4. Constructor Overloading
5. Overriding
6. Method overriding
7. constructor overriding
8. Duck Typing Philosophy of Python:**

**In Python we cannot specify the type explicitly. Based on provided value at runtime the type will
 be considered automatically. Hence Python is considered as Dynamically Typed Programming
 Language.**

**def f1(obj):
 obj.talk()**

**What is the type of obj? We cannot decide at the beginning. At runtime we can pass any type.Then
 how we can decide the type?
 At runtime if 'it walks like a duck and talks like a duck,it must be duck'. Python follows this
 principle. This is called Duck Typing Philosophy of Python.**

**2**

```

```

**Demo Program:**

```
 class Duck:
def talk(self):
print('Quack.. Quack..')
4 )
class Dog:
def talk(self):
print('Bow Bow..')
8 )
class Cat:
def talk(self):
1 print('Moew Moew ..')
12 )
1class Goat:
1def talk(self):
1print('Myaah Myaah ..')
16 )
1def f1(obj):
1obj.talk()
19 )
20 ) l=[Duck(),Cat(),Dog(),Goat()]
2 for obj in l:
2f1(obj)
```

**Output:
 Quack.. Quack..
 Moew Moew ..
 Bow Bow..
 Myaah Myaah ..**

**The problem in this approach is if obj does not contain talk() method then we will get
 AttributeError**

**Eg:**

```
 class Duck:
def talk(self):
print('Quack.. Quack..')
4 )
class Dog:
def bark(self):
print('Bow Bow..')
def f1(obj):
obj.talk()
10 )
1 d=Duck()
1f1(d)
13 )
```

**3**

```

1d=Dog()
1f1(d)
```

**Output:
 D:\durga_classes>py test.py
 Quack.. Quack..
 Traceback (most recent call last):
 File "test.py", line 22, in 
 f1(d)
 File "test.py", line 13, in f1
 obj.talk()
 AttributeError: 'Dog' object has no attribute 'talk'**

**But we can solve this problem by using hasattr() function.**

**hasattr(obj,'attributename')
 attributename can be method name or variable name**

**Demo Program with hasattr() function:**

```
 class Duck:
def talk(self):
print('Quack.. Quack..')
4 )
class Human:
def talk(self):
print('Hello Hi...')
8 )
class Dog:
def bark(self):
1 print('Bow Bow..')
12 )
1def f1(obj):
1if hasattr(obj,'talk'):
1obj.talk()
1elif hasattr(obj,'bark'):
1obj.bark()
18 )
1d=Duck()
20 ) f1(d)
2
2h=Human()
2f1(h)
24 )
2d=Dog()
2f1(d)
2Myaah Myaah Myaah...
```

**4**

```

```

**Overloading:**

**We can use same operator or methods for different purposes.**

**Eg1: + operator can be used for Arithmetic addition and String concatenation
 print(10+20)#30
 print('durga'+'soft')#durgasoft**

**Eg2: \* operator can be used for multiplication and string repetition purposes.
 print(10\*20)#200
 print('durga'*3)#durgadurgadurga**

**Eg3: We can use deposit() method to deposit cash or cheque or dd
 deposit(cash)
 deposit(cheque)
 deposit(dd)**

**There are 3 types of overloading**

**1. Operator Overloading

1. Method Overloading
2. Constructor Overloading
3. Operator Overloading:**

**We can use the same operator for multiple purposes, which is nothing but operator overloading.**

**Python supports operator overloading.**

**Eg1: + operator can be used for Arithmetic addition and String concatenation
 print(10+20)#30
 print('durga'+'soft')#durgasoft**

**Eg2: \* operator can be used for multiplication and string repetition purposes.
 print(10\*20)#200
 print('durga'*3)#durgadurgadurga**

**Demo program to use + operator for our class objects:**

```
 class Book:
def __init__(self,pages):
self.pages=pages
4 )
b1=Book( 100 )
b2=Book( 200 )
print(b1+b2)
```

**5**

```

```

**D:\durga_classes>py test.py
 Traceback (most recent call last):
 File "test.py", line 7, in 
 print(b1+b2)
 TypeError: unsupported operand type(s) for +: 'Book' and 'Book'**

**We can overload + operator to work with Book objects also. i.e Python supports Operator
 Overloading.**

**For every operator Magic Methods are available. To overload any operator we have to override
 that Method in our class.
 Internally + operator is implemented by using \**add\**() method.This method is called magic
 method for + operator. We have to override this method in our class.**

**Demo program to overload + operator for our Book class objects:**

```
 class Book:
def __init__(self,pages):
self.pages=pages
4 )
def __add__(self,other):
return self.pages+other.pages
7 )
b1=Book( 100 )
b2=Book( 200 )
print('The Total Number of Pages:',b1+b2)
```

**Output: The Total Number of Pages: 300**

**The following is the list of operators and corresponding magic methods.**

**+ ---> object.\**add\**(self,other)**

**- ---> object.**sub**(self,other)

- ---> object.**mul**(self,other)
   / ---> object.**div**(self,other)
   // ---> object.**floordiv**(self,other)
   % ---> object.**mod**(self,other)
   ** ---> object.**pow**(self,other)
   += ---> object.**iadd**(self,other)

- = ---> object.**isub**(self,other)
   *= ---> object.**imul**(self,other)
   /= ---> object.**idiv**(self,other)
   //= ---> object.**ifloordiv**(self,other)
   %= ---> object.**imod**(self,other)
   **= ---> object.**ipow**(self,other)
   < ---> object.**lt**(self,other)
   <= ---> object.**le**(self,other)

> ---> object.**gt**(self,other)
>  = ---> object.**ge**(self,other)**

**6**

```

```

**== ---> object.\**eq\**(self,other)
 != ---> object.\**ne\**(self,other)**

**Overloading > and <= operators for Student class objects:**

```
 class Student:
def __init__(self,name,marks):
self.name=name
self.marks=marks
def __gt__(self,other):
return self.marks>other.marks
def __le__(self,other):
return self.marks<=other.marks
9 )
10 )
1 print("10>20 =", 10 > 20 )
1s1=Student("Durga", 100 )
1s2=Student("Ravi", 200 )
1print("s1>s2=",s1>s2)
1print("s1<s2=",s1<s2)
1print("s1<=s2=",s1<=s2)
1print("s1>=s2=",s1>=s2)
```

**Output:
 10>20 = False
 s1>s2= False
 s1<s2= True
 s1<=s2= True
 s1>=s2= False**

**Program to overload multiplication operator to work on Employee objects:**

```
 class Employee:
def __init__(self,name,salary):
self.name=name
self.salary=salary
def __mul__(self,other):
return self.salary*other.days
7 )
class TimeSheet:
def __init__(self,name,days):
self.name=name
1 self.days=days
12 )
1e=Employee('Durga', 500 )
1t=TimeSheet('Durga', 25 )
1print('This Month Salary:',e*t)
```

**Output: This Month Salary: 12500**

**7**

```

```

**2. Method Overloading:**

**If 2 methods having same name but different type of arguments then those methods are said to
 be overloaded methods.**

**Eg: m1(int a)
 m1(double d)**

**But in Python Method overloading is not possible.
 If we are trying to declare multiple methods with same name and different number of arguments
 then Python will always consider only last method.**

**Demo Program:**

```
 class Test:
def m1(self):
print('no-arg method')
def m1(self,a):
print('one-arg method')
def m1(self,a,b):
print('two-arg method')
8 )
t=Test()
#t.m1()
1 #t.m1(10)
1t.m1( 10 , 20 )
```

**Output: two-arg method**

**In the above program python will consider only last method.**

**How we can handle overloaded method requirements in Python:**

**Most of the times, if method with variable number of arguments required then we can handle
 with default arguments or with variable number of argument methods.**

**Demo Program with Default Arguments:**

```
 class Test:
def sum(self,a=None,b=None,c=None):
if a!=None and b!= None and c!= None:
print('The Sum of 3 Numbers:',a+b+c)
elif a!=None and b!= None:
print('The Sum of 2 Numbers:',a+b)
else:
print('Please provide 2 or 3 arguments')
9 )
t=Test()
```

**8**

```

1 t.sum( 10 , 20 )
1t.sum( 10 , 20 , 30 )
1t.sum( 10 )
```

**Output:
 The Sum of 2 Numbers: 30
 The Sum of 3 Numbers: 60
 Please provide 2 or 3 arguments**

**Demo Program with Variable Number of Arguments:**

```
 class Test:
def sum(self,*a):
total= 0
for x in a:
total=total+x
print('The Sum:',total)
7 )
8 )
t=Test()
t.sum( 10 , 20 )
1 t.sum( 10 , 20 , 30 )
1t.sum( 10 )
1t.sum()
```

**3. Constructor Overloading:**

**Constructor overloading is not possible in Python.
 If we define multiple constructors then the last constructor will be considered.**

```
 class Test:
def __init__(self):
print('No-Arg Constructor')
4 )
def __init__(self,a):
print('One-Arg constructor')
7 )
def __init__(self,a,b):
print('Two-Arg constructor')
#t1=Test()
1 #t1=Test(10)
1t1=Test( 10 , 20 )
```

**Output: Two-Arg constructor**

**9**

```

```

**In the above program only Two-Arg Constructor is available.**

**But based on our requirement we can declare constructor with default arguments and variable
 number of arguments.**

**Constructor with Default Arguments:**

```
 class Test:
def __init__(self,a=None,b=None,c=None):
print('Constructor with 0|1|2|3 number of arguments')
4 )
t1=Test()
t2=Test( 10 )
t3=Test( 10 , 20 )
t4=Test( 10 , 20 , 30 )
```

**Output:
 Constructor with 0|1|2|3 number of arguments
 Constructor with 0|1|2|3 number of arguments
 Constructor with 0|1|2|3 number of arguments
 Constructor with 0|1|2|3 number of arguments**

**Constructor with Variable Number of Arguments:**

```
 class Test:
def __init__(self,*a):
print('Constructor with variable number of arguments')
4 )
t1=Test()
t2=Test( 10 )
t3=Test( 10 , 20 )
t4=Test( 10 , 20 , 30 )
t5=Test( 10 , 20 , 30 , 40 , 50 , 60 )
```

**Output:
 Constructor with variable number of arguments
 Constructor with variable number of arguments
 Constructor with variable number of arguments
 Constructor with variable number of arguments
 Constructor with variable number of arguments**

**10**

```

```

**Method overriding:**

**What ever members available in the parent class are bydefault available to the child class through
 inheritance. If the child class not satisfied with parent class implementation then child class is
 allowed to redefine that method in the child class based on its requirement. This concept is called
 overriding.
 Overriding concept applicable for both methods and constructors.**

**Demo Program for Method overriding:**

```
 class P:
def property(self):
print('Gold+Land+Cash+Power')
def marry(self):
print('Appalamma')
class C(P):
def marry(self):
print('Katrina Kaif')
9 )
c=C()
1 c.property()
1c.marry()
```

**Output:
 Gold+Land+Cash+Power
 Katrina Kaif**

**From Overriding method of child class,we can call parent class method also by using super()
 method.**

```
 class P:
def property(self):
print('Gold+Land+Cash+Power')
def marry(self):
print('Appalamma')
class C(P):
def marry(self):
super().marry()
print('Katrina Kaif')
10 )
1 c=C()
1c.property()
1c.marry()
```

**Output:
 Gold+Land+Cash+Power
 Appalamma
 Katrina Kaif**

**11**

```

```

**Demo Program for Constructor overriding:**

```
 class P:
def __init__(self):
print('Parent Constructor')
4 )
class C(P):
def __init__(self):
print('Child Constructor')
8 )
c=C()
```

**Output: Child Constructor
 In the above example,if child class does not contain constructor then parent class constructor will
 be executed**

**From child class constuctor we can call parent class constructor by using super() method.**

**Demo Program to call Parent class constructor by using super():**

```
 class Person:
def __init__(self,name,age):
self.name=name
self.age=age
5 )
class Employee(Person):
def __init__(self,name,age,eno,esal):
super().__init__(name,age)
self.eno=eno
self.esal=esal
1
1def display(self):
1print('Employee Name:',self.name)
1print('Employee Age:',self.age)
1print('Employee Number:',self.eno)
1print('Employee Salary:',self.esal)
17 )
1e1=Employee('Durga', 48 , 872425 , 26000 )
1e1.display()
20 ) e2=Employee('Sunny', 39 , 872426 , 36000 )
2 e2.display()
```

**Output:
 Employee Name: Durga
 Employee Age: 48
 Employee Number: 872425
 Employee Salary: 26000
 Employee Name: Sunny
 Employee Age: 39**

**12**

```

```

**Employee Number: 872426
 Employee Salary: 36000**

**1**

```

```

**OOPs Part - 4**

**1. Abstract Method

1. Abstract class
2. Interface
3. Public,Private and Protected Members
4. **str**() method
5. Difference between str() and repr() functions
6. Small Banking Application**

**Abstract Method:**

**Sometimes we don't know about implementation,still we can declare a method. Such type of
 methods are called abstract methods.i.e abstract method has only declaration but not
 implementation.
 In python we can declare abstract method by using @abstractmethod decorator as follows.**

**@abstractmethod
 def m1(self): pass**

**@abstractmethod decorator present in abc module. Hence compulsory we should import abc
 module,otherwise we will get error.
 abc==>abstract base class module**

```
 class Test:
@abstractmethod
def m1(self):
pass
```

**NameError: name 'abstractmethod' is not defined**

**Eg:**

```
 from abc import *
class Test:
@abstractmethod
def m1(self):
pass
```

**2**

```

```

**Eg:**

```
 from abc import *
class Fruit:
@abstractmethod
def taste(self):
pass
```

**Child classes are responsible to provide implemention for parent class abstract methods.**

**Abstract class:**

**Some times implementation of a class is not complete,such type of partially implementation
 classes are called abstract classes. Every abstract class in Python should be derived from ABC class
 which is present in abc module.**

**Case-1:**

```
 from abc import *
class Test:
pass
4 )
t=Test()
```

**In the above code we can create object for Test class b'z it is concrete class and it does not conatin
 any abstract method.**

**Case-2:**

```
 from abc import *
class Test(ABC):
pass
4 )
t=Test()
```

**In the above code we can create object,even it is derived from ABC class,b'z it does not contain
 any abstract method.**

**Case-3:**

```
 from abc import *
class Test(ABC):
@abstractmethod
def m1(self):
pass
6 )
t=Test()
```

**3**

```

```

**TypeError: Can't instantiate abstract class Test with abstract methods m1**

**Case-4:**

```
 from abc import *
class Test:
@abstractmethod
def m1(self):
pass
6 )
t=Test()
```

**We can create object even class contains abstract method b'z we are not extending ABC class.**

**Case-5:**

```
 from abc import *
class Test:
@abstractmethod
def m1(self):
print('Hello')
6 )
t=Test()
t.m1()
```

**Output: Hello**

**Conclusion: If a class contains atleast one abstract method and if we are extending ABC class then
 instantiation is not possible.**

**"abstract class with abstract method instantiation is not possible"**

**Parent class abstract methods should be implemented in the child classes. otherwise we cannot
 instantiate child class.If we are not creating child class object then we won't get any error.**

**Case-1:**

```
 from abc import *
class Vehicle(ABC):
@abstractmethod
def noofwheels(self):
pass
6 )
class Bus(Vehicle): pass
```

**It is valid b'z we are not creating Child class object**

**4**

```

```

**Case-2:**

```
 from abc import *
class Vehicle(ABC):
@abstractmethod
def noofwheels(self):
pass
6 )
class Bus(Vehicle): pass
b=Bus()
```

**TypeError: Can't instantiate abstract class Bus with abstract methods noofwheels**

**Note: If we are extending abstract class and does not override its abstract method then child class
 is also abstract and instantiation is not possible.**

**Eg:**

```
 from abc import *
class Vehicle(ABC):
@abstractmethod
def noofwheels(self):
pass
6 )
class Bus(Vehicle):
def noofwheels(self):
return 7
10 )
1 class Auto(Vehicle):
1def noofwheels(self):
1return 3
1b=Bus()
1print(b.noofwheels())#7
16 )
1a=Auto()
1print(a.noofwheels())#3
```

**Note: Abstract class can contain both abstract and non-abstract methods also.**

**5**

```

```

**Interfaces In Python:**

**In general if an abstract class contains only abstract methods such type of abstract class is
 considered as interface.**

**Demo program:**

```
 from abc import *
class DBInterface(ABC):
@abstractmethod
def connect(self):pass
5 )
@abstractmethod
def disconnect(self):pass
8 )
class Oracle(DBInterface):
def connect(self):
1 print('Connecting to Oracle Database...')
1def disconnect(self):
1print('Disconnecting to Oracle Database...')
14 )
1class Sybase(DBInterface):
1def connect(self):
1print('Connecting to Sybase Database...')
1def disconnect(self):
1print('Disconnecting to Sybase Database...')
20 )
2 dbname=input('Enter Database Name:')
2classname=globals()[dbname]
2x=classname()
2x.connect()
2x.disconnect()
```

**D:\durga_classes>py test.py
 Enter Database Name:Oracle
 Connecting to Oracle Database...
 Disconnecting to Oracle Database...**

**D:\durga_classes>py test.py
 Enter Database Name:Sybase
 Connecting to Sybase Database...
 Disconnecting to Sybase Database...**

**Note: The inbuilt function globals()[str] converts the string 'str' into a class name and returns the
 classname.**

**6**

```

```

**Demo Program-2: Reading class name from the file**

**config.txt:
 EPSON**

**test.py:**

```
 from abc import *
class Printer(ABC):
@abstractmethod
def printit(self,text):pass
5 )
@abstractmethod
def disconnect(self):pass
8 )
class EPSON(Printer):
def printit(self,text):
1 print('Printing from EPSON Printer...')
1print(text)
1def disconnect(self):
1print('Printing completed on EPSON Printer...')
15 )
1class HP(Printer):
1def printit(self,text):
1print('Printing from HP Printer...')
1print(text)
20 ) def disconnect(self):
2 print('Printing completed on HP Printer...')
22 )
2with open('config.txt','r') as f:
2pname=f.readline()
25 )
2classname=globals()[pname]
2x=classname()
2x.printit('This data has to print...')
2x.disconnect()
```

**Output:
 Printing from EPSON Printer...
 This data has to print...
 Printing completed on EPSON Printer...**

**7**

```

```

**Concreate class vs Abstract Class vs Inteface:**

**1. If we dont know anything about implementation just we have requirement specification then
 we should go for interface.

1. If we are talking about implementation but not completely then we should go for abstract
    class.(partially implemented class)
2. If we are talking about implementation completely and ready to provide service then we should
    go for concrete class.**

```
 from abc import *
class CollegeAutomation(ABC):
@abstractmethod
def m1(self): pass
@abstractmethod
def m2(self): pass
@abstractmethod
def m3(self): pass
class AbsCls(CollegeAutomation):
def m1(self):
1 print('m1 method implementation')
1def m2(self):
1print('m2 method implementation')
14 )
1class ConcreteCls(AbsCls):
1def m3(self):
1print('m3 method implemnentation')
18 )
1c=ConcreteCls()
20 ) c.m1()
2 c.m2()
2c.m3()
```

**Public, Protected and Private Attributes:**

**By default every attribute is public. We can access from anywhere either within the class or from
 outside of the class.**

**Eg:
 name='durga'**

**Protected attributes can be accessed within the class anywhere but from outside of the class only
 in child classes. We can specify an attribute as protected by prefexing with _ symbol.**

**syntax:
 _variablename=value**

**8**

```

```

**Eg:
 _name='durga'**

**But is is just convention and in reality does not exists protected attributes.**

**private attributes can be accessed only within the class.i.e from outside of the class we cannot
 access. We can declare a variable as private explicitly by prefexing with 2 underscore symbols.**

**syntax: __variablename=value**

**Eg: __name='durga'**

**Demo Program:**

```
 class Test:
x= 10
_y= 20
__z= 30
def m1(self):
print(Test.x)
print(Test._y)
print(Test.__z)
9 )
t=Test()
1 t.m1()
1print(Test.x)
1print(Test._y)
1print(Test.__z)
```

**Output:
 10
 20
 30
 10
 20
 Traceback (most recent call last):
 File "test.py", line 14, in 
 print(Test.__z)
 AttributeError: type object 'Test' has no attribute '__z'**

**9**

```

```

**How to access private variables from outside of the class:**

**We cannot access private variables directly from outside of the class.
 But we can access indirectly as follows**

**objectreference._classname__variablename**

**Eg:**

```
 class Test:
def __init__(self):
self.__x= 10
4 )
t=Test()
print(t._Test__x)#10
```

***\*str\**() method:**

**Whenever we are printing any object reference internally \**str\**() method will be called which is
 returns string in the following format**

**<\**main\**.classname object at 0x022144B0>**

**To return meaningful string representation we have to override \**str\**() method.**

**Demo Program:**

```
 class Student:
def __init__(self,name,rollno):
self.name=name
self.rollno=rollno
5 )
def __str__(self):
return 'This is Student with Name:{} and Rollno:{}'.format(self.name,self.rollno)
8 )
s1=Student('Durga', 10
s2=Student('Ravi', 102 )
1 print(s1)
1print(s2)
```

**output without overriding \**str\**():**

**<\**main\**.Student object at 0x022144B0>
 <\**main\**.Student object at 0x022144D0>**

**10**

```

```

**output with overriding \**str\**():**

**This is Student with Name:Durga and Rollno:101
 This is Student with Name:Ravi and Rollno:102**

**Difference between str() and repr() OR Difference between \**str\**() and \**repr\**()**

**str() internally calls \**str\**() function and hence functionality of both is same**

**Similarly,repr() internally calls \**repr\**() function and hence functionality of both is same.**

**str() returns a string containing a nicely printable representation object.
 The main purpose of str() is for readability.It may not possible to convert result string to original
 object.**

**Eg:**

```
 import datetime
today=datetime.datetime.now()
s=str(today)#converting datetime object to str
print(s)
d=eval(s)#converting str object to datetime
```

**D:\durgaclasses>py test.py
 2018 - 05 - 18 22:48:19.890888
 Traceback (most recent call last):
 File "test.py", line 5, in 
 d=eval(s)#converting str object to datetime
 File "", line 1
 2018 - 05 - 18 22:48:19.890888
 ^
 SyntaxError: invalid token**

**But repr() returns a string containing a printable representation of object.
 The main goal of repr() is unambigouous. We can convert result string to original object by using
 eval() function,which may not possible in str() function.**

**Eg:**

```
 import datetime
today=datetime.datetime.now()
s=repr(today)#converting datetime object to str
print(s)
d=eval(s)#converting str object to datetime
print(d)
```

**Output:
 datetime.datetime(2018, 5, 18, 22, 51, 10, 875838)
 2018 - 05 - 18 22:51:10.875838**

**11**

```

```

**Note: It is recommended to use repr() instead of str()**

**Mini Project: Banking Application**

```
 class Account:
def __init__(self,name,balance,min_balance):
self.name=name
self.balance=balance
self.min_balance=min_balance
6 )
def deposit(self,amount):
self.balance +=amount
9 )
def withdraw(self,amount):
1 if self.balance-amount >= self.min_balance:
1self.balance - =amount
1else:
1print("Sorry, Insufficient Funds")
15 )
1def printStatement(self):
1print("Account Balance:",self.balance)
18 )
1class Current(Account):
20 ) def __init__(self,name,balance):
2 super().__init__(name,balance,min_balance=- 1000 )
2def __str__(self):
2return "{}'s Current Account with Balance :{}".format(self.name,self.balance)
24 )
2class Savings(Account):
2def __init__(self,name,balance):
2super().__init__(name,balance,min_balance= 0 )
2def __str__(self):
2return "{}'s Savings Account with Balance :{}".format(self.name,self.balance)
30 )
3 c=Savings("Durga", 10000 )
3print(c)
3c.deposit( 5000 )
3c.printStatement()
3c.withdraw( 16000 )
3c.withdraw( 15000 )
3print(c)
38 )
3c2=Current('Ravi', 20000 )
40 ) c2.deposit( 6000 )
4 print(c2)
4c2.withdraw( 27000 )
4print(c2)
```

**12**

```

```

**Output:
 D:\durgaclasses>py test.py
 Durga's Savings Account with Balance :10000
 Account Balance: 15000
 Sorry, Insufficient Funds
 Durga's Savings Account with Balance :0
 Ravi's Current Account with Balance :26000
 Ravi's Current Account with Balance :- 1000**

**1**

```

```

**Regular Expressions**

**If we want to represent a group of Strings according to a particular format/pattern then we
 should go for Regular Expressions.**

**i.e Regualr Expressions is a declarative mechanism to represent a group of Strings accroding to
 particular format/pattern.**

**Eg 1: We can write a regular expression to represent all mobile numbers**

**Eg 2: We can write a regular expression to represent all mail ids.**

**The main important application areas of Regular Expressions are**

**1. To develop validation frameworks/validation logic

1. To develop Pattern matching applications (ctrl-f in windows, grep in UNIX etc)
2. To develop Translators like compilers, interpreters etc
3. To develop digital circuits
4. To develop communication protocols like TCP/IP, UDP etc.**

**We can develop Regular Expression Based applications by using python module: re
 This module contains several inbuilt functions to use Regular Expressions very easily in our
 applications.**

**1. compile()**

**re module contains compile() function to compile a pattern into RegexObject.**

**pattern = re.compile("ab")**

**2. finditer():**

**Returns an Iterator object which yields Match object for every Match**

**matcher = pattern.finditer("abaababa")**

**On Match object we can call the following methods.**

**1. start()**  **Returns start index of the match

1. end()**  **Returns end+1 index of the match
2. group()**  **Returns the matched string**

**2**

```

```

**Eg:**

```
1) import re count= 0
2) pattern=re.compile("ab")
3) matcher=pattern.finditer("abaababa")
4) for match in matcher:
5) count+= 1
6) print(match.start(),"...",match.end(),"...",match.group())
7) print("The number of occurrences: ",count)
```

**Output:
 0 ... 2 ... ab
 3 ... 5 ... ab
 5 ... 7 ... ab
 The number of occurrences: 3**

**Note: We can pass pattern directly as argument to finditer() function.**

**Eg:**

```
1) import re
2) count= 0
3) matcher=re.finditer("ab","abaababa")
4) for match in matcher:
5) count+= 1
6) print(match.start(),"...",match.end(),"...",match.group())
7) print("The number of occurrences: ",count)
```

**Output:**

**0 ... 2 ... ab
 3 ... 5 ... ab
 5 ... 7 ... ab
 The number of occurrences: 3**

**Character classes:**

**We can use character classes to search a group of characters**

**1. [abc]===>Either a or b or c

1. [^abc] ===>Except a and b and c
2. [a-z]==>Any Lower case alphabet symbol
3. [A-Z]===>Any upper case alphabet symbol
4. [a-zA-Z]==>Any alphabet symbol
5. [0-9] Any digit from 0 to 9
6. [a-zA-Z0-9]==>Any alphanumeric character
7. [^a-zA-Z0-9]==>Except alphanumeric characters(Special Characters)**

**3**

```

```

**Eg:**

```
1) import re
2) matcher=re.finditer("x","a7b@k9z")
3) for match in matcher:
4) print(match.start(),"......",match.group())
```

**x = [abc]
 0 ...... a
 2 ...... b**

**x = [^abc]
 1 ...... 7
 3 ...... @
 4 ...... k
 5 ...... 9
 6 ...... z**

**x = [a-z]
 0 ...... a
 2 ...... b
 4 ...... k
 6 ...... z**

**x = [0-9]
 1 ...... 7
 5 ...... 9**

**x = [a-zA-Z0-9]
 0 ...... a
 1 ...... 7
 2 ...... b
 4 ...... k
 5 ...... 9
 6 ...... z**

**x = [^a-zA-Z0-9]
 3 ...... @**

**Pre defined Character classes:**

**\s**  **Space character
 \S**  **Any character except space character
 \d**  **Any digit from 0 to 9
 \D**  **Any character except digit
 \w**  **Any word character [a-zA-Z0-9]
 \W**  **Any character except word character (Special Characters)**

**.**  **Any character including special characters**

**4**

```

```

**Eg:**

```
1) import re
2) matcher=re.finditer("x","a7b k@9z")
3) for match in matcher:
4) print(match.start(),"......",match.group())
```

**x = \s:
 3 ......**

**x = \S:
 0 ...... a
 1 ...... 7
 2 ...... b
 4 ...... k
 5 ...... @
 6 ...... 9
 7 ...... z**

**x = \d:
 1 ...... 7
 6 ...... 9**

**x = \D:
 0 ...... a
 2 ...... b
 3 ......
 4 ...... k
 5 ...... @
 7 ...... z**

**x = \w:
 0 ...... a
 1 ...... 7
 2 ...... b
 4 ...... k
 6 ...... 9
 7 ...... z**

**x = \W:
 3 ......
 5 ...... @**

**x =.
 0 ...... a
 1 ...... 7
 2 ...... b
 3 ......**

**5**

```

```

**4 ...... k
 5 ...... @
 6 ...... 9
 7 ...... z**

**Qunatifiers:**

**We can use quantifiers to specify the number of occurrences to match.**

**a**  **Exactly one 'a'
 a+**  **Atleast one 'a'
 a***  **Any number of a's including zero number
 a?**  **Atmost one 'a' ie either zero number or one number
 a{m}**  **Exactly m number of a's
 a{m,n}**  **Minimum m number of a's and Maximum n number of a's**

**Eg:**

```
1) import re
2) matcher=re.finditer("x","abaabaaab")
3) for match in matcher:
4) print(match.start(),"......",match.group())
```

**x = a:
 0 ...... a
 2 ...... a
 3 ...... a
 5 ...... a
 6 ...... a
 7 ...... a**

**x = a+:
 0 ...... a
 2 ...... aa
 5 ...... aaa**

**x = a\*:
 0 ...... a
 1 ......
 2 ...... aa
 4 ......
 5 ...... aaa
 8 ......
 9 ......**

**6**

```

```

**x = a?:
 0 ...... a
 1 ......
 2 ...... a
 3 ...... a
 4 ......
 5 ...... a
 6 ...... a
 7 ...... a
 8 ......
 9 ......**

**x = a{3}:
 5 ...... aaa**

**x = a{2,4}:
 2 ...... aa
 5 ...... aaa**

**Note:
 ^x**  **It will check whether target string starts with x or not
 x$**  **It will check whether target string ends with x or not**

**Important functions of re module:**

**1. match()

1. fullmatch()
2. search()
    4.findall()
    5.finditer()
3. sub()
    7.subn()
4. split()
5. compile()
6. match():**

**We can use match function to check the given pattern at beginning of target string.
 If the match is available then we will get Match object, otherwise we will get None.**

**Eg:**

```
1) import re
2) s=input("Enter pattern to check: ")
3) m=re.match(s,"abcabdefg")
4) if m!= None:
5) print("Match is available at the beginning of the String")
6) print("Start Index:",m.start(), "and End Index:",m.end())
```

**7**

```

7) else:
8) print("Match is not available at the beginning of the String")
```

**Output:**

**D:\python_classes>py test.py
 Enter pattern to check: abc
 Match is available at the beginning of the String
 Start Index: 0 and End Index: 3**

**D:\python_classes>py test.py
 Enter pattern to check: bde
 Match is not available at the beginning of the String**

**2. fullmatch():**

**We can use fullmatch() function to match a pattern to all of target string. i.e complete string
 should be matched according to given pattern.
 If complete string matched then this function returns Match object otherwise it returns None.**

**Eg:**

```
1) import re
2) s=input("Enter pattern to check: ")
3) m=re.fullmatch(s,"ababab")
4) if m!= None:
5) print("Full String Matched")
6) else:
7) print("Full String not Matched")
```

**Output:**

**D:\python_classes>py test.py
 Enter pattern to check: ab
 Full String not Matched**

**D:\python_classes>py test.py
 Enter pattern to check: ababab
 Full String Matched**

**3. search():**

**We can use search() function to search the given pattern in the target string.
 If the match is available then it returns the Match object which represents first occurrence of the
 match.
 If the match is not available then it returns None**

**8**

```

```

**Eg:**

```
1) import re
2) s=input("Enter pattern to check: ")
3) m=re.search(s,"abaaaba")
4) if m!= None:
5) print("Match is available")
6) print("First Occurrence of match with start index:",m.start(),"and end index:",m.end())
7) else:
8) print("Match is not available")
```

**Output:**

**D:\python_classes>py test.py
 Enter pattern to check: aaa
 Match is available
 First Occurrence of match with start index: 2 and end index: 5**

**D:\python_classes>py test.py
 Enter pattern to check: bbb
 Match is not available**

**4. findall():**

**To find all occurrences of the match.
 This function returns a list object which contains all occurrences.**

**Eg:**

```
1) import re
2) l=re.findall("[0-9]","a7b9c5kz")
3) print(l)
```

**Output: ['7', '9', '5']**

**5. finditer():**

**Returns the iterator yielding a match object for each match.
 On each match object we can call start(), end() and group() functions.**

**Eg:**

```
1) import re
2) itr=re.finditer("[a-z]","a7b9c5k8z")
3) for m in itr:
4) print(m.start(),"...",m.end(),"...",m.group())
```

**9**

```

```

**Output:
 D:\python_classes>py test.py
 0 ... 1 ... a
 2 ... 3 ... b
 4 ... 5 ... c
 6 ... 7 ... k
 8 ... 9 ... z**

**6. sub():**

**sub means substitution or replacement**

**re.sub(regex,replacement,targetstring)
 In the target string every matched pattern will be replaced with provided replacement.**

**Eg:**

```
1) import re
2) s=re.sub("[a-z]","#","a7b9c5k8z")
3) print(s)
```

**Output: #7#9#5#8#**

**Every alphabet symbol is replaced with # symbol**

**7. subn():**

**It is exactly same as sub except it can also returns the number of replacements.
 This function returns a tuple where first element is result string and second element is number of
 replacements.
 (resultstring, number of replacements)**

**Eg:**

```
1) import re
2) t=re.subn("[a-z]","#","a7b9c5k8z")
3) print(t)
4) print("The Result String:",t[ 0 ])
5) print("The number of replacements:",t[ 1 ])
```

**Output:
 D:\python_classes>py test.py
 ('#7#9#5#8#', 5)
 The Result String: #7#9#5#8#
 The number of replacements: 5**

**10**

```

```

**8. split():**

**If we want to split the given target string according to a particular pattern then we should go for
 split() function.
 This function returns list of all tokens.**

**Eg:**

```
1) import re
2) l=re.split(",","sunny,bunny,chinny,vinny,pinny")
3) print(l)
4) for t in l:
5) print(t)
```

**Output:
 D:\python_classes>py test.py
 ['sunny', 'bunny', 'chinny', 'vinny', 'pinny']
 sunny
 bunny
 chinny
 vinny
 pinny**

**Eg:**

```
1) import re
2) l=re.split("\.","www.durgasoft.com")
3) for t in l:
4) print(t)
```

**Output:
 D:\python_classes>py test.py
 www
 durgasoft
 com**

**^ symbol:**

**We can use ^ symbol to check whether the given target string starts with our provided pattern or
 not.**

**Eg:
 res=re.search("^Learn",s)
 if the target string starts with Learn then it will return Match object,otherwise returns None.**

**11**

```

```

**test.py:**

```
1) import re
2) s="Learning Python is Very Easy"
3) res=re.search("^Learn",s)
4) if res != None:
5) print("Target String starts with Learn")
6) else:
7) print("Target String Not starts with Learn")
```

**Output: Target String starts with Learn**

**$ symbol:**

**We can use $ symbol to check whether the given target string ends with our provided pattern or
 not**

**Eg: res=re.search("Easy$",s)**

**If the target string ends with Easy then it will return Match object,otherwise returns None.**

**test.py:**

```
1) import re
2) s="Learning Python is Very Easy"
3) res=re.search("Easy$",s)
4) if res != None:
5) print("Target String ends with Easy")
6) else:
7) print("Target String Not ends with Easy")
```

**Output: Target String ends with Easy**

**Note: If we want to ignore case then we have to pass 3rd argument re.IGNORECASE for search()
 function.**

**Eg: res = re.search("easy$",s,re.IGNORECASE)**

**test.py:**

```
1) import re
2) s="Learning Python is Very Easy"
3) res=re.search("easy$",s,re.IGNORECASE)
4) if res != None:
5) print("Target String ends with Easy by ignoring case")
6) else:
7) print("Target String Not ends with Easy by ignoring case")
```

**12**

```

```

**Output: Target String ends with Easy by ignoring case**

**App1: Write a Regular Expression to represent all Yava language identifiers**

**Rules:**

**1. The allowed characters are a-z,A-Z,0-9,#

1. The first character should be a lower case alphabet symbol from a to k
2. The second character should be a digit divisible by 3
3. The length of identifier should be atleast 2.**

**[a-k][0369][a-zA-Z0-9#]***

**App2: Write a python program to check whether the given string is Yava**

**language identifier or not?**

```
1) import re
2) s=input("Enter Identifier:")
3) m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
4) if m!= None:
5) print(s,"is valid Yava Identifier")
6) else:
7) print(s,"is invalid Yava Identifier")
```

**Output:**

**D:\python_classes>py test.py
 Enter Identifier:a6kk9z##
 a6kk9z## is valid Yava Identifier**

**D:\python_classes>py test.py
 Enter Identifier:k9b876
 k9b876 is valid Yava Identifier**

**D:\python_classes>py test.py
 Enter Identifier:k7b9
 k7b9 is invalid Yava Identifier**

**App3: Write a Regular Expression to represent all 10 digit mobile numbers.**

**Rules:**

**1. Every number should contains exactly 10 digits

1. The first digit should be 7 or 8 or 9**

**[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]
 or**

**13**

```

```

**[7-9][0-9]{9}
 or
 [7-9]\d{9}**

**App4: Write a Python Program to check whether the given number**

**is valid mobile number or not?**

```
1) import re
2) n=input("Enter number:")
3) m=re.fullmatch("[7-9]\d{9}",n)
4) if m!= None:
5) print("Valid Mobile Number")
6) else:
7) print("Invalid Mobile Number")
```

**Output:**

**D:\python_classes>py test.py
 Enter number:9898989898
 Valid Mobile Number**

**D:\python_classes>py test.py
 Enter number:6786786787
 Invalid Mobile Number**

**D:\python_classes>py test.py
 Enter number:898989
 Invalid Mobile Number**

**App5: Write a python program to extract all mobile numbers present in**

**input.txt where numbers are mixed with normal text data**

```
1) import re
2) f1=open("input.txt","r")
3) f2=open("output.txt","w")
4) for line in f1:
5) list=re.findall("[7-9]\d{9}",line)
6) for n in list:
7) f2.write(n+"\n")
8) print("Extracted all Mobile Numbers into output.txt")
9) f1.close()
10) f2.close()
```

**14**

```

```

**Web Scraping by using Regular Expressions:**

**The process of collecting information from web pages is called web scraping. In web scraping to
 match our required patterns like mail ids, mobile numbers we can use regular expressions.**

**Eg:**

```
1) import re,urllib
2) import urllib.request
3) sites="google rediff".split()
4) print(sites)
5) for s in sites:
6) print("Searching...",s)
7) u=urllib.request.urlopen("http://"+s+".com")
8) text=u.read()
9) title=re.findall("<title>.*</title>",str(text),re.I)
10) print(title[ 0 ])
```

**Eg: Program to get all phone numbers of redbus.in by using web**

**scraping and regular expressions**

```
1) import re,urllib
2) import urllib.request
3) u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
4) text=u.read()
5) numbers=re.findall("[0- 9 - ]{7}[0- 9 - ]+",str(text),re.I)
6) for n in numbers:
7) print(n)
```

**Q. Write a Python Program to check whether the given mail id is**

**valid gmail id or not?**

```
1) import re
2) s=input("Enter Mail id:")
3) m=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",s)
4) if m!=None:
5) print("Valid Mail Id");
6) else:
7) print("Invalid Mail id")
```

**Output:**

**D:\python_classes>py test.py
 Enter Mail id:durgatoc@gmail.com
 Valid Mail Id**

**15**

```

```

**D:\python_classes>py test.py
 Enter Mail id:durgatoc
 Invalid Mail id**

**D:\python_classes>py test.py
 Enter Mail id:durgatoc@yahoo.co.in
 Invalid Mail id**

**Q. Write a python program to check whether given car registration**

**number is valid Telangana State Registration number or not?**

```
1) import re
2) s=input("Enter Vehicle Registration Number:")
3) m=re.fullmatch("TS[012][0-9][A-Z]{2}\d{4}",s)
4) if m!=None:
5) print("Valid Vehicle Registration Number");
6) else:
7) print("Invalid Vehicle Registration Number")
```

**Output:**

**D:\python_classes>py test.py
 Enter Vehicle Registration Number:TS07EA7777
 Valid Vehicle Registration Number**

**D:\python_classes>py test.py
 Enter Vehicle Registration Number:TS07KF0786
 Valid Vehicle Registration Number**

**D:\python_classes>py test.py
 Enter Vehicle Registration Number:AP07EA7898
 Invalid Vehicle Registration Number**

**Q. Python Program to check whether the given mobile number is**

**valid OR not (10 digit OR 11 digit OR 12 digit)**

```
1) import re
2) s=input("Enter Mobile Number:")
3) m=re.fullmatch("(0|91)?[7-9][0-9]{9}",s)
4) if m!=None:
5) print("Valid Mobile Number");
6) else:
7) print("Invalid Mobile Number")
```

**Summary table and some more examples.**

**1**

```

```

**Multi Threading**

**Multi Tasking:**

**Executing several tasks simultaneously is the concept of multitasking.**

**There are 2 types of Multi Tasking**

**1. Process based Multi Tasking

1. Thread based Multi Tasking
2. Process based Multi Tasking:**

**Executing several tasks simmultaneously where each task is a seperate independent process is
 called process based multi tasking.**

**Eg: while typing python program in the editor we can listen mp3 audio songs from the same
 system. At the same time we can download a file from the internet. All these taks are executing
 simultaneously and independent of each other. Hence it is process based multi tasking.**

**This type of multi tasking is best suitable at operating system level.**

**2. Thread based MultiTasking:**

**Executing several tasks simultaneously where each task is a seperate independent part of the
 same program, is called Thread based multi tasking, and each independent part is called a Thread.**

**This type of multi tasking is best suitable at programmatic level.**

**Note: Whether it is process based or thread based, the main advantage of multi tasking is to
 improve performance of the system by reducing response time.**

**The main important application areas of multi threading are:**

**1. To implement Multimedia graphics

1. To develop animations
2. To develop video games
3. To develop web and application servers
    etc...**

**Note: Where ever a group of independent jobs are available, then it is highly recommended to
 execute simultaneously instead of executing one by one.For such type of cases we should go for
 Multi Threading.**

**Python provides one inbuilt module "threading" to provide support for developing threads. Hence
 developing multi threaded Programs is very easy in python.**

**2**

```

```

**Every Python Program by default contains one thread which is nothing but MainThread.**

**Q.Program to print name of current executing thread:**

```
1) import threading
2) print("Current Executing Thread:",threading.current_thread().getName())
```

**o/p: Current Executing Thread: MainThread**

**Note: threading module contains function current_thread() which returns the current executing
 Thread object. On this object if we call getName() method then we will get current executing
 thread name.**

**The ways of Creating Thread in Python:**

**We can create a thread in Python by using 3 ways**

**1. Creating a Thread without using any class

1. Creating a Thread by extending Thread class
2. Creating a Thread without extending Thread class
3. Creating a Thread without using any class:**

```
1) from threading import *
2) def display():
3) for i in range( 1 , 1:
4) print("Child Thread")
5) t=Thread(target=display) #creating Thread object
6) t.start() #starting of Thread
7) for i in range( 1 , 1:
8) print("Main Thread")
```

**If multiple threads present in our program, then we cannot expect execution order and hence we
 cannot expect exact output for the multi threaded programs. B'z of this we cannot provide exact
 output for the above program.It is varied from machine to machine and run to run.**

**Note: Thread is a pre defined class present in threading module which can be used to create our
 own Threads.**

**2. Creating a Thread by extending Thread class**

**We have to create child class for Thread class. In that child class we have to override run() method
 with our required job. Whenever we call start() method then automatically run() method will be
 executed and performs our job.**

```
1) from threading import *
2) class MyThread(Thread):
```

**3**

```

3) def run(self):
4) for i in range( 10 ):
5) print("Child Thread-1")
6) t=MyThread()
7) t.start()
8) for i in range( 10 ):
9) print("Main Thread-1")
```

**3. Creating a Thread without extending Thread class:**

```
1) from threading import *
2) class Test:
3) def display(self):
4) for i in range( 10 ):
5) print("Child Thread-2")
6) obj=Test()
7) t=Thread(target=obj.display)
8) t.start()
9) for i in range( 10 ):
10) print("Main Thread-2")
```

**Without multi threading:**

```
1) from threading import *
2) import time
3) def doubles(numbers):
4) for n in numbers:
5) time.sleep( 
6) print("Double:", 2 *n)
7) def squares(numbers):
8) for n in numbers:
9) time.sleep( 
10) print("Square:",n*n)
11) numbers=[ 1 , 2 , 3 , 4 , 5 , 6 ]
12) begintime=time.time()
13) doubles(numbers)
14) squares(numbers)
15) print("The total time taken:",time.time()-begintime)
```

**With multithreading:**

```
1) from threading import *
2) import time
3) def doubles(numbers):
4) for n in numbers:
5) time.sleep( 
6) print("Double:", 2 *n)
7) def squares(numbers):
8) for n in numbers:
```

**4**

```

9) time.sleep( 
10) print("Square:",n*n)
11)
12) numbers=[ 1 , 2 , 3 , 4 , 5 , 6 ]
13) begintime=time.time()
14) t1=Thread(target=doubles,args=(numbers,))
15) t2=Thread(target=squares,args=(numbers,))
16) t1.start()
17) t2.start()
18) t1.join()
19) t2.join()
20) print("The total time taken:",time.time()-begintime)
```

**Setting and Getting Name of a Thread:**

**Every thread in python has name. It may be default name generated by Python or Customized
 Name provided by programmer.**

**We can get and set name of thread by using the following Thread class methods.**

**t.getName()**  **Returns Name of Thread
 t.setName(newName)**  **To set our own name**

**Note: Every Thread has implicit variable "name" to represent name of Thread.**

**Eg:**

```
1) from threading import *
2) print(current_thread().getName())
3) current_thread().setName("Pawan Kalyan")
4) print(current_thread().getName())
5) print(current_thread().name)
```

**Output:
 MainThread
 Pawan Kalyan
 Pawan Kalyan**

**Thread Identification Number (ident):**

**For every thread internally a unique identification number is available. We can access this id by
 using implicit variable "ident"**

```
1) from threading import *
2) def test():
3) print("Child Thread")
4) t=Thread(target=test)
```

**5**

```

5) t.start()
6) print("Main Thread Identification Number:",current_thread().ident)
7) print("Child Thread Identification Number:",t.ident)
```

**Output:
 Child Thread
 Main Thread Identification Number: 2492
 Child Thread Identification Number: 2768**

**active_count():**

**This function returns the number of active threads currently running.**

**Eg:**

```
1) from threading import *
2) import time
3) def display():
4) print(current_thread().getName(),"...started")
5) time.sleep( 3 )
6) print(current_thread().getName(),"...ended")
7) print("The Number of active Threads:",active_count())
8) t1=Thread(target=display,name="ChildThread1")
9) t2=Thread(target=display,name="ChildThread2")
10) t3=Thread(target=display,name="ChildThread3")
11) t1.start()
12) t2.start()
13) t3.start()
14) print("The Number of active Threads:",active_count())
15) time.sleep( 5 )
16) print("The Number of active Threads:",active_count())
```

**Output:
 D:\python_classes>py test.py
 The Number of active Threads: 1
 ChildThread1 ...started
 ChildThread2 ...started
 ChildThread3 ...started
 The Number of active Threads: 4
 ChildThread1 ...ended
 ChildThread2 ...ended
 ChildThread3 ...ended
 The Number of active Threads: 1**

**enumerate() function:**

**This function returns a list of all active threads currently running.**

**Eg:**

**6**

```

1) from threading import *
2) import time
3) def display():
4) print(current_thread().getName(),"...started")
5) time.sleep( 3 )
6) print(current_thread().getName(),"...ended")
7) t1=Thread(target=display,name="ChildThread1")
8) t2=Thread(target=display,name="ChildThread2")
9) t3=Thread(target=display,name="ChildThread3")
10) t1.start()
11) t2.start()
12) t3.start()
13) l=enumerate()
14) for t in l:
15) print("Thread Name:",t.name)
16) time.sleep( 5 )
17) l=enumerate()
18) for t in l:
19) print("Thread Name:",t.name)
```

**Output:
 D:\python_classes>py test.py
 ChildThread1 ...started
 ChildThread2 ...started
 ChildThread3 ...started
 Thread Name: MainThread
 Thread Name: ChildThread1
 Thread Name: ChildThread2
 Thread Name: ChildThread3
 ChildThread1 ...ended
 ChildThread2 ...ended
 ChildThread3 ...ended
 Thread Name: MainThread**

**isAlive():**

**isAlive() method checks whether a thread is still executing or not.**

**Eg:**

```
1) from threading import *
2) import time
3) def display():
4) print(current_thread().getName(),"...started")
5) time.sleep( 3 )
6) print(current_thread().getName(),"...ended")
7) t1=Thread(target=display,name="ChildThread1")
8) t2=Thread(target=display,name="ChildThread2")
```

**7**

```

9) t1.start()
10) t2.start()
11)
12) print(t1.name,"is Alive :",t1.isAlive())
13) print(t2.name,"is Alive :",t2.isAlive())
14) time.sleep( 5 )
15) print(t1.name,"is Alive :",t1.isAlive())
16) print(t2.name,"is Alive :",t2.isAlive())
```

**Output:
 D:\python_classes>py test.py
 ChildThread1 ...started
 ChildThread2 ...started
 ChildThread1 is Alive : True
 ChildThread2 is Alive : True
 ChildThread1 ...ended
 ChildThread2 ...ended
 ChildThread1 is Alive : False
 ChildThread2 is Alive : False**

**join() method:**

**If a thread wants to wait until completing some other thread then we should go for join() method.**

**Eg:**

```
1) from threading import *
2) import time
3) def display():
4) for i in range( 10 ):
5) print("Seetha Thread")
6) time.sleep( 2 )
7)
8) t=Thread(target=display)
9) t.start()
10) t.join()#This Line executed by Main Thread
11) for i in range( 10 ):
12) print("Rama Thread")
```

**In the above example Main Thread waited until completing child thread. In this case output is:**

**Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread**

**8**

```

```

**Seetha Thread
 Seetha Thread
 Seetha Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread**

**Note: We can call join() method with time period also.**

**t.join(seconds)**

**In this case thread will wait only specified amount of time.**

**Eg:**

```
1) from threading import *
2) import time
3) def display():
4) for i in range( 10 ):
5) print("Seetha Thread")
6) time.sleep( 2 )
7)
8) t=Thread(target=display)
9) t.start()
10) t.join( 5 )#This Line executed by Main Thread
11) for i in range( 10 ):
12) print("Rama Thread")
```

**In this case Main Thread waited only 5 seconds.**

**Output:
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread
 Rama Thread**

**9**

```

```

**Rama Thread
 Rama Thread
 Rama Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread
 Seetha Thread**

**Summary of all methods related to threading module and Thread**

**Daemon Threads:**

**The threads which are running in the background are called Daemon Threads.**

**The main objective of Daemon Threads is to provide support for Non Daemon Threads( like main
 thread)**

**Eg: Garbage Collector**

**Whenever Main Thread runs with low memory, immediately PVM runs Garbage Collector to
 destroy useless objects and to provide free memory,so that Main Thread can continue its
 execution without having any memory problems.**

**We can check whether thread is Daemon or not by using t.isDaemon() method of Thread class or
 by using daemon property.**

**Eg:**

```
1) from threading import *
2) print(current_thread().isDaemon()) #False
3) print(current_thread().daemon) #False
```

**We can change Daemon nature by using setDaemon() method of Thread class.
 t.setDaemon(True)
 But we can use this method before starting of Thread.i.e once thread started,we cannot change its
 Daemon nature,otherwise we will get
 RuntimeException:cannot set daemon status of active thread**

**Eg:**

```
1) from threading import *
2) print(current_thread().isDaemon())
```

**10**

```

3) current_thread().setDaemon(True)
```

**RuntimeError: cannot set daemon status of active thread**

**Default Nature:**

**By default Main Thread is always non-daemon.But for the remaining threads Daemon nature will
 be inherited from parent to child.i.e if the Parent Thread is Daemon then child thread is also
 Daemon and if the Parent Thread is Non Daemon then ChildThread is also Non Daemon.**

**Eg:**

```
1) from threading import *
2) def job():
3) print("Child Thread")
4) t=Thread(target=job)
5) print(t.isDaemon())#False
6) t.setDaemon(True)
7) print(t.isDaemon()) #True
```

**Note: Main Thread is always Non-Daemon and we cannot change its Daemon Nature b'z it is
 already started at the beginning only.**

**Whenever the last Non-Daemon Thread terminates automatically all Daemon Threads will be
 terminated.**

**Eg:**

```
1) from threading import *
2) import time
3) def job():
4) for i in range( 10 ):
5) print("Lazy Thread")
6) time.sleep( 2 )
7)
8) t=Thread(target=job)
9) #t.setDaemon(True)===>Line- 1
10) t.start()
11) time.sleep( 5 )
12) print("End Of Main Thread")
```

**In the above program if we comment Line- 1 then both Main Thread and Child Threads are Non
 Daemon and hence both will be executed until their completion.
 In this case output is:**

**Lazy Thread
 Lazy Thread
 Lazy Thread**

**11**

```

```

**End Of Main Thread
 Lazy Thread
 Lazy Thread
 Lazy Thread
 Lazy Thread
 Lazy Thread
 Lazy Thread
 Lazy Thread**

**If we are not commenting Line-1 then Main Thread is Non-Daemon and Child Thread is Daemon.
 Hence whenever MainThread terminates automatically child thread will be terminated. In this
 case output is**

**Lazy Thread
 Lazy Thread
 Lazy Thread
 End of Main Thread**

**Synchronization:**

**If multiple threads are executing simultaneously then there may be a chance of data inconsistency
 problems.**

**Eg:**

```
1) from threading import *
2) import time
3) def wish(name):
4) for i in range( 10 ):
5) print("Good Evening:",end='')
6) time.sleep( 2 )
7) print(name)
8) t1=Thread(target=wish,args=("Dhoni",))
9) t2=Thread(target=wish,args=("Yuvraj",))
10) t1.start()
11) t2.start()
```

**Output:
 Good Evening:Good Evening:Yuvraj
 Dhoni
 Good Evening:Good Evening:Yuvraj
 Dhoni
 ....
 We are getting irregular output b'z both threads are executing simultaneously wish() function.**

**To overcome this problem we should go for synchronization.**

**12**

```

```

**In synchronization the threads will be executed one by one so that we can overcome data
 inconsistency problems.**

**Synchronization means at a time only one Thread**

**The main application areas of synchronization are**

**1. Online Reservation system

1. Funds Transfer from joint accounts
    etc**

**In Python, we can implement synchronization by using the following**

**1. Lock

1. RLock
2. Semaphore**

**Synchronization By using Lock concept:**

**Locks are the most fundamental synchronization mechanism provided by threading module.
 We can create Lock object as follows
 l=Lock()**

**The Lock object can be hold by only one thread at a time.If any other thread required the same
 lock then it will wait until thread releases lock.(similar to common wash rooms,public telephone
 booth etc)**

**A Thread can acquire the lock by using acquire() method.
 l.acquire()**

**A Thread can release the lock by using release() method.
 l.release()**

**Note: To call release() method compulsory thread should be owner of that lock.i.e thread should
 has the lock already,otherwise we will get Runtime Exception saying
 RuntimeError: release unlocked lock**

**Eg:**

```
1) from threading import *
2) l=Lock()
3) #l.acquire() ==>1
4) l.release()
```

**If we are commenting line-1 then we will get
 RuntimeError: release unlocked lock**

**Eg:**

```
1) from threading import *
```

**13**

```

2) import time
3) l=Lock()
4) def wish(name):
5) l.acquire()
6) for i in range( 10 ):
7) print("Good Evening:",end='')
8) time.sleep( 2 )
9) print(name)
10) l.release()
11)
12) t1=Thread(target=wish,args=("Dhoni",))
13) t2=Thread(target=wish,args=("Yuvraj",))
14) t3=Thread(target=wish,args=("Kohli",))
15) t1.start()
16) t2.start()
17) t3.start()
```

**In the above program at a time only one thread is allowed to execute wish() method and hence we
 will get regular output.**

**Problem with Simple Lock:**

**The standard Lock object does not care which thread is currently holding that lock.If the lock is
 held and any thread attempts to acquire lock, then it will be blocked,even the same thread is
 already holding that lock.**

**Eg:**

```
1) from threading import *
2) l=Lock()
3) print("Main Thread trying to acquire Lock")
4) l.acquire()
5) print("Main Thread trying to acquire Lock Again")
6) l.acquire()
```

**Output:
 D:\python_classes>py test.py
 Main Thread trying to acquire Lock
 Main Thread trying to acquire Lock Again
 \--
 In the above Program main thread will be blocked b'z it is trying to acquire the lock second time.**

**Note: To kill the blocking thread from windows command prompt we have to use ctrl+break. Here
 ctrl+C won't work.**

**If the Thread calls recursive functions or nested access to resources,then the thread may trying to
 acquire the same lock again and again,which may block our thread.**

**14**

```

```

**Hence Traditional Locking mechanism won't work for executing recursive functions.**

**To overcome this problem, we should go for RLock(Reentrant Lock). Reentrant means the thread
 can acquire the same lock again and again.If the lock is held by other threads then only the thread
 will be blocked.
 Reentrant facility is available only for owner thread but not for other threads.**

**Eg:**

```
1) from threading import *
2) l=RLock()
3) print("Main Thread trying to acquire Lock")
4) l.acquire()
5) print("Main Thread trying to acquire Lock Again")
6) l.acquire()
```

**In this case Main Thread won't be Locked b'z thread can acquire the lock any number of times.**

**This RLock keeps track of recursion level and hence for every acquire() call compulsory release()
 call should be available. i.e the number of acquire() calls and release() calls should be matched
 then only lock will be released.**

**Eg:
 l=RLock()
 l.acquire()
 l.acquire()
 l.release()
 l.release()**

**After 2 release() calls only the Lock will be released.**

**Note:**

**1. Only owner thread can acquire the lock multiple times

1. The number of acquire() calls and release() calls should be matched.**

**Demo Program for synchronization by using RLock:**

```
1) from threading import *
2) import time
3) l=RLock()
4) def factorial(n):
5) l.acquire()
6) if n== 0 :
7) result= 1
8) else:
9) result=n*factorial(n- 
10) l.release()
11) return result
```

**15**

```

12)
13) def results(n):
14) print("The Factorial of",n,"is:",factorial(n))
15)
16) t1=Thread(target=results,args=( 5 ,))
17) t2=Thread(target=results,args=( 9 ,))
18) t1.start()
19) t2.start()
```

**Output:
 The Factorial of 5 is: 120
 The Factorial of 9 is: 362880**

**In the above program instead of RLock if we use normal Lock then the thread will be blocked.**

**Difference between Lock and RLock:**

**table**

**Lock:**

**1. Lock object can be acquired by only one thread at a time.Even owner thread also cannot acquire
 multiple times.

1. Not suitable to execute recursive functions and nested access calls
2. In this case Lock object will takes care only Locked or unlocked and it never takes care about
    owner thread and recursion level.**

**RLock:**

**1. RLock object can be acquired by only one thread at a time, but owner thread can acquire same
 lock object multiple times.

1. Best suitable to execute recursive functions and nested access calls
2. In this case RLock object will takes care whether Locked or unlocked and owner thread
    information, recursiion level.**

**Synchronization by using Semaphore:**

**In the case of Lock and RLock,at a time only one thread is allowed to execute.**

**Sometimes our requirement is at a time a particular number of threads are allowed to access(like
 at a time 10 memebers are allowed to access database server,4 members are allowed to access
 Network connection etc).To handle this requirement we cannot use Lock and RLock concepts and
 we should go for Semaphore concept.**

**Semaphore can be used to limit the access to the shared resources with limited capacity.**

**Semaphore is advanced Synchronization Mechanism.**

**16**

```

```

**We can create Semaphore object as follows.**

**s=Semaphore(counter)**

**Here counter represents the maximum number of threads are allowed to access simultaneously.
 The default value of counter is 1.**

**Whenever thread executes acquire() method,then the counter value will be decremented by 1 and
 if thread executes release() method then the counter value will be incremented by 1.**

**i.e for every acquire() call counter value will be decremented and for every release() call counter
 value will be incremented.**

**Case-1: s=Semaphore()
 In this case counter value is 1 and at a time only one thread is allowed to access. It is exactly same
 as Lock concept.**

**Case-2: s=Semaphore(3)
 In this case Semaphore object can be accessed by 3 threads at a time.The remaining threads have
 to wait until releasing the semaphore.**

**Eg:**

```
1) from threading import *
2) import time
3) s=Semaphore( 2 )
4) def wish(name):
5) s.acquire()
6) for i in range( 10 ):
7) print("Good Evening:",end='')
8) time.sleep( 2 )
9) print(name)
10) s.release()
11)
12) t1=Thread(target=wish,args=("Dhoni",))
13) t2=Thread(target=wish,args=("Yuvraj",))
14) t3=Thread(target=wish,args=("Kohli",))
15) t4=Thread(target=wish,args=("Rohit",))
16) t5=Thread(target=wish,args=("Pandya",))
17) t1.start()
18) t2.start()
19) t3.start()
20) t4.start()
21) t5.start()
```

**In the above program at a time 2 threads are allowed to access semaphore and hence 2 threads
 are allowed to execute wish() function.**

**17**

```

```

**BoundedSemaphore:**

**Normal Semaphore is an unlimited semaphore which allows us to call release() method any
 number of times to increment counter.The number of release() calls can exceed the number of
 acquire() calls also.**

**Eg:**

```
1) from threading import *
2) s=Semaphore( 2 )
3) s.acquire()
4) s.acquire()
5) s.release()
6) s.release()
7) s.release()
8) s.release()
9) print("End")
```

**It is valid because in normal semaphore we can call release() any number of times.**

**BounedSemaphore is exactly same as Semaphore except that the number of release() calls should
 not exceed the number of acquire() calls,otherwise we will get**

**ValueError: Semaphore released too many times**

**Eg:**

```
1) from threading import *
2) s=BoundedSemaphore( 2 )
3) s.acquire()
4) s.acquire()
5) s.release()
6) s.release()
7) s.release()
8) s.release()
9) print("End")
```

**ValueError: Semaphore released too many times
 It is invalid b'z the number of release() calls should not exceed the number of acquire() calls in
 BoundedSemaphore.**

**Note: To prevent simple programming mistakes, it is recommended to use BoundedSemaphore
 over normal Semaphore.**

**Difference between Lock and Semaphore:**

**18**

```

```

**At a time Lock object can be acquired by only one thread, but Semaphore object can be acquired
 by fixed number of threads specified by counter value.**

**Conclusion:**

**The main advantage of synchronization is we can overcome data inconsistency problems.But the
 main disadvantage of synchronization is it increases waiting time of threads and creates
 performance problems. Hence if there is no specific requirement then it is not recommended to
 use synchronization.**

**Inter Thread Communication:**

**Some times as the part of programming requirement, threads are required to communicate with
 each other. This concept is nothing but interthread communication.**

**Eg: After producing items Producer thread has to communicate with Consumer thread to notify
 about new item.Then consumer thread can consume that new item.**

**In Python, we can implement interthread communication by using the following ways**

**1. Event

1. Condition
2. Queue
    etc**

**Interthread communication by using Event Objects:**

**Event object is the simplest communication mechanism between the threads. One thread signals
 an event and other thereds wait for it.**

**We can create Event object as follows...**

**event = threading.Event()**

**Event manages an internal flag that can set() or clear()
 Threads can wait until event set.**

**Methods of Event class:**

**1.set()**  **internal flag value will become True and it represents GREEN signal for all waiting
 threads.**

**2. clear()**  **inernal flag value will become False and it represents RED signal for all waiting
 threads.

1. isSet()**  **This method can be used whether the event is set or not**

**19**

```

```

**4. wait()|wait(seconds)**  **Thread can wait until event is set**

**Pseudo Code:**

**event = threading.Event()**

**#consumer thread has to wait until event is set
 event.wait()**

**#producer thread can set or clear event
 event.set()
 event.clear()**

**Demo Program-1:**

```
1) from threading import *
2) import time
3) def producer():
4) time.sleep( 5 )
5) print("Producer thread producing items:")
6) print("Producer thread giving notification by setting event")
7) event.set()
8) def consumer():
9) print("Consumer thread is waiting for updation")
10) event.wait()
11) print("Consumer thread got notification and consuming items")
12)
13) event=Event()
14) t1=Thread(target=producer)
15) t2=Thread(target=consumer)
16) t1.start()
17) t2.start()
```

**Output:
 Consumer thread is waiting for updation
 Producer thread producing items
 Producer thread giving notification by setting event
 Consumer thread got notification and consuming items**

**Demo Program-2:**

```
1) from threading import *
2) import time
3) def trafficpolice():
4) while True:
5) time.sleep( 10 )
6) print("Traffic Police Giving GREEN Signal")
```

**20**

```

7) event.set()
8) time.sleep( 20 )
9) print("Traffic Police Giving RED Signal")
10) event.clear()
11) def driver():
12) num= 0
13) while True:
14) print("Drivers waiting for GREEN Signal")
15) event.wait()
16) print("Traffic Signal is GREEN...Vehicles can move")
17) while event.isSet():
18) num=num+ 1
19) print("Vehicle No:",num,"Crossing the Signal")
20) time.sleep( 2 )
21) print("Traffic Signal is RED...Drivers have to wait")
22) event=Event()
23) t1=Thread(target=trafficpolice)
24) t2=Thread(target=driver)
25) t1.start()
26) t2.start()
```

**In the above program driver thread has to wait until Trafficpolice thread sets event.ie until giving
 GREEN signal.Once Traffic police thread sets event(giving GREEN signal),vehicles can cross the
 signal.Once traffic police thread clears event (giving RED Signal)then the driver thread has to wait.**

**Interthread communication by using Condition Object:**

**Condition is the more advanced version of Event object for interthread communication.A
 condition represents some kind of state change in the application like producing item or
 consuming item. Threads can wait for that condition and threads can be notified once condition
 happend.i.e Condition object allows one or more threads to wait until notified by another thread.**

**Condition is always associated with a lock (ReentrantLock).
 A condition has acquire() and release() methods that call the corresponding methods of the
 associated lock.**

**We can create Condition object as follows
 condition = threading.Condition()**

**Methods of Condition:**

**1. acquire()**  **To acquire Condition object before producing or consuming items.i.e thread
 acquiring internal lock.

1. release()**  **To release Condition object after producing or consuming items. i.e thread releases
    internal lock
2. wait()|wait(time)**  **To wait until getting Notification or time expired**

**21**

```

```

**4. notify()**  **To give notification for one waiting thread

1. notifyAll()**  **To give notification for all waiting threads**

**Case Study:**

**The producing thread needs to acquire the Condition before producing item to the resource and
 notifying the consumers.**

**#Producer Thread
 ...generate item..
 condition.acquire()
 ...add item to the resource...
 condition.notify()#signal that a new item is available(notifyAll())
 condition.release()**

**The Consumer must acquire the Condition and then it can consume items from the resource**

**#Consumer Thread
 condition.acquire()
 condition.wait()
 consume item
 condition.release()**

**Demo Program-1:**

```
1) from threading import *
2) def consume(c):
3) c.acquire()
4) print("Consumer waiting for updation")
5) c.wait()
6) print("Consumer got notification & consuming the item")
7) c.release()
8)
9) def produce(c):
10) c.acquire()
11) print("Producer Producing Items")
12) print("Producer giving Notification")
13) c.notify()
14) c.release()
15)
16) c=Condition()
17) t1=Thread(target=consume,args=(c,))
18) t2=Thread(target=produce,args=(c,))
19) t1.start()
20) t2.start()
```

**22**

```

```

**Output:
 Consumer waiting for updation
 Producer Producing Items
 Producer giving Notification
 Consumer got notification & consuming the item**

**Demo Program-2:**

```
1) from threading import *
2) import time
3) import random
4) items=[]
5) def produce(c):
6) while True:
7) c.acquire()
8) item=random.randint( 1 , 100 )
9) print("Producer Producing Item:",item)
10) items.append(item)
11) print("Producer giving Notification")
12) c.notify()
13) c.release()
14) time.sleep( 5 )
15)
16) def consume(c):
17) while True:
18) c.acquire()
19) print("Consumer waiting for updation")
20) c.wait()
21) print("Consumer consumed the item",items.pop())
22) c.release()
23) time.sleep( 5 )
24)
25) c=Condition()
26) t1=Thread(target=consume,args=(c,))
27) t2=Thread(target=produce,args=(c,))
28) t1.start()
29) t2.start()
```

**Output:
 Consumer waiting for updation
 Producer Producing Item: 49
 Producer giving Notification
 Consumer consumed the item 49
 .....**

**In the above program Consumer thread expecting updation and hence it is responsible to call
 wait() method on Condition object.
 Producer thread performing updation and hence it is responsible to call notify() or notifyAll() on
 Condition object.**

**23**

```

```

**Interthread communication by using Queue:**

**Queues Concept is the most enhanced Mechanism for interthread communication and to share
 data between threads.**

**Queue internally has Condition and that Condition has Lock.Hence whenever we are using Queue
 we are not required to worry about Synchronization.**

**If we want to use Queues first we should import queue module.**

**import queue**

**We can create Queue object as follows**

**q = queue.Queue()**

**Important Methods of Queue:**

**1. put(): Put an item into the queue.

1. get(): Remove and return an item from the queue.**

**Producer Thread uses put() method to insert data in the queue. Internally this method has logic to
 acquire the lock before inserting data into queue. After inserting data lock will be released
 automatically.**

**put() method also checks whether the queue is full or not and if queue is full then the Producer
 thread will entered in to waiting state by calling wait() method internally.**

**Consumer Thread uses get() method to remove and get data from the queue. Internally this
 method has logic to acquire the lock before removing data from the queue.Once removal
 completed then the lock will be released automatically.**

**If the queue is empty then consumer thread will entered into waiting state by calling wait()
 method internally.Once queue updated with data then the thread will be notified automatically.**

**Note:
 The queue module takes care of locking for us which is a great advantage.**

**Eg:**

```
1) from threading import *
2) import time
3) import random
4) import queue
5) def produce(q):
```

**24**

```

6) while True:
7) item=random.randint( 1 , 100 )
8) print("Producer Producing Item:",item)
9) q.put(item)
10) print("Producer giving Notification")
11) time.sleep( 5 )
12) def consume(q):
13) while True:
14) print("Consumer waiting for updation")
15) print("Consumer consumed the item:",q.get())
16) time.sleep( 5 )
17)
18) q=queue.Queue()
19) t1=Thread(target=consume,args=(q,))
20) t2=Thread(target=produce,args=(q,))
21) t1.start()
22) t2.start()
```

**Output:
 Consumer waiting for updation
 Producer Producing Item: 58
 Producer giving Notification
 Consumer consumed the item: 58**

**Types of Queues:**

**Python Supports 3 Types of Queues.**

**1. FIFO Queue:**

**q = queue.Queue()**

**This is Default Behaviour. In which order we put items in the queue, in the same order the items
 will come out (FIFO-First In First Out).**

**Eg:**

```
1) import queue
2) q=queue.Queue()
3) q.put( 10 )
4) q.put( 5 )
5) q.put( 20 )
6) q.put( 15 )
7) while not q.empty():
8) print(q.get(),end=' ')
```

**Output: 10 5 20 15**

**25**

```

```

**2. LIFO Queue:**

**The removal will be happend in the reverse order of insertion(Last In First Out)**

**Eg:**

```
1) import queue
2) q=queue.LifoQueue()
3) q.put( 10 )
4) q.put( 5 )
5) q.put( 20 )
6) q.put( 15 )
7) while not q.empty():
8) print(q.get(),end=' ')
```

**Output: 15 20 5 10**

**3. Priority Queue:**

**The elements will be inserted based on some priority order.**

```
1) import queue
2) q=queue.PriorityQueue()
3) q.put( 10 )
4) q.put( 5 )
5) q.put( 20 )
6) q.put( 15 )
7) while not q.empty():
8) print(q.get(),end=' ')
```

**Output: 5 10 15 20**

**Eg 2: If the data is non-numeric, then we have to provide our data in the form of tuple.**

**(x,y)**

**x is priority
 y is our element**

```
1) import queue
2) q=queue.PriorityQueue()
3) q.put(( 1 ,"AAA"))
4) q.put(( 3 ,"CCC"))
5) q.put(( 2 ,"BBB"))
6) q.put(( 4 ,"DDD"))
7) while not q.empty():
8) print(q.get()[ 1 ],end=' ')
```

**26**

```

```

**Output: AAA BBB CCC DDD**

**Good Programming Practices with usage of Locks:**

**Case-1:**

**It is highly recommended to write code of releasing locks inside finally block.The advantage is lock
 will be released always whether exception raised or not raised and whether handled or not
 handled.**

**l=threading.Lock()
 l.acquire()
 try:
 perform required safe operations
 finally:
 l.release()**

**Demo Program:**

```
1) from threading import *
2) import time
3) l=Lock()
4) def wish(name):
5) l.acquire()
6) try:
7) for i in range( 10 ):
8) print("Good Evening:",end='')
9) time.sleep( 2 )
10) print(name)
11) finally:
12) l.release()
13)
14) t1=Thread(target=wish,args=("Dhoni",))
15) t2=Thread(target=wish,args=("Yuvraj",))
16) t3=Thread(target=wish,args=("Kohli",))
17) t1.start()
18) t2.start()
19) t3.start()
```

**Case-2:**

**It is highly recommended to acquire lock by using with statement. The main advantage of with
 statement is the lock will be released automatically once control reaches end of with block and we
 are not required to release explicitly.**

**This is exactly same as usage of with statement for files.**

**27**

```

```

**Example for File:**

**with open('demo.txt','w') as f:
 f.write("Hello...")**

**Example for Lock:**

**lock=threading.Lock()
 with lock:
 perform required safe operations
 lock will be released automatically**

**Demo Program:**

```
1) from threading import *
2) import time
3) lock=Lock()
4) def wish(name):
5) with lock:
6) for i in range( 10 ):
7) print("Good Evening:",end='')
8) time.sleep( 2 )
9) print(name)
10) t1=Thread(target=wish,args=("Dhoni",))
11) t2=Thread(target=wish,args=("Yuvraj",))
12) t3=Thread(target=wish,args=("Kohli",))
13) t1.start()
14) t2.start()
15) t3.start()
```

**Q. What is the advantage of using with statement to acquire a lock in threading?
 Lock will be released automatically once control reaches end of with block and We are not
 required to release explicitly.**

**Note: We can use with statement in multithreading for the following cases:**

**1. Lock

1. RLock
2. Semaphore
3. Condition**

1

```

```

Python Database Programming

Storage Areas

As the Part of our Applications, we required to store our Data like Customers Information, Billing
 Information, Calls Information etc..

To store this Data, we required Storage Areas. There are 2 types of Storage Areas.

1. Temporary Storage Areas
2. Permanent Storage Areas

1.Temporary Storage Areas:

These are the Memory Areas where Data will be stored temporarily.
 Eg: Python objects like List, Tuple, Dictionary.

Once Python program completes its execution then these objects will be destroyed automatically
 and data will be lost.

1. Permanent Storage Areas:

Also known as Persistent Storage Areas. Here we can store Data permanently.

Eg: File Systems, Databases, Data warehouses, Big Data Technologies etc

File Systems:

File Systems can be provided by Local operating System. File Systems are best suitable to store
 very less Amount of Information.

Limitations:

1. We cannot store huge Amount of Information.
2. There is no Query Language support and hence operations will become very complex.
3. There is no Security for Data.
4. There is no Mechanism to prevent duplicate Data. Hence there may be a chance of Data
    Inconsistency Problems.

To overcome the above Problems of File Systems, we should go for Databases.

Databases:

1. We can store Huge Amount of Information in the Databases.

2

```

```

1. Query Language Support is available for every Database and hence we can perform Database
    Operations very easily.
2. To access Data present in the Database, compulsory username and pwd must be required.
    Hence Data is secured.
3. Inside Database Data will be stored in the form of Tables. While developing Database Table
    Schemas, Database Admin follow various Normalization Techniques and can implement various
    Constraints like Unique Key Constrains, Primary Key Constraints etc which prevent Data
    Duplication. Hence there is no chance of Data Inconsistency Problems.

Limitations of Databases:

1. Database cannot hold very Huge Amount of Information like Terabytes of Data.
2. Database can provide support only for Structured Data (Tabular Data OR Relational Data) and
    cannot provide support for Semi Structured Data (like XML Files) and Unstructured Data (like
    Video Files, Audio Files, Images etc)

To overcome these Problems we should go for more Advanced Storage Areas like Big Data
 Technologies, Data warehouses etc.

Python Database Programming:

Sometimes as the part of Programming requirement we have to connect to the database and we
 have to perform several operations like creating tables, inserting data,updating data,deleting
 data,selecting data etc.

We can use SQL Language to talk to the database and we can use Python to send those SQL
 commands to the database.

Python provides inbuilt support for several databases like Oracle, MySql, SqlServer, GadFly, sqlite,
 etc.
 Python has seperate module for each database.
 Eg: cx_Oralce module for communicating with Oracle database
 pymssql module for communicating with Microsoft Sql Server

Standard Steps for Python database Programming:

1. Import database specific module
    Eg: import cx_Oracle
2. Establish Connection between Python Program and database.
    We can create this Connection object by using connect() function of the module.
    con = cx_Oracle.connect(datbase information)

Eg: con=cx_Oracle.connect('scott/tiger@localhost')

1. To execute our sql queries and to hold results some special object is required, which is nothing
    but Cursor object. We can create Cursor object by using cursor() method.

3

```

```

cursor=con.cursor()

1. Execute SQL Queries By using Cursor object. For this we can use the following methods

i) execute(sqlquery) **** To execute a single sql query
 ii) executescript(sqlqueries) **** To execute a string of sql queries seperated by semi-colon ';'
 iii) executemany() **** To execute a Parameterized query

Eg: cursor.execute("select * from employees")

1. commit or rollback changes based on our requirement in the case of DML
    Queries(insert|update|delete)

commit() **** Saves the changes to the database
 rollback() **** rolls all temporary changes back

1. Fetch the result from the Cursor object in the case of select queries
    fetchone() **** To fetch only one row
    fetchall() **** To fetch all rows and it returns a list of rows
    fecthmany(n) **** To fetch first n rows

Eg 1: data =cursor.fetchone()
 print(data)

Eg 2: data=cursor.fetchall()
 for row in data:
 print(row)

1. close the resources
    After completing our operations it is highly recommended to close the resources in the reverse
    order of their opening by using close() methods.

cursor.close()
 con.close()

Note: The following is the list of all important methods which can be used for python database
 programming.

connect()
 cursor()
 execute()
 executescript()
 executemany()
 commit()
 rollback()
 fetchone()
 fetchall()
 fetchmany(n)

4

```

```

fetch
 close()

These methods won't be changed from database to database and same for all databases.

Working with Oracle Database:

From Python Program if we want to communicate with any database,some translator must be
 required to translate Python calls into Database specific calls and Database specific calls into
 Python calls.This translator is nothing but Driver/Connector.

Diagram

For Oracle database the name of driver needed is cx_Oracle.
 cx_Oracle is a Python extension module that enables access to Oracle Database.It can be used for
 both Python2 and Python3. It can work with any version of Oracle database like 9,10,11 and 12.

Installing cx_Oracle:

From Normal Command Prompt (But not from Python console)execute the following command

D:\python_classes>pip install cx_Oracle

Collecting cx_Oracle
 Downloading cx_Oracle-6.0.2-cp36-cp36m-win32.whl (100kB)
 100% |-----------| 102kB 256kB/s
 Installing collected packages: cx-Oracle
 Successfully installed cx-Oracle-6.0.2

How to Test Installation:

From python console execute the following command:

> > > help("modules")

In the output we can see cx_Oracle

....
 _multiprocessing crypt ntpath timeit
 _opcode csv nturl2path tkinter
 _operator csvr numbers token
 _osx_support csvw opcode tokenize
 _overlapped ctypes operator trace
 _pickle curses optparse traceback
 _pydecimal custexcept os tracemalloc
 _pyio cx_Oracle parser try
 _random data pathlib tty
 _sha1 datetime pdb turtle

5

```

```

_sha256 dbm pick turtledemo
 _sha3 decimal pickle types
 _sha512 demo pickletools typing
 _signal difflib pip unicodedata
 _sitebuiltins dis pipes unittest
 _socket distutils pkg_resources unpick
 _sqlite3 doctest pkgutil update
 _sre dummy_threading platform urllib
 _ssl durgamath plistlib uu
 _stat easy_install polymorph uuid
 .....

App1: Program to connect with Oracle database and print its version.

```
 import cx_Oracle
con=cx_Oracle.connect('scott/tiger@localhost')
print(con.version)
con.close()
```

Output:
 D:\python_classes>py db1.py
 11.2.0.2.0

App2: Write a Program to create employees table in the oracle database :
 employees(eno,ename,esal,eaddr)

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("create table employees(eno number,ename varchar2(10),esal number(10,2),eaddr varchar2(10))")
print("Table created successfully")
except cx_Oracle.DatabaseError as e:
if con:
con.rollback()
print("There is a problem with sql",e)
1 finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

App3: Write a program to drop employees table from oracle database?

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("drop table employees")
print("Table dropped successfully")
except cx_Oracle.DatabaseError as e:
if con:
con.rollback()
print("There is a problem with sql",e)
1 finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

App3: Write a program to insert a single row in the employees table.

6

```

 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("insert into employees values(100,'Durga',1000,'Hyd')")
con.commit()
print("Record Inserted Successfully")
except cx_Oracle.DatabaseError as e:
if con:
con.rollback()
1 print("There is a problem with sql",e)
1finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

Note: While performing DML Operations (insert|update|delte), compulsory we have to use
 commit() method,then only the results will be reflected in the database.

App4: Write a program to insert multiple rows in the employees table by

using executemany() method.

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
sql="insert into employees values(:eno,:ename,:esal,:eaddr)"
records=[( 200 ,'Sunny', 2000 ,'Mumbai'),
( 300 ,'Chinny', 3000 ,'Hyd'),
( 400 ,'Bunny', 4000 ,'Hyd')]
cursor.executemany(sql,records)
con.commit()
1 print("Records Inserted Successfully")
1except cx_Oracle.DatabaseError as e:
1if con:
1con.rollback()
1print("There is a problem with sql",e)
1finally:
1if cursor:
1cursor.close()
1if con:
20 ) con.close()
```

App5: Write a program to insert multiple rows in the employees table with

dynamic input from the keyboard?

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
while True:
eno=int(input("Enter Employee Number:"))
ename=input("Enter Employee Name:")
esal=float(input("Enter Employee Salary:"))
eaddr=input("Enter Employee Address:")
sql="insert into employees values(%d,'%s',%f,'%s')"
1 cursor.execute(sql %(eno,ename,esal,eaddr))
1print("Record Inserted Successfully")
1option=input("Do you want to insert one more record[Yes|No] :")
1if option=="No":
1con.commit()
1break
1except cx_Oracle.DatabaseError as e:
1if con:
1con.rollback()
20 ) print("There is a problem with sql :",e)
2 finally:
2if cursor:
2cursor.close()
2if con:
2con.close()
```

7

```

```

App6: Write a program to update employee salaries with increment for the

certain range with dynamic input.

Eg: Increment all employee salaries by 500 whose salary < 5000

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
increment=float(input("Enter Increment Salary:"))
salrange=float(input("Enter Salary Range:"))
sql="update employees set esal=esal+%f where esal<%f"
cursor.execute(sql %(increment,salrange))
print("Records Updated Successfully")
con.commit()
1 except cx_Oracle.DatabaseError as e:
1if con:
1con.rollback()
1print("There is a problem with sql :",e)
1finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

App7: Write a program to delete employees whose salary greater provided

salary as dynamic input?

Eg: delete all employees whose salary > 5000

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cutoffsalary=float(input("Enter CutOff Salary:"))
sql="delete from employees where esal>%f"
cursor.execute(sql %(cutoffsalary))
print("Records Deleted Successfully")
con.commit()
except cx_Oracle.DatabaseError as e:
1 if con:
1con.rollback()
1print("There is a problem with sql :",e)
1finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

App8: Write a program to select all employees info by using fetchone()

method?

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("select * from employees")
row=cursor.fetchone()
while row is not None:
print(row)
row=cursor.fetchone()
except cx_Oracle.DatabaseError as e:
1 if con:
1con.rollback()
1print("There is a problem with sql :",e)
1finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

8

```

```

App9: Write a program to select all employees info by using fetchall()

method?

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("select * from employees")
data=cursor.fetchall()
for row in data:
print("Employee Number:",row[ 0 ])
print("Employee Name:",row[ 1 ])
print("Employee Salary:",row[ 2 ])
1 print("Employee Address:",row[ 3 ])
1print()
1print()
1except cx_Oracle.DatabaseError as e:
1if con:
1con.rollback()
1print("There is a problem with sql :",e)
1finally:
1if cursor:
20 ) cursor.close()
2 if con:
2con.close()
```

App10: Write a program to select employees info by using fetchmany()

method and the required number of rows will be provided as dynamic input?

```
 import cx_Oracle
try:
con=cx_Oracle.connect('scott/tiger@localhost')
cursor=con.cursor()
cursor.execute("select * from employees")
n=int(input("Enter the number of required rows:"))
data=cursor.fetchmany(n)
for row in data:
print(row)
except cx_Oracle.DatabaseError as e:
1 if con:
1con.rollback()
1print("There is a problem with sql :",e)
1finally:
1if cursor:
1cursor.close()
1if con:
1con.close()
```

Output:
 D:\python_classes>py test.py
 Enter the number of required rows:3
 (100, 'Durga', 1500.0, 'Hyd')
 (200, 'Sunny', 2500.0, 'Mumbai')
 (300, 'Chinny', 3500.0, 'Hyd')

D:\python_classes>py test.py
 Enter the number of required rows:4
 (100, 'Durga', 1500.0, 'Hyd')
 (200, 'Sunny', 2500.0, 'Mumbai')
 (300, 'Chinny', 3500.0, 'Hyd')
 (400, 'Bunny', 4500.0, 'Hyd')

Working with Mysql database:
 Current version: 5.7.19
 Vendor: SUN Micro Systems/Oracle Corporation

9

```

```

Open Source and Freeware
 Default Port: 3306
 Default user: root

Note: In MySQL, everything we have to work with our own databases, which are also known as
 Logical Databases.

The following are 4 default databases available in mysql.

1. information_schema
2. mysql
3. performance_schema
4. test

Diagram

In the above diagram only one physical database is available and 4 logical databases are available.

Commonly used commands in MySql:

1. To know available databases:
    mysql> show databases;
2. To create our own logical database
    mysql> create database durgadb;
3. To drop our own database:
    mysql> drop database durgadb;
4. To use a particular logical database
    mysql> use durgadb; OR mysql> connect durgadb;
5. To create a table:
    create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr
    varchar(10));
6. To insert data:
    insert into employees values(100,'Durga',1000,'Hyd');
    insert into employees values(200,'Ravi',2000,'Mumbai');

In MySQL instead of single quotes we can use double quotes also.

Driver/Connector Information:

From Python program if we want to communicates with MySql database,compulsory some
 translator is required to convert python specific calls into mysql database specific calls and mysql
 database specific calls into python specific calls. This translator is nothing but Driver or Connector.

10

```

```

Diagram

We have to download connector seperately from mysql database.

https://dev.mysql.com/downloads/connector/python/2.1.html

How to check installation:

From python console we have to use
 help("modules")

In the list of modules,compulsory mysql should be there.

Note: In the case of Python3.4 we have to set PATH and PYTHONPATH explicitly

PATH=C:\Python34
 PYTHONPATH=C:\Python34\Lib\site-packages

Q. Write a Program to create table,insert data and display data by using mysql database.

```
 import mysql.connector
try:
con=mysql.connector.connect(host='localhost',database='durgadb',user='root',password='root')
cursor=con.cursor()
cursor.execute("create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(
10))")
print("Table Created...")
7 )
sql = "insert into employees(eno, ename, esal, eaddr) VALUES(%s, %s, %s, %s)"
records=[( 100 ,'Sachin', 1000 ,'Mumbai'),
( 200 ,'Dhoni', 2000 ,'Ranchi'),
1 ( 300 ,'Kohli', 3000 ,'Delhi')]
1cursor.executemany(sql,records)
1con.commit()
1print("Records Inserted Successfully...")
15 )
1cursor.execute("select * from employees")
1data=cursor.fetchall()
1for row in data:
1print("Employee Number:",row[ 0 ])
20 ) print("Employee Name:",row[ 1 ])
2 print("Employee Salary:",row[ 2 ])
2print("Employee Address:",row[ 3 ])
2print()
2print()
2except mysql.connector.DatabaseError as e:
2if con:
2con.rollback()
2print("There is a problem with sql :",e)
2finally:
30 ) if cursor:
3 cursor.close()
3if con:
3con.close()
```

Q. Write a Program to copy data present in employees table of mysql database into Oracle
 database.

```
 import mysql.connector
import cx_Oracle
try:
con=mysql.connector.connect(host='localhost',database='durgadb',user='root',password='root')
```

11

```

cursor=con.cursor()
cursor.execute("select * from employees")
data=cursor.fetchall()
list=[]
for row in data:
t=(row[ 0 ],row[ 1 ],row[ 2 ],row[ 3 ])
1 list.append(t)
1except mysql.connector.DatabaseError as e:
1if con:
1con.rollback()
1print("There is a problem with MySql :",e)
1finally:
1if cursor:
1cursor.close()
1if con:
20 ) con.close()
2
2try:
2con=cx_Oracle.connect('scott/tiger@localhost')
2cursor=con.cursor()
2sql="insert into employees values(:eno,:ename,:esal,:eaddr)"
2cursor.executemany(sql,list)
2con.commit()
2print("Records Copied from MySQL Database to Oracle Database Successfully")
2except cx_Oracle.DatabaseError as e:
30 ) if con:
3 con.rollback()
3print("There is a problem with sql",e)
3finally:
3if cursor:
3cursor.close()
3if con:
3con.close()
```

https://dev.mysql.com/downloads/connector/python/2.1.html

```
 create table employees(eno int(5) primary key,ename varchar(10),esal double(10,2),eaddr varchar(10));
2 )
insert into employees values(100,'Durga',1000,'Hyd');
insert into employees values(200,'Ravi',2000,'Mumbai');
insert into employees values(300,'Shiva',3000,'Hyd');
```

1

```

```

Pattern Programs

Pattern-1:

------

------

------

------

------

------

------

------

------

------

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print("* "*n)
```

Pattern-2:

1 1 1 1 1 1 1 1 1 1
 2 2 2 2 2 2 2 2 2 2
 3 3 3 3 3 3 3 3 3 3
 4 4 4 4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5 5 5
 6 6 6 6 6 6 6 6 6 6
 7 7 7 7 7 7 7 7 7 7
 8 8 8 8 8 8 8 8 8 8
 9 9 9 9 9 9 9 9 9 9
 10 10 10 10 10 10 10 10 10 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(i,end=" ")
print()
```

Pattern- 3 :

1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10

2

```

```

1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(j,end=" ")
print()
```

Pattern- 4 :

A A A A A A A A A A
 B B B B B B B B B B
 C C C C C C C C C C
 D D D D D D D D D D
 E E E E E E E E E E
 F F F F F F F F F F
 G G G G G G G G G G
 H H H H H H H H H H
 I I I I I I I I I I
 J J J J J J J J J J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(chr( 64 +i),end=" ")
print()
```

Pattern- 5 :

A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J
 A B C D E F G H I J

3

```

 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(chr( 64 +j),end=" ")
print()
```

Pattern- 6 :

10 10 10 10 10 10 10 10 10 10
 9 9 9 9 9 9 9 9 9 9
 8 8 8 8 8 8 8 8 8 8
 7 7 7 7 7 7 7 7 7 7
 6 6 6 6 6 6 6 6 6 6
 5 5 5 5 5 5 5 5 5 5
 4 4 4 4 4 4 4 4 4 4
 3 3 3 3 3 3 3 3 3 3
 2 2 2 2 2 2 2 2 2 2
 1 1 1 1 1 1 1 1 1 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(n+ 1 - i,end=" ")
print()
```

Pattern- 6 :

10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(n+ 1 - j,end=" ")
print()
```

4

```

```

Pattern- 7 :

J J J J J J J J J J
 I I I I I I I I I I
 H H H H H H H H H H
 G G G G G G G G G G
 F F F F F F F F F F
 E E E E E E E E E E
 D D D D D D D D D D
 C C C C C C C C C C
 B B B B B B B B B B
 A A A A A A A A A A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(chr( 65 +n-i),end=" ")
print()
```

Pattern- 8 :

J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A
 J I H G F E D C B A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ :
print(chr( 65 +n-j),end=" ")
print()
```

Pattern- 9 :

- 
- - 

------

------

------

------

------

5

```

```

------

------

------

Code - 1:

```
 n=int(input("Enter the number of rows:"))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
print("*",end=" ")
print()
```

Code - 2:

```
 n=int(input("Enter the number of rows:"))
for i in range( 1 ,n+ :
print("* "*i)
```

Pattern- 10 :

1
 2 2
 3 3 3
 4 4 4 4
 5 5 5 5 5
 6 6 6 6 6 6
 7 7 7 7 7 7 7
 8 8 8 8 8 8 8 8
 9 9 9 9 9 9 9 9 9
 10 10 10 10 10 10 10 10 10 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
print(i,end=" ")
print()
```

Pattern- 11 :

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 1 2 3 4 5 6
 1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8

6

```

```

1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
print(j,end=" ")
print()
```

Pattern- 12 :

A
 B B
 C C C
 D D D D
 E E E E E
 F F F F F F
 G G G G G G G
 H H H H H H H H
 I I I I I I I I I
 J J J J J J J J J J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
print(chr( 64 +i),end=" ")
print()
```

Pattern- 13 :

A
 A B
 A B C
 A B C D
 A B C D E
 A B C D E F
 A B C D E F G
 A B C D E F G H
 A B C D E F G H I
 A B C D E F G H I J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
print(chr( 64 +j),end=" ")
print()
```

7

```

 Squares
 Right Angled Triangle
 Reverse of Right Angled Triangle
```

Pattern- 14 :

------

------

------

------

------

------

------

------

- - 
- 

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print("*",end=" ")
print()
```

Pattern- 15 :

1 1 1 1 1 1 1 1 1 1
 2 2 2 2 2 2 2 2 2
 3 3 3 3 3 3 3 3
 4 4 4 4 4 4 4
 5 5 5 5 5 5
 6 6 6 6 6
 7 7 7 7
 8 8 8
 9 9
 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(i,end=" ")
print()
```

8

```

```

Pattern- 16 :

1 2 3 4 5 6 7 8 9 10
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8
 1 2 3 4 5 6 7
 1 2 3 4 5 6
 1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(j,end=" ")
print()
```

Pattern- 17 :

A A A A A A A A A A
 B B B B B B B B B
 C C C C C C C C
 D D D D D D D
 E E E E E E
 F F F F F
 G G G G
 H H H
 I I
 J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(chr( 64 +i),end=" ")
print()
```

Pattern- 18 :

A B C D E F G H I J
 A B C D E F G H I
 A B C D E F G H
 A B C D E F G
 A B C D E F
 A B C D E
 A B C D

9

```

```

A B C
 A B
 A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(chr( 64 +j),end=" ")
print()
```

Pattern- 19 :

10 10 10 10 10 10 10 10 10 10
 9 9 9 9 9 9 9 9 9
 8 8 8 8 8 8 8 8
 7 7 7 7 7 7 7
 6 6 6 6 6 6
 5 5 5 5 5
 4 4 4 4
 3 3 3
 2 2
 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(n+ 1 - i,end=" ")
print()
```

Pattern- 20 :

10 9 8 7 6 5 4 3 2 1
 10 9 8 7 6 5 4 3 2
 10 9 8 7 6 5 4 3
 10 9 8 7 6 5 4
 10 9 8 7 6 5
 10 9 8 7 6
 10 9 8 7
 10 9 8
 10 9
 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(n+ 1 - j,end=" ")
print()
```

10

```

```

Pattern- 21 :

J J J J J J J J J J
 I I I I I I I I I
 H H H H H H H H
 G G G G G G G
 F F F F F F
 E E E E E
 D D D D
 C C C
 B B
 A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(chr( 65 +n-i),end=" ")
print()
```

Pattern- 22 :

J I H G F E D C B A
 J I H G F E D C B
 J I H G F E D C
 J I H G F E D
 J I H G F E
 J I H G F
 J I H G
 J I H
 J I
 J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
for j in range( 1 ,n+ 2 - i):
print(chr( 65 +n-j),end=" ")
print()
```

Pattern- 23 :

- 

**

------

------

------

------

------

11

```

```

------

------

------

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),"*"*i,end=" ")
print()
```

Pattern- 24 :

- 
- - 

------

------

------

------

------

------

------

------

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
```

Pattern- 25 :

1

2 2

3 3 3

4 4 4 4

5 5 5 5 5

6 6 6 6 6 6

7 7 7 7 7 7 7

8 8 8 8 8 8 8 8

12

```

```

9 9 9 9 9 9 9 9 9

10 10 10 10 10 10 10 10 10 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),(str(i)+" ")*i)
print()
```

Pattern- 26 :

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 1 2 3 4 5 6
 1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8
 1 2 3 4 5 6 7 8 9
 1 2 3 4 5 6 7 8 9 10

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(j,end=" ")
print()
```

Pattern- 27 :

A

B B

C C C

D D D D

E E E E E

F F F F F F

G G G G G G G

H H H H H H H H

13

```

 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),(chr( 64 +i)+" ")*i)
print()
```

Pattern- 28 :

A
 A B
 A B C
 A B C D
 A B C D E
 A B C D E F
 A B C D E F G
 A B C D E F G H
 A B C D E F G H I
 A B C D E F G H I J

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(chr( 64 +j),end=" ")
print()
```

Pattern- 29 :

------

------

------

- - 
- 

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(i- ,"* "*(n+ 1 - i))
```

Pattern- 30 :

5 5 5 5 5
 4 4 4 4
 3 3 3
 2 2
 1

14

```

 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(i- ,(str(n+ 1 - i)+" ")*(n+ 1 - i))
```

Pattern- 31 :

1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(i- ,end="")
for j in range( 1 ,n+ 2 - i):
print(j,end=" ")
print()
```

Pattern- 32 :

E E E E E
 D D D D
 C C C
 B B
 A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(i- ,(str(chr( 65 +n-i))+" ")*(n+ 1 - i))
```

Pattern- 33 :

A B C D E
 A B C D
 A B C
 A B
 A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(i- ,end="")
for j in range( 65 , 66 +n-i):
print(chr(j),end=" ")
print()
```

15

```

```

Pattern- 34 :

- 

------

------

------

------

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),"* "*( 2 *i- )
```

Pattern- 35 :

1
 2 2 2
 3 3 3 3 3
 4 4 4 4 4 4 4
 5 5 5 5 5 5 5 5 5

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),(str(i)+" ")*( 2 *i- )
```

Pattern- 36 :

A
 B B B
 C C C C C
 D D D D D D D
 E E E E E E E E E

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),(str(chr( 64 +i)+" "))*( 2 *i- )
```

Pattern- 37 :

A
 C C C
 E E E E E
 G G G G G G G
 I I I I I I I I I

16

```

 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),(str(chr( 64 + 2 *i- +" "))*( 2 *i- )
```

Pattern- 38 :

1
 1 2 3
 1 2 3 4 5
 1 2 3 4 5 6 7
 1 2 3 4 5 6 7 8 9

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 , 2 *i):
print(j,end=" ")
print()
```

Pattern- 39 :

1
 3 2 1
 5 4 3 2 1
 7 6 5 4 3 2 1
 9 8 7 6 5 4 3 2 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 2 *i- 1 , 0 ,- :
print(j,end=" ")
print()
```

Pattern- 40 :

A
 A B C
 A B C D E
 A B C D E F G
 A B C D E F G H I

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 65 , 65 + 2 *i- :
```

17

```

print(chr(j),end=" ")
print()
```

Pattern- 41 :

A
 C B A
 E D C B A
 G F E D C B A
 I H G F E D C B A

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 65 + 2 *i- 2 , 64 ,- :
print(chr(j),end=" ")
print()
```

Pattern- 42 :

0
 1 0 1
 2 1 0 1 2
 3 2 1 0 1 2 3
 4 3 2 1 0 1 2 3 4

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i):
print(i-j,end=" ")
for k in range( 0 ,i):
print(k,end=" ")
print()
```

Pattern- 43 :

A
 B A B
 C B A B C
 D C B A B C D
 E D C B A B C D E

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
```

18

```

for j in range( 1 ,i):
print(chr(i-j+ 65 ),end=" ")
for k in range( 0 ,i):
print(chr(k+ 65 ),end=" ")
print()
```

Pattern- 44 :

1
 1 2 1
 1 2 3 2 1
 1 2 3 4 3 2 1
 1 2 3 4 5 4 3 2 1

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(j,end=" ")
for k in range(i- 1 , 0 ,- :
print(k,end=" ")
print()
```

Pattern- 45 :

A
 A B A
 A B C A B
 A B C D A B C
 A B C D E A B C D

```
 n=int(input("Enter the number of rows: "))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(chr( 64 +j),end=" ")
for k in range( 1 ,i):
print(chr( 64 +k),end=" ")
print()
```

Pattern- 46 :

```
 n=int(input("Enter a number:"))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
```

19

```

print(n+ 1 - j,end=" ")
print()
```

5
 5 4
 5 4 3
 5 4 3 2
 5 4 3 2 1

Pattern- 47 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print("*",end=" ")
for k in range( 1 ,num+ 1 - i):
print("*",end=" ")
print()
```

------

------

------

------

- 

Pattern- 48 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 0 ,num+ 1 - i):
print(num+ 1 - i,end=" ")
for k in range( 1 ,num+ 1 - i):
print(num+ 1 - i,end=" ")
print()
```

5 5 5 5 5 5 5 5 5
 4 4 4 4 4 4 4
 3 3 3 3 3
 2 2 2
 1

20

```

```

Pattern- 49 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 0 ,num+ 1 - i):
print( 2 *num+ 1 - 2 *i,end=" ")
for k in range( 1 ,num+ 1 - i):
print( 2 *num+ 1 - 2 *i,end=" ")
print()
```

9 9 9 9 9 9 9 9 9
 7 7 7 7 7 7 7
 5 5 5 5 5
 3 3 3
 1

Pattern- 50 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(j,end=" ")
for k in range( 2 ,num+ 2 - i):
print(num+k-i,end=" ")
print()
```

1 2 3 4 5 6 7
 1 2 3 4 5
 1 2 3
 1

Pattern- 51 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 65 +num-i),end=" ")
for k in range( 2 ,num+ 2 - i):
print(chr( 65 +num-i),end=" ")
print()
```

21

```

```

E E E E E E E E E
 D D D D D D D
 C C C C C
 B B B
 A

Pattern- 52 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 65 + 2 *num- 2 *i),end=" ")
for k in range( 2 ,num+ 2 - i):
print(chr( 65 + 2 *num- 2 *i),end=" ")
print()
```

I I I I I I I I I
 G G G G G G G
 E E E E E
 C C C
 A

Pattern- 53 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 64 +j),end=" ")
for k in range( 2 ,num+ 2 - i):
print(chr( 68 +k-i),end=" ")
print()
```

A B C D E F G
 A B C D E
 A B C
 A

Pattern- 54 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(j,end=" ")
```

22

```

print()
for k in range( 1 ,num):
print(" "*k,end="")
for l in range( 1 ,num+ 1 - k):
print(l,end=" ")
1 print()
```

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1

Pattern- 55 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
for k in range( 1 ,num):
print(" "*k,end="")
for l in range( 1 ,num+ 1 - k):
print("*",end=" ")
1 print()
```

- 
- - 

------

------

------

------

------

- - 
- 

Pattern- 56 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
```

23

```

print(num-j,end=" ")
print()
for k in range( 1 ,num):
print(" "*k,end="")
for l in range( 1 ,num+ 1 - k):
print(num-l,end=" ")
1 print()
```

4
 4 3
 4 3 2
 4 3 2 1
 4 3 2 1 0
 4 3 2 1
 4 3 2
 4 3
 4

Pattern- 57 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 0 ,i):
print(num+j-i,end=" ")
print()
for k in range( 1 ,num):
print(" "*k,end="")
for l in range( 1 ,num+ 1 - k):
print(l+k- 1 ,end=" ")
1 print()
```

3
 2 3
 1 2 3
 0 1 2 3
 1 2 3
 2 3
 3

Pattern- 58 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 0 ,i):
print(chr( 65 +num+j-i),end=" ")
```

24

```

print()
for k in range( 1 ,num):
print(" "*k,end="")
for l in range( 0 ,num-k):
print(chr( 65 +k+l),end=" ")
1 print()
```

E
 D E
 C D E
 B C D E
 A B C D E
 B C D E
 C D E
 D E
 E

Pattern- 59 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print("*",end=" ")
print()
for a in range( 1 ,num+ :
for k in range( 1 ,num+ 1 - a):
print("*",end=" ")
print()
```

- 
- - 

------

------

------

------

------

- - 
- 

Pattern- 60 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print(num-j,end=" ")
print()
for a in range( 1 ,num+ :
for k in range( 1 ,num+ 1 - a):
```

25

```

print(num-k,end=" ")
print()
```

4
 4 3
 4 3 2
 4 3 2 1
 4 3 2 1 0
 4 3 2 1
 4 3 2
 4 3
 4

Pattern- 61 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print(num-i+j- 1 ,end=" ")
print()
for a in range( 1 ,num+ :
for k in range( 0 ,num-a):
print(k+a,end=" ")
print()
```

4
 3 4
 2 3 4
 1 2 3 4
 0 1 2 3 4
 1 2 3 4
 2 3 4
 3 4
 4

Pattern- 62 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print(chr( 65 +num-i),end=" ")
print()
for a in range( 1 ,num+ :
for k in range( 0 ,num-a):
print(chr( 65 +a),end=" ")
print()
```

26

```

```

E
 D D
 C C C
 B B B B
 A A A A A
 B B B B
 C C C
 D D
 E

Pattern- 63 :

```
 for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print(chr( 65 +num-j),end=" ")
print()
for a in range( 1 ,num+ :
for k in range(num-a, 0 ,- :
print(chr( 64 +k+a),end=" ")
print()
num=int(input("Enter a number:"))
```

E
 E D
 E D C
 E D C B
 E D C B A
 E D C B
 E D C
 E D
 E

Pattern- 64 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
for j in range( 1 ,i+ :
print(chr( 64 +num-i+j),end=" ")
print()
for a in range( 1 ,num+ :
for k in range( 1 ,num-a+ :
print(chr( 64 +k+a),end=" ")
print()
```

27

```

```

E
 D E
 C D E
 B C D E
 A B C D E
 B C D E
 C D E
 D E
 E

Pattern- 65 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
```

- 
- - 

------

------

------

Pattern- 66 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(i,end=" ")
print()
```

1
 2 2
 3 3 3
 4 4 4 4
 5 5 5 5 5

Pattern- 67 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
```

28

```

for j in range( 1 , 1 +i):
print(j,end=" ")
print()
```

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5

Pattern- 68 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 , 1 +i):
print(chr( 64 +i),end=" ")
print()
```

A
 B B
 C C C
 D D D D
 E E E E E

Pattern- 69 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 , 1 +i):
print(chr( 64 +j),end=" ")
print()
```

A
 A B
 A B C
 A B C D
 A B C D E

Pattern- 70 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
```

29

```

print("*",end=" ")
print()
```

------

------

------

- - 
- 

Pattern- 71 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(num-i+ 1 ,end=" ")
print()
```

5 5 5 5 5
 4 4 4 4
 3 3 3
 2 2
 1

Pattern- 72 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(num+ 2 - i-j,end=" ")
print()
```

5 4 3 2 1
 4 3 2 1
 3 2 1
 2 1
 1

Pattern- 73 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 65 +num-i),end=" ")
print()
```

30

```

```

E E E E E
 D D D D
 C C C
 B B
 A

Pattern- 74 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 65 +num+ 1 - i-j),end=" ")
print()
```

E D C B A
 D C B A
 C B A
 B A
 A

Pattern- 75 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ 2 - i):
print(chr( 64 +j),end=" ")
print()
```

A B C D E
 A B C D
 A B C
 A B
 A

Pattern- 76 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
for p in range( 1 ,num):
print(" "*p,end="")
```

31

```

for q in range( 1 ,num+ 1 - p):
print("*",end=" ")
1 print()
```

- 
- - 

------

------

------

------

------

- - 
- 

Pattern- 77 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(i,end=" ")
print()
for p in range( 1 ,num):
print(" "*p,end="")
for q in range( 1 ,num+ 1 - p):
print(num-p,end=" ")
1 print()
```

1
 2 2
 3 3 3
 4 4 4 4
 5 5 5 5 5
 4 4 4 4
 3 3 3
 2 2
 1

Pattern- 78 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(j,end=" ")
print()
for p in range( 1 ,num):
```

32

```

print(" "*p,end="")
for q in range( 1 ,num+ 1 - p):
print(q+p,end=" ")
1 print()
```

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 2 3 4 5
 3 4 5
 4 5
 5

Pattern- 79 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(j,end=" ")
print()
for p in range( 1 ,num):
print(" "*p,end="")
for q in range( 1 ,num+ 1 - p):
print(q,end=" ")
1 print()
```

1
 1 2
 1 2 3
 1 2 3 4
 1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1

Pattern- 80 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(chr( 64 +i),end=" ")
print()
```

33

```

for p in range( 1 ,num):
print(" "*p,end="")
for q in range( 1 ,num+ 1 - p):
print(chr( 64 +num-p),end=" ")
1 print()
```

A
 B B
 C C C
 D D D D
 E E E E E
 D D D D
 C C C
 B B
 A

Pattern- 81 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print(chr( 64 +j),end=" ")
print()
for p in range( 1 ,num):
print(" "*p,end="")
for q in range( 1 ,num+ 1 - p):
print(chr( 64 +q+p),end=" ")
1 print()
```

A
 A B
 A B C
 A B C D
 A B C D E
 B C D E
 C D E
 D E
 E

Pattern- 82 :

```
 n=int(input("Enter a number:"))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(n-i+j,end=" ")
```

34

```

for k in range( 2 ,i+ :
print(n+ 1 - k,end=" ")
print()
for i in range( 1 ,n+ :
print(" "*i,end="")
1 for j in range( 1 +i,n+ :
1print(j,end=" ")
1for k in range( 2 ,n+ 1 - i):
1print(n+ 1 - k,end=" ")
1print()
```

5
 4 5 4
 3 4 5 4 3
 2 3 4 5 4 3 2
 1 2 3 4 5 4 3 2 1
 2 3 4 5 4 3 2
 3 4 5 4 3
 4 5 4
 5

Pattern- 83 :

```
 while True:
n=int(input("Enter a number:"))
for i in range( 1 ,n+ :
print(" "*(n-i),end="")
for j in range( 1 ,i+ :
print(n+ 1 - j,end=" ")
for k in range( 2 ,i+ :
print(n-i+k,end=" ")
print()
for i in range( 1 ,n+ :
1 print(" "*i,end="")
1for j in range( 1 ,n+ 1 - i):
1print(n+ 1 - j,end=" ")
1for k in range( 2 ,n+ 1 - i):
1print(i+k,end=" ")
1print()
```

5
 5 4 5
 5 4 3 4 5
 5 4 3 2 3 4 5
 5 4 3 2 1 2 3 4 5
 5 4 3 2 3 4 5
 5 4 3 4 5
 5 4 5

35

```

```

5

Pattern- 84 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range(i,i+ :
print("*",end=" ")
if i>= 2 :
print(" "*( 2 *i- 4 ),end="")
for k in range(i,i+ :
print("*",end=" ")
print()
```

- 
- - 
- - 
- - 
- - 

Pattern- 85 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range(i,i+ :
print(i,end=" ")
if i>= 2 :
print(" "*( 2 *i- 4 ),end="")
for k in range(i,i+ :
print(i,end=" ")
print()
```

1
 2 2
 3 3
 4 4
 5 5

Pattern- 86 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range(i,i+ :
```

36

```

print(num+ 1 - i,end=" ")
if i>= 2 :
print(" "*( 2 *i- 4 ),end="")
for k in range(i,i+ :
print(num+ 1 - i,end=" ")
print()
```

5
 4 4
 3 3
 2 2
 1 1

Pattern- 87 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range(i,i+ :
print(chr( 64 +num+ 1 - i),end=" ")
if i>= 2 :
print(" "*( 2 *i- 4 ),end="")
for k in range(i,i+ :
print(chr( 64 +num+ 1 - i),end=" ")
print()
```

E
 D D
 C C
 B B
 A A

Pattern- 88 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range(i,i+ :
print(chr( 64 +i),end=" ")
if i>= 2 :
print(" "*( 2 *i- 4 ),end="")
for k in range(i,i+ :
print(chr( 64 +i),end=" ")
print()
```

37

```

```

A
 B B
 C C
 D D
 E E

Pattern- 89 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range(i,i+ :
print("*",end=" ")
if i<= 4 :
print(" "*( 2 *num- 2 *i- 2 ),end="")
for k in range(i,i+ :
print("*",end=" ")
print()
```

- - 
- - 
- - 
- - 
- 

Pattern- 90 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range(i,i+ :
print(i,end=" ")
if i<num:
print(" "*( 2 *num- 2 *i- 2 ),end="")
for k in range(i,i+ :
print(i,end=" ")
print()
```

1 1
 2 2
 3 3
 4 4
 5

38

```

```

Pattern- 91 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range(i,i+ :
print(num-i+ 1 ,end=" ")
if i<= 4 :
print(" "*( 2 *num- 2 *i- 2 ),end="")
for k in range(i,i+ :
print(num-i+ 1 ,end=" ")
print()
```

5 5
 4 4
 3 3
 2 2
 1

Pattern- 92 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range(i,i+ :
print(chr( 64 +num-i+ ,end=" ")
if i<= 4 :
print(" "*( 2 *num- 2 *i- 2 ),end="")
for k in range(i,i+ :
print(chr( 64 +num-i+ ,end=" ")
print()
```

E E
 D D
 C C
 B B
 A

Pattern- 93 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range(i,i+ :
print(chr( 64 +i),end=" ")
if i<= 4 :
```

39

```

print(" "*( 2 *num- 2 *i- 2 ),end="")
for k in range(i,i+ :
print(chr( 64 +i),end=" ")
print()
```

A A
 B B
 C C
 D D
 E

Pattern- 94 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(i- ,end="")
for j in range( 1 ,num+ :
print("*",end=" ")
print()
```

------

------

------

------

------

Pattern- 95 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print(" "*(num-i),end="")
for k in range( 1 ,i+ :
print("*",end=" ")
print()
```

- - 

------

------

------

------

40

```

```

Pattern- 96 :

```
 n=int(input("Enter a number:"))
for i in range( 1 ,n+ :
for j in range( 1 ,i+ :
if (i% 2 != 0 and j% 2 != 0 )or(i% 2 == 0 and j% 2 == 0 ):
print("1",end=" ")
else:
print("0",end=" ")
print()
```

1
 0 1
 1 0 1
 0 1 0 1
 1 0 1 0 1
 0 1 0 1 0 1
 1 0 1 0 1 0 1

Pattern- 97 :

```
 num=int(input("Enter a number:"))
for i in range( 1 ,num+ :
print(" "*( 2 *num-i+ 3 ),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
for i in range( 1 ,num+ 3 ):
print(" "*( 2 *num-i+ ,end="")
for j in range(- 1 ,i+ :
print("*",end=" ")
1 print()
1for i in range( 1 ,num+ 5 ):
1print(" "*( 2 *num-i),end="")
1for j in range(- 2 ,i+ :
1print("*",end=" ")
1print()
1for i in range( 1 ,num+ 3 ):
1print(" "*(( 2 *num)),end="")
1print("* "* 3 )
```

41

```

```

- 
- - 

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

Pattern- 98 :

```
 num=int(input("Enter a number"))
for i in range( 1 ,num+ :
print(" "*( 2 *num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
print()
for i in range( 1 ,num+ :
print(" "*(num-i),end="")
for j in range( 1 ,i+ :
print("*",end=" ")
1 print(" "*(num-i),end="")
1for k in range( 1 ,i+ :
1print("*",end=" ")
1print()
```

- 
- - 

------

------

------

- - 

42

```

```

------

------

------

------

Pattern- 99 :

```
 n=int(input("Enter a number"))
for i in range( 1 , 2 *n+ :
if i% 2 == 0 :
print("*"*i,end=" ")
else:
print("*"*(i+ ,end=" ")
print()
```

**
 **

------

------

------

------

------

------

------

------

Pattern- 100 :

```
 n=int(input("Enter a number:"))
for a in range( 1 ,n+ 1 , 2 ):
for i in range( 1 ,n+ :
print(" "*( 2 *n-i-a),end="")
for j in range( 1 ,i+a):
print("*",end=" ")
print()
for b in range( 1 ,n+ :
print(" "*(n- 2 ),end="")
print("* "* 3 )
```

43

```

```

- 
- - 

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

------

**1**

```

```

## Python

## Logging

### Module

**2**

```

```

**Python Logging**

**It is highly recommended to store complete application flow and exceptions information to a file.
 This process is called logging.**

**The main advanatages of logging are:**

**1. We can use log files while performing debugging

1. We can provide statistics like number of requests per day etc**

**To implement logging, Python provides inbuilt module logging.**

**Logging Levels:**

**Depending on type of information, logging data is divided according to the following 6 levels in
 python**

**1. CRITICAL===>50
 Represents a very serious problem that needs high attention

1. ERROR ===>40
    Represents a serious error
2. WARNING ==>30
    Represents a warning message, some caution needed. It is alert to the programmer.
3. INFO==>20
    Represents a message with some important information
4. DEBUG ===>10
    Represents a message with debugging information
5. NOTSET==>0
    Represents that level is not set**

**By default while executing Python program only WARNING and higher level messages will be
 displayed.**

**3**

```

```

**How to implement Logging:**

**To perform logging, first we required to create a file to store messages and we have to specify
 which level messages required to store.**

**We can do this by using basicConfig() function of logging module.**

**logging.basicConfig(filename='log.txt',level=logging.WARNING)**

**The above line will create a file log.txt and we can store either WARNING level or higher level
 messages to that file.**

**After creating log file, we can write messages to that file by using the following methods**

**logging.debug(message)
 logging.info(message)
 logging.warning(message)
 logging.error(message)
 logging.critical(message)**

**Q. Write a Python Program to create a log file and write WARNING and Higher level messages?**

```
 import logging
logging.basicConfig(filename='log.txt',level=logging.WARNING)
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')
```

**log.txt:
 WARNING:root:warning Information
 ERROR:root:error Information
 CRITICAL:root:critical Information**

**Note:
 In the above program only WARNING and higher level messages will be written to the log file. If
 we set level as DEBUG then all messages will be written to the log file.**

**test.py:**

```
 import logging
logging.basicConfig(filename='log.txt',level=logging.DEBUG)
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
```

**4**

```

logging.error('error Information')
logging.critical('critical Information')
```

**log.txt:
 DEBUG:root:Debug Information
 INFO:root:info Information
 WARNING:root:warning Information
 ERROR:root:error Information
 CRITICAL:root:critical Information**

**How to configure log file in over writing mode:**

**In the above program by default data will be appended to the log file.i.e append is the default
 mode. Instead of appending if we want to over write data then we have to use filemode property.**

**logging.basicConfig(filename='log786.txt',level=logging.WARNING)
 meant for appending**

**logging.basicConfig(filename='log786.txt',level=logging.WARNING,filemode='a')
 explicitly we are specifying appending.**

**logging.basicConfig(filename='log786.txt',level=logging.WARNING,filemode='w')
 meant for over writing of previous data.**

**Note:**

**logging.basicConfig(filename='log.txt',level=logging.DEBUG)**

**If we are not specifying level then the default level is WARNING(30)**

**If we are not specifying file name then the messages will be printed to the console.**

**test.py:**

```
 import logging
logging.basicConfig()
print('Logging Demo')
logging.debug('Debug Information')
logging.info('info Information')
logging.warning('warning Information')
logging.error('error Information')
logging.critical('critical Information')
```

**D:\durgaclasses>py test.py
 Logging Demo
 WARNING:root:warning Information
 ERROR:root:error Information
 CRITICAL:root:critical Information**

**5**

```

```

**How to Format log messages:**

**By using format keyword argument, we can format messages.**

**1. To display only level name:**

**logging.basicConfig(format='%(levelname)s')**

**Output:
 WARNING
 ERROR
 CRITICAL**

**2. To display levelname and message:**

**logging.basicConfig(format='%(levelname)s:%(message)s')**

**Output:
 WARNING:warning Information
 ERROR:error Information
 CRITICAL:critical Information**

**How to add timestamp in the log messages:**

**logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')**

**Output:
 2018 - 06 - 15 11:50:08,325:WARNING:warning Information
 2018 - 06 - 15 11:50:08,372:ERROR:error Information
 2018 - 06 - 15 11:50:08,372:CRITICAL:critical Information**

**How to change date and time format:**

**We have to use special keyword argument: datefmt**

**logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y
 %I:%M:%S %p')**

**datefmt='%d/%m/%Y %I:%M:%S %p' ===>case is important**

**Output:
 15/06/2018 12:04:31 PM:WARNING:warning Information
 15/06/2018 12:04:31 PM:ERROR:error Information
 15/06/2018 12:04:31 PM:CRITICAL:critical Information**

**6**

```

```

**Note:
 %I--->means 12 Hours time scale
 %H--->means 24 Hours time scale**

**Eg:
 logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y
 %H:%M:%S')**

**Output:
 15/06/2018 12:06:28:WARNING:warning Information
 15/06/2018 12:06:28:ERROR:error Information
 15/06/2018 12:06:28:CRITICAL:critical Information**

**https://docs.python.org/3/library/logging.html#logrecord-attributes**

**https://docs.python.org/3/library/time.html#time.strftime**

**How to write Python program exceptions to the log file:**

**By using the following function we can write exception information to the log file.**

**logging.exception(msg)**

**Q. Python Program to write exception information to the log file:**

```
 import logging
logging.basicConfig(filename='mylog.txt',level=logging.INFO,format='%(asctime)s:%(leveln
ame)s:%(message)s',datefmt='%d/%m/%Y %I:%M:%S %p')
logging.info('A new Request Came')
try:
x=int(input('Enter First Number:'))
y=int(input('Enter Second Number:'))
print('The Result:',x/y)
8 )
except ZeroDivisionError as msg:
print('cannot divide with zero')
1 logging.exception(msg)
12 )
1except ValueError as msg:
1print('Please provide int values only')
1logging.exception(msg)
16 )
1logging.info('Request Processing Completed')
```

**D:\durgaclasses>py test.py
 Enter First Number:10
 Enter Second Number:2
 The Result: 5.0**

**7**

```

```

**D:\durgaclasses>py test.py
 Enter First Number:20
 Enter Second Number:2
 The Result: 10.0**

**D:\durgaclasses>py test.py
 Enter First Number:10
 Enter Second Number:0
 cannot divide with zero**

**D:\durgaclasses>py test.py
 Enter First Number:ten
 Please provide int values only**

**mylog.txt:
 15/06/2018 12:30:51 PM:INFO:A new Request Came
 15/06/2018 12:30:53 PM:INFO:Request Processing Completed
 15/06/2018 12:30:55 PM:INFO:A new Request Came
 15/06/2018 12:31:00 PM:INFO:Request Processing Completed
 15/06/2018 12:31:02 PM:INFO:A new Request Came
 15/06/2018 12:31:05 PM:ERROR:division by zero
 Traceback (most recent call last):
 File "test.py", line 7, in 
 print('The Result:',x/y)
 ZeroDivisionError: division by zero
 15/06/2018 12:31:05 PM:INFO:Request Processing Completed
 15/06/2018 12:31:06 PM:INFO:A new Request Came
 15/06/2018 12:31:10 PM:ERROR:invalid literal for int() with base 10: 'ten'
 Traceback (most recent call last):
 File "test.py", line 5, in 
 x=int(input('Enter First Number:'))
 ValueError: invalid literal for int() with base 10: 'ten'
 15/06/2018 12:31:10 PM:INFO:Request Processing Completed**

**Problems with root logger:**

**If we are not defining our own logger,then bydefault root logger will be considered.
 Once we perform basic configuration to root logger then the configurations are fixed and we
 cannot change.**

**Demo Application:**

**student.py:**

```
 import logging
logging.basicConfig(filename='student.log',level=logging.INFO)
logging.info('info message from student module')
```

**8**

```

```

**test.py:**

```
 import logging
import student
logging.basicConfig(filename='test.log',level=logging.DEBUG)
logging.debug('debug message from test module')
```

**student.log:
 INFO:root:info message from student module**

**In the above application the configurations performed in test module won't be reflected,b'z root
 logger is already configured in student module.**

**Need of Our own customized logger:**

**The problems with root logger are:**

**1. Once we set basic configuration then that configuration is final and we cannot change

1. It will always work for only one handler at a time, either console or file, but not both
    simultaneously
2. It is not possible to configure logger with different configurations at different levels
3. We cannot specify multiple log files for multiple modules/classes/methods.**

**To overcome these problems we should go for our own customized loggers**

**Advanced logging Module Features: Logger:**

**Logger is more advanced than basic logging.
 It is highly recommended to use and it provides several extra features.**

**Steps for Advanced Logging:**

**1. Creation of Logger object and set log level**

**logger = logging.getLogger('demologger')
 logger.setLevel(logging.INFO)**

**2. Creation of Handler object and set log level
 There are several types of Handlers like StreamHandler, FileHandler etc**

**consoleHandler = logging.StreamHandler()
 consoleHandler.setLevel(logging.INFO)**

**Note: If we use StreamHandler then log messages will be printed to console**

**9**

```

```

**3. Creation of Formatter object**

**formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
 datefmt='%d/%m/%Y %I:%M:%S %p')**

**4. Add Formatter to Handler
 consoleHandler.setFormatter(formatter)

1. Add Handler to Logger
    logger.addHandler(consoleHandler)
2. Write messages by using logger object and the following methods**

**logger.debug('debug message')
 logger.info('info message')
 logger.warn('warn message')
 logger.error('error message')
 logger.critical('critical message')**

**Note: Bydefault logger will set to WARNING level. But we can set our own level based on our
 requirement.**

**logger = logging.getLogger('demologger')
 logger.setLevel(logging.INFO)**

**logger log level by default available to console and file handlers. If we are not satisfied with logger
 level, then we can set log level explicitly at console level and file levels.**

**consoleHandler = logging.StreamHandler()
 consoleHandler.setLevel(logging.WARNING)**

**fileHandler=logging.FileHandler('abc.log',mode='a')
 fileHandler.setLevel(logging.ERROR)**

**Note:**

**console and file log levels should be supported by logger. i.e logger log level should be lower than
 console and file levels. Otherwise only logger log level will be considered.**

**Eg:
 logger==>DEBUG console===>INFO ------->Valid and INFO will be considered
 logger==>INFO console===>DEBUG ------->Invalid and only INFO will be considered to the
 console.**

**10**

```

```

**Demo Program for Console Handler:**

```
 import logging
class LoggerDemoConsole:
3 )
def testLog(self):
logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)
7 )
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)
10 )
1 formatter = logging.Formatter('%(asctime)s - %(name)s -
%(levelname)s: %(message)s',
1datefmt='%m/%d/%Y %I:%M:%S %p')
13 )
1consoleHandler.setFormatter(formatter)
1logger.addHandler(consoleHandler)
16 )
1logger.debug('debug message')
1logger.info('info message')
1logger.warn('warn message')
20 ) logger.error('error message')
2 logger.critical('critical message')
22 )
2demo = LoggerDemoConsole()
2demo.testLog()
```

**D:\durgaclasses>py loggingdemo3.py
 06/18/2018 12:14:15 PM - demologger - INFO: info message
 06/18/2018 12:14:15 PM - demologger - WARNING: warn message
 06/18/2018 12:14:15 PM - demologger - ERROR: error message
 06/18/2018 12:14:15 PM - demologger - CRITICAL: critical message**

**Note:**

**If we want to use class name as logger name then we have to create logger object as follows**

**logger = logging.getLogger(LoggerDemoConsole.\**name\**)**

**In this case output is:**

**D:\durgaclasses>py loggingdemo3.py
 06/18/2018 12:21:00 PM - LoggerDemoConsole - INFO: info message
 06/18/2018 12:21:00 PM - LoggerDemoConsole - WARNING: warn message
 06/18/2018 12:21:00 PM - LoggerDemoConsole - ERROR: error message
 06/18/2018 12:21:00 PM - LoggerDemoConsole - CRITICAL: critical message**

**11**

```

```

**Demo Program for File Handler:**

```
 import logging
class LoggerDemoConsole:
3 )
def testLog(self):
logger = logging.getLogger('demologger')
logger.setLevel(logging.INFO)
7 )
fileHandler = logging.FileHandler('abc.log',mode='a')
fileHandler.setLevel(logging.INFO)
10 )
1 formatter = logging.Formatter('%(asctime)s - %(name)s -
%(levelname)s: %(message)s',
1datefmt='%m/%d/%Y %I:%M:%S %p')
13 )
1fileHandler.setFormatter(formatter)
1logger.addHandler(fileHandler)
16 )
1logger.debug('debug message')
1logger.info('info message')
1logger.warn('warn message')
20 ) logger.error('error message')
2 logger.critical('critical message')
22 )
2demo = LoggerDemoConsole()
2demo.testLog()
```

**abc.log:
 07/05/2018 08:58:04 AM - demologger - INFO: info message
 07/05/2018 08:58:04 AM - demologger - WARNING: warn message
 07/05/2018 08:58:04 AM - demologger - ERROR: error message
 07/05/2018 08:58:04 AM - demologger - CRITICAL: critical message**

**Logger with Configuration File:**

**In the above program, everything we hard coded in the python script. It is not a good
 programming practice. We will configure all the required things inside a configuration file and we
 can use this file directly in our program.**

**logging.config.fileConfig('logging.conf')
 logger = logging.getLogger(LoggerDemoConf.\**name\**)**

**Note: The extension of the file need not be conf. We can use any extension like txt or durga etc**

**12**

```

```

**logging.conf:**

**[loggers]
 keys=root,LoggerDemoConf**

**[handlers]
 keys=fileHandler**

**[formatters]
 keys=simpleFormatter**

**[logger_root]
 level=DEBUG
 handlers=fileHandler**

**[logger_LoggerDemoConf]
 level=DEBUG
 handlers=fileHandler
 qualname=demoLogger**

**[handler_fileHandler]
 class=FileHandler
 level=DEBUG
 formatter=simpleFormatter
 args=('test.log', 'w')**

**[formatter_simpleFormatter]
 format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
 datefmt=%m/%d/%Y %I:%M:%S %p**

**test.py:**

```
 import logging
import logging.config
class LoggerDemoConf():
4 )
def testLog(self):
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(LoggerDemoConf.__name__)
8 )
logger.debug('debug message')
logger.info('info message')
1 logger.warn('warn message')
1logger.error('error message')
1logger.critical('critical message')
14 )
1demo = LoggerDemoConf()
1demo.testLog()
```

**13**

```

```

**test.log:
 06/18/2018 12:40:05 PM - LoggerDemoConf - DEBUG - debug message
 06/18/2018 12:40:05 PM - LoggerDemoConf - INFO - info message
 06/18/2018 12:40:05 PM - LoggerDemoConf - WARNING - warn message
 06/18/2018 12:40:05 PM - LoggerDemoConf - ERROR - error message
 06/18/2018 12:40:05 PM - LoggerDemoConf - CRITICAL - critical message**

**Case-1: To set log level as INFO:**

**[handler_fileHandler]
 class=FileHandler
 level=INFO
 formatter=simpleFormatter
 args=('test.log', 'w')**

**Case-2: To set Append Mode:**

**[handler_fileHandler]
 class=FileHandler
 level=INFO
 formatter=simpleFormatter
 args=('test.log', 'a')**

**Creation of Custom Logger:**

**customlogger.py:**

```
 import logging
import inspect
def getCustomLogger(level):
# Get Name of class/method from where this method called
loggername=inspect.stack()[ 1 ][ 3 ]
logger=logging.getLogger(loggername)
logger.setLevel(level)
8 )
fileHandler=logging.FileHandler('abc.log',mode='a')
fileHandler.setLevel(level)
1
1formatter = logging.Formatter('%(asctime)s - %(name)s -
%(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
1fileHandler.setFormatter(formatter)
1logger.addHandler(fileHandler)
15 )
1return logger
```

**14**

```

```

**test.py:**

```
 import logging
from customlogger import getCustomLogger
class LoggingDemo:
def m1(self):
logger=getCustomLogger(logging.DEBUG)
logger.debug('m1:debug message')
logger.info('m1:info message')
logger.warn('m1:warn message')
logger.error('m1:error message')
logger.critical('m1:critical message')
1 def m2(self):
1logger=getCustomLogger(logging.WARNING)
1logger.debug('m2:debug message')
1logger.info('m2:info message')
1logger.warn('m2:warn message')
1logger.error('m2:error message')
1logger.critical('m2:critical message')
1def m3(self):
1logger=getCustomLogger(logging.ERROR)
20 ) logger.debug('m3:debug message')
2 logger.info('m3:info message')
2logger.warn('m3:warn message')
2logger.error('m3:error message')
2logger.critical('m3:critical message')
25 )
2l=LoggingDemo()
2print('Custom Logger Demo')
2l.m1()
2l.m2()
30 ) l.m3()
```

**abc.log:
 06/19/2018 12:17:19 PM - m1 - DEBUG: m1:debug message
 06/19/2018 12:17:19 PM - m1 - INFO: m1:info message
 06/19/2018 12:17:19 PM - m1 - WARNING: m1:warn message
 06/19/2018 12:17:19 PM - m1 - ERROR: m1:error message
 06/19/2018 12:17:19 PM - m1 - CRITICAL: m1:critical message
 06/19/2018 12:17:19 PM - m2 - WARNING: m2:warn message
 06/19/2018 12:17:19 PM - m2 - ERROR: m2:error message
 06/19/2018 12:17:19 PM - m2 - CRITICAL: m2:critical message
 06/19/2018 12:17:19 PM - m3 - ERROR: m3:error message
 06/19/2018 12:17:19 PM - m3 - CRITICAL: m3:critical message**

**15**

```

```

**How to create seperate log file Based on Caller:**

```
 import logging
import inspect
def getCustomLogger(level):
loggername=inspect.stack()[ 1 ][ 3 ]
logger=logging.getLogger(loggername)
logger.setLevel(level)
7 )
fileHandler=logging.FileHandler('{}.log'.format(loggername),mode='a')
fileHandler.setLevel(level)
10 )
1 formatter = logging.Formatter('%(asctime)s - %(name)s -
%(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
1fileHandler.setFormatter(formatter)
1logger.addHandler(fileHandler)
14 )
1return logger
```

**test.py:**

**#Same as previous**

```
 import logging
from customlogger import getCustomLogger
class LoggingDemo:
def m1(self):
logger=getCustomLogger(logging.DEBUG)
logger.debug('m1:debug message')
logger.info('m1:info message')
logger.warn('m1:warn message')
logger.error('m1:error message')
logger.critical('m1:critical message')
1 def m2(self):
1logger=getCustomLogger(logging.WARNING)
1logger.debug('m2:debug message')
1logger.info('m2:info message')
1logger.warn('m2:warn message')
1logger.error('m2:error message')
1logger.critical('m2:critical message')
1def m3(self):
1logger=getCustomLogger(logging.ERROR)
20 ) logger.debug('m3:debug message')
2 logger.info('m3:info message')
2logger.warn('m3:warn message')
2logger.error('m3:error message')
2logger.critical('m3:critical message')
25 )
```

**16**

```

2l=LoggingDemo()
2print('Logging Demo with Seperate Log File')
2l.m1()
2l.m2()
30 ) l.m3()
```

**m1.log:
 06/19/2018 12:26:04 PM - m1 - DEBUG: m1:debug message
 06/19/2018 12:26:04 PM - m1 - INFO: m1:info message
 06/19/2018 12:26:04 PM - m1 - WARNING: m1:warn message
 06/19/2018 12:26:04 PM - m1 - ERROR: m1:error message
 06/19/2018 12:26:04 PM - m1 - CRITICAL: m1:critical message**

**m2.log:
 06/19/2018 12:26:04 PM - m2 - WARNING: m2:warn message
 06/19/2018 12:26:04 PM - m2 - ERROR: m2:error message
 06/19/2018 12:26:04 PM - m2 - CRITICAL: m2:critical message**

**m3.log:
 06/19/2018 12:26:04 PM - m3 - ERROR: m3:error message
 06/19/2018 12:26:04 PM - m3 - CRITICAL: m3:critical message**

**Advantages of customized logger:**

**1. We can reuse same customlogger code where ever logger required.

1. For every caller we can able to create a seperate log file
2. For different handlers we can set different log levels.**

**Another Example for Custom Handler:**

**customlogger.py:**

```
 import logging
import inspect
def getCustomLogger(level):
loggername=inspect.stack()[ 1 ][ 3 ]
5 )
logger=logging.getLogger(loggername)
logger.setLevel(level)
fileHandler=logging.FileHandler('test.log',mode='a')
fileHandler.setLevel(level)
formatter=logging.Formatter('%(asctime)s - %(name)s -
%(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
1 fileHandler.setFormatter(formatter)
1logger.addHandler(fileHandler)
1return logger
```

**17**

```

```

**test.py:**

```
 import logging
from customlogger import getCustomLogger
class Test:
def logtest(self):
logger=getCustomLogger(logging.DEBUG)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
1 t=Test()
1t.logtest()
```

**student.py:**

```
 import logging
from customlogger import getCustomLogger
def studentfunction():
logger=getCustomLogger(logging.ERROR)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
studentfunction()
```

**Note: we can disable a partcular level of logging as follows:
 logging.disable(logging.CRITICAL)**