import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1808',
    charset='utf8'
)
cursor = conn.cursor()

insert1 = 'INSERT INTO departments VALUES(%s, %s)'
cursor.execute(insert1, (1, 'HR'))
deps = [(2, '运维'), (3, '开发'), (4, '测试')]
cursor.executemany(insert1, deps)
conn.commit()

cursor.close()
conn.close()
