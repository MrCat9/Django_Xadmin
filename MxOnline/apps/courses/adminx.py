# -*- coding: utf-8 -*-

import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_nums", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["name", "desc", "detail", "degree", "students", "fav_nums", "image", "click_nums"]  # 设置可以做搜索的字段
    list_filter = ["name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_nums", "add_time"]  # 设置可以做过滤分类的字段


class LessonAdmin(object):
    list_display = ["course", "name", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["course__name", "name"]  # 设置可以做搜索的字段  # 搜索的字段不能是外键类型(course)的，所以用外键类型(course)下的char类型(name)来做为搜索的字段
    list_filter = ["course__name", "name", "add_time"]  # 设置可以做过滤分类的字段  # course是外键  # course__name 用外键(course)的name做过滤分类


class VideoAdmin(object):
    list_display = ["lesson", "name", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["lesson__name", "name"]  # 设置可以做搜索的字段
    list_filter = ["lesson", "name", "add_time"]  # 设置可以做过滤分类的字段


class CourseResourceAdmin(object):
    list_display = ["course", "name", "download", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["course", "name", "download"]  # 设置可以做搜索的字段
    list_filter = ["course", "name", "download", "add_time"]  # 设置可以做过滤分类的字段


xadmin.site.register(Course, CourseAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(Lesson, LessonAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(Video, VideoAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(CourseResource, CourseResourceAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)

