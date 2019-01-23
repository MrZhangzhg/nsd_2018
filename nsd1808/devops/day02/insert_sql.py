from dbconn import Departments, Employees, Salary, Session

session = Session()
# hr = Departments(dep_id=1, dep_name='HR')
# session.add(hr)
# session.commit()
#####################################
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qs = Departments(dep_id=4, dep_name='测试部')
# fn = Departments(dep_name='财务部')   # sqlalchemy把主键设置为了自动增长
# session.add_all([ops, dev, qs, fn])
# session.commit()
#####################################
tc = Employees(emp_id=100, emp_name='田超', email='tc@qq.com', dep_id=1)
by = Employees(emp_id=101, emp_name='白宇', email='by@qq.com', dep_id=2)
bss = Employees(emp_id=200, emp_name='白尚松', email='bss@163.com', dep_id=2)
hdy = Employees(emp_id=201, emp_name='何东阳', email='hdy@163.com', dep_id=3)
fg = Employees(emp_id=300, emp_name='房果', email='fg@qq.com', dep_id=2)
wfh = Employees(emp_id=301, emp_name='巫菲红', email='wfh@tedu.com', dep_id=1)
fcw = Employees(emp_id=302, emp_name='冯翠雯', email='fcw@tarena.com', dep_id=4)
sz = Employees(emp_id=400, emp_name='孙正', email='sz@126.com', dep_id=2)
zqh = Employees(emp_id=401, emp_name='章勤浩', email='zqh@126.com', dep_id=3)
cjl = Employees(emp_id=500, emp_name='陈佳乐', email='cjl@qq.com', dep_id=5)
hpw = Employees(emp_id=600, emp_name='黄平武', email='hpw@163.com', dep_id=4)
bh = Employees(emp_id=700, emp_name='柏宏', email='bh@qq.com', dep_id=2)
tr = Employees(emp_id=800, emp_name='唐瑞', email='tr@qq.com', dep_id=5)
lj = Employees(emp_id=900, emp_name='鲁俊', email='lj@qq.com', dep_id=3)
session.add_all([tc, by, bss, hdy, fg, wfh, fcw, sz, zqh, cjl, hpw, bh, tr, lj])
session.commit()


session.close()
