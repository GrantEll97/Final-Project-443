from django.contrib import admin
from Students.models import StudentDetails
from Students.models import CourseDetails

# Register your models here.
admin.site.register(StudentDetails)
admin.site.register(CourseDetails)