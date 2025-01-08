from django.urls import path
from  . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', views.index,name='index'),
    path('tregister/teacherlogin/', LoginView.as_view(template_name='teach_login.html'),name='teacherLogin'),
    path('tregister/', views.Teacher_signup_view,name='teacherRegister'),
    path('sregister/', views.Student_signup_view,name='studentRegister'),
    path('studentlogin/', LoginView.as_view(template_name='stdnt_login.html'),name='studentlogin'),
    path('student-dashboard/', views.student_dashboard_view,name='studentDashboard'),
    path('teacher-dashboard/', views.teacher_dashboard_view,name='teacherDashboard'),
    path('adminlogin/', LoginView.as_view(template_name='admin_login.html'),name='adminlogin'),
    path('admin-dashboard/', views.admin_dashboard_view,name='adminDashboard'),
    path('teacher-profile/', views.teacher_profile_view,name='teacherProfile'),
    path('teacher-attendance/', views.teacher_attendance_view,name='teachStAttendance'),
    path('teacher-marks/', views.teacher_marks_view,name='teachStMarks'),
    path('teacher-stats/', views.teacher_stats_view,name='teachStStats'),
    path('teacher-details/', views.teacher_details_view,name='teachStDetails'),
    path('teacher-home/', views.teacher_home_view,name='teachHome'),
    path('student-home/', views.student_home_view,name='studentHome'),
    path('student-profile/', views.student_profile_view,name='studentProfile'),
    path('student-attendance/', views.student_attendance_view,name='studentAttendance'),
    path('student-marks/', views.student_grades_view,name='studentGrades'),
    path('student-schedule/', views.student_schedule_view,name='studentSchedule'),
    path('admin-home/', views.admin_home_view,name='adminHome'),
    path('admin-student/', views.admin_mg_student_view,name='adminMgStudent'),
    path('admin-teacher/', views.admin_mg_teacher_view,name='adminMgTeacher'),
    path('admin-course/', views.admin_mg_course_view,name='adminMgCourse'),

]
