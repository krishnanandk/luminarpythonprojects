
import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    database="db",
    auth_plugin="mysql_native_password"
)
cursor=db.cursor()
f=open("employee","r")
for lines in f:
    words=lines.rstrip("\n").split(",")

sql="insert into students(rollno, sname, course, marks) values(%s,%s,%s,%s)"

    cursor.execute(sql,tuple(data))
    db.commit()


