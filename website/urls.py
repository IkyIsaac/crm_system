from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('login',views.login_user,name='login'),
    path('add_record',views.add_record,name='add_record'),
    path('logout',views.logout_user,name='logout'),
    path('register',views.register,name='register'),
    path('register_user',views.register_user,name='register_user'),
    path('record/<int:pk>',views.customer_record,name='record'),
    path('delete/<int:pk>',views.delete_record,name='delete_record'),
    path('update/<int:pk>',views.update_record,name='update_record'),
]