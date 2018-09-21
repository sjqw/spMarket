from django.conf.urls import url

from user.views import UserRegister, UserLogin, UserCenter, UserAddress, UserInfo, UserLogout, index

urlpatterns = [
    url(r'^register/$', UserRegister.as_view(), name='register'),
    url(r'^login/$', UserLogin.as_view(), name='login'),
    url(r'^center/$', UserCenter.as_view(), name='center'),
    url(r'^address/$', UserAddress.as_view(), name='address'),
    url(r'^info/$', UserInfo.as_view(), name='info'),
    url(r'^logout/$', UserLogout.as_view(), name='logout'),
    url(r'^index/$', index, name='index'),
]
