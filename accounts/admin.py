from django.contrib import admin
from accounts import models
from redirector.models import URLredirects

# Register your models here.

class URLredirectsinline(admin.TabularInline):
    model = URLredirects

class UserProfileShow(admin.ModelAdmin):

    inlines = [
        URLredirectsinline,
    ]

    list_display = ('email','name')

admin.site.register(models.UserProfile, UserProfileShow)