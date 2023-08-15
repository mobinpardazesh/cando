from django.db import models

# Create your models here.
class Student (models.Model):
    student_name=models.CharField(max_length=100)
    student_familly=models.CharField(max_length=100)
    student_Age=models.IntegerField(default=0)
    student_fathername=models.CharField(max_length=100)
    student_email=models.EmailField(max_length=100)
    student_password=models.CharField(max_length=100)
    student_birthdate=models.DateTimeField(auto_now_add=True)
    student_creatdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name