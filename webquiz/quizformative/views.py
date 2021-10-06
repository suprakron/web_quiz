from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'Home.html')


def teacher_dashboard(request):
    return render(request,'teacher/teacher_dashboard.html')
    
    