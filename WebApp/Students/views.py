from django.shortcuts import render
from django.http import HttpResponse
from Students.models import StudentDetails
from Students.models import CourseDetails
from Students.models import Enrollmenttable
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'students/home.html')

@login_required
def details(request):
    Students = StudentDetails.objects.all()
    paginator = Paginator(Students, 10)
    page = request.GET.get('page')
    studentdetails = paginator.get_page(page)
    return render(request, 'Students/studentdetails.html', {'data':studentdetails})

@login_required
def coursedetails(request):
    Students = CourseDetails.objects.all()
    paginator = Paginator(Students, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
    return render(request, 'Students/coursedetails.html', {'data':coursedata})

@login_required
def enrollment(request):
    studentdata = StudentDetails.objects.all()
    coursedata = CourseDetails.objects.all()
    enrollmentdata = ''
    if ('StudentId' in request.session):
        enrollmentdata = Enrollmenttable.objects.filter(StudentId=request.session['StudentId'])
    if ('StudentId' in request.GET and 'IdCourse' not in request.GET):
        StudentId = request.GET.get('StudentId')
        request.session['StudentId'] = StudentId
        return HttpResponse('Success')
    if ('StudentId' in request.GET and 'IdCourse' in request.GET):
        StudentId = request.GET.get('StudentId')
        IdCourse = request.GET.get('IdCourse')
        enrollmentdata = Enrollmenttable.objects.filter(StudentId=StudentId)
        for row in enrollmentdata:
            if Enrollmenttable.objects.filter(StudentId=StudentId).count() >= 3:
                return HttpResponse('Error')
        newdata = Enrollmenttable(StudentId=StudentId, IdCourse=IdCourse)
        newdata.save()
        return HttpResponse("Success")
    return render(request, 'Students/enrollment.html', {'studentdata':studentdata, 'coursedata':coursedata, 'enrollmentdata':enrollmentdata })