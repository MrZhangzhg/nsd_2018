from dbconn import Departments, Employees, Salary, Session

session = Session()
#############################
hr = Departments(dep_id=1, dep_name='人事部')
# session.add(hr)
#############################
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
finance = Departments(dep_id=5, dep_name='财务部')
ui = Departments(dep_id=6, dep_name='设计部')
session.add_all([ops, dev, qa, finance, ui])
#############################
session.commit()
session.close()
