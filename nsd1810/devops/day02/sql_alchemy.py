from dbconn import Departments, Employees, Session

session = Session()  # 创建会话类的实例
# hr = Departments(dep_id=1, dep_name='人事部')
# session.add(hr)
dev = Departments(dep_id=2, dep_name='开发部')
ops = Departments(dep_id=3, dep_name='运维部')
market = Departments(dep_id=4, dep_name='市场部')
finance = Departments(dep_id=5, dep_name='财务部')
session.add_all([dev, ops, market, finance])



session.commit()
session.close()
