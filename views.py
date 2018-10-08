# -*- coding: utf-8 -*-

from django.shortcuts import render

from .models import UserMessage  # import views.py同目录下的models中的UserMessage

# Create your views here.


def getform(request):
    # # 查询数据库中的数据
    #
    # # 默认的数据表管理器 objects  # all()方法返回数据库中的所有记录
    # # 返回QuerySet类（Django的内置类）
    # all_messages = UserMessage.objects.all()
    # for message in all_messages:
    #     print(message.name)
    #
    # # 取出name="ZhangSan"且address="上海"的
    # all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    # for message in all_messages:
    #     print(message.name)




    # # 向数据库中插入数据
    # user_message = UserMessage()
    # user_message.name = "ZhangSan2"
    # user_message.message = "helloworld2"
    # user_message.address = "北京"
    # user_message.email = "2@2.com"
    # user_message.save()




    # 前端post过来的数据会在request里面




    #            # request    # html文件名称
    return render(request, "message_form.html")
