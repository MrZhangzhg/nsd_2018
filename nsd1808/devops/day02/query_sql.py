from dbconn import Departments, Employees, Session

session = Session()

# query1 = session.query(Departments)
# print(query1)   # 只是一个查询语句
# print('*' * 30)
# print(query1.all())   # 取出表中的每个字段对应的实例
# print('*' * 30)
# for dep in query1:    # 遍历所有部门实例
#     print(dep)
# print('*' * 30)
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#####################################
# query2 = session.query(Employees.emp_name, Employees.email)
# print(query2)
# print('*' * 30)
# print(query2.all())   # 由元组构成的列表
# print('*' * 30)
# for name, email in query2:
#     print('%s: %s' % (name, email))
#####################################
# query3 = session.query(Departments.dep_name.label('部门'))
# print(query3)
# print(query3.all())
# for dep in query3:
#     print(dep.部门)
#####################################
# query4 = session.query(Departments).order_by(Departments.dep_id)
# print(query4)
# for dep in query4:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#####################################
# query5 = session.query(Departments).order_by(Departments.dep_id)[1:3]
# print(query5)   # 不再是SQL语句，是实例列表
# for dep in query5:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#####################################
# query6 = session.query(Departments).filter(Departments.dep_id==3)
# print(query6)
# for dep in query6:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#####################################
# query7 = session.query(Employees.emp_name, Employees.email)\
#     .filter(Employees.dep_id==2)\
#     .filter(Employees.email.like('%@qq.com'))
# print(query7)
# for name, email in query7:
#     print('%s: %s' % (name, email))
#####################################
# query8 = session.query(Employees.emp_name, Employees.email)\
#     .filter(Employees.emp_name.in_(['巫菲红', '章勤浩']))
# print(query8)
# for name, email in query8:
#     print('%s: %s' % (name, email))
#####################################
# query9 = session.query(Employees.emp_name, Employees.email)\
#     .filter(~Employees.emp_name.in_(['巫菲红', '章勤浩']))
# print(query9)
# for name, email in query9:
#     print('%s: %s' % (name, email))
#####################################
# from sqlalchemy import and_, or_
# query10 = session.query(Employees.emp_name, Employees.email, Employees.dep_id)\
#     .filter(or_(Employees.dep_id==2, Employees.email.like('%@qq.com')))
# print(query10)
# for name, email, dep_id in query10:
#     print('%s: %s %s' % (name, email, dep_id))
#####################################
# query11 = session.query(Employees.emp_name, Employees.email)
# print(query11.all())
# print(query11.first())
#####################################
# query12 = session.query(Employees.emp_name, Employees.email)\
#     .filter(Employees.emp_id==100)
# print(query12.one())
# print(query12.scalar())
#####################################
# query13 = session.query(Employees).filter(Employees.dep_id==2)
# print(query13.count())
#####################################
# query14 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments, Employees.dep_id==Departments.dep_id)
# print(query14.all())
#####################################
query15 = session.query(Departments.dep_name, Employees.emp_name)\
    .join(Employees, Employees.dep_id==Departments.dep_id)
print(query15.all())



