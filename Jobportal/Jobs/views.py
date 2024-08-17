from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login,logout



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

# def login(request):
#     return render(request,'login.html')

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

# def signin(request):
#     if request.method == 'POST':
#         name=request.POST['name']
#         email=request.POST['email']
#         password=request.POST['password']
#         pas1=request.POST['cpassword']
#         file=request.FILES['file']
#         if password != pas1:
#             messages.info(request,'Wrong Password bud')
#             return render(request,'signup.html')
#         else:
#             r=Signin.objects.create(name=name,email=email,password=password,file=file)
#             r.set_password(password)
#             r.save()
#             messages.info(request,'A user has been added')
#             return redirect('/index/')
#     return render(request,'signup.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if 'file' in request.FILES:
            cv = request.FILES['file']
        else:
            cv = None
        
        if User.objects.filter(name=name).exists():
            messages.error(request, 'Username is already taken')
            return render(request, 'signup.html')

        if password != cpassword:
            messages.error(request, 'Passwords do not match')
            return render(request, 'signup.html')

        # Create the user
        user = User.objects.create_user(name=name, email=email, password=password)

        # Create the Signin instance
        signin = Signin(user=user, file=cv)
        signin.save()

        messages.success(request, 'Successfully registered')
        return redirect('/index/')  # Redirect to your desired URL after successful registration

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            # Redirect to the desired URL after login
            return redirect('/index/')
        else:
            messages.error(request, 'Invalid email or password. Please try again.')

    return render(request, 'login.html')

# def Post(request):
     
#      return redirect('/portfolio/')
def crud(request):
    stu=User.objects.all()
    context={
        'stu':stu
    }
    return render(request,'crud.html',context)
def delete_user(request,id):
    stu=User.objects.get(id=id)
    print(stu)
    stu.delete()
    return redirect('/Crud/')
# def crud(request):
#     return render(request,'crud.html')