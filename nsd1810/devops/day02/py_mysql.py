import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1810',
    charset='utf8'
)
cursor = conn.cursor()

# create_dep = '''CREATE TABLE department(
# dep_id INT, dep_name VARCHAR(20) NOT NULL UNIQUE ,
# PRIMARY KEY(dep_id)
# )'''
# cursor.execute(create_dep)
############################################
# create_emps = '''CREATE TABLE employees(
# emp_id INT, name VARCHAR(20),birth_date DATE,
# email VARCHAR(50), dep_id INT, PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES department(dep_id)
# )'''
# cursor.execute(create_emps)
############################################
create_sal = '''CREATE TABLE salary(
auto_id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY(auto_id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''
cursor.execute(create_sal)

cursor.close()
conn.close()
