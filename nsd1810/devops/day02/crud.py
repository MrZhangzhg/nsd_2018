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

insert1 = 'INSERT INTO department VALUES (%s, %s)'
cursor.execute(insert1, (1, '人事部'))
cursor.executemany(insert1, [(2, '运维部')])
cursor.executemany(insert1, [(3, '开发部'), (4, '财务部')])


conn.commit()
cursor.close()
conn.close()
