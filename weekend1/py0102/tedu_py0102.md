# tedu_py0102

## gitlab服务器

1. 克隆一台虚拟机，内存修改为4G
2. 配置IP地址、yum
3. 拷贝gitlab镜像和docker软件包到虚拟机
```shell
ftp://172.40.50.116/pub/phase5/docker/docker_pkgs
# cd docker_pkgs
# yum install -y *rpm
```
4. 安装docker并启动
5. 导入gitlab镜像

```shell
[root@node4 images]# docker load < gitlab_zh.tar
```

6. 把虚拟机ssh端口改为2022，因为22端口要留给gitlab使用

```shell
[root@node4 images]# vim /etc/ssh/sshd_config 
Port 2022
[root@node4 images]# systemctl restart sshd
# 退出ssh再重新连接时，使用2022端口
[root@room8pc16 phase5]# ssh -p2022 192.168.4.4
```

7. 启动容器

```shell
[root@node4 ~]# docker run -d -h gitlab --name gitlab -p 443:443 -p 80:80 -p 22:22 --restart always -v /srv/gitlab/config:/etc/gitlab -v /srv/gitlab/logs:/var/log/gitlab -v /srv/gitlab/data:/var/opt/gitlab gitlab_zh:latest
# 容器启动需要几分钟，当docker ps查看时，显示healty才算正常
```

### gitlab中的关键概念

- 群组group：一个团队对应一个组
- 成员member：把用户加入到组中，成为组的成员
- 项目project：每个开发项目对应到gitlab中，成为一个项目

### 访问gitlab

- url: http://x.x.x.x/

- 第一次访问需要设置管理员root密码，8位，符合复杂度要求
- 用户名为root
- 点击创建组，创建名为devops的组，公开的组
- 任何时候都可以点击页面上的扳手图标，查看主要的操作
- 点击“创建用户”，创建一个用户Mrzhang。注意，创建用户的时候，不能设置密码。但是创建完用户后，可以点击“编辑”再设置密码。
- 点击页面上的扳手图标，点击创建项目。为组创建项目，因此项目路径要把root改为devops，最后项目名称随便填一个。可见等级选“公开”
- 创建好项目后，点击左侧工具栏中的齿轮图标->成员->选择要邀请的成员: Mrzhang -> 选择角色权限: 主程序员 -> 点击添加到项目





