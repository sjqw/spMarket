from django.shortcuts import render

# Create your views here.
from django.views import View


# /注册
class UserRegister(View):
    def get(self, request):
        return render(request,'user/reg.html')

    def post(self, request):
        pass


# 登录
class UserLogin(View):
    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        pass


# 个人中心
class UserCenter(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 收货地址
class UserAddress(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


# 个人资料
class UserInfo(View):
    def get(self, request):
        return render(request,'user/infor.html')

    def post(self, request):
        pass


# 退出
class UserLogout(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
