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

insert_dep1 = 'INSERT INTO departments VALUES(%s, %s)'
hr = (1, 'hr')
other_deps = [(2, '运维部'), (3, '开发部'), (4, '测试部')]
cursor.execute(insert_dep1, hr)
cursor.executemany(insert_dep1, other_deps)

conn.commit()
cursor.close()
conn.close()
