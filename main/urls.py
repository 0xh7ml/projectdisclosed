from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Login" ),
    path('signup', views.signup, name="Register" ),
    path('home', views.dashboard, name="Dashboard" ),
    path('reports', views.reports, name="Reports" ),
    path('reports/<int:report_id>', views.update_reports, name="update_report" ),
    path('logout', views.signout, name="logout" ),
]
