import sqlite3 as sql

con = sql.connect("Database.db")
cur = con.cursor()
cur.execute("DROP TABLE if exists Hospital")
con.commit()
cur = con.cursor()
con.commit()

cur.execute("CREATE TABLE Hospital(Hospital_Id integer, Hospital_Name text, Bed_Count integer)")
con.commit()

cur.execute("INSERT INTO Hospital VALUES(1,'Mayo Clinic',200)")
cur.execute("INSERT INTO Hospital VALUES(2,'Cleveland Clinic',400)")
cur.execute("INSERT INTO Hospital VALUES(3,'Johns Hopkins',1000)")
cur.execute("INSERT INTO Hospital VALUES(4,'UCLA Medical Center',1500)")
con.commit()

print("Current Table Contents : ")

cur.execute("SELECT * from Hospital")
data = cur.fetchall()
for line in data:
  print(line)

print("Executing commands to update and delete")

cur.execute("UPDATE Hospital SET Bed_Count=100 WHERE Hospital_Id=1")
cur.execute("DELETE FROM Hospital WHERE Hospital_Id=3")
con.commit()

print("Current Table Contents : ")

cur.execute("SELECT * from Hospital")
data = cur.fetchall()
for line in data:
  print(line)