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
############################################
# insert1 = 'INSERT INTO department VALUES (%s, %s)'
# cursor.execute(insert1, (1, '人事部'))
# cursor.executemany(insert1, [(2, '运维部')])
# cursor.executemany(insert1, [(3, '开发部'), (4, '财务部'), (5, '行政部'), (6, '市场部'), (7, '测试部')])
############################################
select1 = 'SELECT * FROM department order by dep_id'
cursor.execute(select1)
result = cursor.fetchone()
print(result)
print('*' * 30)
result2 = cursor.fetchmany(2)
print(result2)
print('*' * 30)
result3 = cursor.fetchall()
print(result3)




conn.commit()
cursor.close()
conn.close()
