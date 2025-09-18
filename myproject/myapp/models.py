from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)   # String field
    age = models.IntegerField()               # Integer field
    email = models.EmailField(unique=True)    # Unique email field
    enrolled_date = models.DateField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return f"{self.name} ({self.age})"