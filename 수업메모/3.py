import os 


# # print(os.environ)
# print(os.getenv("Path"))

# # os.environ["path"] = r"%PATH%;C:\laragon\bin\mysql\mysql-8.0.30-winx64\bin"

# from  pymysql import Connection
import pymysql
import pymysql.cursors

conn = pymysql.connect(host="localhost",user="encore",passwd="encore1234",database="employees")
print(conn)

cur = conn.cursor(pymysql.cursors.DictCursor)

with open(r"C:\Users\USER\Downloads\employees\employees.sql", encoding='utf-8') as file:
   sql = file.read()
sql = sql.split(";")

for item in sql:
    try:
        print(cur.execute(item))
    except Exception as e:
        print(e)
        item.replace("/",os.path.sep)








        
# result = cur.execute("Select * From titles")

# sq1 = """
# SELECT hire_date* 
# FROM employees
# WHERE emp_no = 10001;
# """
# print(cur)

# print (result)

# result = cur.fetchall()

# print(result[0]["to_date"])


# with open(r"주소 쑤기")
#먼가 출력이 잘 욈 

 