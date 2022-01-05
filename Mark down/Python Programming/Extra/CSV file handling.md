# CSV file handling

```python
import csv

# To write csv data into csv.files
with open('first.csv','w',newline="") as f:
    w = csv.writer(f)
    w.writerow(['ENO','ENAME',"ESAL","EADDR"])
    n = int(input('Enter Numbers of Employees: '))
    for i in range(n):
        eno = input('Enter employee no: ')
        ename = input('Enter employee name: ')
        esal = input('Enter employee salary: ')
        eaddr = input('Enter employee address: ')
        w.writerow([eno,ename,esal,eaddr])
    print("Employees Added!!")
```

