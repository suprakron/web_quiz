from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('/teacher_dashboard',views.teacher_dashboard, name="teacher_dashboard"),
]
