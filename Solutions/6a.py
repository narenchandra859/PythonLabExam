import sqlite3 as sql

con = sql.connect("Employee.db")
cur = con.cursor()

cur.execute("DROP TABLE if exists Employees")
con.commit()

cur.execute("CREATE TABLE Employees(id integer, name text, sal real, dept text)")
con.commit()

cur.execute("INSERT INTO Employees VALUES(101,'Ramesh',75000,'DEP A')")
cur.execute("INSERT INTO Employees VALUES(102,'Suresh',25000,'DEP C')")
cur.execute("INSERT INTO Employees VALUES(103,'Dinesh',45000,'DEP D')")
cur.execute("INSERT INTO Employees VALUES(104,'Vignesh',85000,'DEP A')")
cur.execute("INSERT INTO Employees VALUES(105,'Himesh',95000,'DEP B')")
con.commit()

cur.execute("SELECT * from Employees")
data = cur.fetchall()
for line in data:
  print(line)

print()
print()

cur.execute("SELECT id,name FROM Employees WHERE sal>=50000")
data = cur.fetchall()
for line in data:
  print(line)