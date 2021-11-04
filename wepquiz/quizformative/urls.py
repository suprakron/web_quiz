from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='home'),
    path('loginForm/', views.loginform, name='loginform'),
    path('register_optionsForm/', views.register_optionsform,
         name="register_optionsForm"),
    path('registerform_lecturer/', views.registerform__lecturer),
    path('registerform_student/', views.registerform_student),
    path('registerstudent/', views.registerstudent, name="registerstudent"),
    path('registerlecturer/', views.registerlecturer, name="registerlecturer"),
    path('login/', views.login, name="login"),
    path('student/', views.student, name="student"),
    path('lecturer/', views.lecturer, name="lecturer"),
    path('logout/',views.logout_view ,name="logout")
]
