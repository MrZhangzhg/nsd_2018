from dbconn import Departments, Session, Employees

session = Session()

modify1 = session.query(Departments).filter(Departments.dep_name=='hr')
# hr = modify1.one()
# print(hr)
# hr.dep_name = '人力资源部'
delete = session.query(Employees).filter(Employees.emp_id==11)
emp = delete.one()
session.delete(emp)

session.commit()
session.close()
