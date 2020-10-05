from django.urls import path, include

from .views import view_finance

urlpatterns = [
    path('', view_finance, name='view_finance'),
]