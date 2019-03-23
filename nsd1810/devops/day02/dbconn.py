from sqlalchemy import create_engine

engine = create_engine(
    # 用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1810?charset=utf8',
    encoding='utf8',
    echo=True  # 在屏幕终端输出详细日志，生产环境不要设置
)


