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




    # # 网页提交表单（前端接收用户填写的数据，post给后端，后端把数据存入数据库）
    # # 前端post过来的数据会在request里面
    # if request.method == "POST":  # 判断是post方法才往数据库里存数据，是get方法不存
    #     # 接收前端post过来的数据
    #     name = request.POST.get("name", "")  # get()方法用于取字典里的某个值（如："name"），如果取不到返回""
    #     message = request.POST.get("message", "")
    #     address = request.POST.get("address", "")
    #     email = request.POST.get("email", "")
    #
    #     # 把数据存入数据库
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld3"
    #     user_message.save()




    # # 删除数据库中的数据
    # all_messages = UserMessage.objects.filter(name="ZhangSan", address="上海")
    # for message in all_messages:
    #     message.delete()




    # 将数据库里的数据显示到html页面中
    message = None
    all_messages = UserMessage.objects.filter(name="ZhangSan2")
    if all_messages:  # 如果数据库里已经有ZhangSan2的数据
        message = all_messages[0]




    #            # request    # html文件名称
    return render(request, "message_form.html", {
        "my_message": message  # 向前端传递数据  # 在html文件中配置，使得后端数据能够展示到前端
    })
