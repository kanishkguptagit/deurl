from django.shortcuts import redirect, render
from django.views import View
from redirector.models import URLredirects
from django.contrib import messages
import random
import string

# Create your views here.

class urlredirect(View):

    def get(self,request):
        if request.user.is_authenticated:
            all_urls = URLredirects.objects.filter(user=request.user)
        else:
            all_urls={}
        return render(request,'home.html',{'urls':all_urls})

    def post(self,request):
        url = request.POST['url']
        custname = request.POST['cust']
        if (custname is not None):
            hashc = URLredirects.objects.filter(urlhash=custname)
            if hashc is not None:                
                new_hash = custname                
            else:
                messages.error(request,'Custom Name already taken')
                return redirect("/")

        else:
            new_hash = ''.join(random.choice(string.ascii_letters) for x in range(10))
            while (URLredirects.objects.filter(urlhash = new_hash).exists()):
                new_hash = ''.join(random.choice(string.ascii_letters) for x in range(10))
            
        new_url = URLredirects(user=request.user,url=url, urlhash=new_hash)
        new_url.save()
        messages.info(request, 'URL shortened')
        return redirect('/')