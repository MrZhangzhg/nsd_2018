# MariaDB [(none)]> CREATE DATABASE tedu1807 DEFAULT CHARSET utf8;
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(  # 创建到mysql的引擎
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1807?charset=utf8',
    encoding='utf8',  # 编码
    # echo=True   # 在终端打印日志，生产环境要设置为False
)
Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return "部门：%s" % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
