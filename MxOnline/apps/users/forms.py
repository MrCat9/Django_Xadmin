# -*- coding: utf-8 -*-

from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)  # required=True 必填字段，不填报错
    password = forms.CharField(required=True, min_length=5)
    # password = forms.CharField(required=True, max_length=5, min_length=1)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)  # 要与html中input的name一样
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 自定义要抛出的错误信息


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)  # 要与html中input的name一样
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})  # 自定义要抛出的错误信息


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)  # 要与html中input的name一样
    password2 = forms.CharField(required=True, min_length=5)

