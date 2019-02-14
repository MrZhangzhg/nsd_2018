from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker

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
    print(query.all())
