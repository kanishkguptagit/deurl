from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [    
    path('signin/',TemplateView.as_view(template_name="signin.html"), name='signin'),
    path('signup/',TemplateView.as_view(template_name="signup.html"), name='signup'),
]