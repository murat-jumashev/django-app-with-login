from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=255, verbose_name='Full name')

    def __str__(self):
        return self.username

