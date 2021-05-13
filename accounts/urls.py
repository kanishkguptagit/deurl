from django.urls import path
from django.views.generic import TemplateView
from accounts.views import UserSignUp,UserSignIn,UserSignOut

urlpatterns = [    
    path('signin/',UserSignIn.as_view(), name='signin'),
    path('signup/',UserSignUp.as_view(), name='signup'),
    path('logout/',UserSignOut.as_view(), name='signout'),
]