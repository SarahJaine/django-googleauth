from django.conf.urls import *
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='googleauth_login'),
    url(r'^callback/$', views.callback, name='googleauth_callback'),
    url(r'^logout/$', views.logout, name='googleauth_logout'),
]
