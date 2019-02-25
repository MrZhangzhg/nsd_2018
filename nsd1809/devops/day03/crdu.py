from dbconn import Departments, Session

hr = Departments(dep_name='人事部')
ops = Departments(dep_name='运维部')
dev = Departments(dep_name='开发部')
qa = Departments(dep_name='测试部')
finance = Departments(dep_name='财务部')
xz = Departments(dep_name='行政部')
session = Session()
# session.add(hr)
session.add_all([ops, dev, qa, finance, xz])
session.commit()
session.close()
