# -*- coding: utf-8 -*-

from django import forms
import re

from operation.models import UserAsk


# class UserAskForm(forms.Form):  # Form
#     name = forms.CharField(required=True, min_length=2, max_length=10)
#     phone = forms.CharField(required=True, min_length=11, max_length=11)
#     course_name = forms.CharField(required=True, min_length=5, max_length=50)


class UserAskForm(forms.ModelForm):  # ModelForm

    # my_filed = forms.CharField()  # ModelForm 可新增字段

    class Meta:
        model = UserAsk  # 指明该 ModelForm 是由哪个 Model 转换来的
        fields = ['name', 'mobile', 'course_name']  # 挑选 Model 中的部分字段做转换

    '''
    form中的变量名要和html中的name一致
                        <input type="text" name="course_name" id="companyAddress" placeholder="课程名" maxlength="50" />
    '''

    def clean_mobile(self):  # 自定义对mobile做表单验证  # 必须以 clean 开头命名方法
        """
        验证手机号码是否合法
        """

        # 取出form中的mobile
        mobile = self.cleaned_data['mobile']

        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'  # 正则
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:  # 不匹配，抛出异常，返回错误信息
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")



