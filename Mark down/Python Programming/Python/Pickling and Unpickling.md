## Pickling and Unpickling

### Pickling and unpickling single object

```python
import pickle

class Student:
    """Class to store the data related to student"""

    def __init__(self, name, roll_no) -> None:
        self.name = name
        self.roll_no = roll_no

    def __repr__(self) -> str:
        return f"{self.name} -- {self.roll_no}"
    
s1 = Student("sharique", 334)

FILEPATH = "stud.dat"

# To save data in binary file
with open(Filepath,'wb') as f:
    pickle.dump(s1, f)

# To read data from binary file
with open(Filepath,'rb') as f:
    pickle.load(f)
```

### Pickling and Unpickling multiple object 

```python
import pickle

class Student:
    """Class to store the data related to student"""

    def __init__(self, name, roll_no) -> None:
        self.name = name
        self.roll_no = roll_no

    def __repr__(self) -> str:
        return f"{self.name} -- {self.roll_no}"

s1 = Student("sharique", 334)
s2 = Student("Sudhanshu", 335)
s3 = Student("Ayush", 336)
s4 = Student("Nargis", 337)
list1 = [s1, s2, s3, s4]

def dumpData(filepath,l):
	with open(filepath, "wb") as f:   
		 for obj in l:
			pickle.dump(obj, f)

def loadData(filepath):
    with open(filepath, 'rb') as f:
        try:
            yield pickle.load(f)
		except EOFerror:
            break

dumpData("stud.dat",list1)  
objs = list(loadData("stud.dat"))
print(objs)
```

