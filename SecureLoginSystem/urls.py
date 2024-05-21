from django.urls import path

from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.Register ,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user-login',views.logout_user,name='user_logout'),
    path('account-locked',views.accountLocked,name='account_locked'),

]