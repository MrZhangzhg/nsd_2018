from dbconn import Departments, Employees, Session

session = Session()

hr = Departments(dep_name='人事部')
ops = Departments(dep_name='运维部')
dev = Departments(dep_name='开发部')
qa = Departments(dep_name='测试部')
finance = Departments(dep_name='财务部')
xz = Departments(dep_name='行政部')
# session.add(hr)
# session.add_all([ops, dev, qa, finance, xz])
#######################################
gyh = Employees(
    emp_name='耿宇航',
    gender='男',
    birth_date='1993-8-23',
    email='gyh@qq.com',
    dep_id=2
)
zjy = Employees(
    emp_name='张钧溢',
    gender='男',
    birth_date='1990-10-15',
    email='zjy@163.com',
    dep_id=2
)
jp = Employees(
    emp_name='蒋鹏',
    gender='男',
    birth_date='1995-3-23',
    email='jp@qq.com',
    dep_id=3
)
ljj = Employees(
    emp_name='李杰君',
    gender='男',
    birth_date='1995-4-18',
    email='ljj@126.com',
    dep_id=3
)
ghn = Employees(
    emp_name='郭浩南',
    gender='男',
    birth_date='1992-2-5',
    email='ghn@qq.com',
    dep_id=1
)
wyf = Employees(
    emp_name='王宇峰',
    gender='男',
    birth_date='1994-12-9',
    email='wyf@qq.com',
    dep_id=4
)
cl = Employees(
    emp_name='陈磊',
    gender='男',
    birth_date='1994-11-2',
    email='cl@qq.com',
    dep_id=2
)
xkn = Employees(
    emp_name='徐康宁',
    gender='男',
    birth_date='1994-9-12',
    email='xkn@qq.com',
    dep_id=2
)
ytt = Employees(
    emp_name='余婷婷',
    gender='女',
    birth_date='1996-5-18',
    email='ytt@qq.com',
    dep_id=3
)
session.add_all([gyh, zjy, jp, ljj, ghn, wyf, cl, xkn, ytt])
#######################################
session.commit()
session.close()
