# 训练第十三章部分--数据库
import sqlite3
conn=sqlite3.connect("test.db")
print("Opened database successfully")
c=conn.cursor()
c.execute("DELETE FROM COMPANY  WHERE  ID=4")
conn.commit()
print(conn.total_changes)
cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")

# print "Operation done successfully";
conn.close()