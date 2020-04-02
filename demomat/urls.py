from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^index2/$', views.index2),
    url(r'^index3/$', views.index3),
    url(r"^doc/",views.doc)

]
