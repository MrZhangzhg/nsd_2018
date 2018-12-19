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

# insert_dep1 = 'INSERT INTO departments VALUES(%s, %s)'
# hr = (1, 'hr')
# other_deps = [(2, '运维部'), (3, '开发部'), (4, '测试部')]
# cursor.execute(insert_dep1, hr)
# cursor.executemany(insert_dep1, other_deps)
#############################
#
insert_emp = 'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)'
gw = (10, '高伟', '男', 'gaowei@163.com', '15012345678', 2)
hl = (11, '何林', '男', 'hl@qq.com', '13512344321', 2)
zs = (12, '张思', '男', 'zs@qq.com', '15098761234', 2)
zj = (13, '周婕', '女', 'zj@163.com', '17600112233', 4)
ws = (20, '王顺', '男', 'ws@sohu.com', '18900998877', 3)
zy = (25, '张羽', '男', 'zy@163.com', '13366778899', 1)
py = (30, '潘越', '男', 'py@sohu.com', '13256789876', 3)
zzy = (42, '张之毅', '男', 'zzy@126.com', '13898765678', 4)
ll = (45, '林灵', '男', 'll@aliyun.com', '13789896786', 1)
bsf = (48, '白松峰', '男', 'bsf@163.com', '13987654321', 2)
xej = (50, '夏二姣', '女', 'xej@qq.com', '15098567800', 2)
emps = [gw, hl, zs, zj, ws, zy, py, zzy, ll, bsf, xej]
cursor.executemany(insert_emp, emps)

conn.commit()
cursor.close()
conn.close()
