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

```python
    all_messages = UserMessage.objects.all()
    for message in all_messages:
        print(message.name)

    all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    for message in all_messages:
        print(message.name)
```

### 向数据库中插入数据

```python
    user_message = UserMessage()
    user_message.name = "ZhangSan2"
    user_message.message = "helloworld2"
    user_message.address = "北京"
    user_message.email = "2@2.com"
    user_message.save()
```

### 前端post过来的数据会在views.py下的方法的request里面

### {% csrf_token %}  <!-- Django有保护机制，需要csrf_token才能提交表单 -->

Django有保护机制，需要csrf_token才能提交表单

（见message_form.html）

### 网页提交表单（前端接收用户填写的数据，post给后端，后端把数据存入数据库）

```python
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
```

### 删除数据库中的数据

```python
    all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    for message in all_messages:
        message.delete()
```
        



## 将数据库里的数据显示到html页面中

（见views.py）

```python
def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name="ZhangSan2")
    if all_messages:  # 如果数据库里已经有ZhangSan2的数据
        message = all_messages[0]

    return render(request, "message_form.html", {
        "my_message": message  # 向前端传递数据  # 在html文件中配置，使得后端数据能够展示到前端（见message_form.html）
    })
```




## django的html模板templates中可以使用if判断逻辑，ifequal等函数

（见message_form.html）




## url配置技巧（url的name）

（见urls.py）

（见message_form.html）

```python
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    
    url(r'^form/$', getform, name='go_form'),  # $是结束符  # 在html中用url的name的话，便于维护
    
    url(r'^form_go/$', getform, name='go_form')  # http://127.0.0.1:8000/form/ 和 http://127.0.0.1:8000/form_go/  访问同一个页面
    
]
```








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
```python
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
```




## 在cmd下运行django

cmd下

转到工程目录下

λ python manage.py runserver 0.0.0.0:8000

ctrl+c 可以退出




## 搭建后台管理系统（django admin）

权限管理

settings.py下可以将后台管理系统（django admin）改为中文

```python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'  # 时区改为上海

USE_TZ = False  # 不使用国际时间
```




### 新建超级用户

manage下

manage.py@MxOnline > createsuperuser




### 将users_userprofile表注册到auth_group（组）中

在MxOnline\apps\users\admin.py下注册后台管理系统

```python
class UserProfileAdmin(admin.ModelAdmin):  # 为 UserProfile 写一个管理器

    pass

admin.site.register(UserProfile, UserProfileAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)

model注册后可以在后台进行增删改查
```




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

```python
'xadmin',

'crispy_forms',
```




### 将默认的admin指向xadmin

在urls.py中

```python
import xadmin

urlpatterns = [

    url(r'^xadmin/', xadmin.site.urls),
    
]
```




### 建xadmin的默认的表

manage下

manage.py@djangotest > makemigrations  #生成数据表的py文件

manage.py@djangotest > migrate  #生成数据表




### 将model注册到xadmin后台管理系统中

在app下新建adminx.py文件

```python
class LessonAdmin(object):

    list_display = ["course", "name", "add_time"]  # 设置要在后台显示的字段
    
    search_fields = ["course__name", "name"]  # 设置可以做搜索的字段  # 搜索的字段不能是外键类型(course)的，所以用外键类型(course)下的char类型(name)来做为搜索的字段
    
    list_filter = ["course__name", "name", "add_time"]  # 设置可以做过滤分类的字段  # course是外键  # course__name 用外键(course)的name做过滤分类

    
xadmin.site.register(Course, CourseAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
```




### xadmin的全局配置

可以将xadmin的全局配置写在 MxOnline\apps\users\adminx.py 里

```python
class BaseSetting(object):  # xadmin的全局配置

    enable_themes = True  # 使用xadmin的主题功能
    
    use_bootswatch = True

    
class GlobalSettings(object):

    site_title = "慕学后台管理系统"
    
    site_footer = "慕学在线网"
    
    menu_style = "accordion"

    
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册BaseSetting

xadmin.site.register(views.CommAdminView, GlobalSettings)# 注册GlobalSettings
```




### 设置app在后台管理系统中的显示名称

#### 在app下的apps.py模块下

```python
class OperationConfig(AppConfig):

    name = 'operation'
    
    verbose_name = u"用户操作"
```

#### 在app下的__init__.py模块下配置

```python
default_app_config = "operation.apps.OperationConfig"
```




## 用户的登录




### 拷贝index.html文件到templates文件夹下




### 在工程目录下新建一个文件夹static用于存放静态文件（css、js、img等）




### 在urls.py中配置处理静态文件

```python
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name="index.html"), name="index")  # TemplateView的as_view()方法会把template转化为view
]
```




