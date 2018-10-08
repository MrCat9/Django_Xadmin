# Django_xadmin
摘自 https://coding.imooc.com/class/78.html




## 执行manage命令
pycharm下

tools-->run manage.py task-->输入命令


## 新建app
pycharm下

tools-->run manage.py task-->startapp <app名>




## 运行django
cmd下

#转到工程目录

λ python manage.py runserver




## 生成数据表
manage下

manage.py@djangotest > makemigrations  #生成数据表的py文件

manage.py@djangotest > migrate  #生成数据表

更改了models.py（数据模型）（数据库）后，要执行makemigrations和migrate




## 要在settings.py中配置
1. 数据库database

2. TEMPLATES目录（html文件的目录）

3. STATICFILES_DIRS目录（静态文件的目录）




## 在urls.py中配置url和响应，在views.py中写具体如何响应




## orm
也就是Django的model，使操作数据库像操作类一样简单


