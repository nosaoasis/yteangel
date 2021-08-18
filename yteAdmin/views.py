from django.shortcuts import render

# Create your views here.


def login(request, *args, **kwargs):
    return render(request, 'admin_pages/login.html', {})
