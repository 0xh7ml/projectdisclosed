from django.shortcuts import render, HttpResponse ,redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


@login_required(login_url='Login')
def dashboard(request):
    
    if request.method == "GET":
        queryset_severity = Report.objects.values('severity').annotate(severity_dataset=Count('severity'))
        queryset_cwe = Report.objects.values('cwe').annotate(cwe_dataset=Count('cwe'))
        queryset_is_read = Report.objects.values('is_read').annotate(is_read_dataset=Count('severity'))

        context = {
            "severity_data" : queryset_severity,
            "cwe_data" : queryset_cwe,
            "read_data" : queryset_is_read
        }
        return render(request, 'home.html', context=context)

@login_required(login_url='Login')
def reports(request):
    if request.method == "GET":
        report_list = Report.objects.all().order_by('-report_id')
        
        """ Paginator """
        paginator = Paginator(report_list, per_page=10)
        
        
        """ default page num """
        page_num = request.GET.get('page', 1)
    
        
        try:
            reports = paginator.page(page_num)
        except PageNotAnInteger:
            reports = paginator.page(1)
        except EmptyPage:
            reports = paginator.page(paginator.num_pages)            
        context = {
            "data" : reports ,
        }
        return render(request, 'reports.html', context=context)
    return HttpResponse({"message" : "Method Not Allowd"}, status=405)

@login_required(login_url='Login')
def update_reports(request,  report_id):
    if request.method == "POST":
        if request.user.is_authenticated:
            report_read_status = Report.objects.filter(report_id=report_id).update(is_read=True)
            return JsonResponse({"success": True})
        return JsonResponse({"message": "Unauthorized"}, status=401)
    return JsonResponse({"message": "Method Not Allowd"}, status=405)


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        check_user = User.objects.filter(username=username).exists()
        
        if check_user:
            context = {
                "message" : 'Username already exists'
            }
            return render(request, 'signup.html', context=context)
        # Creating the user
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashboard')
        return render(request, 'signup.html')  # Redirect to dashboard or any other desired page
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect('Login')