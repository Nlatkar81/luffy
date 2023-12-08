from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.template import loader
from home.models import Home
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        area=request.POST.get('area')
        a=Home(fname=fname,lname=lname,email=email,area=area)
        a.save()
    return render(request,"home.html")

def show(request):
    # myhome=Home.objects.all().values()
    # myhome=Home.objects.filter(id=14).values()|Home.objects.filter(id=15).values()
    myhome=Home.objects.order_by('fname','-area').values()
    # myhome=Home.objects.order_by('-area').values()
    template=loader.get_template('show.html')
    context={
        'myhome':myhome,
    }
    return HttpResponse(template.render(context,request))

