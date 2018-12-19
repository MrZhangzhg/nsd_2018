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

update_hr = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
data = ('人事部', 'hr')
cursor.execute(update_hr, data)

delete_dep = 'DELETE FROM departments WHERE dep_id=%s'
cursor.execute(delete_dep, (4,))

conn.commit()
cursor.close()
conn.close()
