from django.db import models

# Create your models here.


class AdminUser(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False,
                              null=False, max_length=30)
    password = models.CharField(max_length=30, blank=False, null=False)
    admin_role = models.CharField(max_length=20, blank=False, null=False)
    token = models.IntegerField(blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)


class AdminRole(models.Model):
    admin_role = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False,
                              null=False, max_length=30)
    token = models.IntegerField(blank=False, null=False)
