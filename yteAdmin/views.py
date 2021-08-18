import random
from django.shortcuts import render

# Create your views here.


def login(request, *args, **kwargs):
    return render(request, 'admin_pages/login.html', {})


def register(request, *args, **kwargs):
    return render(request, 'admin_pages/register.html', {})


def role_generator(request, *args, **kwargs):
    random_number = random.randint(0, 2388193672)
    context = {
        'token': random_number
    }

    return render(request, 'admin_pages/role_generator.html', context)
