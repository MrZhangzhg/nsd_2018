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

create_dep = """CREATE TABLE departments(
dep_id INT, dep_name VARCHAR(20) NOT NULL UNIQUE, PRIMARY KEY(dep_id))
"""
cursor.execute(create_dep)

cursor.close()
conn.close()


