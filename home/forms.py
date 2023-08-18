from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm

from home.models import Student


# Create your forms here.

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            'placeholder': 'John Doe',
            'maxlength': '16',
            'minlength': '6',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'placeholder': 'JohnDoe@mail.com',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'placeholder': 'password',
            'maxlength': '22',
            'minlength': '8'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'required': '',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'placeholder': 'password',
            'maxlength': '22',
            'minlength': '8'
        })

    username = forms.CharField(max_length=20, label=False)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class Student_Register_Form(ModelForm):
    # student_name = forms.CharField(max_length=100)
    # student_familly = forms.CharField(max_length=100)
    # student_Age = forms.IntegerField(max_value=100)
    # student_fathername = forms.CharField(max_length=100)
    # student_username=forms.CharField(max_length=100)
    # student_email = forms.EmailField(required=True)
    # # student_birthdate = forms.DateTimeField()
    student_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ["student_name", "student_familly", "student_Age", "student_fathername", "student_username",
                  "student_password", "student_email"]
        widgets = {
            "student_password": forms.PasswordInput
        }
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
        user.Student_password = self.cleaned_data['student_password']
        user.student_email = self.cleaned_data['student_email']
        # user.student_birthdate = self.cleaned_data['student_birthdate']
        # student_Register_Form = Student_Register_Form(request.POST)

        if commit:
            user.save()
        return user


class Student_Login_Form(ModelForm):
    class Meta:
        model = Student
        fields = ["student_username", "student_password"]
        widgets = {
            "student_password": forms.PasswordInput
        }

class Login_Form(ModelForm):
    class Meta:
        pass

class Check_Email_Form(ModelForm):
    pass


class Forget_Password_Form(ModelForm):
    pass


class Reset_Password_Form(ModelForm):
    pass
