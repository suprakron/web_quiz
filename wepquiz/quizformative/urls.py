from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),                                                      #หน้าแรก
    path('loginForm/', views.loginform, name='loginform'),                                   #หน้าเข้าสู่ระบบ
    path('register_optionsForm/', views.register_optionsform,name="register_optionsForm"),   #หน้าเลือกลงทะเบียน
    path('registerform__teacher/', views.registerform__teacher),                             #หน้าลงทะเบียนของครู
    path('registerform_student/', views.registerform_student),                               #หน้าลงทะเบียนของนักเรียน
    path('registerstudent/', views.registerstudent, name="registerstudent"),                 #ฟังก์ชั่นลงทะเบียนของนักเรียน
    path('registerteacher/', views.registerteacher, name="registerteacher"),                 #ฟังก์ชั่นลงทะเบียนของนักเรียน
   
    path('login/', views.login, name="login"),                                                #ฟังก์ชั่นหน้าlogin

    path('teacher/',views.teacher_dashboard, name="teacher_dashboard"),                         #หน้าหลักของครู
    path('create_quiz/',views.create_quiz, name="create_quiz"),                                 #หน้าสร้างแบบทดสอบ
    
    path('reply_score/', views.reply_score, name="reply_score"),                                #หน้าตอบกลับคะแนนนักเรียนของครู
   



    path('student/',views.student_dashboard, name="student_dashboard"),       #หน้าหลักของนักเรียน
    path('view_score/',views.view_scores, name="viewscore"),                  #หน้าดูคะแนนแบบทดสอบของนักเรียน
    path('doing_quiz/',views.doing_quiz, name="doing_quiz"),                  #หน้าทำแบบทดสอบของนักเรียน
  

    path('logout/',views.logout_view ,name="logout")
]
 
