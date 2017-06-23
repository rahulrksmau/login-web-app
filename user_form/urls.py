from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/success/$', views.register_success, name='r_success'),
    url(r'^home/$', views.home, name='home'),
    url(r'^change-password/$', views.change_pass, name='change_pass'),
    url(r'^$', views.index, name='index'),
    url(r'^resetting/$', views.reset, name='reset'),
]
