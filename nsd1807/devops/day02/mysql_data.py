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
create_employees = 'CREATE XXX'
cursor.execute(create_employees)
conn.commit()
cursor.close()
conn.close()
