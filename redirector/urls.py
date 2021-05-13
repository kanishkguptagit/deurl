from django.urls import path
from redirector.views import urlredirect

urlpatterns = [
    path('', urlredirect.as_view(), name='redirector'),
    #path('u/<str:slugs>', urlredirect.as_view(), name='redirector'),
]