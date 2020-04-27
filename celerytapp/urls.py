from django.conf.urls import include, url
from celerytapp import views
from celerytapp.views import *




urlpatterns = [

    url(r"^celery/", views.celery),
    url(r"^red/(?P<id>\d+)$", views.red),

]
