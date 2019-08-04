# nsd_weekend1_02

## SQLAlchemy

- 可以连接任意的关系型数据库，mysql / oracle / sqlite / postgresql
- 不用书写SQL语句，只要使用python语法即可

### ORM

- O: Object对象
- R: Relationship关系
- M: Mapping映射
- python的class与数据库的表进行映射
- class中的类变量与表中的字段一一映射
- class的实例与表的记录映射
- sqlalchemy为数据库表的每个字段也创建了一个映射类

### 安装与配置

```python
# 创建虚拟环境
[root@room8pc16 weekend1]# python3 -m venv ~/weekend1
# 激活虚拟环境
[root@room8pc16 weekend1]# source ~/weekend1/bin/activate
# 安装sqlalchemy和pymysql
(weekend1) [root@room8pc16 weekend1]# pip3 install zzg_pypkgs/sqlalchemy_pkgs/*
(weekend1) [root@room8pc16 weekend1]# pip3 install zzg_pypkgs/pymysql_pkgs/*

# 创建数据库
MariaDB [(none)]> CREATE DATABASE wtedu1 DEFAULT CHARSET utf8;
```

















