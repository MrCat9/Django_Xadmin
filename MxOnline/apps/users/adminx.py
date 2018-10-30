# -*- coding: utf-8 -*-

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):  # xadmin的全局配置
    enable_themes = True  # 使用xadmin的主题功能
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "慕学后台管理系统"
    site_footer = "慕学在线网"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):  # 为 EmailVerifyRecord 写一个管理器
    list_display = ["code", "email", "send_type", "send_time"]  # 设置要在后台显示的字段
    search_fields = ["code", "email", "send_type"]  # 设置可以做搜索的字段
    list_filter = ["code", "email", "send_type", "send_time"]  # 设置可以做


class BannerAdmin(object):
    list_display = ["title", "image", "url", "index", "add_time"]  # 设置要在后台显示的字段
    search_fields = ["title", "image", "url", "index"]  # 设置可以做搜索的字段
    list_filter = ["title", "image", "url", "index", "add_time"]  # 设置可以做过滤分类的字段


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)
xadmin.site.register(Banner, BannerAdmin)  # 把admin和model进行关联注册  # register(model, 管理该model的admin)

xadmin.site.register(views.BaseAdminView, BaseSetting)  # 注册BaseSetting
xadmin.site.register(views.CommAdminView, GlobalSettings)# 注册GlobalSettings

