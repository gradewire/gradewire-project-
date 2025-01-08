from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from . import forms,models
from .models import Teacher,Student
from django.contrib.auth.decorators import login_required
from .forms import TeacherForm
from django.contrib import messages
from django.contrib.auth.models import Group
# Create your views here.
def index(request):
    return render(request,'index.html')
def studentLogin(request):

    return render(request,'stdnt_login.html')
def student_dashboard_view(request):
    return render(request,'stdnt_dashboard.html')

def admin_login(request):
    correct_username = 'group1'
    correct_password = '4321'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == correct_username and password == correct_password:
            return redirect('adminDashboard')
        else:
            return HttpResponse('Invalid credentials, please try again.')
    return render(request, 'admin_login.html')
       


def Teacher_signup_view(request):
    teacherForm=forms.TeacherForm()
    mydict={'teacherForm':teacherForm}
    if request.method=='POST':
        teacherForm=forms.TeacherForm(request.POST,request.FILES)
        if teacherForm.is_valid():
            teacher=teacherForm.save()
            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
        return HttpResponseRedirect('teacherlogin')
    return render(request,'teach_register.html',context=mydict)

def is_teacher(user):
    return user.group.filter(name='TEACHER').exists()

from django.contrib import messages

from .models import Student
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def teacherLogin(request):
    if request.method == 'POST':
        username = request.POST['teacher_id']
        password = request.POST['password']
        
        # Authenticate the user with the username (username could be the teacher_id)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the student_id exists in the Student model
            try:
                teacher = Teacher.objects.get(teacher_id=username)
                # If the student exists, log the user in
                login(request, user)
                return redirect('student_dashboard')
            except Teacher.DoesNotExist:
                # If no Teacher entry is found for this teacher_id
                messages.error(request, 'No student account found for this ID or not registered as a teacher.')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'teach_login.html')


@login_required
def teacher_dashboard_view(request):
    return render(request,'teach_dashboard.html')
    



from .forms import StudentForm
def Student_signup_view(request):
    if request.method == 'POST':
        # Create the form instance with POST data and file data (if any)
        studentForm = StudentForm(request.POST, request.FILES)
        
        if studentForm.is_valid():
            studentForm.save()
            return redirect('studentlogin')  # Make sure 'studentlogin' is a valid URL name in your urls.py
        else:
            return render(request, 'stdnt_register.html', {'studentForm': studentForm})

    else:
        studentForm = StudentForm()

    return render(request, 'stdnt_register.html', {'studentForm': studentForm})


def is_student(user):
    return user.group.filter(name='STUDENT').exists()

def studentLogin(request):
    if request.method=='POST':
      username=request.POST['register_id']
      password = request.POST['password']
      user = authenticate(request,username = username,password = password)

      if user is not None:
          login(request, user)
          return redirect('studentDashbord')
      else:
          return render(request,'stdnt_login.html',{'error':'Invalid credentials'} )
    return render(request, 'stdnt_login.html')

@login_required
def student_dashboard_view(request):
    return render(request,'stdnt_dashboard.html')

def manage_student_view(request):
    students = models.Student.objects.all(is_student=True)
    return render(request, 'admin_mg_student.html',{'student':students})

def manage_teacher_view(request):
    teachers = models.Teacher.objects.all(is_teacher=True)
    return render(request, 'admin_mg_teacher.html',{'teacher':teachers})

def afterlogin_view(request):
    if is_teacher(request.user):
        accountapproval=models.Teacher.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('admin-dashboard')
        
    elif is_student(request.user):
        return redirect('student-home')
    else:
        return redirect('teacher-home')

@login_required
def admin_dashboard_view(request):
    return render(request,'admin_dashboard.html')

def teacher_profile_view(request):
    return render(request,'teacher_profile.html')

def teacher_attendance_view(request):
    return render(request,'teach_st_attendance.html')

def teacher_marks_view(request):
    return render(request,'teach_st_marks.html')

def teacher_stats_view(request):
    return render(request,'teach_st_stats.html')

def teacher_details_view(request):
    return render(request,'teach_st_details.html')

def teacher_home_view(request):
    return render(request,'teach_home.html')

def student_home_view(request):
    return render(request,'stdnt_home.html')

def student_profile_view(request):
    return render(request,'stdnt_profile.html')

def student_attendance_view(request):
    return render(request,'stdnt_attendance.html')

def student_grades_view(request):
    return render(request,'stdnt_grades.html')

def student_schedule_view(request):
    return render(request,'stdnt_schedule.html')

def admin_home_view(request):
    return render(request,'admin_home.html')

def admin_mg_student_view(request):
    return render(request,'admin_mg_student.html')

def admin_mg_teacher_view(request):
    return render(request,'admin_mg_teacher.html')

def admin_mg_course_view(request):
    return render(request,'admin_mg_course.html')