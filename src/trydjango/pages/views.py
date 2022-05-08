from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request)
    return render(request,"home.html",{})

def about_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request)
    return render(request,"about.html",{})

def contact_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request)
    return render(request,"contact.html",{})

