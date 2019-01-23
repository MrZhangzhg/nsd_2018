from dbconn import Departments, Session

session = Session()
# sales = Departments(dep_id=6, dep_name='销售')
# session.add(sales)
# session.commit()
##########################
# xs = session.query(Departments).filter(Departments.dep_id==6)
# xs = xs.one()   # 取出实例
# print(xs)
# xs.dep_name = '销售部'   # 实例重新赋值
# session.commit()
##########################
xs = session.query(Departments).filter(Departments.dep_id==6)
xs = xs.one()
session.delete(xs)
session.commit()




session.close()
