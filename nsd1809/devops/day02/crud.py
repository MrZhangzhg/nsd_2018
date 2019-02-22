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

insert_dep1 = 'INSERT INTO departments(dep_id, dep_name) VALUES (%s, %s)'
# cursor.execute(insert_dep1, (1, '人事部'))
# cursor.executemany(insert_dep1, [(2, '运维部'), (3, '开发部')])
# cursor.executemany(insert_dep1, [(4, '财务部'), (5, '测试部'), (6, '行政部')])

insert_emp1 = 'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)'
# cursor.executemany(
#     insert_emp1,
#     [
#         (1, '黄涛', '男', '1991-1-10', 'ht@qq.com', 2),
#         (2, '邱彬', '男', '1993-3-14', 'qb@163.com', 3)
#     ]
# )

query_dep1 = 'SELECT * FROM departments ORDER BY dep_id'
cursor.execute(query_dep1)
# result1 = cursor.fetchone()  # 取1行
# print(result1)
# print('*' * 30)
# result2 = cursor.fetchmany(2)  # 取多行
# print(result2)
# print('*' * 30)
# result3 = cursor.fetchall()  # 取全部
# print(result3)

cursor.scroll(2, mode='absolute')
result4 = cursor.fetchone()
print(result4)
print('*' * 30)
cursor.scroll(1)  # 默认以相对位置的方式移动
result5 = cursor.fetchone()
print(result5)

conn.commit()
cursor.close()
conn.close()
