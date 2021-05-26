from django.shortcuts import redirect, render
from django.views import View
from redirector.models import URLredirects
from django.contrib import messages
import random,string
from urlredirect import settings

# Create your views here.

class urlRedirectCreate(View):

    def get(self,request):
        if request.user.is_authenticated:
            all_urls = URLredirects.objects.filter(user=request.user)
            domain = settings.urlhosting
            data = {
                'urls' : all_urls,
                'domain' : domain
            }
        else:
            data = {}
        return render(request,'home.html',{'data':data})

    
    def post(self,request):
        if (request.user.is_authenticated):
            url = request.POST['url']
            custname = request.POST['cust']
            new_hash=''

            if set(custname).difference(string.ascii_letters + string.digits):
                messages.info(request,'no special characters allowed')
                return redirect("/")

            if(URLredirects.objects.filter(user=request.user).filter(url=url).exists()):
                messages.info(request,'redirect already exist')
                return redirect("/")

            if(url[:5] == 'https'):
                url = url[8:]

            if (custname is not None):            
                if URLredirects.objects.filter(urlhash=custname).exists():                
                    messages.error(request,'Custom Name already taken')
                    return redirect("/")
                else:
                    new_hash = custname                

            if (custname == ''):
                new_hash = ''.join(random.choice(string.ascii_letters) for x in range(10))
                print("I was here********",new_hash)
                while (URLredirects.objects.filter(urlhash = new_hash).exists()):
                    new_hash = ''
                    new_hash = ''.join(random.choice(string.ascii_letters) for x in range(10))
                
            new_url = URLredirects(user=request.user,url=url, urlhash=new_hash)
            new_url.save()
            messages.info(request, 'URL shortened')
            return redirect('/')
        else:
            return redirect('/accounts/signin')


def deleteUrl(request,urldelete=None):
    URLredirects.objects.filter(urlhash=urldelete).delete()
    return redirect('/')


def urlRedirect(request, urlto=None):
    data = URLredirects.objects.get(urlhash=urlto)
    new_site = "https://"+data.url
    return redirect(new_site)
