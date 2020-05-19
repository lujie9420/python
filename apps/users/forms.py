# @ Time    : 2019/9/25 21:43
# @ Author  : JuRan
from django import forms
from captcha.fields import CaptchaField
import redis
from django.conf import settings
from apps.users.models import UserProfile
import re

class DynamicloginForm(forms.Form):
    # myfield = AnyOtherField()
    captcha = CaptchaField()
    mobile = forms.CharField(required=True,max_length=11,min_length=11)

# ModelForm
# Form
# 登录验证  验证用户名和密码
class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=2)
    password = forms.CharField(required=True,min_length=3)


class DynamicloginPostForm(forms.Form):
    code = forms.CharField(required=True,max_length=4,min_length=4)
    mobile = forms.CharField(required=True, max_length=11, min_length=11)

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        code = self.cleaned_data.get('code')
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0,
                                  charset='utf8', decode_responses=True)
        redis_code = r.get(str(mobile))
        if redis_code != code:
            raise forms.ValidationError('验证不正确')
        return self.cleaned_data



class RegisterGetForm(forms.Form):
    captcha = CaptchaField()



class RegisterPostForm(forms.Form):
    mobile = forms.CharField(max_length=11,min_length=11,required=True)
    code = forms.CharField(min_length=4,max_length=4,required=True)
    password = forms.CharField(required=True)

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        mobile_exists = UserProfile.objects.filter(mobile=mobile)

        if mobile_exists:
            raise forms.ValidationError('手机号码已经存在')
        return mobile

    def clean(self):
        mobile = self.cleaned_data.get('mobile')
        code = self.cleaned_data.get('code')
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0,
                                  charset='utf8', decode_responses=True)
        redis_code = r.get(str(mobile))
        if redis_code != code:
            raise forms.ValidationError('验证不正确')
        return self.cleaned_data