from sqlalchemy import create_engine
from sqlalchemy.ext.declarative	import declarative_base
from sqlalchemy import Column, Integer, String

# 连接指定 用户名:密码@服务器/数据库?参数
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1808?charset=utf8',
    encoding='utf8',
    # echo=True    # 显示调试信息，在生产环境下，不要设置
)
Base = declarative_base()   # 生成ORM需要的基类


class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return "<部门: %s>" % self.dep_name

if __name__ == '__main__':
    Base.metadata.create_all(engine)
