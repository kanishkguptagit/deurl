from django.contrib import admin
from accounts import models

# Register your models here.

class UserProfileShow(admin.ModelAdmin):
    list_display = ('email','name')

admin.site.register(models.UserProfile, UserProfileShow)