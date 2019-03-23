from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    # 用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1810?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕终端输出详细日志，生产环境不要设置
)
Base = declarative_base()


class Departments(Base):
    __tablename__ = 'departments'   # 类对应的表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return '%s: %s' % (self.dep_id, self.dep_name)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
