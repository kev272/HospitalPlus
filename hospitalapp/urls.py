
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index , name='index'),
    path('starter/', views.starter , name='starter'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('serve/', views.serve, name='serve'),
    path('departments/', views.departments, name='departments'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('contacts/', views.contact, name='contact'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),

#mpesa api
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),
]