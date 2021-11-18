from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='home'),
    path('loginForm/', views.loginform, name='loginform'),
    path('register_optionsForm/', views.register_optionsform,name="register_optionsForm"),
    path('registerform__teacher/', views.registerform__teacher),
    path('registerform_student/', views.registerform_student),
    path('registerstudent/', views.registerstudent, name="registerstudent"),
    path('registerteacher/', views.registerteacher, name="registerteacher"),
    path('teacher/',views.teacher_dashboard, name="teacher_dashboard"),
    path('login/', views.login, name="login"),
    path('student/', views.student, name="student"),
    path('teacher/', views.teacher, name="teacher"),
    path('logout/',views.logout_view ,name="logout")
]


