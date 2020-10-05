from django.urls import path, include

from appGeneral.views import home

urlpatterns = [
    path('', home, name='index'),
    path('home', home, name='home'),
]
