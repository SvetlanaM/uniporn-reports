from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    IP = models.GenericIPAddressField(protocol = 'both', blank = True, null = True)
    is_returning = models.BooleanField(default = True)
    novistits = models.PositiveIntegerField(default = 0)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
