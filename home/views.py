from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView  # Import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from home.forms import Student_Register_Form


class Home(TemplateView):
    template_name = "home.html"


def register(request):
    if request.method == "POST":
        student_Register_Form = Student_Register_Form(request.POST)
        if student_Register_Form.is_valid():
            new_student = student_Register_Form.save()
            # login(request, new_student)
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return redirect("cando:register")
    messages.success(request, "Registration successful.")
    return render(request=request, template_name="register.html", context={"register": Student_Register_Form})


def login(request):
	if request.method == "POST":
		student_login_Form = AuthenticationForm(request, data=request.POST)
		if student_login_Form.is_valid():
			username = student_login_Form.cleaned_data.get('username')
			password = student_login_Form.cleaned_data.get('password')
			student = authenticate(username=username, password=password)
			if student is not None:
				login(request, student)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login":Student_Register_Form})