### 在settings.py中配置static文件路径

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static")
)
```




### 修改index.html中静态文件的引用路径

（见 MxOnline\templates\index.html）




### 将登录的html文件（login.html）拷贝到templates文件夹下




### 修改login.html中静态文件的引用路径




### 配置urls.py  跳转到login页面

```python
    url('^login/$', TemplateView.as_view(template_name="login.html"), name="login"),
    # TemplateView的as_view()方法会把template转化为view，这样就不需要自己写后台的view
```




### 配置index.html，使能从index.html跳转到login页面

```html
                        <a style="color:white" class="fr loginbtn" href="/login/">登录</a>
```




### 在 MxOnline\apps\users\views.py 下写后台逻辑




### 在 MxOnline\MxOnline\urls.py 下配置login的url

```python
    url(r'^login/$', login, name="login"),  # login不能加括号login()，加括号的话就是调用函数，不加的话只是一个句柄，指向函数login
```




### django有保护机制，post表单的时候要带上csrf，否则会报403错误

在 MxOnline\templates\login.html 下

```html
                <form action="/login/" method="post" autocomplete="off">
                ···
                ···
                ···
                {% csrf_token %}
                </form>
```




### 在 MxOnline\templates\index.html 下做判断，使得登录后显示用户头像，没登录显示“登录”，“注册”按钮

```html
            {% if request.user.is_authenticated %}
                <div class="top"...>
                ...
                ...
                {% else %}
                <div class="top"...>
                ...
                ...
            {% endif %}
```




### django默认通过用户名和密码来登录，要用邮箱登录可以：




#### 在settings.py中配置

```python
AUTHENTICATION_BACKENDS = (  # django默认通过用户名和密码来登录，要用邮箱登录可以在settings.py中配置
    'users.views.CustomBackend',  # 指明函数
)
```




#### 在 MxOnline\apps\users\views.py 下定义

```python
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))  # 先用username查  # get()方法只会取出一个，当有多个时，报错
            # user = UserProfile.objects.get(Q(username=username)|Q(email=username), password=password)  # username=username或email=username  并password=password
            if user.check_password(password):  # 检查密码是否正确
                return user
        except Exception as e:
            return None
```




#### 这样在 MxOnline\apps\users\views.py 下的user_login(request)方法中的authenticate就会调用 CustomBackend 下自定义的authenticate




### 登录失败时，在login.html页面上显示错误信息：




#### 在 MxOnline\apps\users\views.py 下的 user_login(request) 方法中，用 render() 方法向前端传递错误信息

```python
            return render(request, "login.html", {"msg": "用户名或密码错误！"})
```




#### 在 MxOnline\templates\login.html 下配置

```html
                    <div class="error btns login-form-tips" id="jsLoginTips">{{ msg }}</div>
```




### 把 MxOnline\apps\users\views.py 里的def改写成class 基于类的书写 ：




#### MxOnline\apps\users\views.py 下

```python
class LoginView(View):
    ···
    ···

```




#### 在 MxOnline\MxOnline\urls.py 下

```python
from users.views import LoginView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),  # TemplateView的as_view()方法会把template转化为view，这样就不需要自己写后台的view
    # url(r'^login/$', user_login, name="login"),  # login不能加括号login()，加括号的话就是调用函数，不加的话只是一个句柄，指向函数login
    url(r'^login/$', LoginView.as_view(), name="login"),

    url(r'^logout/$', user_logout, name="logout"),
]
```




### 用form实现登录

form  对用户传来的数据进行预处理




#### 在 MxOnline\apps\users 下新建 forms.py  用来放form定义

```python
class LoginForm(forms.Form):
    username = forms.CharField(required=True)  # required=True 必填字段，不填报错
    password = forms.CharField(required=True, min_length=5)
    # password = forms.CharField(required=True, max_length=5, min_length=1)
```




#### 在 MxOnline\apps\users\views.py 中应用forms

```python
from .forms import LoginForm

        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 如果form验证成功，再用数据库进行验证
            ···
            ···
```




#### 账号或者密码出错时加红框  在template里对form进行操作

在 MxOnline\templates\login.html 下

```html
                    <div class="form-group marb20 {% if login_form.errors.username %}errorput{% endif %}">

                    <div class="form-group marb8 {% if login_form.errors.password %}errorput{% endif %}">
```




#### 将form提供的错误信息显示到网页上  在template里对form进行操作

在 MxOnline\templates\login.html 下

```html
                    <div class="error btns login-form-tips" id="jsLoginTips">{% for key,error in login_form.errors.items %}{{ key }}:{{ error }}{% endfor %}{{ msg }}</div>
