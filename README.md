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

#### {{  }} 与 {%  %}的区别

```
{{ csrf_token }}是取值
{% csrf_token %}会生成一段html代码
```

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




#### 这样在 MxOnline\apps\users\views.py 下的 class LoginView(View): 类中的 def post(self, request): 方法中的authenticate就会调用 CustomBackend 下自定义的authenticate




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




#### 在 MxOnline\apps\users\views.py 下写点击激活链接后的处理

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




### 将 forgetpwd.html 拷贝到 MxOnline\templates\ 下




### 在 MxOnline\MxOnline\urls.py 下配置忘记密码的url

```python
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
```




### 在 MxOnline\apps\users\views.py 下写忘记密码的后台逻辑

```python
class ForgetPwdView(View):
    def get(self, request):
    ···
    ···
```




### 在 MxOnline\templates\login.html 下配置url，使能从 login.html 跳转到 forgetpwd.html

```html
                        <a class="fr" href="{% url 'forget_pwd' %}">忘记密码？</a>
```




### 修改 forgetpwd.html 中的静态文件路径

```html
{% load staticfiles %}
···
···
	<link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
	<link rel="stylesheet" type="text/css" href="{% static 'css/login.css' %}">
···
···
```




### 在 MxOnline\apps\users\forms.py 下定义form

```python
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)  # 要与html中input的name一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 自定义要抛出的错误信息
```




### 在 MxOnline\apps\users\views.py 下使用form

```python
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})
```




### 在 MxOnline\templates\forgetpwd.html 下配置使用form，生成验证码

```html
                        {{ forget_form.captcha }}
```




### 在 MxOnline\apps\users\views.py 下完善忘记密码的后台逻辑 post

```python
class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, "forgetpwd.html", {"forget_form": forget_form})

    def post(self,request):
        forget_form = ForgetForm(request.POST)

        if forget_form.is_valid():

            # <div class="form-group marb20 ">
            #     <label>帐&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
            #     <input type="text" id="account" name="email" value="" placeholder="邮箱" />
            # </div>

            #             get()方法中取的要与html中的name一致
            email = request.POST.get("email", "")
            ···
            ···
```




### post 中发送邮箱的 send_register_email() 方法写在 MxOnline\apps\utils\email_send.py 下




### 新建html页面 MxOnline\templates\send_success.html 用于显示已经成功发送密码重置邮件




### 在 MxOnline\templates\forgetpwd.html 下配置post到 /forget/ 

```html
                <form id="jsFindPwdForm" method="post" action="{% url 'forget_pwd' %}" autocomplete="off">
```




### 在 MxOnline\templates\forgetpwd.html 下配置post的时候带上csrf

```html
                {% csrf_token %}
```




### 在 MxOnline\templates\forgetpwd.html 下配置显示form的错误信息

```html
                    <div class="error btns" id="jsForgetTips">{% for key,error in forget_form.errors.items %}{{ error }}{% endfor %}{{ msg }}</div>
```




### 在 MxOnline\templates\forgetpwd.html 下配置给错误的地方标红

```html
                    <div class="form-group marb20 {% if forget_form.errors.email %}errorput{% endif %}">
```




### 在 MxOnline\templates\forgetpwd.html 下配置回填 email

```html
                    <div class="form-group marb20 {% if forget_form.errors.email %}errorput{% endif %}">
```




### 处理密码重置链接




#### 在 MxOnline\MxOnline\urls.py 配置url




#### 在 MxOnline\apps\users\views.py 下写点击密码重置链接后的处理  ResetView

跳转到重置密码页面

```python
class ResetView(View):
    def get(self, request, reset_code):
        ···
        ···
```




#### 在 MxOnline\templates\password_reset.html 下配置

获取 MxOnline\apps\users\views.py 中传过来的email，以确定是哪个用户修改密码

```html
                <input type="hidden" name="email" value="{{ email }}">
```


点击提交新密码，post 到 modify_pwd

```html
        <form id="reset_password_form" action="{% url 'modify_pwd' %}" method="post">
```

csrf_token

```html
            </ul>
            {% csrf_token %}
        </form>
```




