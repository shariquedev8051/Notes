### Python MySQL connection

```powershell
pip install mysql-connector-python
```

- make connection

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

print(mydb) 
```

