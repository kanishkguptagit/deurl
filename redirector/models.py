from django.db import models
from django.conf import settings

# Create your models here.

class URLredirects(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    url = models.URLField(max_length=300)
    urlhash = models.CharField(max_length=30)

    def __str__(self):
        return self.url