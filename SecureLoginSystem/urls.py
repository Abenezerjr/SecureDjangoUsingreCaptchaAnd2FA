from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.Register ,name='register'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('user-login',views.logout_user,name='user_logout'),
    path('account-locked',views.accountLocked,name='account_locked'),

    #password managemnet viwes

    path('reset_password',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_done',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    # path('reset_password_done',auth_views.PasswordResetDoneView.as_view(),name='reset_password_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view,name='password_reset_confirm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view,name='password_reset_complete')


]