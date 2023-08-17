import datetime
from django import forms
from django.forms import ModelForm
from home.models import Student
from django.db import models
from django.core.exceptions import NON_FIELD_ERRORS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class Student_Register_Form(ModelForm):
	# student_name = forms.CharField(max_length=100)
	# student_familly = forms.CharField(max_length=100)
	# student_Age = forms.IntegerField(max_value=100)
	# student_fathername = forms.CharField(max_length=100)
	# student_username=forms.CharField(max_length=100)
	# student_email = forms.EmailField(required=True)
	# # student_birthdate = forms.DateTimeField()
	class Meta:
		model = Student
		fields = ("student_name", "student_familly", "student_Age", "student_fathername","student_username","student_email")
		error_messages = {
					NON_FIELD_ERRORS: {
						"unique_together": "%(model_name)s's %(field_labels)s are not unique.",
					}
				}
	def save(self, commit=True):
		user = super(Student_Register_Form, self).save(commit=False)
		user.student_name = self.cleaned_data['student_name']
		user.student_familly = self.cleaned_data['student_familly']
		user.student_Age = self.cleaned_data['student_Age']
		user.student_fathername = self.cleaned_data['student_fathername']
		user.student_username = self.cleaned_data['student_username']
		user.student_email = self.cleaned_data['student_email']

		# user.student_birthdate = self.cleaned_data['student_birthdate']
		# student_Register_Form = Student_Register_Form(request.POST)

		if commit:
			user.save()
		return user