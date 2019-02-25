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
# gyh = Employees(
#     emp_name='耿宇航',
#     gender='男',
#     birth_date='1993-8-23',
#     email='gyh@qq.com',
#     dep_id=2
# )
# zjy = Employees(
#     emp_name='张钧溢',
#     gender='男',
#     birth_date='1990-10-15',
#     email='zjy@163.com',
#     dep_id=2
# )
# jp = Employees(
#     emp_name='蒋鹏',
#     gender='男',
#     birth_date='1995-3-23',
#     email='jp@qq.com',
#     dep_id=3
# )
# ljj = Employees(
#     emp_name='李杰君',
#     gender='男',
#     birth_date='1995-4-18',
#     email='ljj@126.com',
#     dep_id=3
# )
# ghn = Employees(
#     emp_name='郭浩南',
#     gender='男',
#     birth_date='1992-2-5',
#     email='ghn@qq.com',
#     dep_id=1
# )
# wyf = Employees(
#     emp_name='王宇峰',
#     gender='男',
#     birth_date='1994-12-9',
#     email='wyf@qq.com',
#     dep_id=4
# )
# cl = Employees(
#     emp_name='陈磊',
#     gender='男',
#     birth_date='1994-11-2',
#     email='cl@qq.com',
#     dep_id=2
# )
# xkn = Employees(
#     emp_name='徐康宁',
#     gender='男',
#     birth_date='1994-9-12',
#     email='xkn@qq.com',
#     dep_id=2
# )
# ytt = Employees(
#     emp_name='余婷婷',
#     gender='女',
#     birth_date='1996-5-18',
#     email='ytt@qq.com',
#     dep_id=3
# )
# session.add_all([gyh, zjy, jp, ljj, ghn, wyf, cl, xkn, ytt])
#######################################
# query1 = session.query(Departments)
# print(query1)  # query1只是一个SQL查询语句
# print(query1.all())  # 返回的是Departments所有实例组成的列表
# for dep in query1:   # 取出查询结果中的每一个实例
#     print(dep)
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))  # 打印实例的属性
#######################################
# query2 = session.query(Departments).order_by(Departments.dep_id)
# print(query2)
# for dep in query2:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# query3 = session.query(Employees.emp_name, Employees.email)
# print(query3)
# print(query3.all())  # 结果是由元组构成的列表
# for name, email in query3:
#     print('%s: %s' % (name, email))
#######################################
# query4 = session.query(Departments.dep_name.label('部门'))
# print(query4)
# for dep in query4:
#     print(dep.部门)
#######################################
# query5 = session.query(Departments).order_by(Departments.dep_id)
# dep = query5[0]   # 不再是SQL语句，因为取切片、下标是取值
# print(dep)
# print('%s: %s' % (dep.dep_id, dep.dep_name))
# qset = query5[1:3]
# print(qset)
# for dep in qset:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# query6 = session.query(Employees).filter(Employees.dep_id==2)
# print(query6)
# for emp in query6:
#     print('%s: %s' % (emp.emp_name, emp.dep_id))
#######################################
# query7 = session.query(Employees).filter(Employees.dep_id==3)\
#     .filter(Employees.email.like('%@qq.com'))
# print(query7.all())
# for emp in query7:
#     print('%s: %s' % (emp.emp_name, emp.email))
#######################################
# query8 = session.query(Departments).filter(Departments.dep_id!=1)
# print(query8)
# for dep in query8:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# query9 = session.query(Departments).filter(Departments.dep_id.in_([1, 3]))
# print(query9)
# for dep in query9:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# query10 = session.query(Departments).filter(~Departments.dep_id.in_([1, 3]))
# print(query10)
# for dep in query10:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# from sqlalchemy import and_
# query11 = session.query(Departments)\
#     .filter(and_(Departments.dep_id>1, Departments.dep_id<4))
# print(query11)
# for dep in query11:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# from sqlalchemy import or_
# query12 = session.query(Departments)\
#     .filter(or_(Departments.dep_id<3, Departments.dep_id>5))
# print(query12)
# for dep in query12:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#######################################
# query13 = session.query(Departments)
# print(query13.all())  # 返回实例列表，常用
# print(query13.first())  # 返回all实例列表中的第一项
#######################################
# query14 = session.query(Departments).filter(Departments.dep_id==1)
# print(query14.one())  # 返回一个具体的实例，多于1或少于1都会报错，常用
#######################################
query15 = session.query(Departments.dep_name, Departments.dep_id)\
    .filter(Departments.dep_id==1)
print(query15.scalar())  # 返回one结果中的第一项


#######################################

session.commit()
session.close()
