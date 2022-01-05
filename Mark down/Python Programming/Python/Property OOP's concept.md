## Property OOP's concept

there are three main type of properties:-

1. setter 
2. getter
3. deleter

```python
class Person:
	def __init__(self,name):
		self.__name = name
        
	def get_name(self):
		return self.__name
    
	def set_name(self,value):
		self.__name=value
    
    def del_name(self,name):
        del self.__name
    
    name = property(fget = get_name, fset= set_name, fdel= del_name)
    
p=Person('Sharique')
print(p.name) # calling setter methode
p.name = 'Sufiyan' # calling getter methode
print(p.name)
del name # calling deleter method
       
```

