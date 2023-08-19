from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
# from .forms import Check_Email_Form, Forget_Password_Form, Reset_Password_Form
from .forms import LoginForm ,SignUpForm
from django.contrib import messages


def sign_up(request):
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


def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, template_name="users/login.html", context={"login": form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('home')

        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'login': form})
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')
#
#
# def check_email(request):
#     return render(request, template_name="users/check-email.html", context={"check-email": Check_Email_Form})
#
#
# def forget_password(request):
#     return render(request, template_name="users/forget-password.html", context={"forget_password": Forget_Password_Form})
#
#
# def reset_password(request):
#     return render(request, template_name="users/reset-password.html", context={"reset_password": Reset_Password_Form})
