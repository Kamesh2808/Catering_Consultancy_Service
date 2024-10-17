
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home),
    path('login.html', views.login),
    path('signup.html', views.signup),
    path('index.html',views.index),
    path('caterersignup.html',views.caterersignup),
    path('main.html',views.home),
    path('main1.html',views.home1),
    path('cateringinfo.html',views.cateringinfo),
    path('booking1.html',views.booking1),
    path('booking2.html',views.booking2),
    path('booking3.html',views.booking3),
    path('booking4.html',views.booking4),
    path('booking5.html',views.booking5),
    path('booking6.html',views.booking6),
    path('booking7.html',views.booking7),
    path('booking8.html',views.booking8),
    path('booking9.html',views.booking9),
    path('booking10.html',views.booking10),
    path('booking11.html',views.booking11),
    path('booking12.html',views.booking12),
    path('booking13.html',views.booking13),
    
]

