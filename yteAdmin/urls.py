from django.urls import path
from .views import login, register, role_generator

urlpatterns = [
    path('', login),
    path('register', register),
    path('admin-role', role_generator),
]
