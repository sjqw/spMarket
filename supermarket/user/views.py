from django.http import HttpResponse
from django.shortcuts import render, redirect
import hashlib

# Create your views here.
from django.urls import reverse
from django.views import View

from user.forms import UserModelForm, RegisterModelForm
from user.models import User
import hashlib


# 首页
def index(request):
    return render(request, 'user/index.html')


# /注册
class UserRegister(View):
    def get(self, request):
        if request.session.get('username') == 'zhangsan':
            return render(request, 'user/reg.html')
        else:
            redirect(reverse('用户:login'))

    def post(self, request):
        if request.session.get('username') == 'zhangsan':
            pram = request.POST
            pwdd = pram.get('pwdd')
            form = RegisterModelForm(pram)
            if form.is_valid():
                clean_data = form.cleaned_data
                if clean_data.get('pwd') == pwdd:
                    pwd = clean_data.get('pwd')
                    m = hashlib.md5()
                    # print(pwd.encode())  # 把字符串转换成bytes类型
                    m.update(pwd.encode())  # 不能直接对字符串加密，要先把字符串转换成bytes类型
                    pwd = m.hexdigest()
                    User.objects.create(UserName=clean_data.get('UserName'), pwd=pwd)
                    return redirect(reverse('用户:login'))
                else:
                    context = {'parms': '两次输入的密码不一致'}
                    return render(request, 'user/reg.html', context)

                # pwd=clean_data.get('pwd')
            else:
                context={'form':form}
                return render(request,'user/reg.html',context)
        else:
            redirect(reverse('用户:login'))


# 登录
class UserLogin(View):
    def get(self, request):
        request.session['username'] = 'zhangsan'
        return render(request, 'user/login.html')

    def post(self, request):
        if request.session.get('username') == 'zhangsan':
            data = request.POST
            form = UserModelForm(data)
            if form.is_valid():
                data = form.cleaned_data
                UserName = data.get('UserName')
                if User.objects.filter(UserName=UserName):
                    pwd = data.get('pwd')
                    m = hashlib.md5()
                    # print(pwd.encode())  # 把字符串转换成bytes类型
                    m.update(pwd.encode())  # 不能直接对字符串加密，要先把字符串转换成bytes类型
                    pwd = m.hexdigest()

                    if User.objects.filter(pwd=pwd):
                        return redirect(reverse('用户:index', ))
                    else:
                        context = {'date': '密码错误'}
                        return render(request, 'user/login.html', context)
                else:
                    context = {'data': '用户名错误'}
                    return render(request, 'user/login.html', context)
            else:
                context = {'form': form}
                return render(request, 'user/login.html', context)
        else:
            return HttpResponse('验证失败')


# 个人中心
class UserCenter(View):
    def get(self, request):
        return render(request, 'user/member.html')

    def post(self, request):
        pass


# 收货地址
class UserAddress(View):
    def get(self, request):
        return render(request, 'user/address.html')

    def post(self, request):
        pass


# 个人资料
class UserInfo(View):
    def get(self, request):
        return render(request, 'user/infor.html')

    def post(self, request):
        pass


# 退出
class UserLogout(View):
    def get(self, request):
        return render(request, 'user/member.html')

    def post(self, request):
        pass
