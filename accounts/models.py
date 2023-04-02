from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    patronymic = models.CharField(max_length=54, verbose_name='Отчетсво')
    rules = models.BooleanField(default=False, verbose_name='Согласие с правилами регистрации')
