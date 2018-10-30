# -*- coding: utf-8 -*-

import xadmin

from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    list_display = ["name", "mobile", "course_name", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["name", "mobile", "course_name"]  # 设置可以做搜索的字段
    list_filter = ["name", "mobile", "course_name", "add_time"]  # 设置可以做过滤分类的字段


class CourseCommentsAdmin(object):
    list_display = ["user", "course", "comments", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["user", "course", "comments"]  # 设置可以做搜索的字段
    list_filter = ["user", "course", "comments", "add_time"]  # 设置可以做过滤分类的字段


class UserFavoriteAdmin(object):
    list_display = ["user", "fav_id", "fav_type", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["user", "fav_id", "fav_type"]  # 设置可以做搜索的字段
    list_filter = ["user", "fav_id", "fav_type", "add_time"]  # 设置可以做过滤分类的字段


class UserMessageAdmin(object):
    list_display = ["user", "message", "has_read", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["user", "message", "has_read"]  # 设置可以做搜索的字段
    list_filter = ["user", "message", "has_read", "add_time"]  # 设置可以做过滤分类的字段


class UserCourseAdmin(object):
    list_display = ["user", "course", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["user", "course"]  # 设置可以做搜索的字段
    list_filter = ["user", "course", "add_time"]  # 设置可以做过滤分类的字段


xadmin.site.register(UserAsk, UserAskAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(UserMessage, UserMessageAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(UserCourse, UserCourseAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
