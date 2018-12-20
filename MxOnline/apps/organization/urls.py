# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView

urlpatterns = [

    # 课程机构列表页
    url(r'^list/$', OrgView.as_view(), name="org_list"),

    # 点击“我要学习”的提交
    url(r'^ask_add/$', AddUserAskView.as_view(), name="ask_add"),

    # 课程机构详情页  机构首页
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),

    # 课程机构详情页  机构课程页
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),

    # 课程机构详情页  机构介绍页
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),

    # 课程机构详情页  机构教师页
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),

    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

]
