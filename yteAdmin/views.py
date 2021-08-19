import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import AdminUser, AdminRole
from .forms import RegisterForm
from django.utils.http import is_safe_url
from django.conf import settings


# Create your views here.


def login(request, *args, **kwargs):
    return render(request, 'admin_pages/login.html', {})


def register(request, *args, **kwargs):
    return render(request, 'admin_pages/register.html')


def register_new_admin(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'admin_pages/register.html', {})
    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('password_2'):
            context = {
                'error_text': 'Your password does not match.'
            }
            return JsonResponse(context, status=400)
        admin_role_input = request.POST.get('admin_role') or None
        token_input = request.POST.get('token') or None
        email_input = request.POST.get('email') or None
        # get from the "AdminRole" table in the db the email, admin_role and token using user input respectively
        qs_email = AdminRole.objects.get(email=email_input)
        qs_admin_role = AdminRole.objects.get(admin_role=admin_role_input)
        qs_token = AdminRole.objects.get(token=token_input)
        # if any one is missing
        if not qs_admin_role.exists() or not qs_token.exists() or not qs_email.exists():
            context = {
                'error_text': 'Sorry, you are not authorized for Admin.'
            }
            return JsonResponse(context, status=401)
        # let form
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            return render(request, 'public_pages/home.html', {})
    return render(request, 'admin_pages/register.html', {})


def role_generator(request, *args, **kwargs):
    random_number = random.randint(0, 238893672)
    context = {
        'token': random_number
    }
    return render(request, 'admin_pages/role_generator.html', context)


def generate_admin(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'admin_pages/register.html', {})
    if request.method == 'POST':
        admin_role_input = request.POST.get('admin_role')
        email_input = request.POST.get('email')
        token_gen = request.POST.get('token')
        print(admin_role_input, email_input, token_gen)
        return render(request, 'admin_pages/role_generator.html', {})
