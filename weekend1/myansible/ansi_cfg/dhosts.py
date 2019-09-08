#!/root/weekend1/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "sqlite:////var/ftp/nsd_2018/weekend1/myansible/db.sqlite3",
    encoding='utf8'
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Group(Base):
    __tablename__ = 'webadmin_group'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_group.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    result = {}
    for group, ip in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)

    print(result)
