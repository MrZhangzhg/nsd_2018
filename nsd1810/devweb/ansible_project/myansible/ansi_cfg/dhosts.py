#!/opt/djenv/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1810/devweb/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'web_ansi_hostgroup'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(100), unique=True)

class Host(Base):
    __tablename__ = 'web_ansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('web_ansi_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.group_name, Host.ipaddr).join(Host)
    print(qset.all())
