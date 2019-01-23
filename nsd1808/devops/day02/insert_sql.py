from dbconn import Departments, Employees, Salary, Session

session = Session()
# hr = Departments(dep_id=1, dep_name='HR')
# session.add(hr)
# session.commit()
#####################################
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qs = Departments(dep_id=4, dep_name='测试部')
fn = Departments(dep_name='财务部')   # sqlalchemy把主键设置为了自动增长
session.add_all([ops, dev, qs, fn])
session.commit()





session.close()
