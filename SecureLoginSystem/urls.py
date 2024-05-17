from django.urls import path

from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.Register ,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('login',views.login_user,name='login'),
]