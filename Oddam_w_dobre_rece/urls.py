from django.contrib import admin
from django.urls import path
from OddamApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('form-confirmation/', views.form_confirmation, name='form-confirmation'),

    path('base/', views.base, name='base'),

    path('profile/', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('logout/', views.logout_view, name='logout'),


]
