from django.urls import path
from redirector.views import urlRedirectCreate,urlRedirect,deleteUrl

app_name="redirector"
urlpatterns = [
    path('', urlRedirectCreate.as_view(), name='redirectcreate'),
    path('delete/<slug:urldelete>/', deleteUrl, name='deleteurl'),    
    path('<slug:urlto>/', urlRedirect, name='urlredirect'),    
]