#### 在 MxOnline\apps\users\forms.py 下写 form  ModifyPwdForm




#### 在 MxOnline\apps\users\views.py 下写点击提交新密码后的处理  ResetView

```python
class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
        ···
        ···
```




## 授课机构列表页功能




### django templates模板继承




#### 新建 MxOnline\templates\base.html

变动的地方用block包起来
```html
	<title>{% block title %}慕学在线首页{% endblock %}</title>
```




#### 新建 MxOnline\templates\org-list.html  使用 {% extends 'base.html' %}




### 机构列表页展示




#### 在xadmin下新增数据

城市  课程机构（上传logo）  




##### 上传文件目录配置 media




###### 新建 MxOnline\media 文件夹




###### 在 MxOnline\MxOnline\settings.py 下配置上传文件的存放路径

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
```




#### 在 MxOnline\MxOnline\urls.py 下配置url，转到机构列表页  org_list




#### 在 MxOnline\apps\organization\views.py 下写跳转到机构列表页后的逻辑




#### 在 MxOnline\templates\org-list.html 下调用view中传过来的数据


```html
		<div class="all">共<span class="key">{{ org_nums }}</span>家</div>
```

```html
                                {% for city in all_citys %}
                                    <a href="?city=1&ct="><span class="">{{ city.name }}</span></a>
                                {% endfor %}
```

```html
            {% for course_org in all_orgs %}
                <dl class="des difdes">
                    <dt>
                        <a href="{% url 'org:org_home' course_org.id %}">
                            <img width="200" height="120" class="scrollLoading" data-url="{{ MEDIA_URL }}{{ course_org.image }}"/>
                            ···
                            ···
```




##### 使用{{ MEDIA_URL }}的话要在settings.py下配置 'django.core.context_processors.media'

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]
```




##### 要显示课程机构的logo要在 urls.py 下配置

```python
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
```




### 分页功能

使用开源库 pure-pagination
https://github.com/jamespacileo/django-pure-pagination




#### pip install django-pure-pagination




#### 使用 pure-pagination

见 https://github.com/jamespacileo/django-pure-pagination

见 MxOnline\templates\org-list.html




### 筛选功能




#### 根据城市筛选




##### 点击城市后，前端将回传城市的id

MxOnline\templates\org-list.html

```html
                                {% for city in all_citys %}
                                    <a href="?city={{ city.id }}"><span class="">{{ city.name }}</span></a>
                                {% endfor %}
```




##### 后端接收城市id

MxOnline\apps\organization\views.py

```python
        # 取出筛选城市
        city_id = request.GET.get('city', "")
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
```




##### 让选中的城市显示为被选中状态

```html
                        <a href="?ct={{ category }}"><span class="{% ifequal city_id '' %}active2{% endifequal %}">全部</span></a>
                                {% for city in all_citys %}
                                    <a href="?city={{ city.id }}&ct={{ category }}"><span class="{% ifequal city_id city.id|stringformat:"i" %}active2{% endifequal %}">{{ city.name }}</span></a>
                                {% endfor %}
```




#### 根据类别筛选




### 授课机构排名功能




#### 根据点击量

MxOnline\apps\organization\views.py

```python
        # 课程机构按照点击量排名
        hot_orgs = all_orgs.order_by("-click_nums")[:3]  # -倒序排列  # 取前三
```




#### 显示排名在网页上

MxOnline\templates\org-list.html

```html
            {% for curent_org in hot_orgs %}
                <dl class="des">
                    <dt class="num fl">{{ forloop.counter }}</dt>  {# 排名 #}
                    <dd>
                        <a href="/company/2/"><h1>{{ curent_org.name }}</h1></a>
                        <p>{{ curent_org.address }}</p>
                    </dd>
                </dl>
            {% endfor %}
```




### 排序功能




#### 变更数据库-->变更model

修改 models.py

makemigrations organization

migrate organization




#### 前端回传排序方式

MxOnline\templates\org-list.html

```html
					<li class=""><a href="?sort=students&ct=&city=">学习人数 &#8595;</a></li>
					<li class=""><a href="?sort=courses&ct=&city=">课程数 &#8595;</a></li>
```




