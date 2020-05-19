# @ Time    : 2019/9/25 20:45
# @ Author  : JuRan
from django.urls import path ,re_path
from . import views
from django.views.decorators.csrf import csrf_exempt
# 应用命名空间
app_name = 'front'

urlpatterns = [
    path("",views.index,name='index'),

    # path("register",views.Register,name='register'),
    path("login/",views.LoginView.as_view(),name='login'),
    path("logout/",views.LogoutView.as_view(),name='logout'),
    path("send_sms/",csrf_exempt(views.SendDynamicloginView.as_view()),name='send_sms'),
    path("d_login/",csrf_exempt(views.DynamicLoginView.as_view()),name='d_login'),
    path("register/",csrf_exempt(views.RegisterView.as_view()),name='register'),




]