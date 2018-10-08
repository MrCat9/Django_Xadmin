# Django_xadmin
摘自 https://coding.imooc.com/class/78.html




## 执行manage命令
pycharm下

tools-->run manage.py task-->输入命令


## 新建app
pycharm下

tools-->run manage.py task-->startapp <app名>




## 新建好的app需要在setting.py下注册
INSTALLED_APPS




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




## models.py在app目录下
models.py下
（见models.py）




## 定义好model后，通过model直接生成数据表
tools-->run manage.py task  进入到manage下

manage.py@djangotest > makemigrations message  # makemigrations (app名)  # 生成数据表的py文件

manage.py@djangotest > migrate message  # migrate (app名)  # 生成数据表

更改了models.py（数据模型）（数据库）后，要执行makemigrations和migrate

默认生成的表的名称是  （app名称）_（model名称（小写））

未给表指定主键的情况下会生成id作为主键，指定主键之后会删除自动生成的id




## model的增删改查
（见views.py）
#### 查询数据库中的数据
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print(message.name)

    all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    for message in all_messages:
        print(message.name)

#### 向数据库中插入数据
    user_message = UserMessage()
    user_message.name = "ZhangSan2"
    user_message.message = "helloworld2"
    user_message.address = "北京"
    user_message.email = "2@2.com"
    user_message.save()

#### 前端post过来的数据会在views.py下的方法的request里面

#### {% csrf_token %}  <!-- Django有保护机制，需要csrf_token才能提交表单 -->
Django有保护机制，需要csrf_token才能提交表单
（见message_form.html）


