```




### session和cookie

见 https://github.com/MrCat9/Python_Scrapy-Redis_elasticsearch_django/blob/master/scrapy%E7%88%AC%E5%8F%96%E7%9F%A5%E4%B9%8E1_cookie_session.py




## 用户的注册




### 拷贝 register.html 文件到 templates 文件夹下




### 在 MxOnline\MxOnline\urls.py 下配置 register.html

```python
    url(r'^register/$', RegisterView.as_view(), name="register"),
```




### 在 MxOnline\apps\users\views.py 下写后台逻辑

```python
    class RegisterView(View):
        ···
        ···
```




### 修改 register.html 中静态文件的引用路径

```html
{% load staticfiles %}
···
···
    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/login.css' %}">
···
···
```




### 在 MxOnline\templates\index.html 下配置，使能够从 index 页面跳转到register页面

```html
                        <a style="color:white" class="fr registerbtn" href="{% url 'register' %}">注册</a>
```




### 在 MxOnline\templates\login.html 下配置，使能够从 login 页面跳转到register页面

```html
                <li><a href="{% url 'register' %}">[注册]</a></li>
                ···
                ···
                <p class="form-p">没有慕学在线网帐号？<a href="{% url 'register' %}">[立即注册]</a></p>
```




### 用 django 的第三方插件 https://github.com/mbi/django-simple-captcha 做验证码

在cmd下安装：

λ pip install django-simple-captcha==0.4.6

使用方法：

https://django-simple-captcha.readthedocs.io/en/latest/usage.html#installation




### 在 MxOnline\apps\users\forms.py 下定义 RegisterForm

```python
from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 自定义要抛出的错误信息
```




### 完善 MxOnline\apps\users\views.py 下的后台逻辑

```python
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})
```




### 在 MxOnline\templates\register.html 配置使用 register_form

```html
                        <div class="form-group marb8 captcha1 ">
                            <label>验&nbsp;证&nbsp;码</label>
                            {{ register_form.captcha }}
                        </div>
```

{{ register_form.captcha }} 会生成一段 html 代码

```html
<img src="/captcha/image/574914ff49afe8846c0bfde07a094e4a56a7910c/" alt="captcha" class="captcha" /> <input id="id_captcha_0" name="captcha_0" type="hidden" value="574914ff49afe8846c0bfde07a094e4a56a7910c" /> <input autocomplete="off" id="id_captcha_1" name="captcha_1" type="text" />
```

574914ff49afe8846c0bfde07a094e4a56a7910c 和 用户输入的验证码

将传到后台数据库验证验证码是否填写正确

数据库 captcha_captchastore 表：

```
ID       challenge   response    hashkey                                         expiration
···
···
6        ZTSO        ztso        574914ff49afe8846c0bfde07a094e4a56a7910c        2018-11-12 21:36:15.474660
```




### 完善 MxOnline\apps\users\views.py 下的后台逻辑  用于注册时提交表单的post

```python
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})
    def post(self, request):
        ···
        ···
```




### post 中用到的发送邮箱 写在 MxOnline\apps\utils\email_send.py 下




### 在 MxOnline\MxOnline\settings.py 下配置邮件的发送者

```python
EMAIL_HOST = "smtp.sina.com"
# 查找邮箱的host
# 登录邮箱后 --> 设置 --> SMTP服务 --> SMTP服务器
EMAIL_PORT = 25
EMAIL_HOST_USER = "···"
EMAIL_HOST_PASSWORD = "···"
EMAIL_USE_TLS = False
EMAIL_FROM = "···"
```




### 处理激活链接




#### 在 MxOnline\MxOnline\urls.py 配置url

```python
    # 处理用户通过邮箱激活注册的账号
    url(r'^active/(?P<active_code>.*)/$'),  # (?P<active_code>.*) 提取url的部分， .* 为正则表达式，匹配出来的值放到 active_code
```




#### 在 MxOnline\apps\users\views.py 下写点击激链接后的处理

```python
class ActiveUserView(View):
    def get(self, request, active_code):
    ···
    ···
```




### 将注册时的报错信息传给 register.html

```html
                        <div class="error btns" id="jsEmailTips">{% for key,error in register_form.errors.items %}{{ error }}{% endfor %}</div>
```




### 注册时报错的话做标红 register.html

```html
                        <div class="form-group marb20 {% if register_form.errors.email %}errorput{% endif %}">
```




### 回填用户注册时填写的值

```html
                            <input  type="text" id="id_email" name="email" value="{{ register_form.email.value }}" placeholder="请输入您的邮箱地址" />
```




### 配置 MxOnline\templates\register.html post表单到 /register/

```html
                    <form id="email_register_form" method="post" action="{% url 'register' %}" autocomplete="off">
```




### {% csrf_token %}  <!-- Django有保护机制，需要csrf_token才能提交表单 -->

```html
                    {% csrf_token %}
```




## 用户找回密码




