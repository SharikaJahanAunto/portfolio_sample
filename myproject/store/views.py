from django.shortcuts import render
from .models import About

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    about = About.objects.all()
    return render(request,'about.html',{'about':about})

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')