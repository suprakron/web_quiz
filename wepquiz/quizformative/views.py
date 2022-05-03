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

#################################code Quiz###########################################
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied
from .models import Quiz
from quizformative.utils.createQuiz import createQuiz
from quizformative.utils.updateQuiz import _updateQuiz
from quizformative.utils.duplicateQuiz import duplicateQuiz
 
 
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




#################################ส่วนของระบบแบบทดสอบ###########################################

class QuizDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Quiz

    def test_func(self):
        return self.request.user == self.get_object().maker


class QuizListView(LoginRequiredMixin, ListView):
    model = Quiz

    def get_queryset(self):
        return Quiz.objects.filter(maker=self.request.user).order_by('-id')
    # paginate_by = 100


class QuizDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Quiz
    success_url = reverse_lazy('quiz-list')

    def test_func(self):
        return self.request.user == self.get_object().maker


@login_required
def newQuiz(request):
    if request.method == 'POST':
        data = request.POST.dict()
        print(data)

        createQuiz(data, request.user)

        return redirect('teacher_dashboard')

    defaultNumberOfChoices = range(1, 5)
    return render(request, 'quiz/new_quiz.html', {'defaultNumberOfChoices': defaultNumberOfChoices})


@login_required
def updateQuiz(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)

    if request.user != quiz.maker:
        raise PermissionDenied

    if request.method == 'POST':
        data = request.POST.dict()
        print(data)
        _updateQuiz(data, quiz)

        return redirect('quiz-list')

    startDate = quiz.getStartDate()
    startTime = quiz.getStartTime()

    return render(request, 'quiz/quiz_update.html', {'quiz': quiz, 'startDate': startDate, 'startTime': startTime})


@require_POST
def quizDuplicate(request, pk):
    parentQuiz = get_object_or_404(Quiz, id=pk)

    if request.user != parentQuiz.maker:
        raise PermissionDenied

    data = request.POST.dict()

    quiz = duplicateQuiz(request.user, parentQuiz, data['quiz'])

    return redirect('quiz-update', pk=quiz.id)


@login_required
def quizResult(request, pk):
    quiz = get_object_or_404(Quiz, id=pk)

    if request.user != quiz.maker:
        raise PermissionDenied

    takers = quiz.taker_set.all()
    return render(request, 'quiz/result.html', {'quiz': quiz, 'takers': takers})

 