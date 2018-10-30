# -*- coding: utf-8 -*-

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ["name", "desc", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["name", "desc"]  # 设置可以做搜索的字段
    list_filter = ["name", "desc", "add_time"]  # 设置可以做过滤分类的字段


class CourseOrgAdmin(object):
    list_display = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city"]  # 设置可以做搜索的字段
    list_filter = ["name", "desc", "click_nums", "fav_nums", "image", "address", "city", "add_time"]  # 设置可以做过滤分类的字段


class TeacherAdmin(object):
    list_display = ["org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums"]  # 设置可以做搜索的字段
    list_filter = ["org", "name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums", "add_time"]  # 设置可以做过滤分类的字段


xadmin.site.register(CityDict, CityDictAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(Teacher, TeacherAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)

