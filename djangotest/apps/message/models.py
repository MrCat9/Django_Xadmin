# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class UserMessage(models.Model):

    object_id = models.CharField(max_length=50, default="", primary_key=True)
    #           char类型数据  最大长度        该字段可以为空       设置默认值        类似于注释
    name = models.CharField(max_length=20, null=True, blank=True, default="",verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    # models.ForeignKey  # 外键类型
    # models.DateTimeField
    # models.IntegerField
    # models.IPAddressField
    # models.FileField  # 上传文件
    # models.ImageField

    # ctrl+鼠标右键  进入models，进入fields  查看Field

    # 定义meta信息
    class Meta:
        # 数据表的显示名称
        verbose_name = u"用户留言信息"
        # 为了自动生成数据表，不指定db_table
        # db_table

        # db_table = "uesr_message"  # 生成的数据表名为uesr_message

        # 默认排序
        # ordering = "-object_id"  # 通过object_id做倒序排列

        # 复述信息，默认为verbose_name后面加上s
        verbose_name_plural = verbose_name
