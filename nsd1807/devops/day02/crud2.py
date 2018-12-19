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

# query1 = 'SELECT * FROM departments'
# cursor.execute(query1)
# result = cursor.fetchone()
# result2 = cursor.fetchmany(2)
# result3 = cursor.fetchall()
# print(result)
# print('-' * 30)
# print(result2)
# print('-' * 30)
# print(result3)
##############################
# query1 = 'SELECT * FROM departments ORDER BY dep_id'
# cursor.execute(query1)
# cursor.scroll(2, mode='absolute')  # 绝对移动是从开头算
# result = cursor.fetchone()
# print(result)
# print('-' * 30)
# cursor.scroll(-2)   # 默认是相对移动
# result1 = cursor.fetchone()
# print(result1)
##############################
query3 = '''SELECT e.emp_name, d.dep_name FROM employees AS e
JOIN departments AS d ON e.dep_id = d.dep_id'''
cursor.execute(query3)
result = cursor.fetchall()
print(result)


cursor.close()
conn.close()
