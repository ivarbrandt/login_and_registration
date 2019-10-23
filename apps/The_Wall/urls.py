from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^postmessage$', views.postmessage),
    url(r'^postcomment$', views.postcomment),
    url(r'^deletemessage/(?P<id>\d+)$', views.deletemessage),

]