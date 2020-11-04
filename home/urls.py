from django.conf.urls import url
from .views import Home
from django.urls import path

urlpatterns = [
    path('', Home.as_view(), name='home'),
]