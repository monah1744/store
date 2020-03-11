from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return "{}".format(self.username)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    user_token = models.CharField(max_length=69, blank=True, null=True)
    email_confirmed = models.BooleanField(default=False)
    wallet = models.IntegerField(default=0)