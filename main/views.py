from django.shortcuts import render, HttpResponse, get_object_or_404 ,redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.


def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
    
    elif request.user.is_authenticated:
        return redirect('Dashboard')
        
    return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')

@login_required(login_url='Login')
def dashboard(request):
    return render(request, 'home.html')

@login_required(login_url='Login')
def reports(request):
    data = Report.objects.all()
    context = {
        'data' : data
    }
    
    return render(request, 'reports.html', context=context)

@login_required(login_url='Login')
def update_reports(request, report_id):
    if request.method == "POST":
        report = get_object_or_404(Report, report_id = report_id)
        if request.user.is_authenticated:
            report_read_status = ReportReadStatus.objects.get_or_create(user=request.user, report=report)
            report_read_status.is_read = True
            report_read_status.save()
            return HttpResponse('Success')
    return HttpResponse("error happened")


def signout(request):
    logout(request)
    return redirect('Login')