#### 后端接收排序方式

MxOnline\apps\organization\views.py

```python
        # 排序
        sort = request.GET.get("sort", "")
        if sort:
            if sort == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort == "courses":
                all_orgs = all_orgs.order_by("-course_nums")
```




#### 展示排序结果

MxOnline\templates\org-list.html

```html
					<li class="{% if sort == '' %}active{% endif %}"><a href="?ct={{ category }}&city={{ city_id }}">全部</a> </li>
					<li class="{% if sort == 'students' %}active{% endif %}"><a href="?sort=students&ct={{ category }}&city={{ city_id }}">学习人数 &#8595;</a></li>
					<li class="{% if sort == 'courses' %}active{% endif %}"><a href="?sort=students&ct={{ category }}&city={{ city_id }}">课程数 &#8595;</a></li>
```




### 用户提交“我要学习”功能  modelform表单提交




#### 新建 MxOnline\apps\organization\forms.py

```python
class UserAskForm(forms.ModelForm):  # ModelForm

    # my_filed = forms.CharField()  # ModelForm 可新增字段

    class Meta:
        model = UserAsk  # 指明该 ModelForm 是由哪个 Model 转换来的
        fields = ['name', 'mobile', 'course_name']  # 挑选 Model 中的部分字段做转换

    '''
    form中的变量名要和html中的name一致
                        <input type="text" name="course_name" id="companyAddress" placeholder="课程名" maxlength="50" />
    '''

    def clean_mobile(self):  # 自定义对mobile做表单验证  # 必须以 clean 开头命名方法
        """
        验证手机号码是否合法
        """

        # 取出form中的mobile
        mobile = self.cleaned_data['mobile']

        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'  # 正则
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:  # 不匹配，抛出异常，返回错误信息
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
```




#### 新建 MxOnline\apps\organization\urls.py

存放关于课程机构的url配置




#### 在 MxOnline\MxOnline\urls.py 下

整理课程机构的url

用 include 连接 MxOnline\apps\organization\urls.py 

```python
    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),  # namespace 命名空间，这样即使organization.urls中有name和urls下的name相同，也不会冲突
```




##### 在 MxOnline\templates\base.html 下使用 namespace

```html
							<li class="active" ><a href="{% url 'org:org_list' %}">授课机构</a></li>
```




#### 使用 modelform 验证表单，提交表单




##### 在 MxOnline\apps\organization\urls.py 下配置提交表单的 url

```python
    # 点击“我要学习”的提交
    url(r'^ask_add/$', AddUserAskView.as_view(), name="ask_add"),
```




##### 在 MxOnline\apps\organization\views.py 下写点击提交表单后的后台逻辑

使用 modelform 验证表单

```python
class AddUserAskView(View):
    """
    用户添加咨询
    """
    def post(self, request):
        userask_form = UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask = userask_form.save(commit=True)  # ModelForm 可以选择直接保存到数据库
            return HttpResponse("{'status': 'success'}", content_type='application/json')  # 返回json
        else:
            # return HttpResponse('{"status": "fail", "msg": {0}}'.format(userask_form.errors), content_type='application/json')  # 返回json
            return HttpResponse('{"status": "fail", "msg": "添加出错"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
```




#### 用ajax提交表单

MxOnline\templates\org-list.html 中的js

```js
<script>
    $(function(){
        $('#jsStayBtn').on('click', function(){
            $.ajax({
                cache: false,
                type: "POST",
                url:"{% url "org:ask_add" %}",
                data:$('#jsStayForm').serialize(),
                async: true,
                success: function(data) {  {# data是views.py中传过来的json #}
                    if(data.status == 'success'){
                        $('#jsStayForm')[0].reset();
                        alert("提交成功")
                    }else if(data.status == 'fail'){
                        $('#jsCompanyTips').html(data.msg)
                    }
                },
            });
        });
    })

</script>
```




## 机构详情页 机构首页




### 在xadmin下新增数据




#### 重载str方法  MxOnline\apps\organization\models.py

