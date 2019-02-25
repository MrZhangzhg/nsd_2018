from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1809?charset=utf8',
    # 用户名:密码@服务器/数据库
    encoding='utf8',  # 编码
    # echo=True  # 控制台显示详细的日志输出，生产环境下要关闭
)
Session = sessionmaker(bind=engine)
Base = declarative_base()  # 创建ORM映射的基类

class Departments(Base):   # 继承于Base基类，对应一张表
    __tablename__ = 'departments'  # 声明该类对应哪张表
    dep_id = Column(Integer, primary_key=True)  # 主键默认自动增长
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return "部门: %s" % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return "员工: %s" % self.emp_name

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    date = Column(Date)
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
