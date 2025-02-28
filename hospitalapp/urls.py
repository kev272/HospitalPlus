
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name='index'),
    path('starter/', views.starter , name='starter'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('serve/', views.serve, name='serve'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('contacts/', views.contact, name='contact'),
]