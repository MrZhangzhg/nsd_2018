import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1809',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标，类似于文件对象，用它来执行SQL语句

# create_departments = """CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(20) NOT NULL UNIQUE,
# PRIMARY KEY(dep_id)
# )"""
# cursor.execute(create_departments)

# create_employees = """CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(20), gender VARCHAR(6),
# birth_date DATE, email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id),
# FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )"""
# cursor.execute(create_employees)

create_salary = """CREATE TABLE salary(
auto_id INT, emp_id INT, date DATE, basic INT, awards INT,
PRIMARY KEY(auto_id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""
cursor.execute(create_salary)

conn.commit()
cursor.close()
conn.close()
