#! /opt/djenv/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1808/devweb/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(50), unique=True, nullable=False)

    def __str__(self):
        return self.group_name

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), nullable=False)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    query = session.query(HostGroup.group_name, Host.ipaddr).join(Host)
    # print(query.all())
    # for group, ip in query:    # 取出查询结果的组和IP地址
    #     print(group, ip)
    # result = {}
    # for group, ip in query:   # 构建result = {'g1': {}, 'g2': {}}
    #     if group not in result:
    #         result[group] = {}
    # print(result)
    # for group, ip in query:
    #     if group not in result:
    #         result[group] = {}
    #         result[group]['hosts'] = []  构建result = {'g1': {'hosts': []}, 'g2': {'hosts': []}}
    # print(result)
    result = {}
    for group, ip in query:
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)  # 向列表中追加主机IP地址
    print(json.dumps(result))
