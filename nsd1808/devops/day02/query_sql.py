from dbconn import Departments, Employees, Session

session = Session()

query1 = session.query(Departments)
print(query1)   # 只是一个查询语句
print('*' * 30)
print(query1.all())   # 取出表中的每个字段对应的实例
print('*' * 30)
for dep in query1:    # 遍历所有部门实例
    print(dep)
print('*' * 30)
for dep in query1:
    print('%s: %s' % (dep.dep_id, dep.dep_name))
