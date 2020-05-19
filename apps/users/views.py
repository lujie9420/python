from django.shortcuts import render, reverse, redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from apps.users.forms import LoginForm, DynamicloginForm,RegisterGetForm,DynamicloginPostForm,RegisterPostForm
from django.conf import settings
from apps.utils.yunpian import Send_to_mess
from apps.utils.random_str import generate_random
from apps.users.models import UserProfile
import redis

"""
验证码 pip install django-simple-captcha
"""
import redis


# Create your views here.

def index(request):
    # return render(request,'index.html')
    return render(request, 'index.html')
    # return HttpResponse('success')





# def loginout(request):
#     return render(request,'login.html')

class LogoutView(View):
    def get(self, request):
        # Django内置的logout方法，得到request后删除sessionid中的信息
        logout(request)
        return redirect(reverse('front:index'))


class LoginView(View):
    """
    jr  jr123!!
    """

    def get(self, request):
        # if判断 验证当前用户有没有登录，若登录则返回当前页面，反之则进入登录页面重新登录
        if request.user.is_authenticated:
            return redirect(reverse('front:index'))
        """
        动态验证码定义：
        """
        login_Dynamic = DynamicloginForm()
        return render(request, 'login.html', {'Dynamic_login': login_Dynamic})

    #
    #
    def post(self, request):

        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            # 验证用户名和密码是否已经存在
            # User.objects.filter(username=username,password=password)
            users = authenticate(username=username, password=password)

            if users is not None:
                # 查询到用户 内置login方法
                # cookie和session
                login(request, users)
                # 页面重定向
                return redirect(reverse('front:index'))
                # return render(request,'index.html')
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            print(forms.errors.get_json_data())
            return render(request, 'login.html', {'forms_errors': forms.errors, 'forms': forms})


class SendDynamicloginView(View):
    def post(self, request):

        send_sms_form = DynamicloginForm(request.POST)
        re_dict = {}
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data.get('mobile')
            code = generate_random(4, 1)
            sms_json = Send_to_mess(settings.YP_APIKEY, code, mobile)
            if sms_json['code'] == 0:
                # decode_responses=True 不加这个参数，就是一个字节
                # 验证码存入redis并设置过期时间
                con = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0,
                                  charset='utf8', decode_responses=True)
                con.set(mobile, code)
                con.expire(str(mobile), 60 * 5)
                re_dict['status'] = 'success'
            else:
                re_dict['msg'] = sms_json['msg']

        else:
            print(send_sms_form.errors.get_json_data())
            for key, value in send_sms_form.errors.items():
                re_dict[key] = value[0]

        return JsonResponse(re_dict)


class DynamicLoginView(View):
    def post(self,request):
        dynamic_login = False
        login_form = DynamicloginPostForm(request.POST)
        d_form = DynamicloginForm(request.POST)
        if login_form.is_valid():
            mobile = login_form.cleaned_data.get('mobile')
            #返回的是Queryset列表
            existed_users = UserProfile.objects.filter(mobile=mobile)
            if existed_users:
                user = existed_users[0]
            else:
                #新建一个用户
                user = UserProfile(username=mobile)
                password = generate_random(10,2)
                user.set_password(password)
                user.mobile =mobile
                user.save()
            login(request,user)
            return redirect(reverse('front:index'))
        else:
            dynamic_login = True
            print(login_form.errors.get_json_data())
            return render(request,'login.html',{'login_form':login_form,
                                                'forms_errors':login_form.errors,'d_form':d_form
                                                ,'dynamic_login':dynamic_login})






class RegisterView(View):
    def get(self,request):
        r_from = RegisterGetForm()
        return render(request,'register.html',{'r_form':r_from})

    def post(self,request):
        r_post_form = RegisterPostForm(request.POST)
        P_from = RegisterGetForm()
        if r_post_form.is_valid():
            mobile = r_post_form.cleaned_data.get('mobile')
            password = r_post_form.cleaned_data.get('password')
            # 注册新建一个用户
            user = UserProfile(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()
            #登录
            login(request,user)
            return redirect(reverse('front:index'))
        else:
            content = {
                'r_form':P_from,
                'forms_errors':r_post_form.errors
            }
            return render(request,'register.html',context=content)