import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1811',
    charset='utf8'
)
cursor = conn.cursor()
##############################
insert_dep1 = 'INSERT INTO departments VALUES (%s, %s)'
deps = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '市场部')]
# cursor.executemany(insert_dep1, deps)

deps2 = [(5, '测试部')]
# cursor.executemany(insert_dep1, deps2)

deps3 = [(6, '财务部'), (7, '运营部')]
# cursor.executemany(insert_dep1, deps3)
##############################
update_hr = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
data = ('人力资源部', '人事部')
# cursor.execute(update_hr, data)
##############################
del_yy = 'DELETE FROM departments WHERE dep_name=%s'
yy_dep = ('运营部',)
# cursor.execute(del_yy, yy_dep)
##############################
# select1 = 'SELECT * from departments ORDER BY dep_id'
# cursor.execute(select1)
# result1 = cursor.fetchone()  # 取一行记录
# result2 = cursor.fetchmany(2)   # 取2行记录
# result3 = cursor.fetchall()   # 取全部数据
# print(result1)
# print('#' * 30)
# print(result2)
# print('#' * 30)
# print(result3)
##############################
select2 = 'SELECT * from departments ORDER BY dep_id'
cursor.execute(select2)
cursor.scroll(3, mode='absolute')  # 以绝对方式向下移动3条记录
result1 = cursor.fetchone()
cursor.scroll(-1)  # 默认以相对方式移动
result2 = cursor.fetchone()
print(result1)
print('#' * 30)
print(result2)
##############################
conn.commit()    # 提交改动
cursor.close()   # 关闭游标
conn.close()
