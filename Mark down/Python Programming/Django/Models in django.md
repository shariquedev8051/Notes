# Models in Django

## Models

**Reference**:- Geeks For Geeks	[click me](https://www.geeksforgeeks.org/django-models/)

| Function                       | Application                                    |
| ------------------------------ | ---------------------------------------------- |
| **emp****.save()**             | To save object into database.                  |
| emp.\_\_dict\_\_               | To see dictionary representation of an object. |
| Employee.objects.create(kwrgs) | To create and save object in database.         |
| Employee.objects.all()         | To fetch all objects data from the database    |

- Use following command to run orm queries in shell

```python
exec(open(FILE_PATH).read())
```

- Create db_shell.py on project level....
- To get printable objects override **str** and **repr** methods in the class. 

## Relations

### one to one relationship:-

```python
class Adhaar(models.Model):
    uid = models.CharField(max_length=20, primary_key=True)
    DOB = models.DateField(null=True)
    employee = models.OneToOneField(Employee, related_name='adhaar', on_delete=models.CASCADE)
```

