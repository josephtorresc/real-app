from django.urls import path, include

from .views import view_rent

urlpatterns = [
    path('', view_rent, name='view_rent'),
]