import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='wnsd1',
    charset='utf8'
)
# 创建游标
cursor = conn.cursor()

#############################################
# 创建表的SQL语句
# create_dep = '''CREATE TABLE departments(
# dep_id INT, dep_name VARCHAR(50),
# PRIMARY KEY(dep_id)
# )'''
# create_emp = '''CREATE TABLE employees(
# emp_id INT, emp_name VARCHAR(50), email VARCHAR(50), dep_id INT,
# PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
# )'''
# create_sal = '''CREATE TABLE salary(
# id INT, date DATE, emp_id INT, basic INT, awards INT,
# PRIMARY KEY(id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
# )'''

# 执行SQL语句
# cursor.execute(create_dep)
# cursor.execute(create_emp)
# cursor.execute(create_sal)

#############################################
# 插入语句
# insert_dep = 'INSERT INTO departments VALUES(%s, %s)'
# cursor.executemany(insert_dep, [(1, '人事部')])
# deps = [(2, '财务部'), (3, '运维部'), (4, '开发部'), (5, '测试部'), (6, '市场部')]
# cursor.executemany(insert_dep, deps)

#############################################
# 修改
# update1 = 'UPDATE departments set dep_name=%s WHERE dep_name=%s'
# cursor.execute(update1, ('人力资源部', '人事部'))
#############################################
# 删除
delete1 = 'DELETE FROM departments WHERE dep_name=%s'
cursor.execute(delete1, ('市场部',))

#############################################
# 查询
select = 'SELECT * FROM departments'
cursor.execute(select)
result = cursor.fetchone()  # 相当于文件的f.readline()
print(result)
print('*' * 30)
result2 = cursor.fetchmany(2)  # 读取两行记录
print(result2)
print('*' * 30)
result3 = cursor.fetchall()   # 相当于文件的f.readlines()
print(result3)


conn.commit()   # 确认
# 关闭游标和到数据库的网络连接
cursor.close()
conn.close()
