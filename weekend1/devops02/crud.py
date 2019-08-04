from dbconn import Session, Departements, Employees

session = Session()  # 创建会话实例
###############################################
# 增加，直接通过创建实例实现
# hr = Departements(dep_id=1, dep_name='人事部')
# session.add(hr)
###############################################
# 增加多项
# ops = Departements(dep_id=2, dep_name='运维部')
# dev = Departements(dep_id=3, dep_name='开发部')
# qa = Departements(dep_id=4, dep_name='测试部')
# finance = Departements(dep_id=5, dep_name='财务部')
# sales = Departements(dep_id=6, dep_name='销售部')
# market = Departements(dep_id=7, dep_name='市场部')
# session.add_all([ops, dev, qa, finance, sales, market])
###############################################
# wt = Employees(
#     emp_id=1,
#     emp_name='王涛',
#     email='wangtao@qq.com',
#     dep_id=3
# )
# zj = Employees(
#     emp_id=2,
#     emp_name='张钧',
#     email='zhangjun@163.com',
#     dep_id=3
# )
# sy = Employees(
#     emp_id=3,
#     emp_name='苏艳',
#     email='suyan@qq.com',
#     dep_id=1
# )
# wjy = Employees(
#     emp_id=4,
#     emp_name='吴计印',
#     email='wujiying@126.com',
#     dep_id=4
# )
# kzw = Employees(
#     emp_id=5,
#     emp_name='康志文',
#     email='kangzhiwen@qq.com',
#     dep_id=4
# )
# hzq = Employees(
#     emp_id=6,
#     emp_name='胡志强',
#     email='huzhiqiang@163.com',
#     dep_id=5
# )
# lh = Employees(
#     emp_id=7,
#     emp_name='李浩',
#     email='lihao@126.com',
#     dep_id=2
# )
# session.add_all([wt, zj, sy, wjy, kzw, hzq, lh])
###############################################
# 查询时，直接查找类名，返回的是实例
# qset1 = session.query(Departements)
# print(qset1)  # 只是sql语句，只有取值时语句才执行
# print(list(qset1))
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
###############################################
# 查询时指定要查询的具体字段，返回的是元组
# qset2 = session.query(Departements.dep_id, Departements.dep_name)
# for dep in qset2:
#     print(dep)
###############################################
# qset3 = session.query(Departements).filter(Departements.dep_id>3)\
#     .order_by(Departements.dep_id)
# for dep in qset3:
#     print(dep)
###############################################
# qset4 = session.query(Departements).filter(Departements.dep_id>3)\
#     .filter(Departements.dep_id<7)
# for dep in qset4:
#     print(dep)
###############################################
# 降序
# qset5 = session.query(Departements).order_by(Departements.dep_id.desc())
# for dep in qset5:
#     print(dep)
###############################################
# all方法可以取出全部的值
# qset6 = session.query(Departements).filter(Departements.dep_id>3)\
#     .filter(Departements.dep_id<7)
# deps = qset6.all()
# print(deps)
# for dep in deps:
#     print(dep)
###############################################
# first取出第一个值
# qset7 = session.query(Departements).filter(Departements.dep_id>3)\
#     .filter(Departements.dep_id<7)
# dep = qset7.first()
# print(dep)
###############################################
# one要求查询结果只有一个值，0或多个值都报错
# qset8 = session.query(Departements).filter(Departements.dep_id==3)
# dep = qset8.one()
# print(dep)
###############################################
# 修改，只要对对象重新赋值即可
# qset9 = session.query(Departements).filter(Departements.dep_name=='人事部')
# hr = qset9.one()
# hr.dep_name = '人力资源部'
###############################################
# 删除，也是找到实例，删除即可
# qset10 = session.query(Departements).filter(Departements.dep_id==7)
# market = qset10.one()
# session.delete(market)
###############################################
# 多表查询，查询时sqlalchemy会根据外键约束进行连接
# qset11 = session.query(Employees.emp_name, Departements.dep_name)\
#     .join(Departements)
# print(qset11.all())
# query时，先写Departments.dep_name就要join Employees
qset12 = session.query(Departements.dep_name, Employees.emp_name)\
    .join(Employees)
print(qset12.all())


###############################################
session.commit()   # 增删改需要commit
session.close()


