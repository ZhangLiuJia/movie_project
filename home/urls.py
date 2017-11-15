from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'(^$)|(index.html)', views.index),
    url(r'animation/$', views.animation),
    url(r'login/$', views.login),
    url(r'logout/$', views.logout),
    url(r'register/$', views.register),
    url(r'user/$', views.user),
    url(r'pwd/$', views.pwd),
    url(r'comments/$', views.coments),
    url(r'loginlog/$', views.loginlog),
    url(r'moviecol/$', views.moviecol),
    url(r'search/$', views.search),
    url(r'play/$', views.play),
]
