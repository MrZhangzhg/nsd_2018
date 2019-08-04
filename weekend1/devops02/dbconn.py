from sqlalchemy import create_engine, Date, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative	import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器地址/数据名?参数
    "mysql+pymysql://root:tedu.cn@127.0.0.1/wtedu1?charset=utf8",
    encoding='utf8',
    # echo=True   # 打开debug消息，用于屏幕回显，生产环境不要设置
)

# 创建会话类，用于将来实现到数据库的会话连接
Session = sessionmaker(bind=engine)

# 生成ORM实体类的基类
Base = declarative_base()

# 创建实体类
class Departements(Base):
    __tablename__ = 'departments'  # 声明与哪个表映射
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

    def __str__(self):
        return "%s号部门: %s" % (self.dep_id, self.dep_name)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(50))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey("departments.dep_id"))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey("employees.emp_id"))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中无表则创建，有表不会再创建一遍
    Base.metadata.create_all(engine)
