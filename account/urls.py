from django.urls import path, include
from . import views

#URLConf
urlpatterns = [
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
]