from django.urls import path
from redirector.views import urlRedirectCreate,urlRedirect

app_name="redirector"
urlpatterns = [
    path('', urlRedirectCreate.as_view(), name='redirectcreate'),  
    path('<slug:urlto>/', urlRedirect, name='urlredirect'),    
]