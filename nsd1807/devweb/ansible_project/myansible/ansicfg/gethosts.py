#!/opt/djenv/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1807/devweb/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.groupname

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), unique=True, nullable=False)
    ipaddr = Column(String(15), nullable=False)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return '%s: %s' % (self.hostname, self.ipaddr)

if __name__ == '__main__':
    result = {}
    session = Session()
    query = session.query(HostGroup.groupname, Host.ipaddr)\
        .join(Host, HostGroup.id==Host.group_id)
    # print(list(query))
    for group, ip in query:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(json.dumps(result))
