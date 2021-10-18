from django.urls import path
from . import views

urlpatterns = [
    path('register',views.user_register, name='register'),
    path('account',views.user_login,name='account'),
    path('logout',views.user_logout,name='logout'),
]