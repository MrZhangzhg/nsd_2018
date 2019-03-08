#!/opt/djenv/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1809/devweb/ansible_project/myansible/db.sqlite3'
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return "组: %s" % self.group_name

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), nullable=False, unique=True)
    ipaddr = Column(String(15), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return "%s: %s" % (self.hostname, self.ipaddr)

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.group_name, Host.ipaddr).join(Host)
    # print(qset.all())
    result = {}
    for group, ip in qset:
        if group not in result:  # group=dbservers
            result[group] = {}   # {'dbservers': {}}
            result[group]['hosts'] = []   # {'dbservers': {'hosts': []}}
        result[group]['hosts'].append(ip)
    print(json.dumps(result))
