from django.contrib import admin

# Register your models here.
from .models import User

# from django.contrib.auth.admin import UserAdmin


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    list_per_page = 25

admin.site.register(User, UserAdmin)
