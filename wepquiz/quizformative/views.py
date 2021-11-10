from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth, Group
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'page/index.html')


def loginform(request):
    return render(request, 'page/loginform.html')


def register_optionsform(request):
    return render(request, 'page/register_options.html')


def registerform__lecturer(request):
    return render(request, 'page/registerform_lecturer.html')


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


def registerlecturer(request):
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
            user_group = Group.objects.get(name='lecturer')
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
                elif user.groups.filter(name='lecturer').exists():
                    print("ครู")
                    auth.login(request, user)
                    return JsonResponse({"groups": "lecturer"}, status=200)
            else:
                return JsonResponse({"errors": "รหัสผ่านผิดพลาด"}, status=403)
        else :
            return JsonResponse({"errors": "ไม่มีอีเมลล์ นี้ในระบบ"}, status=403)


def student(request):
    # return HttpResponse('student')
    if not request.user.is_authenticated:
        return redirect('/loginForm')
    else:
        return HttpResponse("นักเรียน <a href='/logout'>Logout</a>")


def lecturer(request):
    if not request.user.is_authenticated:
        return redirect('/loginForm')
    else:
        return HttpResponse("ครู <a href='/logout'>Logout</a>")

#################################หน้าหลักครู###########################################

def teacher_dashboard(request):
    return render(request, 'page/teacher/teacherdashboard.html')



def logout_view(request):
    auth.logout(request)
    return redirect('/loginForm')
