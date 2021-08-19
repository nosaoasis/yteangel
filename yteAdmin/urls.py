from django.urls import path
from .views import (
    login,
    register,
    role_generator,
    register_new_admin,
    generate_admin,
)

urlpatterns = [
    path('', login, name='admin_login_page'),
    path('register', register, name='admin_register_page'),
    path('admin-role', role_generator, name='admin_generator_page'),
    path('create-admin', register_new_admin, name='create'),
    path('generate-admin', generate_admin, name='generate'),
]
