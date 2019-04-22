import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1811',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标
# SQL语句
# create_dep = '''CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(20),
# PRIMARY KEY(dep_id)
# )'''
# cursor.execute(create_dep)   # 执行sql语句
# create_emps = '''CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(20), email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )'''
# cursor.execute(create_emps)
create_sal = '''CREATE TABLE salary(
auto_id INT, emp_id INT, date DATE, basic INT, awards INT,
PRIMARY KEY(auto_id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''
cursor.execute(create_sal)
conn.commit()    # 提交改动
cursor.close()   # 关闭游标
conn.close()     # 关闭连接
