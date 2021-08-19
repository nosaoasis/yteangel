from django import forms
from .models import AdminUser
from django.conf import settings


class RegisterForm(forms.ModelForm):
    class Meta:
        model = AdminUser
        fields = ['first_name', 'last_name', 'email',
                  'password', 'admin_role', 'token']
