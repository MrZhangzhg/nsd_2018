from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1809?charset=utf8',
    # 用户名:密码@服务器/数据库
    encoding='utf8',  # 编码
    # echo=True  # 控制台显示详细的日志输出，生产环境下要关闭
)
Base = declarative_base()  # 创建ORM映射的基类

class Departments(Base):   # 继承于Base基类，对应一张表
    __tablename__ = 'departments'  # 声明该类对应哪张表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return "部门: %s" % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
