#! C:\Users\aiman\AppData\Local\Programs\Python\Python310-32\python.exe
print("Content-Type: text/html\r\n\r\n")
import cgi
#!/usr/bin/python

print("Content-Type: text/html\n")

import cgi
import mysql.connector

# Step 1: Get form data
f = cgi.FieldStorage()
print("<html><body>")
for i in range(1, 5):
    print(f"t{i} = {f.getvalue(f't{i}')}<br>")
print("</body></html>")

pid = f.getvalue('t1')
pname = f.getvalue('t2')
total_sem = f.getvalue('t3')
description = f.getvalue('t4')

# Step 2: Connect to MySQL
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",                      # your MySQL username
        password="#mysql@2027",                      # your MySQL password
        database="stud_prog"              # correct DB name (as seen in your image)
    )
    cursor = conn.cursor()

    # Step 3: Insert query
    query = """INSERT INTO Program
    (pid, pname, total_sem, description) 
    VALUES (%s, %s, %s, %s)"""
    
    values = (pid ,pname, total_sem, description)

    cursor.execute(query, values)
    conn.commit()

    print("<html><body><h2>Data Inserted Successfully into Program!</h2></body></html>")

except Exception as e:
    print(f"<html><body><h2>Error: {e}</h2></body></html>")

finally:
    cursor.close()
    conn.close()