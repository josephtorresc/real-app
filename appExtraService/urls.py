from django.urls import path, include

from .views import view_extra_service

urlpatterns = [
    path('', view_extra_service, name='view_extra_service'),
]