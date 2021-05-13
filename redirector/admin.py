from django.contrib import admin
from redirector.models import URLredirects

# Register your models here.

class URLredirectsShow(admin.ModelAdmin):

    list_display = ('user','url','urlhash')

admin.site.register(URLredirects,URLredirectsShow)