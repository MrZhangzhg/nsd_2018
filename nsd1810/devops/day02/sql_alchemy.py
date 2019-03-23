from dbconn import Departments, Employees, Session

session = Session()  # 创建会话类的实例
hr = Departments(dep_id=1, dep_name='人事部')
session.add(hr)



session.commit()
session.close()
