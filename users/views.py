from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import Check_Email_Form, Forget_Password_Form, Reset_Password_Form
from .forms import SignUpForm ,Login_Form


def signup(request):
    signup_form = SignUpForm(request.POST)
    if signup_form.is_valid():
        signup_form.save()
        username = signup_form.cleaned_data.get('username')
        password = signup_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    context = {
        'signup_form': signup_form
    }
    return render(request, 'users/signup.html', context)


def login(request):
    if request.method == "POST":
        student_login_Form = Login_Form(request)
        if student_login_Form.is_valid():
            username = student_login_Form.cleaned_data.get('student_username')
            password = student_login_Form.cleaned_data.get('student_password')
            student = authenticate(username=username, password=password)
            if student is not None:
                login(request, student)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = Login_Form()
    return render(request=request, template_name="users/login.html", context={"login": Login_Form})


def check_email(request):
    return render(request, template_name="users/check-email.html", context={"check-email": Check_Email_Form})


def forget_password(request):
    return render(request, template_name="users/forget-password.html", context={"forget_password": Forget_Password_Form})


def reset_password(request):
    return render(request, template_name="users/reset-password.html", context={"reset_password": Reset_Password_Form})
