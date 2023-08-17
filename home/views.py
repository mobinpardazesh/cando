from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView  # Import TemplateView

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
        messages.success(request, "Registration successful.")
        return redirect("cando:home")
    return render(request=request, template_name="register.html", context={"register": Student_Register_Form})


def login(request):
    return render(request, "login.html", {})
# Create your  views here.
# def home(request):
#     # form = Customerform()
#     # if request.method == "POST":
#     #     form = Customerform(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #     # else:
#     #     #     form = Customerform
#     #     # context = {}
#     #     # context['form'] = Customerform()
#     #
#     # context = {'form': form}
#     return render(request, "home.html", {})
