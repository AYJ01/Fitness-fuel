"""
URL configuration for FitnessFuel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Fuel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.contact),
    path('commonhome/',views.contact),
    path('signin/', views.signin),
    path('userRegister/', views.userRegister),
    path('Register/', views.Register),
    path('trainerRegister/', views.trainerRegister),
    path('userhome/', views.userhome),
    path('trainerhome/', views.trainerhome),
    path('shophome/', views.shophome),
    path('adminhome/', views.adminhome),
    path('shopproducts/', views.shopproducts),
    path('userproducts/', views.userproducts),
    path('usercart/', views.usercart),
    path('cart/', views.cart),
    path('payment/', views.payment),
    path('adminproducts/', views.adminproducts),
    path('adminusers/', views.adminusers),
    path('adminshops/', views.adminshops),
    path('admintrainers/', views.admintrainers),
    path('adminarticles/', views.adminarticles),
    path('admindeletearticle/', views.admindeletearticle),
    path('admindeleteuser/', views.admindeleteuser),
    path('admindeleteshops/', views.admindeleteshops),
    path('admindeletetrainer/', views.admindeletetrainer),
        path('usertrainers/', views.usertrainers),
    path('userchat/', views.userchat),
    path('send_message/<int:trainer_id>/', views.send_message),
    path('userarticles/', views.userarticles),
    path('traineruser/', views.traineruser),
    path('trainerchat/', views.trainerchat),
    path('shoporder/', views.shoporder),
    path('shopdelivery/', views.shopdelivery),
    
]
