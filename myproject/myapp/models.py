from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)   
    age = models.IntegerField()               
    email = models.EmailField(unique=True)   

    def __str__(self):
        return "{} ({})".format(self.name,self.email)
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.Textfield(max_length=350)

    def __str__(self):
        return "{} - {}".format(self.code, self.title)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add =True)

    def __str__(self):
        return "{} enrolled in {}".format(self.student.name, self.course.code)