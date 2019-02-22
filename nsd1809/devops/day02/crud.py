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
cursor.executemany(insert_dep1, [(2, '运维部'), (3, '开发部')])


conn.commit()
cursor.close()
conn.close()
