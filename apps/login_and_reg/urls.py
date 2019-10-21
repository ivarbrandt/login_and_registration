from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.registration_page),
    url(r'^success$', views.successful_login_page),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
]