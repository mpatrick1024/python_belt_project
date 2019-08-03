from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *
from apps.jobs_app.models import *
# Create your views here
def index (request):
    print ("*"*80)
    print ("IN ROOT ROUTE, INDEX FUNCTION")
    all_users = User.objects.all().values()
    context = {
        "users": all_users
    }
    return render (request, "login_dashboard_app/index.html", context)

def success (request):
    print ("*"*80)
    print ("IN SUCCESS FUNCTION")
    if 'user_id' not in request.session:
        print ("user not logged in, redirecting")
        return redirect ("/")
    else:
        return render (request, "login_dashboard_app/success.html")

def create_user (request):
    print ("*"*80)
    print ("IN CREATE USER FUNCTION")
    errors = User.objects.user_validator (request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        User.objects.create (first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=request.POST["password"])
        user = User.objects.last()
        print(user)
        print (user.id)
        request.session['user_id'] = user.id
        request.session['user_name'] = user.first_name
        messages.success (request, 'Registration Successful.')
        return redirect ("/success")

def get_user (request):
    print ("*"*80)
    print ("IN GET USER FUNCTION")
    errors = User.objects.login_validator (request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['user_name'] = user.first_name
        messages.success (request, 'Login Successful.')
        return redirect ("/success")

def dashboard (request):
    print ("*"*80)
    print ("IN DASHBOARD FUNCTION")
    all_jobs = Job.objects.all()
    context = {
        "all_jobs": all_jobs
    }
    return render (request, "login_dashboard_app/dashboard.html", context)

def destroy (request):
    print ("*"*80)
    print ("IN DESTROY FUNCTION")
    if 'user_id' in request.session:
        request.session.clear()
    return redirect ("/")