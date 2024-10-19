from django.urls import path, include
from . import views

#URLConf
urlpatterns = [
    path('', views.searchresults, name= 'searchresults'),
]