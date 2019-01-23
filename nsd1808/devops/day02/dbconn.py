from sqlalchemy import create_engine
from sqlalchemy.ext.declarative	import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker


# 连接指定 用户名:密码@服务器/数据库?参数
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1808?charset=utf8',
    encoding='utf8',
    # echo=True    # 显示调试信息，在生产环境下，不要设置
)
Base = declarative_base()   # 生成ORM需要的基类
Session = sessionmaker(bind=engine)

class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return "<部门: %s>" % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return "<姓名: %s>" % self.emp_name

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
