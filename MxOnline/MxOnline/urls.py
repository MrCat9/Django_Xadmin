"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve  # 处理静态文件（课程机构的logo）

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, user_logout
# from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),  # TemplateView的as_view()方法会把template转化为view，这样就不需要自己写后台的view
    # url(r'^login/$', user_login, name="login"),  # login不能加括号login()，加括号的话就是调用函数，不加的话只是一个句柄，指向函数login
    url(r'^login/$', LoginView.as_view(), name="login"),

    url(r'^logout/$', user_logout, name="logout"),

    url(r'^register/$', RegisterView.as_view(), name="register"),

    url(r'^captcha/', include('captcha.urls')),
    # 处理用户通过邮箱激活注册的账号
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # (?P<active_code>.*) 提取url的部分， .* 为正则表达式，匹配出来的值放到 active_code

    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),

    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # (?P<active_code>.*) 提取url的部分， .* 为正则表达式，匹配出来的值放到 reset_code

    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    # # 课程机构首页
    # url(r'^org_list/$', OrgView.as_view(), name="org_list"),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),  # namespace 命名空间，这样即使organization.urls中有name和urls下的name相同，也不会冲突

]
