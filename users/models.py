from django.db import models


# from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_familly = models.CharField(max_length=100)
    user_age = models.IntegerField(default=0)
    user_fathername = models.CharField(max_length=100)
    user_username = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100,default="123")
    user_email = models.EmailField(max_length=100)

    # student_birthdate=models.DateTimeField(auto_now_add=True)
    # student_creatdate=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user_name} || {self.user_familly}  || {self.user_email}  || {self.user_fathername} || {self.user_username} || {self.user_password} || {self.user_age}'
