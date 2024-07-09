from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')



def blog_single(request):
    return render(request,'blog-single.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def gallery(request):
    return render(request,'gallery.html')

def job_listings(request):
    return render(request,'job-listings.html')

def job_single(request):
    return render(request,'job-single.html')

def login(request):
    return render(request,'login.html')

def portfolio_single(request):
    return render(request,'portfolio-single.html')

def portfolio(reqeust):
    return render(reqeust,'portfolio.html')

def post_job(request):
    return render(request,'post-job.html')

def service_single(request):
    return render(request,'service-single.html')

def services(request):
    return render(request,'services.html')

def testimonials(request):
    return render(request,'testimonials.html')

def signin(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        # pas1=request.POST['pass1']
        file=request.FILES['file']
        r=Signin.objects.create(name=name,email=email,password=password,file=file)
        messages.info(request,'A user has been added')
        return redirect('/index/')
    return render(request,'signup.html')