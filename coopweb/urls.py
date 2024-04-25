"""coopweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views as user_views
from portal import views as portal_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('signup/', user_views.signup, name='signup'),
    path('dashboard/', portal_views.dashboard, name='dashboard'),
    path('transactions/', portal_views.transactions, name='transactions'),
    path('loanapplication/', portal_views.loanapplication, name='application'),
    path('shopindex/', portal_views.shopindex, name='shop-index'),
    path('categories/', portal_views.categories, name='categories'),
    path('dashboard_year/<periodid>', portal_views.dashboard_year,name='dashboard-year'),
    path('transactions_year/<periodid>',portal_views.transactions_year,name='transactions-year'),
    #path('transactions/<str:name>', portal_views.account_details, name='account_data'),
]