```python
    def __str__(self):  # 重载str方法
        return self.name
```




### 给课程新增所属机构的外键




#### 修改models MxOnline\apps\courses\models.py

```python
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    ···
    ···
```




#### 生成数据表

```
makemigrations courses

migrate courses
```




### 拷贝html到 MxOnline\templates 下




### 在 MxOnline\templates 下新建 org_base.html




### 使用 org_base.html 完成 MxOnline\templates\org-detail-homepage.html

```html
{% extends 'org_base.html' %}

{% load staticfiles %}

{% block custom_title %}机构首页 - 慕学网{% endblock %}

{% block page_path %}机构首页{% endblock %}

{% block custom_course_org_name %}{{ course_org.name }}{% endblock %}

{% block right_form %}
<div class="right companycenter layout grouping" >
···
<div class="right companycenter layout" >
···
<div class="right companycenter layout" >
···
{% endblock %}
```




### 配置url  MxOnline\apps\organization\urls.py

```python
    # 课程机构详情页  机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
```




### 写view  MxOnline\apps\organization\views.py

```python
class OrgHomeView(View):
    """
    课程机构首页
    """

    def get(self, request, org_id):
        current_page = "home"
        course_org = CourseOrg.objects.get(id=int(org_id))

        # 用户是否收藏了该课程机构
        has_fav = False
        if request.user.is_authenticated():  # 如果用户登录了
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=2):
                has_fav = True
        # MxOnline\templates\org_base.html
        #                  {% if has_fav %}已收藏{% else %}收藏{% endif %}

        # all_courses = course_org.course_set.all()[:3]  # 取出所有以 course_org 为外键的 Course  # [models下的class名]_set  # 取3个
        all_courses = course_org.course_set.all()  # 取出所有以 course_org 为外键的 Course  # [models下的class名]_set
        all_teachers = course_org.teacher_set.all()
        return render(request, 'org-detail-homepage.html', {
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            "course_org": course_org,
            "current_page": current_page,
            "has_fav": has_fav,

        })
```




### 在html中展示view传过来的数据  MxOnline\templates\org-detail-homepage.html

显示课程

```html
            {% for course in all_courses %}
                <div class="module1_5 box">
                    <a href="course-detail.html"><img width="214" src="{{ MEDIA_URL }}{{ course.image }}"/></a>
                    <div class="des">
                        <a href="course-detail.html"><h2>{{ course.name }}</h2></a>
                        <span class="fl">课时：<i class="key">{{ course.learn_times }}</i></span>
                        <span class="fr">参加人数：{{ course.students }}</span>
                    </div>
                    <div class="bottom">
                        <span class="fl">{{ course.course_org.name }}</span>
                         <span class="star fr  notlogin
                            " data-favid="13"  data-fav-type="4">
                            {{ course.fav_nums }}
                        </span>
                    </div>
                </div>
            {% endfor %}
```

显示教师

```html
    {% for teacher in all_teachers %}
    <div class="diarys">
        <div class="module5 share company-diary-box" style="padding:10px 0;">
            <div class="left">
                <img class="pic" src="{{ MEDIA_URL }}{{ teacher.image }}"/>
                <p>昵称：{{ teacher.name }}</p>
            </div>
            <div class="right">
                <div class="top">
                    <div class="fl">
                        <a href=""><h1>java开发教程</h1></a>
                        <span>发表于：2015-10-12</span>
                    </div>
                </div>
                <div class="middle" style="border-bottom:0;">课程介绍</div>
            </div>
        </div>
    </div>
    {% endfor %}
```

显示机构介绍

