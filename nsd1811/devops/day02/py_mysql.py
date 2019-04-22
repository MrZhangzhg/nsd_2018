import pymysql

# 创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1811',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标
create_dep = ''   # SQL语句
cursor.execute(create_dep)   # 执行sql语句
conn.commit()    # 提交改动
cursor.close()   # 关闭游标
conn.close()     # 关闭连接
