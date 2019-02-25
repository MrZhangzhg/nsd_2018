from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1809?charset=utf8',
    # 用户名:密码@服务器/数据库
    encoding='utf8',  # 编码
    echo=True  # 控制台显示详细的日志输出，生产环境下要关闭
)



