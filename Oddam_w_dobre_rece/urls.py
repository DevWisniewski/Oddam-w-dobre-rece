from django.contrib import admin
from django.urls import path
from OddamApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('form/', views.form, name='form'),
    path('form-confirmation/', views.form_confirmation, name='form-confirmation'),

    # ścieżki do widoków generowanych przy pomocy base.html
    path('index1/', views.index, name='index1'),
    path('login1/', views.login, name='login1'),
    path('register1/', views.register, name='register1'),
    path('form1/', views.form, name='form1'),
    path('form-confirmation1/', views.form_confirmation, name='form-confirmation1'),


]
