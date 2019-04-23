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
cursor.executemany(insert_dep1, deps)
##############################
conn.commit()    # 提交改动
cursor.close()   # 关闭游标
conn.close()
