from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker

# 创建引擎，根据数据库类型，选择适当的连接方式
# 用户名:密码@服务器/数据库?参数
# echo=True，调试模式，屏幕上打印操作详情，生产环境需要关闭
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1811?charset=utf8',
    encoding='utf8',
    # echo=True
)
Base = declarative_base()  # 创建ORM映射类的基类
Session = sessionmaker(bind=engine)   # 创建会话类，绑定引擎

class Departments(Base):
    __tablename__ = 'departments'  # 指定该类与哪个表对应
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    baisc = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 没有表创建，有表不再创建
