import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="db",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
# sql="create table students(rollno int,sname varchar(50),course varchar(50),marks int)"
#
# cursor.execute(sql)
# data=cursor.fetchall()
# print(data)
# db.close()

sql="insert into students(rollno, sname, course, marks) values(1,'arun','science',100)"
sql="insert into students(rollno, sname, course, marks) values(2,'akhiil','cs',300)"
try:
    cursor.execute(sql)
    db.commit()

except Exception as e:
    print(e.args)
    db.rollback()


