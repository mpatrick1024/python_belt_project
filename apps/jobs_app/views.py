from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index (request):
    print ("*"*80)
    print ("IN ROOT ROUTE, INDEX FUNCTION OF JOB APP")
    return redirect ("/jobs/new")

def job_new (request):
    print ("*"*80)
    print ("IN JOB NEW FUNCTION")
    this_user = User.objects.get (id=request.session['user_id'])
    context = {
        "user": this_user
    }
    return render (request, "jobs_app/job_new.html", context)

def job_create (request):
    print ("*"*80)
    print ("IN JOB CREATE FUNCTION")
    errors = Job.objects.job_validator (request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/jobs/new')
    else:
        this_user = User.objects.get (id=request.session['user_id'])
        this_job = Job.objects.create (title=request.POST["title"], description=request.POST["description"], location=request.POST["location"], category=request.POST.get("category"), user=this_user)
        this_job = Job.objects.last()
        return redirect ("/dashboard")

def job_cancel (request):
    print ("*"*80)
    print ("IN JOB CANCEL FUNCTION")
    return redirect ('/dashboard')

def job_show (request, job_id):
    print ("*"*80)
    print ("IN JOB SHOW FUNCTION")
    job = Job.objects.get(id=job_id)
    user = User.objects.get (id=request.session['user_id'])

    context = {
        'job': job,
        'user': user
    }
    return render (request, "jobs_app/job_show.html", context)

def job_edit (request, job_id):
    print ("*"*80)
    print ("IN JOB EDIT FUNCTION")
    job = Job.objects.get (id=job_id)
    context = {
        'job' : job
    }
    return render (request, "jobs_app/job_edit.html", context)

def job_update (request, job_id):
    this_job = Job.objects.get(id=job_id)
    this_job.title = (request.POST["title"])
    this_job.description = (request.POST["description"])
    this_job.location = (request.POST["location"])
    this_job.save()
    return redirect ('/dashboard')

def job_destroy (request, job_id):
    print ("*"*80)
    print ("IN JOB DESTROY FUNCTION")
    job = Job.objects.get(id=job_id)
    job.delete()
    return redirect ("/dashboard")

def job_giveup (request, job_id):
    print ("*"*80)
    print ("IN JOB GIVEUP FUNCTION")
    this_job = Job.objects.get(id=job_id)
    this_job.worker = None
    this_job.save()
    return redirect ("/dashboard")
    
def job_add (request, job_id):
    print ("*"*80)
    print ("IN JOB ADDFUNCTION")
    this_user = User.objects.get(id=request.session['user_id'])
    this_job = Job.objects.get(id=job_id)
    this_job.worker = this_user
    this_job.save()
    return redirect ("/dashboard")