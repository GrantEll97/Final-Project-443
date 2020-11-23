from django.db import models


class StudentDetails(models.Model):
    StudentId = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length = 50)
    LastName = models.CharField(max_length = 50)
    Major = models.CharField(max_length = 50)
    Year = models.CharField(max_length = 50)
    GPA = models.DecimalField(max_digits = 3, decimal_places = 2)
# Create your models here.

class CourseDetails(models.Model):
    IdCourse = models.IntegerField(primary_key=True)
    CourseTitle = models.CharField(max_length = 50)
    CourseName = models.CharField(max_length = 50)
    CourseSectionCode = models.IntegerField()
    CourseDepartment = models.CharField(max_length = 50)
    InstructorFullName = models.CharField(max_length = 50)

class Enrollmenttable(models.Model):
    StudentId = models.IntegerField()
    IdCourse = models.IntegerField()
