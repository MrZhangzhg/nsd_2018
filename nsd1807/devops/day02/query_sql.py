from dbconn import Departments, Session, Employees

session = Session()
query1 = session.query(Departments)
# print(query1)  # query1只是sql语句
# print(list(query1))  # 列表是所有部门的实例集合
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
###################################
query2 = session.query(Employees.emp_name, Employees.email)
# print(query2)
# print(list(query2))
###################################
query3 = session.query(Departments).order_by(Departments.dep_id)
# print(query3)
# for dep in query3:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
###################################
query4 = session.query(Departments).order_by(Departments.dep_id)[:2]
# print(query4)  # 取切片后，就不是sql语句了，而是实例集合
# for dep in query4:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
###################################
query5 = session.query(Departments).filter(Departments.dep_id==2)
# print(query5)   # sql语句
# print(list(query5))
# for dep in query5:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
###################################
query6 = session.query(Employees).filter(Employees.dep_id==2)\
    .filter(Employees.gender=='女')
# print(query6)
# for emp in query6:
#     print('%s: %s' % (emp.dep_id, emp.emp_name))
###################################
query7 = session.query(Departments).filter(Departments.dep_id.in_([1, 3, 5]))
# print(query7)
# for dep in query7:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
###################################
# query1 = session.query(Departments)
# print(query1.all())   # 取出全部，构成实例集合
# query5 = session.query(Departments).filter(Departments.dep_id==2)
# print(query5.one())   # 返回一个具体的实例
# query8 = session.query(Departments.dep_name, Departments.dep_id).filter(Departments.dep_id==2)
# print(query8.scalar())  # 调用one，返回结果的第一项
###################################
query9 = session.query(Departments).count()
# print(query9)
###################################
query10 = session.query(Employees.emp_name, Departments.dep_name)\
    .join(Departments, Employees.dep_id==Departments.dep_id)
# print(query10.all())
query11 = session.query(Departments.dep_name, Employees.emp_name)\
    .join(Employees, Employees.dep_id==Departments.dep_id)
print(query11.all())

session.close()
