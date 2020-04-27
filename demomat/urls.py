from django.conf.urls import include, url
from demomat import views
from demomat.views import *




urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^index2/$', views.index2),
    url(r'^index3/$', views.index3),
    url(r"^doc/",views.doc),
    url(r'^login/$', LoginView.as_view(), name='login'),  # 登录
    url(r'^logout/$', LogoutView.as_view(), name=''),  # 登录

    url(r'^user_center/$', UserCenterView.as_view(), name=''),  # 个人中心


    url(r"^demo/", views.demo),
    url(r"^demo1/(?P<id>\d+)$", views.demo1),

]
