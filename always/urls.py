from django.conf.urls import url
from always import views

urlpatterns = [
    url(r'index.html$', views.index),
    url(r'login/$', views.login),
    url(r'logout/', views.logout),
    url(r'pwd/', views.pwd),
    url(r'tag_add/', views.tag_add),
    url(r'tag_list/', views.tag_list),
    url(r'movie_add/', views.movie_add),
    url(r'movie_list/', views.movie_list),
    url(r'preview_add', views.preview_add),
    url(r'preview_list', views.preview_list),
    url(r'user_list', views.user_list),
    url(r'user_view', views.user_view),
    url(r'comment_list', views.comment_list),
    url(r'moviecol_list', views.moviecol_list),
    url(r'oplog_list', views.oplog_list),
    url(r'adminloginlog_list', views.adminloginlog_list),
    url(r'userloginlog_list', views.userloginlog_list),
    url(r'auth_add', views.auth_add),
    url(r'auth_list', views.auth_list),
    url(r'role_add', views.role_add),
    url(r'role_list', views.role_list),
    url(r'admin_add', views.admin_add),
    url(r'admin_list', views.admin_list),
]