```html
    <div class="cont">&nbsp; &nbsp; <p>&nbsp; &nbsp;</p><h1 class="ue_t" label="Title center" name="tc" style="border-bottom-color:#cccccc;border-bottom-width:2px;border-bottom-style:solid;padding:0px 4px 0px 0px;text-align:center;margin:0px 0px 20px;"><span style="color:#c0504d;">[键入文档标题]</span></h1><p style="text-align:center;"><strong class="ue_t">[键入文档副标题]</strong></p><h3><span class="ue_t" style="font-family:幼圆">[标题 1]</span></h3><p class="ue_t" style="text-indent:2em;">{{ course_org.desc }}</p><p class="ue_t" style="text-indent:2em;"><img src="{% static 'media/courses/ueditor/57aa86a0000145c512000460_20161210234050_865.jpg' %}" title="" alt="57aa86a0000145c512000460.jpg"/> </p><h3><span class="ue_t" style="font-family:幼圆">[标题 2]</span></h3><p><img src="http://api.map.baidu.com/staticimage?center=116.410899,39.863624&zoom=11&width=530&height=340&markers=116.404,39.915" width="530" height="340"/> </p><p class="ue_t" style="text-indent:2em;">在“开始”选项卡上，通过从快速样式库中为所选文本选择一种外观，您可以方便地更改文档中所选文本的格式。 您还可以使用“开始”选项卡上的其他控件来直接设置文本格式。大多数控件都允许您选择是使用当前主题外观，还是使用某种直接指定的格式。</p><h3><span class="ue_t" style="font-family:幼圆">[标题 3]</span></h3><p>2016-12-10</p><p class="ue_t">对于“插入”选项卡上的库，在设计时都充分考虑了其中的项与文档整体外观的协调性。 您可以使用这些库来插入表格、页眉、页脚、列表、封面以及其他文档构建基块。 您创建的图片、图表或关系图也将与当前的文档外观协调一致。</p><p class="ue_t"><br/> </p><p><br/></p><p><br/></p><a href="/company/desc/22/"><span class="green">[查看更多]</span></a></div>
```




## 机构详情页 机构课程页




### 使用 org_base.html 完成 MxOnline\templates\org-detail-course.html




### 配置url  MxOnline\apps\organization\urls.py




### 写view  MxOnline\apps\organization\views.py




### 在html中展示view传过来的数据  MxOnline\templates\org-detail-course.html




## 机构详情页 机构介绍页




### 使用 org_base.html 完成 MxOnline\templates\org-detail-desc.html




### 配置url  MxOnline\apps\organization\urls.py




### 写view  MxOnline\apps\organization\views.py




### 在html中展示view传过来的数据  MxOnline\templates\org-detail-desc.html




## 机构详情页 机构教师页  （同上）




## 课程机构收藏功能




### 配置url  MxOnline\apps\organization\urls.py

```python
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
```




### 写view  MxOnline\apps\organization\views.py

```python
class AddFavView(View):
    """
    用户收藏，用户取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)

        if not request.user.is_authenticated():  # 如果用户未登录
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
            # 这里只回传json数据，跳转到登录页面由ajax完成

        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:  # 如果记录已经存在，说明用户是要取消收藏
            exist_records.delete()
            return HttpResponse('{"status": "success", "msg": "收藏"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.save()
                return HttpResponse('{"status": "success", "msg": "已收藏"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
            else:
                return HttpResponse('{"status": "fail", "msg": "收藏失败"}', content_type='application/json')  # 返回json  # json数据里面的引号要用双引号！！！
```




### 修改html  MxOnline\templates\org-base.html  中的ajax

```html
function add_fav(current_elem, fav_id, fav_type){
    $.ajax({
        cache: false,
        type: "POST",
        url:"{% url 'org:add_fav' %}",
        data:{'fav_id':fav_id, 'fav_type':fav_type},
        async: true,
        beforeSend:function(xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");  {# 取csrf_token的值 #}
        },                                                               {# {% csrf_token %} 会生成一段html代码 #}
        success: function(data) {  {# data 是一个json数据 #}
            if(data.status == 'fail'){
                if(data.msg == '用户未登录'){
                    window.location.href="{% url 'login' %}";  {# 跳转到登录页面 #}
                }else{
                    alert(data.msg)
                }

            }else if(data.status == 'success'){
                current_elem.text(data.msg)
            }
        },
    });
}

$('.collectionbtn').on('click', function(){  {# 监听点击 #}
    add_fav($(this), {{ course_org.id }}, 2);  {# fav_id 为课程机构的id #}  {# fav_type 为2 （收藏的是课程机构） #}
});
```




