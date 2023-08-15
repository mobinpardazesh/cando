import datetime
from django import forms
from home.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class RegisterForm(UserCreationForm):
	student_name = forms.CharField(max_length=100)
	student_familly = forms.CharField(max_length=100)
	student_Age = forms.IntegerField()
	student_fathername = forms.CharField()
	student_email = forms.EmailField(required=True)
	USERNAME_FIELD=forms.CharField(max_length=100)
	student_password = forms.CharField(widget=forms.PasswordInput)
	student_birthdate = forms.DateTimeField()
	class Meta:
		model = Student
		fields = ("student_name", "student_familly", "student_Age", "student_fathername","USERNAME_FIELD","student_email","student_password")

	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.student_name = self.cleaned_data['student_name']
		user.student_familly = self.cleaned_data['student_familly']
		user.student_Age = self.cleaned_data['student_Age']
		user.student_fathername = self.cleaned_data['student_fathername']
		user.student_email = self.cleaned_data['student_email']
		user.student_password = self.cleaned_data['student_password']
		user.USERNAME_FIELD = self.cleaned_data['USERNAME_FIELD']

		# user.student_birthdate = self.cleaned_data['student_birthdate']


		if commit:
			user.save()
		return user