from django.urls import path, include

from .views import view_apartment

urlpatterns = [
    path('', view_apartment, name='view_apartment'),
]