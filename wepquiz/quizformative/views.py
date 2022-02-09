from multiprocessing import context
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, Http404, reverse, HttpResponse
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
 

import json
import datetime
from django.http import HttpResponseBadRequest

# from .forms import QuestionForms
# from .models import  Question
 
# Create your views here.
 


def index(request):
    return render(request, 'page/index.html')

 
def loginform(request):
    return render(request, 'page/loginform.html')


def register_optionsform(request):
    return render(request, 'page/register_options.html')


def registerform__teacher(request):
    return render(request, 'page/registerform_teacher.html')


def registerform_student(request):
    return render(request, 'page/registerform_student.html')


def registerstudent(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            print("Username นี้ใช้งานระบบแล้ว")
            return JsonResponse({"errors": "username นี้ใช้งานระบบแล้ว"}, status=403)
            # return HttpResponse('Username นี้ใช้งานระบบแล้ว')
        elif User.objects.filter(email=email).exists():
            print("Email นี้ใช้งานระบบแล้ว")
            return JsonResponse({"errors": "Email นี้ใช้งานระบบแล้ว"}, status=403)
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user_group = Group.objects.get(name='student')
            user.groups.add(user_group)
            return JsonResponse({"success": "success"}, status=200)


def registerteacher(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            print("Username นี้ใช้งานระบบแล้ว")
            return JsonResponse({"errors": "username นี้ใช้งานระบบแล้ว"}, status=403)
        elif User.objects.filter(email=email).exists():
            print("Email นี้ใช้งานระบบแล้ว")
            return JsonResponse({"errors": "Email นี้ใช้งานระบบแล้ว"}, status=403)
        else:
            user = User.objects.create_user(
                username=username, password=password, email=email)
            user_group = Group.objects.get(name='teacher')
            user.groups.add(user_group)
            return JsonResponse({"success": "success"}, status=200)


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if  User.objects.filter(email=email).exists():
            username = User.objects.get(email=email)
            print(username)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.groups.filter(name='student').exists():
                    print("นักเรียน")
                    auth.login(request, user)
                    return JsonResponse({"groups": "student"}, status=200)
                elif user.groups.filter(name='teacher').exists():
                    print("ครู")
                    auth.login(request, user)
                    return JsonResponse({"groups": "teacher"}, status=200)
            else:
                return JsonResponse({"errors": "รหัสผ่านผิดพลาด"}, status=403)
        else :
            return JsonResponse({"errors": "ไม่มีอีเมลล์ นี้ในระบบ"}, status=403)


#################################หน้าหลักนักเรียน###########################################
def student_dashboard(request):
    # return HttpResponse('student')
    if not request.user.is_authenticated:
        return redirect('/loginForm')
    else:
        return render(request, 'dashboard/studentdashboard.html')

def view_scores(request):
    return render(request, 'page/student/view_score.html')

def doing_quiz(request):
    return render(request, 'page/student/doing_quiz.html')


#################################หน้าหลักครู###########################################

def teacher_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/loginForm')
    else:
        return render(request, 'dashboard/teacherdashboard.html')

 

def create_quiz(request):
    return render(request, 'page/teacher/create_quiz.html') 
 


 
def reply_score(request):
    return render(request, 'page/teacher/reply_score.html')


def logout_view(request):
    auth.logout(request)
    return redirect('/loginForm')
