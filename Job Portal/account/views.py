from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy

from account.models import *
from jobapp.models import *
from account.forms import *
from jobapp.permission import user_is_employee 


def get_success_url(request):

    """
    Handle Success Url After LogIN

    """
    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('jobapp:home')



def employee_registration(request):

    """
    Handle Employee Registration

    """
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'account/employee-registration.html',context)


def employer_registration(request):

    """
    Handle Employee Registration 

    """

    form = EmployerRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect('account:login')
    context={
        
            'form':form
        }

    return render(request,'account/employer-registration.html',context)


@login_required(login_url=reverse_lazy('accounts:login'))
@user_is_employee
def employee_edit_profile(request, id=id):

    """
    Handle Employee Profile Update Functionality

    """

    user = get_object_or_404(User, id=id)
    form = EmployeeProfileEditForm(request.POST or None, instance=user)
    if form.is_valid():
        form = form.save()
        messages.success(request, 'Your Profile Was Successfully Updated!')
        return redirect(reverse("account:edit-profile", kwargs={
                                    'id': form.id
                                    }))
    context={
        
            'form':form
        }

    return render(request,'account/employee-edit-profile.html',context)




# def user_logIn(request):

#     """
#     Provides users to logIn

#     """

#     form = UserLoginForm(request.POST or None)
    

#     if request.user.is_authenticated:
#         return redirect('/')
    
#     else:
#         if request.method == 'POST':
#             if form.is_valid():
#                 auth.login(request, form.get_user())
#                 return HttpResponseRedirect(get_success_url(request))
#     context = {
#         'form': form,
#     }

#     return render(request,'account/login.html',context)
def user_logIn(request):
    """
    Provides users to logIn
    """
    form = UserLoginForm(request.POST or None)

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect('account:admin_dashboard')  # Redirect to admin dashboard
        else:
            return redirect('user_dashboard')  # Adjust this as needed for regular users

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            if user.is_staff:
                return redirect('account:admin_dashboard')  # Redirect admin to admin dashboard
            else:
                return redirect('jobapp:home')  # Redirect regular users to home

    context = {
        'form': form,
    }

    return render(request, 'account/login.html', context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    return redirect('account:login')

def is_admin(user):
    return user.is_staff  # Assuming 'is_staff' indicates admin status

@login_required(login_url=reverse_lazy('account:login'))
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    """
     Admin dashboard to view overall statistics and manage users/jobs.
     """
    total_jobs = Job.objects.count()
    total_employee = User.objects.filter(role='employee').count()
    total_employer = User.objects.filter(role='employer').count()
    total_applicants = Applicant.objects.count()
    admin_user = User.objects.filter(is_superuser=True).first()
    active_applications = Applicant.objects.filter(job__is_closed=False).count()

    # admin_name = admin_user.get_full_name() if admin_user else "Admin"
    
    context = {
         'total_jobs': total_jobs,
         'total_employee': total_employee,
         'total_employer': total_employer,
         'total_applicants': total_applicants,
         'admin_user':admin_user,
         "active_applications":active_applications
    }
    print(admin_user)

    return render(request, 'Dashboard/admin_dashboard.html',context)

# def admin_dashboard_view(request):
#     return render(request, 'Dashboard/admin_dashboard.html')

