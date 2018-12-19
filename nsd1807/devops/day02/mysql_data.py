import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1807',
    charset='utf8'
)
cursor = conn.cursor()
# create_dep = '''CREATE TABLE departments(dep_id INT,
# dep_name VARCHAR(20) UNIQUE NOT NULL, PRIMARY KEY(dep_id))
# '''
create_emp = '''CREATE TABLE employess(emp_id INT,
emp_name VARCHAR(20), gender VARCHAR(6), email VARCHAR(50),
phone CHAR(11), dep_id INT, PRIMARY KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES departments(dep_id))'''
# cursor.execute(create_dep)
cursor.execute(create_emp)
conn.commit()
cursor.close()
conn.close()
