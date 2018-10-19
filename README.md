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
### 查询数据库中的数据
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print(message.name)

    all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    for message in all_messages:
        print(message.name)

### 向数据库中插入数据
    user_message = UserMessage()
    user_message.name = "ZhangSan2"
    user_message.message = "helloworld2"
    user_message.address = "北京"
    user_message.email = "2@2.com"
    user_message.save()

### 前端post过来的数据会在views.py下的方法的request里面

### {% csrf_token %}  <!-- Django有保护机制，需要csrf_token才能提交表单 -->
Django有保护机制，需要csrf_token才能提交表单

（见message_form.html）

### 网页提交表单（前端接收用户填写的数据，post给后端，后端把数据存入数据库）
    if request.method == "POST":  # 判断是post方法才往数据库里存数据，是get方法不存
        """接收前端post过来的数据"""
        name = request.POST.get("name", "")  # get()方法用于取字典里的某个值（如："name"），如果取不到返回""
        message = request.POST.get("message", "")
        address = request.POST.get("address", "")
        email = request.POST.get("email", "")
		""""""

        """把数据存入数据库"""
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "helloworld3"
        user_message.save()
        """"""

### 删除数据库中的数据
    all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    for message in all_messages:
        message.delete()




## 将数据库里的数据显示到html页面中
（见views.py）
def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name="ZhangSan2")
    if all_messages:  # 如果数据库里已经有ZhangSan2的数据
        message = all_messages[0]

    return render(request, "message_form.html", {
        "my_message": message  # 向前端传递数据  # 在html文件中配置，使得后端数据能够展示到前端（见message_form.html）
    })




## django的html模板templates中可以使用if判断逻辑，ifequal等函数
（见message_form.html）




## url配置技巧（url的name）
（见urls.py）

（见message_form.html）

urlpatterns = [

    url(r'^admin/', admin.site.urls),
	
    url(r'^form/$', getform, name='go_form'),  # $是结束符  # 在html中用url的name的话，便于维护
	
    url(r'^form_go/$', getform, name='go_form')  # http://127.0.0.1:8000/form/ 和 http://127.0.0.1:8000/form_go/  访问同一个页面
	
]








# 慕学网项目




## django app 设计 --> 各app的models设计 --> 数据表生成与修改




## 分析需要的app有：
users - 用户管理

courses - 课程管理

organization - 机构和教师管理

operation - 用户操作管理




## 新建虚拟环境
cmd下

mkvirtualenv mxonline




## 新建django项目




## 配置settings.py中的DATABASE




## 在Navicat下创建数据库 mxonline




## 生成django默认的数据表
tools-->run manage.py task

manage.py@MxOnline > makemigrations

manage.py@MxOnline > migrate




## users app的models设计




### 新建app users
manage下

manage.py@MxOnline > startapp users




### 在setting.py中注册新建的app




### 编写users的models.py
django会生成默认的user表（auth_user）
可以在models.py中继承默认的表，然后改写，扩展django默认的user表
改写后要在settings.py中配置AUTH_USER_MODEL， 覆盖默认的user表




### 为users的models进行makemigrations，migrate
manage下

manage.py@MxOnline > makemigrations users

manage.py@MxOnline > migrate users




## django中的循环引用
可以建更高级的models（operation的models）来调用低级的models（users，courses，organization的models）




## courses app的models设计




### 新建app courses




### 在setting.py中注册新建的app




### 编写courses的models.py
Course - 课程的基本信息
Lesson - 章节信息
Video - 视频
CourseResource - 课程资源




## organization app的models设计




### 新建app organization




### 在setting.py中注册新建的app




### 编写organization的models.py
CourseOrg - 课程机构基本信息
Teacher - 教师基本信息
CityDict - 城市信息




## operation app的models设计




### 新建app operation




### 在setting.py中注册新建的app




### 编写operation的models.py
UserAsk - 用户咨询
CourseComments - 用户评论
UserFavorite - 用户收藏
UserMessage - 用户消息
UserCourse - 用户学习的课程




## 为models进行makemigrations，migrate
manage下

manage.py@MxOnline > makemigrations

manage.py@MxOnline > migrate




## 可以在工程目录下新建python package （apps）用来存放众多app




## 将apps设为根目录
右键apps文件夹，mark directory as --> sources root 




## 在settings.py中配置apps为根目录
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))




## 在cmd下运行django
cmd下

转到工程目录下

λ python manage.py runserver 0.0.0.0:8000

ctrl+c 可以退出




## 搭建后台管理系统（django admin）
权限管理

settings.py下可以将后台管理系统（django admin）改为中文

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'  # 时区改为上海

USE_TZ = False  # 不使用国际时间




### 新建超级用户
manage下

manage.py@MxOnline > createsuperuser




### 将users_userprofile表注册到auth_group（组）中
在MxOnline\apps\users\admin.py下注册后台管理系统

class UserProfileAdmin(admin.ModelAdmin):  # 为 UserProfile 写一个管理器
    pass

admin.site.register(UserProfile, UserProfileAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)

model注册后可以在后台进行增删改查




## xadmin后台管理系统




### 安装xadmin




#### 方法一：（推荐）
GitHub下搜索xadmin

下载xadmin源码

将xadmin-master下的xadmin拷贝到工程目录下

在工程目录下新建一个python package（extra_apps），用于存放第三方app

将xadmin放到extra_apps下

将extra_apps设为根目录




#### 方法二：
cmd下

pip install xadmin




### 在settings.py中注册新建的app（xadmin）

'xadmin',

'crispy_forms',




### 将默认的admin指向xadmin
在urls.py中

import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
]




### 建xadmin的默认的表
manage下

manage.py@djangotest > makemigrations  #生成数据表的py文件

manage.py@djangotest > migrate  #生成数据表




### 将model注册到xadmin后台管理系统中
在app下新建adminx.py文件

class LessonAdmin(object):
    list_display = ["course", "name", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["course__name", "name"]  # 设置可以做搜索的字段  # 搜索的字段不能是外键类型(course)的，所以用外键类型(course)下的char类型(name)来做为搜索的字段
    list_filter = ["course__name", "name", "add_time"]  # 设置可以做过滤分类的字段  # course是外键  # course__name 用外键(course)的name做过滤分类

	
xadmin.site.register(Course, CourseAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)




### xadmin的全局配置
可以将xadmin的全局配置写在 MxOnline\apps\users\adminx.py 里

class BaseSetting(object):  # xadmin的全局配置
    enable_themes = True  # 使用xadmin的主题功能
    use_bootswatch = True

	
class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"

	
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册BaseSetting
xadmin.site.register(views.CommAdminView, GlobalSettings)# 注册GlobalSettings





### 可以在app下的apps.py模块下设置app的显示名称





##




##




##




##




##




##




##




##




##




##




##




##




##




##




##




##




##




##




##


























































