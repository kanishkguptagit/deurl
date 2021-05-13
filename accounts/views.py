from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

# Create your views here.

class UserSignUp(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self, request):
        email = request.POST['email']
        name = request.POST['name']
        password1 = request.POST['pass']
        password2 = request.POST['repass']

        if(password1 == password2):
            if(User.objects.filter(email=email).exists()):
                messages.error(request,'account already exist')
                return redirect('/accounts/signup/')
            else:
                user = User.objects.create_user(email=email, name=name, password=password1)
                user.save()
                return redirect('/')

        else:
            messages.error(request,'password not matching')
            return redirect('/accounts/signup/')


class UserSignIn(View):
    def get(self,request):
        return render(request,'signin.html')

    def post(self,request):
        email = request.POST['email']
        password = request.POST['pass']

        user = auth.authenticate(email=email, password=password)

        if(user is not None):
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
            return redirect('/accounts/signin/')


class UserSignOut(View):
    def get(self,request):
        auth.logout(request)
        return redirect("/")