from dbconn import Departments, Session

hr = Departments(dep_id=1, dep_name='hr')
op = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
session = Session()
# session.add(hr)
session.add_all([op, dev, qa])
session.commit()
session.close()

