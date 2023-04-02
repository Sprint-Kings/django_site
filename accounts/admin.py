from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass
