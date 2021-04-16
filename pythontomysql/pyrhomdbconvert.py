#mysql-connector
#step 1- import mysql module
# import mysql.connector
#
# #step 2- establisg connection
#  db=mysql.connector.connect(
#      host="localhost",
#      user="root",
#      passwd="Password@123"
# )
#step 3- create cursor object
#execute queries
#close db connection

import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Password@123",
    auth_plugin="mysql_native_password"
)

cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
db.close()