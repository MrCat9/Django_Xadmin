from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # 用来做 or 并集
from django.views.generic.base import View  # 基类
from django.contrib.auth.hashers import make_password  # 用于加密明文的 password
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email

# Create your views here.


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))  # 先用username查  # get()方法只会取出一个，当有多个时，报错
            # user = UserProfile.objects.get(Q(username=username)|Q(email=username), password=password)  # username=username或email=username  并password=password
            if user.check_password(password):  # 检查密码是否正确
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                # 根据 email 去改 UserProfile 表
                user = UserProfile.objects.get(email=email)
                user.is_active = True  # 改为激活
                user.save()
        else:
            return render(request, "active_fail.html")
        return render(request, "login.html")


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()  # 实例化 form
        return render(request, "register.html", {'register_form': register_form})  # 将 form 传给 html，完成验证码

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():  # 如果通过验证，就开始注册
            # 从前端接收 email，pass_word
            email = request.POST.get("email", "")
            pass_word = request.POST.get("password", "")

            # 判断邮箱是否已注册
            if UserProfile.objects.filter(email=email):
                return render(request, "register.html", {"register_form": register_form, "msg": "该邮箱已注册"})

            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False  # 默认激活状态为 False， 邮箱验证后才激活
            user_profile.save()

            # 发送邮箱
            send_register_email(email, "register")

            return render(request, "login.html")
        else:  # 如果注册失败
            return render(request, "register.html", {"register_form": register_form})


class LoginView(View):
    def get(self, request):
        # print(1/0)  # 测试 500 页面
        return render(request, "login.html", {})

    def post(self, request):
        # 先通过form检查用户名和密码
        login_form = LoginForm(request.POST)
        if login_form.is_valid():  # 如果form验证成功，再用数据库进行验证
            # 从前端接收user_name，pass_word
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            # 验证用户名和密码
            user = authenticate(username=user_name, password=pass_word)  # 验证不通过的话会是一个None
            # 会调用 CustomBackend 下自定义的authenticate

            if user is not None:  # 如果验证通过了
                if user.is_active:  # 如果是激活的用户
                    login(request, user)  # 就登录
                    # return render(request, "index.html")
                    response = HttpResponseRedirect(reverse('index'))
                    return response

                else:
                    return render(request, "login.html", {"msg": "用户未激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误！", })
        else:
            return render(request, "login.html", {"login_form": login_form, })


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

            # 从 post 中获取 email
            #             get()方法中取的要与html中的name一致
            email = request.POST.get("email", "")

            # 发送邮件
            send_register_email(email, "forget")

            return render(request, "send_success.html")

        else:
            return render(request, "forgetpwd.html", {"forget_form": forget_form})


class ResetView(View):
    def get(self, request, reset_code):
        all_records = EmailVerifyRecord.objects.filter(code=reset_code)
        if all_records:
            for record in all_records:
                email = record.email  # 拿出email
                return render(request, "password_reset.html", {"email": email})  # 跳转到重置密码页面


class ModifyPwdView(View):
    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            #  get()方法中取的要与html中的name一致
            '''
                                <input type="password" name="password1" id="pwd" placeholder="6-20位非中文字符">
           '''

            if pwd1 != pwd2:
                return render(request, "password_reset.html", {"email": email, "msg": "密码不一致"})  # 跳转到重置密码页面

            # 修改密码
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd2)
            user.save()

            return render(request, "login.html")
        else:
            email = request.POST.get("email", "")
            return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})  # 跳转到重置密码页面





# def user_login(request):
#     if request.method == "POST":
#         # 从前端接收user_name，pass_word
#         user_name = request.POST.get("username", "")
#         pass_word = request.POST.get("password", "")
#
#         # 验证用户名和密码
#         user = authenticate(username=user_name, password=pass_word)  # 验证不通过的话会是一个None
#         # 会调用 CustomBackend 下自定义的authenticate
#
#         if user is not None:  # 如果验证通过了
#             login(request, user)  # 就登录
#             return render(request, "index.html")
#         else:
#             return render(request, "login.html", {"msg": "用户名或密码错误！"})
#
#     elif request.method == "GET":
#         return render(request, "login.html", {})


def user_logout(request):
    logout(request)
    return render(request, "index.html", {})
