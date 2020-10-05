from django.urls import path, include

from appUser.views import login

urlpatterns = [
    path('login', login, name='login'),
]
